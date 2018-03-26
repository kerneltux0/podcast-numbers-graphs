#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 16:53:02 2018

@author: inspirationflow
"""

#print(data.columns)

import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('/home/inspirationflow/Projects/Podcasts/HOVPodcast/Numbers/CSVs/Vimeo/Last_Month/vimeo_video_stats.csv')

useful = data.loc[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]

video_plays = useful['plays']
video_dls = useful['downloads']
video_name = useful['name']
video_perc = useful['mean_percent']


plt.figure(figsize=(20,20))
plt.bar(video_name, video_plays)
ax = plt.gca()
#ax.set_ylim([])
plt.savefig('/home/inspirationflow/Projects/Podcasts/HOVPodcast/Numbers/Graphs/Vimeo/Last_Month/graph_video_plays.png')

plt.figure(figsize=(20,20))
plt.bar(video_name, video_dls)
ax = plt.gca()
#ax.set_ylim([])
plt.savefig('/home/inspirationflow/Projects/Podcasts/HOVPodcast/Numbers/Graphs/Vimeo/Last_Month/graph_video_downloads.png')

plt.figure(figsize=(20,20))
plt.bar(video_name, video_perc)
ax = plt.gca()
#ax.set_ylim([])
plt.savefig('/home/inspirationflow/Projects/Podcasts/HOVPodcast/Numbers/Graphs/Vimeo/Last_Month/graph_video_percentage.png')


plays_data = data[['name', 'plays']]
#print(plays_data)
#plays_data.plot()