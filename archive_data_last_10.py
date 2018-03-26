
import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_csv('/home/inspirationflow/Projects/Podcasts/HOVPodcast/Numbers/CSVs/Archive.org/Last-10/archive-last-10.csv')

print(data.columns)

data.dls = data['downloads']
data.title = data['title']

plt.bar(data.title, data.dls)
ax = plt.gca()
ax.set_xlabel('Episode')
ax.set_ylabel('Downloads')
plt.savefig('/home/inspirationflow/Projects/Podcasts/HOVPodcast/Numbers/Graphs/Archive.org/Last-10/graph_last_10.png')

