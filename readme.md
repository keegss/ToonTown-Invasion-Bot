<h3>ToonTown Rewritten Twitter Bot<h3>

The hardest part about this project is making a Twitter.

To run this program, you must first create a Twitter, apply for a developer account, wait a week for them to accept your application, then create a project with that account. Then on the project details screen, go to the Keys and tokens tab. Now, create a file called secrets.py and place it in this same directory as bot.py. Within that file you must provide the following fields:

```
C_KEY = ""
C_SECRET = ""
A_TOKEN = ""
A_TOKEN_SECRET = ""
```

I already had a twitter, so I created the project on that account, so now I can spam my friends with ToonTown invasion updates. I applied to have the API keys transfered over to a new account to be the dedicated bot. Time to wait another week.

Before you run, open up api.py and change the `'From'` field to your github url, so the people at TTR know where these requests are coming from. You don't have to, but it would be nice.

Now simply run bot.py and voila, invasion udpates every 30 seconds, posted to Twitter.
