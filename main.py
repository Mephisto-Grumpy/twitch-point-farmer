from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time
import datetime

class TwitchPointFarmer():
    def __init__(self, browser, driverPath, authTokenCookie, streamers, hideTheBot, logs):
        self.browser = browser
        self.driverPath = driverPath
        self.authTokenCookie = authTokenCookie
        self.streamers = streamers
        self.hideTheBot = hideTheBot
        self.logs = logs
        self.driver = None
        self.currentStreamer = None

    def main(self):
        self.init_driver()
        self.login()

        while True:
            try:
                # Set the current streamer
                if self.currentStreamer is None:
                    self.get_next_current_streamer()

                # Click on the reward
                self.collect_reward()

                # Wait before the next iteration
                time.sleep(8)
            except Exception as e:
                self.log(f"❌ An error occurred: {type(e).__name__} - {str(e)}")
                self.restart_browser()


    def init_driver(self):
        try:
            if self.browser.lower() == 'chrome':
                chrome_options = ChromeOptions()
                if self.hideTheBot:
                    chrome_options.add_argument("--headless")
                service = ChromeService(executable_path=self.driverPath)
                self.driver = webdriver.Chrome(service=service, options=chrome_options)
            elif self.browser.lower() == 'firefox':
                firefox_options = FirefoxOptions()
                if self.hideTheBot:
                    firefox_options.add_argument("--headless")
                service = FirefoxService(executable_path=self.driverPath)
                self.driver = webdriver.Firefox(service=service, options=firefox_options)
            else:
                raise ValueError(f"Unsupported browser: {self.browser}")
            self.log(f"✅ Initialized {self.browser} driver")
        except Exception as e:
            self.log(f"❌ Error initializing browser")
            raise

    def login(self):
        try:
            self.driver.get("https://www.twitch.tv")
            self.driver.add_cookie({
                "name": "auth-token", 
                "value": self.authTokenCookie
            })
            self.log("✅ Logged in with auth token")
        except Exception as e:
            self.log(f"❌ Error logging in")
            raise

    def get_next_current_streamer(self):
        try:
            for streamer in self.streamers:
                if self.check_if_user_is_streaming(streamer):
                    self.currentStreamer = streamer
                    self.log(f"🎮 Is farming {self.currentStreamer.capitalize()}")
                    time.sleep(8)
                    self.skip_age_verification()
                    return
            self.currentStreamer = None
            self.log("ℹ️ No streamers are currently online")
        except Exception as e:
            self.log(f"❌ Error getting next current streamer")
            raise

    def check_if_user_is_streaming(self, user):
        try:
            self.driver.get(f"https://www.twitch.tv/{user}")
            self.log(f"🔍 Checking if {user.capitalize()} is streaming")
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "p[data-a-target='animated-channel-viewers-count']"))
            )
            self.log(f"📹 {user.capitalize()} is streaming")
            return True
        except Exception as e:
            self.log(f"🚫 {user.capitalize()} is not streaming")
            return False

    def collect_reward(self):
        try:
            reward_button = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.ScCoreButton-sc-ocjdkq-0.ScCoreButtonSuccess-sc-ocjdkq-5.ljgEdo.fEpwrH"))
            )
            reward_button.click()
            self.log("✨ Drop collected")
        except Exception as e:
            self.log(f"❌ Error collecting reward")

    def skip_age_verification(self):
        try:
            age_verification_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-a-target='player-overlay-mature-accept']"))
            )
            age_verification_button.click()
            self.log("✅ +18 overlay skipped")
        except Exception as e:
            self.log(f"❌ No +18 overlay found or failed to click")

    def restart_browser(self):
        try:
            if self.driver:
                self.driver.quit()
        except Exception as e:
            self.log(f"❌ Error while quitting browser")

        try:
            self.init_driver()
            self.login()
        except Exception as e:
            self.log(f"❌ Error while restarting browser")
            time.sleep(60)  # Wait for 1 minute before retrying

    def log(self, content):
        if self.logs:
            print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {content}")

if __name__ == '__main__':
    try:
        with open("config.json", "r", encoding="utf8") as f:
            config = json.load(f)
            browser = config["browser"]
            driverPath = config["driverPath"]
            authTokenCookie = config["authTokenCookie"]
            streamers = config["streamers"]
            hideTheBot = config["hideTheBot"]
            logs = config["logs"]

        twitchPointFarmer = TwitchPointFarmer(browser, driverPath, authTokenCookie, streamers, hideTheBot, logs)
        twitchPointFarmer.main()
    except Exception as e:
        print(f"❌ Error during execution")
