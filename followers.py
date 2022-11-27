from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from credentials import username, password


class InstaUnfollowers:
    def __init__(self, user, pwd):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        print("--------------------------------")
        print("WebDriver Manager successfully initialized.")
        self.driver.get("https://instagram.com")
        override = "off"  # Set override if Auto-Login not possible
        sleep(2)
        # Accept cookies
        try:
            accept_all_btn = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]')
            accept_all_btn.click()
            sleep(2)
        except:
            pass
        # Check if credentials are empty
        if (login == "auto" or login == "a") and (username == "" or password == ""):
            print("Error: No values given in credentials.py, please attempt manual login.")
            override = "manual"
        # Try auto-login
        if (login == "auto" or login == "a") and override == "off":
            username_type = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input")
            username_type.send_keys(user)
            password_type = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input")
            password_type.send_keys(pwd)
            log_in = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button')
            log_in.click()
            sleep(8)
            if self.driver.current_url == "https://instagram.com":
                print("Auto-Login unsuccessful, please attempt manual login.")
                override = "manual"
            else:
                print("Auto-Login successful.")
        # Expect Manual-Login
        if (login == "manual" or login == "m") or override == "manual":
            print("Please log in to your account in the opened window and confirm any text and press enter.")
            print("You can also exit the program with 'exit'")
            waitforinput = input(">> ")
            if waitforinput == "exit":
                quit()
            print("Continue...")

    def get_unfollowers(self):
        # Go to given account
        print("Accessing profile...")
        self.driver.get(accountUrl)
        sleep(3)
        # Get following people
        print("Getting following people, this might take a while...")
        following_element = self.driver.find_element(By.PARTIAL_LINK_TEXT, local2)
        following_element.click()
        following_list = self.get_people()
        # Get followers
        print("Getting followers, this might take a while...")
        followers_element = self.driver.find_element(By.PARTIAL_LINK_TEXT, local1)
        followers_element.click()
        followers_list = self.get_people()
        # Get not following people in list
        not_following_back = [user for user in following_list if user not in followers_list]
        # print data in ordered list
        not_following_back.sort()
        print("These people are not following you:")
        for name in not_following_back:
            print(name)
        print("Total: " + str(len(not_following_back)))

    def get_people(self):  # Get people in list, return as list
        sleep(2)
        # Access scroll-box
        scroll_box = self.driver.find_element(By.CLASS_NAME, "_aano")
        prev_height, height = 0, 1
        # Execute while there are more people to load
        while prev_height != height:
            prev_height = height
            sleep(3)
            height = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
        # Get people by anchor elements
        links = scroll_box.find_elements(By.TAG_NAME, 'a')
        names = [name.text for name in links if name.text != '']
        print("Got one list of: " + str(len(names)))
        self.driver.get(accountUrl)
        sleep(5)
        return names


# Entry-Point
print("--------------------------------")
print("   Instagram Unfollow-Checker")
print("--------------------------------\n")
# Ask user for account name
print("Enter the account name you want to check.")
account = input("*The profile has to be accessible from the credentials you set. (public or followed)*\n>> ")
accountUrl = "https://instagram.com/" + str(account) + "/"

# Ask user for language and set localization
language = input("Please select the language you are opening Instagram with.\n[en] English\n[de] German\n>> ")
if (language != "en") and (language != "de"):
    print("Unknown input, automatically selected English.")
if language == "de":
    local1, local2 = "Abonnenten", "abonniert"
else:
    local1, local2 = "follower", "following"

print("Have you set up your credentials in the credentials.py file?")
print("You can login manually if you don't have it set up (standard).")
login = input("Type '[a]uto' or '[m]anual'.\n>> ")
if login not in {"auto","manual","a","m"}:
    print("Unknown input, automatically selected manual login.")
    login = "manual"

# Run bot
print("Initializing WebDriver Manager")
print("--------------------------------")
sleep(1)
my_bot = InstaUnfollowers(username, password)
my_bot.get_unfollowers()
try:
    my_bot.driver.close()
except:
    print("Fail")
    my_bot.driver.close()