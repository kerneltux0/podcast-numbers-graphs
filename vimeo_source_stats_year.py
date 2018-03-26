#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 18:15:15 2018

@author: inspirationflow
"""

import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('/home/inspirationflow/Projects/Podcasts/HOVPodcast/Numbers/CSVs/Vimeo/Last_Year/vimeo_source_stats.csv')

#print(data.columns)

src_plays = data['plays']
src_dls = data['downloads']
src_name = data['domain']
src_perc = data['mean_percent']

plt.figure(figsize=(100,20))
plt.bar(src_name, src_plays)
ax = plt.gca()
#ax.set_ylim([0,30])
plt.savefig('/home/inspirationflow/Projects/Podcasts/HOVPodcast/Numbers/Graphs/Vimeo/Last_Year/graph_source_plays.png')

plt.figure(figsize=(100,20))
plt.bar(src_name, src_dls)
ax = plt.gca()
#ax.set_ylim([])
plt.savefig('/home/inspirationflow/Projects/Podcasts/HOVPodcast/Numbers/Graphs/Vimeo/Last_Year/graph_source_downloads.png')

plt.figure(figsize=(100,20))
plt.bar(src_name, src_perc)
ax = plt.gca()
ax.set_ylim([0,100])
plt.savefig('/home/inspirationflow/Projects/Podcasts/HOVPodcast/Numbers/Graphs/Vimeo/Last_Year/graph_source_percentage.png')