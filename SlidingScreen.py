# encoding: utf-8
'''
滑动屏幕
'''
# 向上滑动
def swipe_up(driver, t=500, n=1):
    s = driver.get_window_size()
    x1 = s['width'] * 0.5  # x坐标
    y1 = s['height'] * 0.75  # 起点y坐标
    y2 = s['height'] * 0.25  # 终点y坐标
    for i in range(n):
        driver.swipe(x1, y1, x1, y2, t)


# 向下滑动
def swipe_down(driver, t=500, n=1):
    s = driver.get_window_size()
    x1 = s['width'] * 0.5  # x坐标
    y1 = s['height'] * 0.25  # 起点y坐标
    y2 = s['height'] * 0.75  # 终点y坐标
    for i in range(n):
        driver.swipe(x1, y1, x1, y2, t)
# 长按
def long_press(driver,xpath_button,time_long):
    el = driver.find_element_by_xpath(xpath_button)
    elx = el.location.get('x')
    ely = el.location.get('y')
    driver.tap([(elx, ely)], time_long)


# 向左滑动
def swipe_left(driver, t=500, n=1):
    s = driver.get_window_size()
    x1 = s['width'] * 0.75
    y1 = s['height'] * 0.5
    x2 = s['width'] * 0.25
    for i in range(n):
        driver.swipe(x1, y1, x2, y1, t)


# 向右
def swipe_right(driver, t=500, n=1):
    l = driver.get_window_size()
    x1 = l['width'] * 0.25
    y1 = l['height'] * 0.5
    x2 = l['width'] * 0.75
    for i in range(n):
        driver.swipe(x1, y1, x2, y1, t)