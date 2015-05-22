# Antonio Rios
# 9-30-2014
# CS126
# Lab 5
###########################


# import modules
from time import time
from time import sleep

# declare a global variable
global tweets

# assign an empty dictionary to the global variable
tweets = {}



def update_func(status, audience_list, userid):
    """
    The update_func() function updates the tweets dictionary by
    checking if the post time of the tweet and if it exists it updates
    the new tweet for the user with the new status. If the post time of
    the tweet does not exist in the dictionary then it gets added to tweets
    dictionary.

    paramaters: STRING type status, audience_list, and userid
    returns: The function returns the post time of the tweet which is a FLOAT type number.                

    """

    # declare a variable and assign it the curent time the message was posted
    post_time = time()  # time() Returns the time in seconds since the epoch as a floating point number.

    # check if the time is in the dictionary
    if post_time in tweets:
            
        sleep(1)            # wait for one second
        post_time = time()  # get current time the message was posted
        
        # create a dictionary entry with the value in post_time as the key
        tweets[post_time] = {userid: {'status': status,                 # nested dictionary
                                      'audience': audience_list,
                                      'time':post_time}}
    # If post_time is not in tweets then it is
    # added to the tweets dictionary
    else:
        
        tweets[post_time] = {userid: {'status': status,
                                      'audience': audience_list,
                                      'time':post_time}}

    # The update_func() function returns the post_time of the tweet
    return post_time


def display(userid, time_posted):
    """Prints the tweetsfor the given userid and time."""


    # declare and assign the string message that will be formatted with
    # the proper variables.
    message = """
Time:{0}
Groups: {1}
{2} says:
{3}
""".format(tweets[time_posted][userid]['time'],
           tweets[time_posted][userid]['audience'], userid,
           tweets[time_posted][userid]['status'])

    print(message)  # print the message to console

# test code
p = update_func("Storming the village at 9. Anyone interested?",
                ["Zombies", "Vampires"],
                "BarnabasCollins")

q = update_func("Can I come?",
                ["Vampires"],
                "Casper")

r = update_func("Forgot to include the ghost! LOL",
                ["Ghosts"],
                "BarnabasCollins")

s = update_func("Lots of villagers with forks here...",
                ["Vampires", "Zombies", "Ghosts"], "BarnabasCollins")

display("BarnabasCollins", r)
print("----------------")
display("Casper", q)
