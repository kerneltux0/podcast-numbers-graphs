#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 17:46:11 2018

@author: inspirationflow
"""

#print(data.columns)

import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('/home/inspirationflow/Projects/Podcasts/HOVPodcast/Numbers/CSVs/Vimeo/Last_Month/vimeo_device_stats.csv')

#print(data.columns)

dev_plays = data['plays']
dev_dls = data['downloads']
dev_name = data['device_type']
dev_perc = data['mean_percent']

plt.figure(figsize=(20,20))
plt.bar(dev_name, dev_plays)
ax = plt.gca()
#ax.set_ylim([])
plt.savefig('/home/inspirationflow/Projects/Podcasts/HOVPodcast/Numbers/Graphs/Vimeo/Last_Month/graph_device_plays.png')

plt.figure(figsize=(20,20))
plt.bar(dev_name, dev_dls)
ax = plt.gca()
#ax.set_ylim([])
plt.savefig('/home/inspirationflow/Projects/Podcasts/HOVPodcast/Numbers/Graphs/Vimeo/Last_Month/graph_device_downloads.png')

plt.figure(figsize=(20,20))
plt.bar(dev_name, dev_perc)
ax = plt.gca()
#ax.set_ylim([])
plt.savefig('/home/inspirationflow/Projects/Podcasts/HOVPodcast/Numbers/Graphs/Vimeo/Last_Month/graph_device_percentage.png')
