#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 16:32:01 2018

@author: inspirationflow
"""

import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as plticker



data = pd.read_csv('/home/inspirationflow/Projects/Podcasts/HOVPodcast/Numbers/CSVs/Vimeo/Last_Year/vimeo_region_stats.csv')

#print(data.columns)
region_names = data['name']
region_plays = data['plays']
region_dls = data['downloads']
region_perc = data['mean_percent']

#region_plays_use = pd.to_numeric(region_plays, errors='ignore')

plt.figure(figsize=(100,25))
plt.bar(region_names, region_plays)
ax = plt.gca()
#loc = plticker.MultipleLocator(base=1.0) # this locator puts ticks at regular intervals
#ax.yaxis.set_major_locator(loc)
plt.savefig('/home/inspirationflow/Projects/Podcasts/HOVPodcast/Numbers/Graphs/Vimeo/Last_Year/graph_region_plays.png')

plt.figure(figsize=(100,25))
plt.bar(region_names, region_dls)
ax = plt.gca()
#ax.set_ylim([])
plt.savefig('/home/inspirationflow/Projects/Podcasts/HOVPodcast/Numbers/Graphs/Vimeo/Last_Year/graph_region_downloads.png')

plt.figure(figsize=(100,25))
plt.bar(region_names, region_perc)
ax = plt.gca()
ax.set_ylim([0,100])
plt.savefig('/home/inspirationflow/Projects/Podcasts/HOVPodcast/Numbers/Graphs/Vimeo/Last_Year/graph_region_percentage.png')


