# from selenium import webdriver
# import time
# wd=webdriver.Chrome()
# wd.implicitly_wait(3)
# wd.get('http://cdn1.python3.vip/files/selenium/sample2.html')
# shuru=wd.find_element_by_id('kw')
# shuru.send_keys('黄兴')
# dian=wd.find_element_by_id('su')
# dian.click()
# wd.switch_to.frame('frame1')

# a=wd.find_elements_by_css_selector('.animal')
# print(element.get_attribute('innerText') )
# wd.quit()
# a=wd.find_element_by_css_selector('[href]')
# for b in a:
    # print(b.get_attribute('outerHTML'))
    # print(b.text)
# wd.quit()
# wd.get
# print(wd.title)
from selenium import webdriver


wd = webdriver.Chrome()
wd.implicitly_wait(10)

wd.get('http://cdn1.python3.vip/files/selenium/sample3.html')

# 点击打开新窗口的链接
link = wd.find_element_by_tag_name("a")
link.click()
c = wd.current_window_handle
for handle in wd.window_handles:
    # 先切换到该窗口
    wd.switch_to.window(handle)
    # 得到该窗口的标题栏字符串，判断是不是我们要操作的那个窗口
    if 'Bing' in wd.title:
        # 如果是，那么这时候WebDriver对象就是对应的该该窗口，正好，跳出循环，
        break
# wd.title属性是当前窗口的标题栏 文本
print(wd.title)
print(wd.get_window_size())
wd.switch_to_window(c)
print(wd.get_window_size())
wd.set_window_size(50,50)
print(wd.get_window_size())
print(wd.title)
print(wd.current_url)