from selenium import webdriver
from time import sleep
from creditentials import username, password


class InstaUnfollowers:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com")
        sleep(2)
        # instagram login
        username_type = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
        username_type.send_keys(username)
        password_type = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
        password_type.send_keys(password)
        submit = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button')
        submit.click()
        sleep(3)
        ad = self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")
        ad.click()
        sleep(3)
        ad = self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")
        ad.click()

    def get_unfollowers(self):
        usernames = self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img")
        usernames.click()
        profile = self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[2]/div[2]/a[1]/div/div[2]/div/div/div/div").click()
        sleep(3)
        Following = self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")
        Following.click()
        following = self.get_people()
        Followers = self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]")
        Followers.click()
        followers = self.get_people()
        not_following_back = [user for user in following if user not in followers]
        print(not_following_back)

    def get_people(self):
        sleep(2)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
        prev_height, height = 0, 1
        while prev_height != height:
            prev_height = height
            sleep(3)
            height = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        close = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button")
        close.click()
        return names


my_bot = InstaUnfollowers(username, password)
my_bot.get_unfollowers()
try:
    my_bot.driver.close()
except:
    print("Fail")
    my_bot.driver.close()