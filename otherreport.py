import pandas as pd

heard5 = pd.read_csv("unheard.csv", sep = "\t", engine = "python", quoting = 3)
heard6 = pd.read_csv("saved_list.csv", sep = "\t", engine = "python", quoting = 3)
heard7 = pd.read_csv("queue.csv", sep = "\t", engine = "python", quoting = 3)
heard8 = pd.read_csv("playlists.csv", sep = "\t", engine = "python", quoting = 3)

for i in [heard5, heard6, heard7, heard8]:
	i.columns.values[0] = "Playlist"
	i = i.drop(columns = "ID")

heard6 = heard6.drop_duplicates(subset = ["Playlist", "Artists"])

big_unheard = heard5.append(heard6, ignore_index = True)
del heard5
del heard6
big_unheard = big_unheard = big_unheard.append(heard7, ignore_index = True)
big_unheard = big_unheard = big_unheard.append(heard8, ignore_index = True)
del heard7
del heard8

big_unheard["Title"] = big_unheard.iloc[:, 0]
grouped = big_unheard.groupby(["Title", "Artists"]).count()
del big_unheard
repeats = grouped[grouped["ExCol"] > 1].copy()
del grouped
pd.set_option("display.max_rows", 500, "display.max_columns", None)

if repeats.shape == (0,0):
	print("No Overlaps, well done!")
else:
	print(repeats.sort_values("Artists"))