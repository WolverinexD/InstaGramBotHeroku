""" Quickstart script for InstaPy usage """
# imports
from instapy import InstaPy
from instapy import smart_run
from config import usernaam, userpass 
import schedule
import time
import pyfiglet







# login credentials
insta_username = ''  # <- enter username here
insta_password = ''  # <- enter password here
# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background







def banner():
    ascii_banner = pyfiglet.figlet_format("VAIBHAV OP!!")
    print(ascii_banner)








# session = InstaPy(username=usernaam, password=userpass, headless_browser=True)
banner()

def job():
    print("STARTED WORKING")
    session = InstaPy(username=usernaam, password=userpass, headless_browser=False)
    with smart_run(session):
        """ Activity flow """


        # general settings
        #sets the percentage of people you want to follow
        session.set_do_follow(True, percentage=30)

        #sets the percentage of posts you want to comment
        session.set_do_comment(True, percentage=90)

        #list of random comments you want to post
        session.set_comments(["🥲😂", "😊😉", "😋👍", "Follow Mehh Plz... 🥲", "Noice😋👍", "Plz...Help Mehh Complete 1k Follwoers😋👍", "Follow me if you fancy being second...🤪", "You may follow me.", "Do it Now. Sometimes ‘Later’ Becomes Never", "Koi Follow kerlo plz... 🥲"])

        #setting quotas for the daily and hourly action(I said it's smart)
        session.set_quota_supervisor(enabled=True, peak_comments_daily=250, peak_comments_hourly=30, peak_likes_daily=250, peak_likes_hourly=30,sleep_after=['likes', 'follows', 'unfollows', 'server_calls'])

        #again some set of configuration which figures out whom to follow
        session.set_relationship_bounds(enabled=True, delimit_by_numbers=True, min_followers=500, min_following=2)

        #tags to get posts from and amout is the actions you want 
        session.like_by_tags(["followback", "instagram", "fyp", "love", "style", "explore", "k", "photoshoot", "photographer", "india", "pubgindia", "bgmi","viral", "explorepage", "loveyourself", "bhfyp"], amount=20)



        session.set_dont_unfollow_active_users(enabled=True, posts=1)
        session.unfollow_users(amount = 11, nonFollowers=True, style="LIFO") 

        session.end()





schedule.every().day.at("16:14").do(job)
schedule.every().day.at("07:30").do(job)


while True:
    schedule.run_pending()
    time.sleep(1)
