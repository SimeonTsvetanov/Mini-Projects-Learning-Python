# Welcome to the Tweeter-Profile-Reviewer

***
This project was created as part of a assignment from [Softuni](https://softuni.bg/), during the Python Fundamentals Course.


### The aim of the Project was to create a Twitter Profile Reviewer App with Python. That runs in its own GUI.
When started, the program will present you, with a interactive help lbl(on the top of the screen),asking you to add the Tweeter account name @handle and to press search.
Once done,It will present you with basic information of the searched user and their last several tweets.

To run the program you will need to import:
- [tweepy](https://www.tweepy.org/) - In order to pull the details from Tweeter (Be aware you will need to install tweepy in the python env.)
- [tkinter](https://wiki.python.org/moin/TkInter) - For the GUI of the application. (integrated in Python)
- [pickle](https://docs.python.org/3/library/pickle.html) - for saving files in the system (integrated in Python)

Next -> you need to have a Tweeter Developer App(API key, API secret key, Access token and Access token secret)
If you haven't done that before. click [here](https://developer.twitter.com/en/apps) to create accaunt and get it.
Next -> download or copy the code from: [Tweeter_Account_review.py](https://github.com/SimeonTsvetanov/Mini-Projects-Learning-Python/blob/master/Tweeter-Profile-Scraper/Tweeter_Account_review.py)
and run it in your system.
If you are more intrested in how the code works. I have created comments for everything in the code.

### The program has very basic menu with 4 Main Elements: ###
- ***Interactive Label***: It will help the user with information text. Which changes, depending on the state of the program.
- ***Input text field***: To get the input of the user.
- ***Search button***: Well, you know what is that. (Added extra function to use the RETURN key on the keyboard, to do the same thing)
- ***Text Field***: To input all the information that we have found for the user in Tweeter :) 

The program is using pickle for storing only THE LAST input @handle (user), It is not needed at this moment, but If you decide to, keep more information in the future. Just add extra functions and do it. On run the app will create the “family.pickle” file In your system directory if one is needed. 

Check this image(samples) of the program GUI, so you can get a better idea:
![first-picture](https://github.com/SimeonTsvetanov/Mini-Projects-Learning-Python/blob/master/Tweeter-Profile-Scraper/TPS01.jpg)
![second-picture](https://github.com/SimeonTsvetanov/Mini-Projects-Learning-Python/blob/master/Tweeter-Profile-Scraper/TPS02.jpg)
