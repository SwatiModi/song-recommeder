# song-recommeder
> *"A simple song recommender using python and GUI using Tkinter."*

## Table of Contents
* [Installation](#installation)
* [Data](#data)
* [Usage](#usage)
* [Examples](#examples)

### Installation
##### 1. Download the repository

Clone the base repository onto your desktop with `git` as follows:
```console
$ git clone https://github.com/SwatiModi/song-recommeder.git
```

##### 2. Install necessary dependencies

```console
$ pip install -r requirements.txt
```

### Data 

We will use subset of **Million Songs Dataset**. It is a mixture of songs from various websites with the rating that users gave after listening to the song.<br>
It contains of two files, ***triplet_file.txt*** and ***song_data.csv***<br> 
The ***triplet_file*** contains *user_id*, *song_id* and *listen count*<br>
The ***songdata_file*** contains *song_id*, *title*, *release_by* and *artist_name*<br> 

Get the data as follows: 

```console
$ wget https://static.turi.com/datasets/millionsong/10000.txt
$ wget https://static.turi.com/datasets/millionsong/song_data.csv
```

### Usage

To launch the app, launch it as follows:

```console
$ python app.py
```
![](/Screenshots/GUI.png)

### Examples
#### *Whats Popular today?*
![](/Screenshots/popularity_based_recommendations.png)


#### *What about Content Based Recommendations?*
![](/Screenshots/Content_based_recommendations.png)


#### *How about Collaborative filtering based Recommendations ?*
![](/Screenshots/Collaborative_filtering.png)
