from tkinter import *  
import pandas as pd
from sklearn.model_selection import train_test_split
import Recommenders as Recommenders
from tkinter import ttk

# get the data
song_df_1 = pd.read_table("10000.txt",header=None)
song_df_1.columns = ['user_id', 'song_id', 'listen_count']

song_df_2 =  pd.read_csv('song_data.csv')

# merge both files : triplets.txt, metadata.csv
song_df = pd.merge(song_df_1, song_df_2.drop_duplicates(['song_id']), on="song_id", how="left")

# Using a subset, the first 10,000 songs
song_df = song_df.head(10000)

#Merge song title and artist_name columns to make a merged column
song_df['song'] = song_df['title'].map(str) + " - " + song_df['artist_name']

# get listen_count of each song.
song_grouped = song_df.groupby(['song']).agg({'listen_count': 'count'}).reset_index()
grouped_sum = song_grouped['listen_count'].sum()

# popularity based sorting  
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
# GUI.geometry('500x180')
# GUI.wm_iconbitmap('song.ico')
lbl = Label(GUI, text = "Music Recommender System",font=("Times New Roman", 20))
lbl.grid(row=0,column=0,padx=(30, 10),pady=(10 ,10))

lbl = Label(GUI, text = "Enter the USER_ID and SONG_NAME",font=("Times New Roman", 12))
lbl.grid(row=1,column=0,padx=(40, 20),pady=(5 ,0))

def Popularity():
	pop_list = []
	pop_str = ''
	user_id_val = int(user_id.get())
	song_name_val = str(song_name.get())
	# print(song_name_val)
	# print(user_id_val)	
	pm = Recommenders.popularity_recommender_py()
	pm.create(train_data, 'user_id', 'song')
	user_id_ip = users[user_id_val]
	pop_list = pm.recommend(user_id_ip)['song'].tolist()
	pop_str = '\n'.join(pop_list)
	lbl['text'] = pop_str

def similar_song():
	sim_str = ''
	sim_list = []
	user_id_val = int(user_id.get())
	song_name_val = str(song_name.get())
	# print(song_name_val)
	# print(user_id_val)
	is_model = Recommenders.item_similarity_recommender_py()
	is_model.create(train_data, 'user_id', 'song')
	song = song_name_val
	sim_list = is_model.get_similar_items([song])['song'].tolist()
	sim_str = '\n'.join(sim_list)
	lbl['text'] = sim_str
	# print(sim_str)

def user_based():
	user_str = ''
	user_list = []
	user_id_val = int(user_id.get())
	song_name_val = str(song_name.get())
	# print(song_name_val)
	# print(user_id_val)	
	is_model = Recommenders.item_similarity_recommender_py()
	is_model.create(train_data, 'user_id', 'song')
	user_id_ip = users[user_id_val]
	user_items = is_model.get_user_items(user_id_ip)
	user_list = is_model.recommend(user_id_ip)['song'].tolist()
	user_str = '\n'.join(user_list)
	lbl['text'] = user_str
	# print(user_str)

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
lbl1.grid(row=3,column=1,padx=(90, 0))
entry = Entry(frame, width=8)
entry.grid(row=4,column=1,padx=(90, 0))
user_id = entry

lbl2 = Label(frame, text = "SONG NAME",font=("Times New Roman", 9))
lbl2.grid(row=3,column=2,padx=(90, 0))
entry = Entry(frame, width=8)
entry.grid(row=4,column=2,padx=(90, 0))
song_name = entry

btn1 = ttk.Button(frame,text = 'Popularity', command=Popularity)
btn1.grid(row=5,column=1,padx=(10, 0),pady=(10,10))

btn2 = ttk.Button(frame,text = 'Similar Songs', command=similar_song)
btn2.grid(row=5,column=2,padx=(0, 33),pady=(10,10))

btn3 = ttk.Button(frame,text = 'User Based', command=user_based)
btn3.grid(row=5,column=3,padx=(0, 10),pady=(10,10))

GUI.mainloop()  
