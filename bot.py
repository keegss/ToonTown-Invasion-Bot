import tweepy
import sched

from api import *
from secret import *

def update_forever(sc, tweet, currentInvasions):

    invasions = retrieve_invasions()

    # post when an invasion begins
    for district, data in invasions.items():

        if district not in currentInvasions:
            print('%ss have taken over ToonTown (%s)!' % (data['type'], district))
            currentInvasions[district] = data

    # post when an invasions ends
    for district, data in list(currentInvasions.items()):
        if district not in invasions:
            print('The %s invasion has ended! (%s)' % (data['type'], district))
            del(currentInvasions[district])

    sc.enter(30, 1, update_forever, (sc, tweet, currentInvasions))

def setup():

    # setup tweep
    auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
    auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
    tweet = tweepy.API(auth)

    # assume no current invasions
    currentInvasions = {}

    # scheduler setup
    s = sched.scheduler(time.time, time.sleep)
    s.enter(5, 1, update_forever, (s, tweet, currentInvasions))
    s.run()


if __name__ == "__main__":
    setup()
