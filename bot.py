import os
import tweepy
import sched

from api import *

def update_forever(sc, tweet, currentInvasions):

    invasions = retrieve_invasions()

    # post when an invasion begins
    for district, data in invasions.items():

        if district not in currentInvasions:
            tweet.update_status('%ss have taken over ToonTown (%s)!' % (data['type'], district))
            currentInvasions[district] = data

    # post when an invasions ends
    for district, data in list(currentInvasions.items()):
        if district not in invasions:
            tweet.update_status('The %s invasion has ended! (%s)' % (data['type'], district))
            del(currentInvasions[district])

    sc.enter(30, 1, update_forever, (sc, tweet, currentInvasions))

def setup():

    # setup tweep
    auth = tweepy.OAuthHandler(os.environ.get('C_KEY'), os.environ.get('C_SECRET'))
    auth.set_access_token(os.environ.get('A_TOKEN'), os.environ.get('A_TOKEN_SECRET'))
    tweet = tweepy.API(auth)

    # assume no current invasions
    currentInvasions = {}

    # scheduler setup
    s = sched.scheduler(time.time, time.sleep)
    s.enter(5, 1, update_forever, (s, tweet, currentInvasions))
    s.run()


if __name__ == "__main__":
    setup()
