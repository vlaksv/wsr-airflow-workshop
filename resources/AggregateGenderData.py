import pandas as pd
from datetime import datetime

def main():

    source_csv = '/Users/varalakshmi.venkatraman/WSR/source_file/emma_tweets.csv'
    data = pd.read_csv(source_csv)
    data.to_csv('/Users/varalakshmi.venkatraman/WSR/target_file/agg_gender_diversity.csv',index=False)

if __name__=='__main__':
    main()
