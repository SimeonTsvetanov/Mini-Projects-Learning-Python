from tkinter import *
import pickle
import tweepy
auth = tweepy.OAuthHandler('Change me with: API key',
                           'Change me with: API secret key')
auth.set_access_token('Change me with: Access token',
                      'Change me with: Access token secret')
api = tweepy.API(auth)  # To authenticate the program

"""
Just to make it future proof, this will save the date in pickle file. And delete it after each search.
In case I decide to make something different with the data of the user. In the future.
But at the moment it will not remember anything, but the last searched user.
"""


# Functions:
# This function saves the code to the family.pickle file check the description above to understand why.
def save():
    family_file = open("family.pickle", "wb")
    pickle.dump(family, family_file)
    family_file.close()


# This function will check if there is already data file and if there is none it will create it.
def check():
    global family
    try:
        family_file = open("family.pickle", "rb")
        family = pickle.load(family_file)
    except IOError or EOFError:
        family = []


check()  # call the check function to run the check for the family file.


def get_save_print_user_info():  # As the name this is the main code of the program. It will do almost everything.
    del_all_information()  # First Delete all the information from before
    handle = handle_input.get()  # Pull the @handle name from the input field
    a = False  # yep, there are strange things, happening here. BUT it works this way.
    if handle != "":
        name = handle
        try:
            user = api.get_user(name)
            a = True
        except tweepy.TweepError:
            lbl_interactive["text"] = "Incorrect Twitter @handle, Try again:"  # Adding a message
            handle_input.delete(0, "end")  # Clear the interactive label
            a = False
            pass
        if a:
            user = api.get_user(handle)
            family.append(f"-------------------------Tweeter user Description:-----------------------" + "\n")
            family.append(f"Name: {user.name}, or @{user.screen_name}" + "\n")
            family.append(f"Profile Picture: {user.profile_image_url}" + "\n")
            if not user.location:
                family.append(f"Location: Not Provided" + "\n")
            else:
                family.append(f"Location: {user.location}" + "\n")
            family.append(f"Followers: {user.followers_count}" + "\n")
            family.append(f"Friends: {user.friends_count}" + "\n")
            family.append(f"Total Tweets: {user.statuses_count}" + "\n")
            if not user.url:
                family.append(f"Website: Not Provided" + "\n")
            else:
                family.append(f"Website: {user.url}" + "\n")
            if user.description == "":
                family.append(f"Description: Not Provided" + "\n")
            else:
                family.append(f"Description: {user.description}" + "\n")
            username = user.screen_name
            tweets = api.user_timeline(screen_name=username)
            last_tweets = [tweet for tweet in tweets]  # Create list with the last Tweets
            max_tweets_count = 5  # how many tweets will be printed: change the number for more than 5
            if user.statuses_count == 0:  # Check if any tweets
                pass
            else:  # If there are tweets, Print them in that order:
                family.append("-------------------------------Last Tweets:------------------------------" + "\n")
                counter = 0  # counter is part of the extra functionality to decide how many tweets to print
                for item in last_tweets:  # Printing the tweets
                    if item != "":  # just to make sure that there are no mistakes. We are too deep for that.
                        family.append(f"On: {item.created_at}: User Tweeted:" + "\n")  # First print - the tweet date :)
                        family.append(f"{item.text}" + "\n")  # Second print - the Tweet itself.
                        family.append(f"- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
                        counter += 1
                        if counter == max_tweets_count:  # Extra - you can print more tweets (up to 200)
                            break
            save()  # save the family file
            update_all_information()  # Update the handle list, so ti will be clean. And then change the message:
            lbl_interactive["text"] = "To search again: Enter the Twitter account @handle and press Search."
            handle_input.delete(0, "end")  # Clear the interactive label
    else:  # in case user has clicked the Search button, without adding any name first:
        lbl_interactive["text"] = "You need to add the Twitter @username first."  # Adding a message


def del_all_information():  # Delete all the information.
    family.clear()  # This will clear the whole file.
    save()  # Save the file cleaned.
    update_all_information()  # Update the information list, so ti will be clean.


def show_all():  # Show All the information for the Tweeter user.
    clear_all_information()  # Clear the list from all the prev. user information
    for task in family:  # Update the Task List if update is needed.
        user_info_textbox.insert("end", task)


def update_all_information():
    clear_all_information()  # Clear the list from all the prev. items.
    for task in family:  # Update the user information list if update is needed.
        user_info_textbox.insert("end", task)  # insert all the information


def clear_all_information():  # Clear the task list. Otherwise it overpopulates.
    user_info_textbox.delete(1.0, END)


# GUI

# Create the Window
window = Tk()

# Change the Window Background color
window.configure(bg="gray")

# Change the title
window.title("Tweeter User Accounts Reviewer")

# Change the window size:
window.geometry("602x560")

# This is the interactive visual label
lbl_interactive = Label(window, text='Enter the Twitter account @handle and press: Search or hit Enter.'
                                     '', bg="light gray", width=85)
lbl_interactive.grid(row=0, column=0, columnspan=2)

# Text input field for the @handle input
handle_input = Entry(window, width=65, bg="white", border=4)
handle_input.grid(row=2, column=0)

# Button Search
btn_search = Button(window, text="Search", bg="black", fg="white", border=1, width="27",
                    command=get_save_print_user_info)
btn_search.grid(row=2, column=1)

# Add the Enter button to work the same way as pressing search
window.bind("<Return>", (lambda event: get_save_print_user_info()))

# Show all the User information as a Text Box.
user_info_textbox = Text(window, width=73, height=31, border=8, bg="light gray", fg="black", wrap=WORD)
user_info_textbox.grid(row=3, column=0, rowspan=10, columnspan=2)


if __name__ == '__main__':
    window.mainloop()  # Start The main Window.
    save()  # Run the save function.
