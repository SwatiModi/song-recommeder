from tkinter import *  
import tkinter
from PIL import ImageTk,Image,ImageFilter,ImageChops 
import pandas as pd
import numpy as np
import os
import sys
from sklearn.externals import joblib
from sklearn.model_selection import train_test_split
import Recommenders as Recommenders
from tkinter import ttk

song_df_1 = pd.read_table("triplets_file.txt",header=None)
song_df_1.columns = ['user_id', 'song_id', 'listen_count']
song_df_2 =  pd.read_csv('song_data.csv')
song_df = pd.merge(song_df_1, song_df_2.drop_duplicates(['song_id']), on="song_id", how="left")
song_df = song_df.head(10000)
#Merge song title and artist_name columns to make a merged column
song_df['song'] = song_df['title'].map(str) + " - " + song_df['artist_name']
song_grouped = song_df.groupby(['song']).agg({'listen_count': 'count'}).reset_index()
grouped_sum = song_grouped['listen_count'].sum()
song_grouped['percentage']  = song_grouped['listen_count'].div(grouped_sum)*100
song_grouped.sort_values(['listen_count', 'song'], ascending = [0,1])
# print(song_df.head())
users = song_df['user_id'].unique()
# print(len(users)) ## return 365 unique users
songs = song_df['song'].unique()
# print(len(songs)) ## return 5151 unique songs
train_data, test_data = train_test_split(song_df, test_size = 0.20, random_state=0)

GUI = Tk()  
GUI.title("Music Recommendation System")
GUI.geometry('500x180')
# GUI.wm_iconbitmap('song.ico')
lbl = Label(GUI, text = "Music Recommender System",font=("Times New Roman", 20))
lbl.grid(row=0,column=0,padx=(30, 10),pady=(10 ,10))

lbl = Label(GUI, text = "Enter the USER_ID and SONG_NAME",font=("Times New Roman", 12))
lbl.grid(row=1,column=0,padx=(40, 20),pady=(5 ,0))

def Popularity():
	None

def similar_song():
	None

def user_based():
	None

frame = ttk.Frame(GUI, padding=10)
frame.grid(row=2,column=0)

global user_id_val
global song_name_val
global user_id
global song_name

user_id = None
song_name = None
user_id_val = None
song_name_val = None

lbl1 = Label(frame, text = "USER ID",font=("Times New Roman", 9))
lbl1.grid(row=3,column=1,padx=(130, 10),pady=(10 ,5))
entry = Entry(frame, width=8)
entry.grid(row=4,column=1,padx=(130, 10))
user_id = entry

lbl2 = Label(frame, text = "SONG NAME",font=("Times New Roman", 9))
lbl2.grid(row=3,column=2,padx=(90, 10),pady=(10 ,5))
entry = Entry(frame, width=8)
entry.grid(row=4,column=2,padx=(90, 10))
song_name = entry

btn1 = ttk.Button(frame,text = 'Popularity', command=Popularity)
btn1.grid(row=5,column=1,padx=(10, 0),pady=(10 ,10))

btn2 = ttk.Button(frame,text = 'Similar Songs', command=similar_song)
btn2.grid(row=5,column=2,padx=(10, 10),pady=(10 ,10))

btn3 = ttk.Button(frame,text = 'User Based', command=user_based)
btn3.grid(row=5,column=3,padx=(0, 10),pady=(10 ,10))

GUI.mainloop()  