import time

from main import upload
from seliky import WebDriver

ups = upload()
p = WebDriver(executable_path=r'D:\s\Python310\chromedriver.exe')
p.open_browser()
p.get('https://www.baidu.com/')
p.click('//span[@class="soutu-btn"]')
loc = "//span[text()='选择文件']"
loc2 = '//input[@class="upload-pic"]'  # 运行时可以打开，调试时打不开


ups.close_if_opened()
p.click(loc2)
ups.upping('demo1.png')

# with upload() as f:
#     p.click(loc2)  # 运行时可以打开，调试时打不开
#     f.upping(r'D:\uploads\uploads\demo1.png')

print('end')