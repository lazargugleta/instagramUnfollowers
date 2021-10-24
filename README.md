# instagramUnfollowers
This is a fork of lazargugleta/instagramUnfollowers, which I updated to add functionality and remove deprecated statements.

## Required packages
Running this will require:
- Selenium
- ChromeDriver
- Chrome

## Set Up
Setting this up is relatively easy. Open credentials.py and you will find this:
```
username = ""
password = ""
```
Set as username the account you want to access and as password the password for that account.
Note that you cannot use accounts that are secured by Two-Factor-Authentication.

I recommend creating a new account and use that for this program.

## Usage
Run the program from followers.py.
The program will first prompt you to enter the account you want to check. Note that the account you want to access has to be public or you have to follow that account.

The program will then ask you for the language Instagram will be opened with. Since I couldn't get a direct XPATH to the elements required somehow, the program uses PARTIAL_LINK_TEXT to access the required elements, which requires localization.

After that, the program will go through the follower and the followed list, store both of them in sepereate lists, and return a sorted list that contains only the people that don't follow you back.

## Note
This program is unfortunately a bit unaccurate, because Instagram doesn't seem to show all users in the specific lists. (about 5% less). Aside that it is very accurate.
