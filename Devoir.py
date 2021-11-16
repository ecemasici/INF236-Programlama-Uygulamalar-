#!/usr/bin/env python
# coding: utf-8
import streamlit as st
import re
import time
import numpy as np
import pandas as pd
from gensim.models import KeyedVectors
from sklearn.metrics.pairwise import cosine_similarity

st.text('Houston, burası Apollo 11... Penceremde Dünya var')
st.title("ASTRONOMİ BİLGİNİNE HOŞ GELDİNİZ!")
st.image('https://yalansavar.files.wordpress.com/2016/12/01-star-power-carl-sagan__800x600_q85_crop_subject_location-530193.jpg')
st.audio('https://www.youtube.com/watch?v=f7Gy3IY7bUM')
st.markdown('Tavsiyelerimiz hazır sen de hazırsan...Cosmos yolculuğumuz başlıyor!') 


Film="""
Ad Astra
Life
Passengers
Apollo 13
Hidden Figures
The Martian
Interstellar
2001: A Space Odyssey
Inspiration4
"""
Kitap="""
Kozmos-Carl SAGAN
Karanlık Bir Dünyada Bilimin Mum Işığı-Carl SAGAN
Broca'nın Beyni-Carl SAGAN
Bir Astronota Sorun-Tım PEAKE
Evren 101-Carolyn C. Petersen
Evren Bir Biyografi-John Gribbin
Zamanın Kısa Tarihi-Stephen Hawking
Zamanın Resimli Kısa Tarihi-Stephen Hawking
Büyük Sorulara Kısa Yanıtlar-Stephen Hawking
Kara Delikler -Stephen Hawking
Kara Delikler ve Bebek Evrenler- Stephen Hawking
Ceviz Kabuğundaki Evren-Stephen Hawking

"""
Ozlusoz="""
Bir yerlerde inanılmaz bir şey keşfedilmeyi bekliyor.-Carl Sagan
Bilim, sadece bir bilgi topluluğundan daha fazlasıdır. Bir düşünme şeklidir, evreni şüphecilikle sorgulamanın bir yoludur.-Carl Sagan
Bilimi açıklamamak bana ahlaksızlık gibi geliyor, Aşık olunca bunu tüm dünyaya duyurmak istersiniz.-Carl Sagan
Eğer tüm evrende yaşam sadece Dünya'da varsa, bu çok büyük bir yer israfı olurdu.-Carl Sagan
İnanmak istemiyorum, bilmek istiyorum.-Carl Sagan
Kanıtın yokluğu, yokluğun kanıtı değildir.-Carl Sagan
DNA’mızdaki nitrojen, dişlerimizdeki kalsiyum, kanımızdaki demir, elmalı turtamızdaki karbon, çöken yıldızların içlerinde yapıldı. Bizler, yıldızların malzemesinden yapıldık."-Carl Sagan
Dinozorlar yok oldu çünkü bir uzay programları yoktu...
"""

categories = [Film,Kitap,Ozlusoz]
categories_name = ["Film","Kitap","Ozlusoz"]

for i in range(len(categories)):
    categories[i] = categories[i].split("\n")
df=[]    
df = pd.DataFrame(df,columns=['sentence','category'])


for i in range(len(categories_name)):
    for k in range(len(categories[i])):
        df = df.append({'sentence': categories[i][k], 'category': categories_name[i]}, ignore_index=True)
    
    df = df[df['sentence']!=""]
    df.reset_index(drop=True, inplace=True)

df["cleaned_sentence"]=df['sentence'].copy()

for i in range(len(df)):
    df["cleaned_sentence"][i] = re.sub('[!@#’‘?.,\'$]', '', df["cleaned_sentence"][i])

    df["cleaned_sentence"][i] = df["cleaned_sentence"][i].lower()
    



def give_a_recomendation():
    result = []
    
    answer=st.text_area('Area for textual entry')
    answer=answer.lower()
  
 

 
    if len(answer.split())>1:
        
        for i in range(len(df)):
            
            a = set(df["cleaned"][i].split()) 
            b = set(answer.split())
            c = a.intersection(b)
            result.append(float(len(c)) / (len(a) + len(b) - len(c)))
          
        pd.DataFrame(result)   
        df['result'] = result
        
        return df[df['result']==df['result'].max()].values[0][0]


    else:
        for i in categories_name:
            i=i.lower()
            if(i==answer):
                return df["sentence"][df["category"].str.lower()==answer].sample(n=1).values[0]
        return df["sentence"].sample(n=1).values[0]   
    
st.markdown(give_a_recomendation())  