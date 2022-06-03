

# test_mainlogin.py

import time

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


# coding:utf-8
import pytest

class TestCase(object):
    def setup(self):
        desired_caps = dict(
            platformName = "Android",
            platformVersion = "12",
            automationName = 'Uiautomator2',
            deviceName = 'emulator-5556',
        
            app = '/Users/xiao.dong/Downloads/packages/httk-android43.apk',
            appPackage = 'com.htkk.push',
            appActivity = 'com.htkk.push.SplashScreenActivity'
        )
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        time.sleep(25)
        #self.driver.start_activity(app_package="com.htkk.push", app_activity="com.htkk.push.MyFlutterActivity")
        

    def teardown(self):
        self.driver.quit()

    def test_mainlogin(self): 
        time.sleep(5)
        els1 = self.driver.find_element(by=By.XPATH, value= '//android.widget.Button[@content-desc=\"スキップ\"]')
        #");/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout
        
        els1.click()
        time.sleep(10)

        el2 = self.driver.find_element(by=By.XPATH, value= '(//android.view.View[@content-desc=\"こちら\"])[1]')
        #"(//android.view.View[@content-desc=\"こちら\"])[1]"

        time.sleep(2)
        el2.click()

        time.sleep(2)
        el3 = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]")
        el3.click()
        action1 = ActionChains(self.driver)
        action1.click(on_element=el3)
        action1.send_keys("08071015272")
        action1.perform()
        el3.click()

        time.sleep(2) 
        el4 = self.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]")
        el4.click()
        action2 = ActionChains(self.driver)
        action2.click(on_element=el4)
        action2.send_keys("Weiruan1234")
        action2.perform()
        el4.click()

        time.sleep(3)
        #
        el5 = self.driver.find_element(by=By.XPATH, value='//android.widget.Button[@content-desc="ログイン"]')
        #CLASS_NAME, value="android.widget.Button").click()
        
        el5.click()
        time.sleep(20)
        print('hello')
        


if __name__ == "__main__":
    pytest.main(["-s", "test_mainlogin.py"])
