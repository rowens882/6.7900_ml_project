import pandas as pd
import re

#Remove hyperlinks, hashtag symbols, @username, and retweet text
def clean_tweets(tweets):
    if type(tweets) == str:   
        tweets = re.sub(r'https?:\/\/.\S+', "", tweets)
        tweets = re.sub(r'#', '', tweets)
        tweets = re.sub('@[^\s]+','',tweets)
        tweets = re.sub(r'^RT[\s]+', '', tweets)

    return(tweets)


election_df = pd.read_excel('elections_with_tweets.xlsx')
print("Before cleaning:")
print(election_df['Tweets - Union'].head(10))

election_df['Tweets - General'] = election_df['Tweets - General'].apply(clean_tweets)
election_df['Tweets - Union'] = election_df['Tweets - Union'].apply(clean_tweets)
election_df['Tweets - Labor Org'] = election_df['Tweets - Labor Org'].apply(clean_tweets)
election_df['Tweets - Case Name'] = election_df['Tweets - Case Name'].apply(clean_tweets)
print("After cleaning:")
print(election_df['Tweets - Union'].head(10))

election_df.to_excel("elections_with_cleaned_tweets.xlsx")