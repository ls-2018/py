# 1、输入账号、密码，然后点击登陆
# 2、点击按钮，弹出没有缺口的图
# 3、针对没有缺口的图片进行截图
# 4、点击滑动按钮，弹出有缺口的图
# 5、针对有缺口的图片进行截图
# 6、对比两张图片，找出缺口，即滑动的位移
# 7、按照人的行为行为习惯，把总位移切成一段段小的位移
# 8、按照位移移动
# 9、完成登录
import time
import os
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from PIL import Image
from selenium import webdriver
import random


def simulate_reaction(func):
    """模拟人类的反应时间"""
    from functools import wraps

    @wraps
    def inner(self, *args, **kwargs):
        time.sleep(random.uniform(0.2, 1))
        ret = func(self, *args, **kwargs)
        return ret

    return inner


class SVCR:
    """识别滑动验证码   极验验证"""

    def __init__(self, driver):
        self.driver = driver
        self.get_full_img = True

    # @simulate_reaction
    def run(self):
        """执行识别流程"""
        # 1. 点击按钮开始验证
        self.click_start_btn()

        # 2. 根据验证类型验证
        return self.judge_and_auth()

    def judge_and_auth(self):
        """判断验证类型并执行相应的验证方法"""
        if True:
            return self.auth_slide()
        else:
            pass

    def auth_slide(self):

        def get_distance(img1, img2):
            """计算滑动距离"""
            threshold = 60
            # 忽略可动滑块部分
            start_x = 57

            for i in range(start_x, img1.size[0]):
                for j in range(img1.size[1]):
                    rgb1 = img1.load()[i, j]
                    rgb2 = img2.load()[i, j]
                    res1 = abs(rgb1[0] - rgb2[0])
                    res2 = abs(rgb1[1] - rgb2[1])
                    res3 = abs(rgb1[2] - rgb2[2])
                    if not (res1 < threshold and res2 < threshold and res3 < threshold):
                        return i - 7  # 经过测试，误差为大概为7

        def get_tracks(distance):
            """
            制造滑动轨迹

            策略：匀加速再匀减速，超过一些，再回调，左右小幅度震荡
            """

            v = 0
            current = 0
            t = 0.2
            tracks = []
            if not distance:
                return tracks
            # 正向滑动
            while current < distance + 10:
                if current < distance * 2 / 3:
                    a = 2
                else:
                    a = -3
                s = v * t + 0.5 * a * (t ** 2)
                current += s
                tracks.append(round(s))
                v = v + a * t

            # 往回滑动
            current = 0
            while current < 13:
                if current < distance * 2 / 3:
                    a = 2
                else:
                    a = -3
                s = v * t + 0.5 * a * (t ** 2)
                current += s
                tracks.append(-round(s))
                v = v + a * t

            # 最后修正
            tracks.extend([2, 2, -3, 2])

            return tracks

        # 1. 截取完整图片
        if self.get_full_img:
            time.sleep(2)  # 等待图片加载完毕
            img_before = self.get_img()
        else:
            img_before = self._img_before

        # 2. 点击出现缺口图片
        slider_btn = self.driver.find_element_by_class_name("geetest_slider_button")
        slider_btn.click()

        # 3. 截取缺口图片
        time.sleep(2)  # 等待图片加载完毕
        img_after = self.get_img()

        # 4. 生成移动轨迹
        tracks = get_tracks(get_distance(img_before, img_after))

        # 5. 模拟滑动
        slider_btn = self.driver.find_element_by_class_name("geetest_slider_button")
        ActionChains(self.driver).click_and_hold(slider_btn).perform()
        for track in tracks:
            ActionChains(self.driver).move_by_offset(xoffset=track, yoffset=0).perform()

        # 6. 释放鼠标
        time.sleep(0.5)  # 0.5秒后释放鼠标
        ActionChains(self.driver).release().perform()

        # 7. 验证是否成功

        time.sleep(2)
        div_tag = self.driver.find_element_by_class_name("geetest_fullpage_click")
        if "display: block" in div_tag.get_attribute("style"):
            '''判断模块对话框是否存在，如果存在就说明没有验证成功，"display: block"，重新去验证'''
            self.get_full_img = False
            setattr(self, "_img_before", img_before)
            return self.auth_slide()
        else:
            # 如果验证成功"display: none"
            time.sleep(1000)
            return True

    # @simulate_reaction
    def click_start_btn(self, search_style="CLASS_NAME", search_content="geetest_radar_tip"):
        """找到开始按钮并点击"""
        btn = getattr(self.driver, "find_element")(getattr(By, search_style), search_content)
        btn.click()

    def get_img(self):
        """截取图片"""
        div_tag = self.driver.find_element_by_class_name("geetest_slicebg")

        # 计算截取图片大小
        img_pt = div_tag.location  # {'x': 296, 'y': 15}
        img_size = div_tag.size  # {'height': 159, 'width': 258}
        img_box = (img_pt["x"], img_pt["y"], img_pt["x"] + img_size["width"], img_pt["y"] + img_size["height"])

        # 保存当前浏览页面
        self.driver.save_screenshot("snap.png")

        # 截取目标图片
        img = Image.open("snap.png")
        return img.crop(img_box)


def auth():
    driver = webdriver.Chrome(
        executable_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), "utils", 'chromedriver.exe'))

    driver.get("https://passport.cnblogs.com/user/signin")  # 请求页面
    driver.implicitly_wait(3)
    # 第一步：输入账号、密码，然后点击登陆
    input_name = driver.find_element_by_id('input1')  # 找到输入用户名的框
    input_pwd = driver.find_element_by_id('input2')  # 找到输入密码的框
    input_button = driver.find_element_by_id('signin')  # 找到按钮
    input_name.send_keys("name")  # 博客园的账号
    input_pwd.send_keys("pwd")  # 博客园的密码
    input_button.click()  # 进行点击
    return driver


def main():
    driver = auth()  # 进行验证，
    _auth = SVCR(driver)
    _auth.run()


if __name__ == '__main__':
    main()