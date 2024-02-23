# tweepy-bots/bots/config.py
import tweepy
import logging
import os

logger = logging.getLogger()

def create_api():
    consumer_key = os.getenv("SOLMoG7lKt75JThincqUUbCpO")
    consumer_secret = os.getenv("YE36ydwzSDHNlWobORbdDRU9om0QDyvyRxFm6C98CP7gEvjujt") 
    access_token = os.getenv("818843796846821376-QjSPSAGs2gj6jiHCCJ9Mx9kSAbkyT6t")
    access_token_secret = os.getenv("FB3lA1VHzDFYAJqqHYwDGtfp5U3tOJEbx7Kn8xstguot6")
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    print("Authentication OK")
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created"
    return api
    
# Create API object
