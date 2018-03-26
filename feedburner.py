# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('/home/inspirationflow/Projects/Podcasts/HOVPodcast/Numbers/CSVs/Feedburner/feedStats.csv')

sub_data = data[['Day', 'Subscribers']]
sub_data.plot()
ax = plt.gca()
ax.set_xlabel("Date")
ax.set_xlim([0,31])
plt.savefig('/home/inspirationflow/Projects/Podcasts/HOVPodcast/Numbers/Graphs/Feedburner/graph_subs.png')

reach_data = data[['Day', 'Reach']]
reach_data.plot()
ax = plt.gca()
ax.set_xlabel("Date")
ax.set_xlim([0,31])
plt.savefig('/home/inspirationflow/Projects/Podcasts/HOVPodcast/Numbers/Graphs/Feedburner/graph_reach.png')

click_data = data[['Day', 'Clickthroughs']]
click_data.plot()
ax = plt.gca()
ax.set_xlabel("Date")
ax.set_xlim([0,31])
plt.savefig('/home/inspirationflow/Projects/Podcasts/HOVPodcast/Numbers/Graphs/Feedburner/graph_click.png')

