import news_db as db
import pandas as pd
import math

def get_all():
    items= db.get_all()
    news_item=""

    for i in items:
        news_item+=str(i[2])+"\n"
        news_item+=str(i[1])+"\n\n"

    return news_item

def update():
    df=pd.read_csv('data/news.csv',engine='python')
    for i, j in df.iterrows(): 
        if math.isnan(float(j[0])):
            pass
        else:
            story=j[1]
            datepub=j[2]

            db.insert(story,datepub)

if __name__ == '__main__':
    print(len(get_all()))