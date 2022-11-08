import openai, tweepy, random, config


# Twitter API credentials
api_key=config.twitter_api_key
api_key_secret =config.twitter_api_key_secret
access_token=config.access_token
access_token_secret=config.access_token_secret


#OpenAI API credentials
openai.api_key =config.open_ai_key

# Connecting to Twitter
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

print("Connected to Twitter")

# # Creating Tweets
prompts = [
    {
        "hashtag": "#softwaredeveloper",
        "text": "I want to become a bettter developer"
    },
]

# def __init__(self):
#     error = 1
#     while(error == 1):
#         tweet = self.create_tweet()
#         try:
#             error = 0
#             self.api.update_status(tweet)
#         except:
#             error = 1

def create_tweet():
    chosen_prompt = random.choice(prompts)
    text = chosen_prompt["text"]
    hashtags = chosen_prompt["hashtag"]

    response = openai.Completion.create(
        engine="text-davinci-001",
        prompt=text,
        max_tokens=50,
    )

    tweet = response.choices[0].text
    tweet = tweet + " " + hashtags + " " + "#ai #openai #gpt3"
    return tweet

tweet = create_tweet()
api.update_status(tweet)