# instagramUnfollowers
This program lets you see the people that are not following a provided account back.
<p align="center">
  <kbd>
  <img src="https://i.imgur.com/qxAqSvD.jpg" alt="drawing" width="250" style="border-radius:50%" align="center"/>
  </kbd>
</p>

## Required packages
Running this will require:
- Selenium
- ChromeDriver
- Chrome

Install them by running these commands in your venv:
```
pip install selenium
pip install webdriver_manager
```

## Set Up
Setting this up is relatively easy. You can either login manually or save your credentials in credentials.py:
```
username = ""
password = ""
```
Set as username the account you want to access Instagram with and as password the password for that account.
Note that you cannot use accounts that are secured by Two-Factor-Authentication with auto-login. I recommend using a new account for auto-login.

If you login manually, you can also use Two-Factor-Authentication.

## Usage
Run the program from followers.py.
The program will first prompt you to enter the account you want to check. Note that the account you want to access has to be public or you have to follow that account.

The program will then ask you for the language Instagram will be opened with. Since I couldn't get a direct XPATH to the elements required somehow, the program uses PARTIAL_LINK_TEXT to access the required elements, which requires localization.

Then, enter how you want to login. If there are no credentials saved or the auto-login fails, the program will also prompt you to login manually.

After that, the program will go through the follower and the followed list, store both of them in sepereate lists, and return a sorted list that contains only the people that don't follow you back.

## Example usage
### Watch on youtube:
[![Watch the video](https://i.imgur.com/R04ORae.png)](https://youtu.be/yH8j8sscMpc)


## Note
For accurate results I recommend using your own account and not another one. While debugging I discovered that when using another account to scan a different account, the people in the list are about 5% less.
