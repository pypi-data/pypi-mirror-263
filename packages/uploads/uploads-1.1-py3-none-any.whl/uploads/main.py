"""
winspy工具识别到win的窗口位置，点击Tree展开所在的层级，通过识别外围一步一步向下传递.
每个步骤之间要考虑延时
可代替autoit调用工具的形式，更加pythonic。
无界面上传只能通过send_keys和playwright的send_files了。

包括以下的情况：
1. 窗口不存在直接结束
2. 文件地址为空直接结束
3. 没有此文件，要取消上传
4. 一上来就是‘找不到’的窗口，要去掉该窗口，再上传
5. 文件和窗口正常，正常上传
"""
import time
import sys
from functools import wraps
import os
import ctypes
import threading
import win32gui
import win32con


def overtime(timeout):
    def _overtime(func):
        return wraps(func)(lambda *args, **kwargs: _overtime_(timeout, func, args=args, arg2=kwargs))

    def _overtime_(_timeout, func, args=(), arg2=None):
        if not arg2:
            arg2 = {}
        if not args:
            args = ()

        ret = []
        exception = []
        is_stopped = False

        def funcwrap(args2, kwargs2):
            try:
                ret.append(func(*args2, **kwargs2))
            except TimeoutError:
                pass
            except Exception as e:
                exc_info = sys.exc_info()
                if is_stopped is False:
                    e.__traceback__ = exc_info[2].tb_next
                    exception.append(e)

        thread = StoppableThread(target=funcwrap, args=(args, arg2))
        thread.daemon = True

        thread.start()
        thread.join(_timeout)

        if thread.is_alive():
            is_stopped = True
            thread.stop_thread(TimeoutError)
            thread.join(min(.1, _timeout / 50.0))
            raise TimeoutError('Out of %s seconds' % _timeout)
        else:
            thread.join(.5)
        if exception:
            raise exception[0] from None
        if ret:
            return ret[0]

    class StoppableThread(threading.Thread):
        def stop_thread(self, exception, raise_every=2.0):
            if self.is_alive() is False:
                return True
            self._stderr = open(os.devnull, 'w')
            jt = JoinThread(self, exception, repeat_every=raise_every)
            jt._stderr = self._stderr
            jt.start()
            jt._stderr = self._stderr

    class JoinThread(threading.Thread):
        def __init__(self, other_thread, exception, repeat_every=2.0):
            threading.Thread.__init__(self)
            self.otherThread = other_thread
            self.exception = exception
            self.repeatEvery = repeat_every
            self.daemon = True

        def run(self):
            self.otherThread._Thread__stderr = self._stderr
            while self.otherThread.is_alive():
                ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(self.otherThread.ident),
                                                           ctypes.py_object(self.exception))
                self.otherThread.join(self.repeatEvery)
            try:
                self._stderr.close()
            except:
                ...

    return _overtime


class _Win32:
    """
    对两个find增加耗时处理，sendmessage不用增加耗时处理
    """

    def __init__(self, win32gui, win32con):
        self.win32gui = win32gui
        self.win32con = win32con

    def find_window(self, class_, title, n: int = 5):
        """
        原生FindWindow很容易出现找不到的情况，以此来避免
        """
        time.sleep(0.2)
        while n:
            n -= 1
            try:
                handle_id = self.win32gui.FindWindow(class_, title)
            except:
                handle_id = 0
            if not handle_id:
                time.sleep(0.2)
                return self.find_window(class_, title, n)
            return handle_id

    def find_window_ex(self, dialog, m, class_, text, n: int = 5):
        """
        原生FindWindowEx很容易出现找不到的情况，以此来避免
        """
        time.sleep(0.2)
        while n:
            n -= 1
            try:
                handle_id = self.win32gui.FindWindowEx(dialog, m, class_, text)
            except:
                handle_id = 0
            if not handle_id:
                time.sleep(0.2)
                return self.find_window_ex(dialog, m, class_, text, n)
            return handle_id


BROWSER = 'chrome'


class upload:
    """
    winspy工具识别到win的窗口位置，点击Tree展开所在的层级，通过识别外围一步一步向下传递.
    每个步骤之间要考虑延时
    可代替autoit调用工具的形式，更加pythonic。
    无界面上传只能通过send_keys和playwright的send_files了。

    包括以下的情况：
    1. 窗口不存在直接结束
    2. 文件地址为空直接结束
    3. 没有此文件，要取消上传
    4. 一上来就是‘找不到’的窗口，要去掉该窗口，再上传
    5. 文件和窗口正常，正常上传
    """

    def __enter__(self):
        self.close_if_opened()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        ...

    def __init__(self):
        self.__title__ = self.__get_title()
        assert self.__title__
        self.__win32gui = win32gui
        self.__win32con = win32con
        self.__win32 = _Win32(win32gui, win32con)

    def close_if_opened(self):
        """
        如果点击之前就有弹窗，说明是上一次的弹窗，会影响接下来的操作，需要关掉。
        这是系统级的判断，如果另一个浏览器打开了窗口，可能把那个关了。
        如果能保证一个电脑同时只有一个浏览器在上传，那可以用。
        担有极少数的场景是：多个谷歌浏览器在同时上传，那么就没办法了。
        包括uploads方法也是，如果有另一个浏览器打开了‘打开’窗口，那填充的值跑到另一个浏览器上去了。
        至于autoit，更别提了。
        优先使用原生的send_keys、fill等；如果不行再用uploads+此方法结合；如果有多个浏览器上传不要用这个方法。
        ups.close_if_opened
        page.click('//button')
        ups.upload
        """
        dialog = self._dialog(n=1)
        if dialog:
            return self.__cancel(dialog)

    def upping(self, file_path: str, timeout: float = 6):
        """
        上传动作（触发的动作不要放到这个库里，上传不了是点击的元素本身有问题，要用js点有的js点了也没反应）
        :param file_path: 上传的文件地址
        # :param browser_type: 浏览器类型
        :param timeout: 等待时间
        """
        # 此对象在‘打开’窗口 和‘文件不存在’窗口可复用
        dialog = self._dialog()

        if not dialog:
            print("'打开' 窗口不存在")
            return False  # 说明点击有问题，给false的意思是让外部再触发一次。

        if not file_path:
            print("文件名为空，取消上传")
            self.__cancel(dialog)
            return True  # 文件名为空，不是点击问题，不需要外部再触发。

        self.__occur_no_exist(n=1)  # 如果一开始/上传过某些文件之后，出现‘找不到窗口’，需要关闭这个窗口，这里不管你是否出现，我都要填写，所以没必要搞个对象接收

        return self.__fill_and_open(file_path, timeout - 1)

    @staticmethod
    def __get_title():
        brs = BROWSER.lower()
        title = "打开" if brs in ["chrome", 'edge'] else "文件上传" if brs == "firefox" else False
        return title if title else print("建议用谷歌浏览器噢")  # 利用 print 返回的是None

    def _dialog(self, n=2):
        """定位一级窗口"#32770"-"打开"，参数1-class的值；参数2-title的值"""
        dialog = self.__win32.find_window("#32770", self.__title__, n=n)
        return dialog if dialog else False

    def __cancel(self, dialog):
        """对打开的窗口做‘取消’处理"""

        # 参数1-父窗口对象；参数2未知一般为None；参数3-子窗口类名；参数4-子窗口的text值
        # ‘取消’的布局在chrome和firefox一致
        cancel = self.__win32.find_window_ex(dialog, 0, 'Button', "取消")

        # 参数1-窗口句柄，参数2-消息类型；参数3-文本大小；参数4-存储位置
        # 点击取消为什么不能用点击’打开‘那种方式，kb
        self.__win32gui.SendMessage(cancel, self.__win32con.WM_LBUTTONDOWN, 0, 0)
        self.__win32gui.SendMessage(cancel, self.__win32con.WM_LBUTTONUP, 0, 0)
        return False

    def __occur_no_exist(self, n=3):
        """
        出现“找不到文件”的窗口，需要点’确定‘。
        细节：此时文件路径变为最后结尾处的文件名，这里曾影响我判断过。
        """
        # 除了self.__title__其它布局在chrome和firefox一致
        new_dialog = self.__win32.find_window("#32770", self.__title__, n=n)
        sure1 = self.__win32.find_window_ex(new_dialog, 0, 'DirectUIHWND', None, n=n)
        if not sure1:
            return False

        sure2 = self.__win32.find_window_ex(sure1, 0, 'CtrlNotifySink', None, n=n)
        sure3 = self.__win32.find_window_ex(sure2, 0, 'Button', '确定')
        self.__win32gui.SendMessage(new_dialog, self.__win32con.WM_COMMAND, 1, sure3)
        return True

    def __fill_and_open(self, file_path, delay):
        """定位 “文件名(N):” 后面的编辑框所在的位置，点击打开"""
        # 输入框的布局在chrome和firefox一致
        dialog = self.__win32.find_window("#32770", self.__title__)
        edit_out2 = self.__win32.find_window_ex(dialog, 0, "ComboBoxEx32", None)
        edit_out1 = self.__win32.find_window_ex(edit_out2, 0, "ComboBox", None)
        edit = self.__win32.find_window_ex(edit_out1, 0, "Edit", None)

        # 发送文件路径
        self.__win32gui.SendMessage(edit, self.__win32con.WM_SETTEXT, None, file_path)
        time.sleep(0.2)

        # 定位‘打开’，布局在chrome和firefox一致
        open_button = self.__win32.find_window_ex(dialog, 0, 'Button', "打开(&O)")

        # 点击打开
        @overtime(1)
        def _click_open():
            self.__win32gui.SendMessage(dialog, self.__win32con.WM_COMMAND, 1, open_button)

        try:
            _click_open()
        except TimeoutError:
            print("不存在该文件，点击打开按钮超时")
            self.__occur_no_exist()
            self.__cancel(dialog)
            return False
        # 判断是不是出现了‘找不到文件‘的窗口
        if self.__occur_no_exist():
            self.__cancel(dialog)
            return False
        else:
            if delay >= 2:
                delay = delay - 2
            time.sleep(delay)
            return True
