#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 16:32:01 2018

@author: inspirationflow
"""

import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('/home/inspirationflow/Projects/Podcasts/HOVPodcast/Numbers/CSVs/Vimeo/Last_Month/vimeo_region_stats.csv')

#print(data.columns)
region_names = data['name']
region_plays = data['plays']
region_dls = data['downloads']
region_perc = data['mean_percent']

plt.figure(figsize=(25,25))
plt.bar(region_names, region_plays)
ax = plt.gca()
ax.set_ylim([0,10])
plt.savefig('/home/inspirationflow/Projects/Podcasts/HOVPodcast/Numbers/Graphs/Vimeo/Last_Month/graph_region_plays.png')

plt.figure(figsize=(25,25))
plt.bar(region_names, region_dls)
ax = plt.gca()
#ax.set_ylim([])
plt.savefig('/home/inspirationflow/Projects/Podcasts/HOVPodcast/Numbers/Graphs/Vimeo/Last_Month/graph_region_downloads.png')

plt.figure(figsize=(25,25))
plt.bar(region_names, region_perc)
ax = plt.gca()
ax.set_ylim([0,100])
plt.savefig('/home/inspirationflow/Projects/Podcasts/HOVPodcast/Numbers/Graphs/Vimeo/Last_Month/graph_region_percentage.png')


