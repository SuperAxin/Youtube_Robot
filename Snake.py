import time
import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options as EdgeOptions

from User_Agent import User_Agent
from Word_List import Word_List

class Catch:
    def __init__(self, User_ID, Password):
        self.User_ID = User_ID
        self.Password = Password

    def FireFox(self):
        # Firefox Options
        self.option = EdgeOptions()
        self.option.add_argument("user-agent=" + User_Agent())
        self.option.add_argument("--disable-gpu")
        self.option.add_argument("--disable-software-rasterizer")
        self.option.add_argument('--ignore-certificate-errors')
        self.option.add_argument('--allow-running-insecure-content')
        self.option.add_argument("--mute-audio")
        self.option.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Edge(options=self.option)

    def Login_Google(self):

        ### 會被判定為不安全瀏覽器，目前無法使用 ###

        # 啟動Driver
        print('Start FireFox Driver')
        self.driver.get('https://accounts.google.com/v3/signin/identifier?dsh=S1846348859%3A1664301386175408&continue=https%3A%2F%2Fwww.google.com.tw%2F%3Fhl%3Dzh_TW&ec=GAZAmgQ&hl=zh-TW&passive=true&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=AQDHYWpmS40ET8S1E0tUO5Psnl1CRE2Jh-Z9uVzs2_O_glZRDE2mg0JwG-AQc9QYR3HVGSQZ9hfL')

        # 輸入帳號
        google_email = self.driver.find_element(By.NAME, "identifier")
        google_email.clear()
        google_email.send_keys(self.User_ID)
        google_email.send_keys(Keys.RETURN)
        time.sleep(3)

        # 輸入密碼
        google_password = self.driver.find_element(By.NAME, "Passwd")
        google_password.clear()
        google_password.send_keys(self.Password)
        google_password.send_keys(Keys.RETURN)
        time.sleep(3)

        #　登入成功
        print("Success")

    def Youtube_Robot(self):
        #　開啟Youtube
        self.driver.get('https://www.youtube.com/')

        # Cookies 設定
        try:
            time.sleep(3)
            self.driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[6]/div[1]/ytd-button-renderer[1]').click()
            print("Reject Cookies")
        except:
            print("No Cookies Setting")

        # 隨機搜尋影片
        search = str(Word_List())
        time.sleep(3)
        self.driver.find_element(By.NAME, "search_query").click()
        time.sleep(1)
        self.driver.find_element(By.NAME, "search_query").clear()
        time.sleep(1)
        print("Search", search)
        self.driver.find_element(By.NAME, "search_query").send_keys(search)
        time.sleep(1)
        self.driver.find_element(By.NAME, "search_query").send_keys(Keys.ENTER)
        time.sleep(5)

        # 隨機選擇影片
        Video_Index = random.randint(1, 3)
        Video_Click = self.driver.find_element(By.XPATH, f'//*[@id="contents"]/ytd-video-renderer[{Video_Index}]')
        Video_Click.click()
        time.sleep(3)

        # 顯示影片名稱
        try:
            Video_Name = self.driver.find_element(By.XPATH, '//*[@id="title"]/h1/yt-formatted-string').text
        except:
            Video_Name = self.driver.find_element(By.XPATH, '//*[@id="container"]/h1/yt-formatted-string').text

        # 播放20秒
        print("Play Video: ", Video_Name)
        Video_Time = 20
        time.sleep(Video_Time)

        # 關閉瀏覽器
        self.driver.close()