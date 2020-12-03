import sys, os
sys.path.append('/var/www/webApp/webApp')

import numpy as np
import pandas as pd
import centres_db as db
import news_db as news_db
import math 


def update_centres():
    df=pd.read_csv('data/phase3_clean.csv',engine='python')
    for i, j in df.iterrows(): 
        if math.isnan(float(j[0])):
            pass
        else:
            province=j[1]
            district=j[2]
            constituency=j[3]
            ward=j[4]
            polling_district_name=j[5]
            polling_station_name=j[6]
            phase=j[7]

            db.insert(province,district,constituency,ward,polling_district_name,polling_station_name,phase)

def update_news():
    df=pd.read_csv('data/news.csv',engine='python')
    for i, j in df.iterrows(): 
        if math.isnan(float(j[0])):
            pass
        else:
            story=j[1]
            datepub=j[2]

            news_db.insert(story,datepub)



def num_items():
    items=news_db.get_all()
    return len(items)

if __name__ == '__main__':
    update_centres()
    print(num_items())

