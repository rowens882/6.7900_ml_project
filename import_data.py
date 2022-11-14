import pandas as pd

#import pandas dataframe with NLRB election results and scraped tweets
#tweets are formatted as a column 'Tweets' that has a list of strings
election_df = pd.read_excel('elections_with_tweets.xlsx')
print(election_df.head())