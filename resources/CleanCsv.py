import pandas as pd
from datetime import datetime

def main():

    emma_tweets_csv = '/Users/varalakshmi.venkatraman/WSR/source_file/emma_tweets.csv'
    data = pd.read_csv(emma_tweets_csv)
    data.to_csv('/Users/varalakshmi.venkatraman/WSR/target_file/emma_tweets_filtered.csv',index=False)

if __name__=='__main__':
    main()
