# encoding=utf-8

import jieba
import numpy as np
import pandas as pd
from collections import Counter
import json
jieba.set_dictionary("/Users/peternapolon/desktop/dict.txt.big.txt")

rawdata=pd.read_csv("/Users/peternapolon/desktop/carousell_project/analysis/data/test.csv",encoding='utf-8')

'''
l=[]
for i in mydata['item_title']:
    #刪掉 on carousell
    i=i[:-12]
    
    #將title切分
    seg_list= jieba.cut(i, cut_all=False)
    l.append(','.join(seg_list))
    
mydata['newtitle']=l
#print mydata.head(10)
'''

#print rawdata['avg_weekly_likes'].describe()[6]

def split_to_words_list(n,t):
    mydata=rawdata[(rawdata.item_category==n) & (rawdata.post_weeks_to_now<=t)]
    l=[]
    for i in mydata['item_title']:
        #刪掉 on carousell
        i=i[:-12]
        seg_list= jieba.lcut(i, cut_all=False)
        for j in seg_list:
            g=0
            for k in j:
                if u'\u4e00' <= k and k <= u'\u9fff':
                    g=g+1
                else:
                    continue
            if g>0:
                l.append(j)

    temp=Counter(l).most_common()
    f=file('/Users/peternapolon/desktop/carousell_project/analysis/data/'+n+'_words_'+t+'weeks.csv','w')
    for x in temp:
        y1=x[0].encode('utf-8')
        y2=str(x[1])
        y2=y2.encode('utf-8')
        f.write(y1+','+y2+'\n')
    print 'The keywords list of '+n+' is ready!'

def split_to_contents_list(n):
    mydata=rawdata[rawdata['item_category']==n]
    l=[]
    for i in mydata['item_description']:
        try:
            seg_list= jieba.lcut(i, cut_all=False)
            for j in seg_list:
                g=0
                for k in j:
                    if u'\u4e00' <= k and k <= u'\u9fff':
                        g=g+1
                    else:
                        continue
                if g>0:
                    l.append(j)
        except:
            print i
    temp=Counter(l).most_common()
    f=file('/Users/peternapolon/desktop/carousell_project/analysis/data/'+n+'_contents.csv','w')
    for x in temp:
        y1=x[0].encode('utf-8')
        y2=str(x[1])
        y2=y2.encode('utf-8')
        f.write(y1+','+y2+'\n')
    print 'The description list of '+n+' is ready!'

def split_to_contents_list_A(n):
    mydata=rawdata[rawdata['item_category']==n]
    mmode=rawdata['avg_weekly_likes'].describe()[6]
    mydata=mydata[mydata['avg_weekly_likes'] >= mmode]
    l=[]
    for i in mydata['item_description']:
        try:
            seg_list= jieba.lcut(i, cut_all=False)
            for j in seg_list:
                g=0
                for k in j:
                    if u'\u4e00' <= k and k <= u'\u9fff':
                        g=g+1
                    else:
                        continue
                if g>0:
                    l.append(j)
        except:
            print i
    temp=Counter(l).most_common()
    f=file('/Users/peternapolon/desktop/carousell_project/analysis/data/'+n+'_contents_A.csv','w')
    for x in temp:
        y1=x[0].encode('utf-8')
        y2=str(x[1])
        y2=y2.encode('utf-8')
        f.write(y1+','+y2+'\n')
    print 'The description list of '+n+' is ready!'

def split_to_contents_list_B(n):
    mydata=rawdata[rawdata['item_category']==n]
    mmode=rawdata['avg_weekly_likes'].describe()[6]
    mydata=mydata[mydata['avg_weekly_likes'] < mmode]
    l=[]
    for i in mydata['item_description']:
        try:
            seg_list= jieba.lcut(i, cut_all=False)
            for j in seg_list:
                g=0
                for k in j:
                    if u'\u4e00' <= k and k <= u'\u9fff':
                        g=g+1
                    else:
                        continue
                if g>0:
                    l.append(j)
        except:
            print i
    temp=Counter(l).most_common()
    f=file('/Users/peternapolon/desktop/carousell_project/analysis/data/'+n+'_contents_B.csv','w')
    for x in temp:
        y1=x[0].encode('utf-8')
        y2=str(x[1])
        y2=y2.encode('utf-8')
        f.write(y1+','+y2+'\n')
    print 'The description list of '+n+' is ready!'


'''
split_to_words_list('women-s-fashion-4',1)
split_to_words_list('men-s-fashion-3',1)
split_to_words_list('luxury-20',1)
split_to_words_list('health-beauty-11',1)

split_to_contents_list('women-s-fashion-4')
split_to_contents_list('men-s-fashion-3')
split_to_contents_list('luxury-20')
split_to_contents_list('health-beauty-11')

split_to_contents_list_A('women-s-fashion-4')
split_to_contents_list_A('men-s-fashion-3')
split_to_contents_list_A('luxury-20')
split_to_contents_list_A('health-beauty-11')

split_to_contents_list_B('women-s-fashion-4')
split_to_contents_list_B('men-s-fashion-3')
split_to_contents_list_B('luxury-20')
split_to_contents_list_B('health-beauty-11')
'''

mensdata=rawdata[rawdata['item_category']=='men-s-fashion-3']
othersdata=rawdata[rawdata['item_category']!='men-s-fashion-3']

#Pick top n keywords in selected group
#--input: A selected group with type of dataframe, and number n you want to pick up
#--output: Top keywords list of titles in selected group
def pick_keywords(df,n):
    # Get All keywords by jieba
    l=[]
    for j in df['item_title']:
        # Delete "on carousell"
        j=j[:-12]
        seg_list= jieba.lcut(j, cut_all=False)
        l=[i for i in seg_list if len(i)>1]
        for k in seg_list:
            g=0
            for t in k:
                if u'\u4e00' <= t and t <= u'\u9fff':
                    g=g+1
                else:
                    continue
            if g>0:
                l.append(k)
            elif len(t)>1:
                l.append(k)
            else:
                continue
    # Calculate frequencies of all keywords, and sort them by frequency
    titlelist=[]
    timeslist=[]
    for q in l:
        titlelist.append(q)
        timeslist.append(l.count(q))
    df=pd.DataFrame({'title':titlelist,'times': timeslist})
    df=df.sort(columns='times', ascending= False)
    df=df.drop_duplicates(subset='title', keep='first')

    # Find top n keywords
    flist=df['title'][0:n]
    return flist

#Creates a table that counts the number of keyword occurrences for titles of selected groups
#--input: A selected group with type of dataframe, and list of top keywords, and a tag x for further classification
#--output: A dataframe includes tag x and the number of keyword occurrences for all titles
def Count_table(df,li,n):
    arr=np.array([],dtype=float)
    new=[]
    t=0
    for x in df['item_title']:
        seg_list= jieba.lcut(x, cut_all=False)
        for y in li:
            for z in seg_list:
                if y==z:
                    t=t+1
            new.append(t)
            t=0
    arr=np.array(new,dtype=float)
    arr.shape=len(df['item_title']),len(li)
    ndf=pd.DataFrame(arr, columns=li)
    ndf['Y']=n
    return ndf
  
A = Count_table(rawdata[rawdata['item_category']!='luxury-20'],pick_keywords(rawdata,1001),'N')
B = Count_table(rawdata[rawdata['item_category']=='luxury-20'],pick_keywords(rawdata,1001),'Y')

final=pd.concat([A, B],axis=0)
final.to_csv(path_or_buf='test01.csv',sep=',', encoding='utf-8')