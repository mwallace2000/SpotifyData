import getplaylists
import pandas as pd
import numpy as np

other_songs = pd.read_csv("playlists.csv", sep='\t')
other_songs["Title"] = other_songs.index

other_songs["Artists"] = other_songs["Artists"].str.replace("feat. ", ", ")
other_songs["Artists"] = other_songs["Artists"].str.replace("Tyler, The Creator", "Tyler The Creator")
other_songs["Artists"] = other_songs["Artists"].str.replace("Hank Williams, Jr.", "Hank Williams Jr.", regex=False)
other_songs["Artists"] = other_songs["Artists"].str.replace("Meechie Darko", "Meechy Darko")
other_songs["Artists"] = other_songs["Artists"].str.replace("Nyck @ Knight", "Nyck Caution, Kirk Knight")
other_songs["Artists"] = other_songs["Artists"].str.replace("Aloe Blacc X David Correy", "Aloe Blacc, David Correy")
other_songs["Artists"] = other_songs["Artists"].str.replace("Slim Jxmmi of Rae Sremmurd", "Slim Jxmmi")
other_songs["Artists"] = other_songs["Artists"].str.replace("Bazzi vs.", "Bazzi")
other_songs["Artists"] = other_songs["Artists"].str.replace("B.o.B. /Krizz Kaliko", "B.o.B., Krizz Kaliko", regex=False)
other_songs["Artists"] = other_songs["Artists"].str.replace("Nate Feuerstein", "NF")
other_songs["Artists"] = other_songs["Artists"].str.replace("Conway the Machine", "Conway")
other_songs["Artists"] = other_songs["Artists"].str.replace("nothing,nowhere.", "nothing;nowhere.", regex=False)
other_songs["Artists"] = other_songs["Artists"].str.replace("MGK", "Machine Gun Kelly")
other_songs["Artists"] = other_songs["Artists"].str.replace("MGK", "Machine Gun Kelly")
other_songs["Artists"] = other_songs["Artists"].str.replace("Alex Da Kid", "_BY.ALEXANDER", regex=False)
other_songs["Artists"] = other_songs["Artists"].str.replace("Holly Brook", "Skylar Grey")
other_songs["Artists"] = other_songs["Artists"].str.replace("Marina & The Diamonds", "MARINA")
other_songs["Artists"] = other_songs["Artists"].str.replace("Seth Avett & Jessica Lea Mayfield", "Seth Avett, Jessica Lea Mayfield") 
other_songs["Artists"] = other_songs["Artists"].str.replace("Sharpay Evans", "Ashley Tisdale")
other_songs["Artists"] = other_songs["Artists"].str.replace("Eric B. & Rakim", "Eric B., Rakim", regex = False)
other_songs["Artists"] = other_songs["Artists"].str.replace("Gabriella Montez", "Vanessa Hudgens")
other_songs["Artists"] = other_songs["Artists"].str.replace("Snow The Product", "Snow Tha Product")
other_songs["Artists"] = other_songs["Artists"].str.replace("Dimitri Vegas & Like Mike", "Dimitri Vegas, Like Mike")
other_songs["Artists"] = other_songs["Artists"].str.replace("Hamilton Leithauser + Rostam", "Hamilton Leithauser, Rostam")
other_songs["Artists"] = other_songs["Artists"].str.replace("Jared Evan & Statik Selektah", "Jared Evan, Statik Selektah")
other_songs["Artists"] = other_songs["Artists"].str.replace("Will Butler vs The Knocks", "Will Butler, The Knocks")
other_songs["Artists"] = other_songs["Artists"].str.replace('Crystal "Røvél" Torres', 'Crystal Torres')
other_songs["Artists"] = other_songs["Artists"].str.replace('DEF Loaf', 'DeJ Loaf')
other_songs["Artists"] = other_songs["Artists"].str.replace('Mase & Puff Daddy', 'Mase, Diddy')
other_songs["Artists"] = other_songs["Artists"].str.replace('Macklemore & Ryan Lewis', 'Macklemore, Ryan Lewis')
other_songs["Artists"] = other_songs["Artists"].str.replace('Mumford & Sons (Remix)', 'Mumford & Sons', regex=False)
other_songs["Artists"] = other_songs["Artists"].str.replace('Denaun', 'Mr. Porter')
other_songs["Artists"] = other_songs["Artists"].str.replace('Mr Porter', 'Mr. Porter')
other_songs["Artists"] = other_songs["Artists"].str.replace('Kevin Parker', 'Tame Impala')
other_songs["Artists"] = other_songs["Artists"].str.replace('Alex Lasarenko', 'Alexander Lasarenko')
other_songs["Artists"] = other_songs["Artists"].str.replace('B.o.B.', 'B.o.B', regex=False)
other_songs["Artists"] = other_songs["Artists"].str.replace('CJ Fly of Pro Era', "CJ Fly")
other_songs["Artists"] = other_songs["Artists"].str.replace('Uncle Charlie Wilson', "Charlie Wilson")
other_songs["Artists"] = other_songs["Artists"].str.replace('Jethro Sheeran', 'Alonestar')
other_songs["Artists"] = other_songs["Artists"].str.replace('Hannah Montana', 'Miley Cyrus')
other_songs["Artists"] = other_songs["Artists"].str.replace('Troi Martin', 'Troi Irons')
other_songs["Artists"] = other_songs["Artists"].str.replace('Troi', 'Troi Irons')

other_songs['Artists'] = np.where(other_songs["Artists"].str.contains("Underachievers"), other_songs["Artists"]+", Issa Gold", other_songs["Artists"])
other_songs['Artists'] = np.where(other_songs["Artists"].str.contains("Underachievers"), other_songs["Artists"]+", AKTHESAVIOR", other_songs["Artists"])

other_songs['Artists'] = np.where(other_songs['Artists'].str.contains("PRhyme") & (~other_songs['Artists'].str.contains('''Royce Da 5'9"''')), other_songs['Artists']+''', Royce Da 5'9"''', other_songs['Artists'])
other_songs['Artists'] = np.where(other_songs['Artists'].str.contains("PRhyme") & (~other_songs['Artists'].str.contains("DJ Premier")), other_songs['Artists']+", DJ Premier", other_songs['Artists'])
other_songs['Artists'] = np.where(other_songs['Artists'].str.contains("Bad Meets Evil") & (~other_songs['Artists'].str.contains('''Royce Da 5'9"''')), other_songs['Artists']+''', Royce Da 5'9"''', other_songs['Artists'])
other_songs['Artists'] = np.where(other_songs['Artists'].str.contains("Bad Meets Evil") & (~other_songs['Artists'].str.contains("Eminem")), other_songs['Artists']+", Eminem", other_songs['Artists'])
other_songs['Artists'] = np.where(other_songs['Artists'].str.contains("KIDS SEE GHOSTS") & (~other_songs['Artists'].str.contains("Kanye West")), other_songs['Artists']+", Kanye West", other_songs['Artists'])
other_songs['Artists'] = np.where(other_songs['Artists'].str.contains("KIDS SEE GHOSTS") & (~other_songs['Artists'].str.contains("Kid Cudi")), other_songs['Artists']+", Kid Cudi", other_songs['Artists'])
other_songs['Artists'] = np.where(other_songs['Artists'].str.contains("mansionz") & (~other_songs['Artists'].str.contains("blackbear")), other_songs['Artists']+", blackbear", other_songs['Artists'])
other_songs['Artists'] = np.where(other_songs['Artists'].str.contains("mansionz") & (~other_songs['Artists'].str.contains("Mike Posner")), other_songs['Artists']+", Mike Posner", other_songs['Artists'])
other_songs['Artists'] = np.where(other_songs['Artists'].str.contains("Black Hippy"), other_songs['Artists']+", ScHoolboy Q", other_songs['Artists'])
other_songs['Artists'] = np.where(other_songs['Artists'].str.contains("Black Hippy"), other_songs['Artists']+", Kendrick Lamar", other_songs['Artists'])
other_songs['Artists'] = np.where(other_songs['Artists'].str.contains("Black Hippy") & (~other_songs["Other Songs I Know"].str.contains("PAIN")), other_songs['Artists']+", Jay Rock", other_songs['Artists'])
other_songs['Artists'] = np.where(other_songs['Artists'].str.contains("Black Hippy"), other_songs['Artists']+", Ab-Soul", other_songs['Artists'])
other_songs['Artists'] = np.where(other_songs['Artists'].str.contains("TWENTY88"), other_songs['Artists']+", Jhené Aiko", other_songs['Artists'])
other_songs['Artists'] = np.where(other_songs['Artists'].str.contains("TWENTY88"), other_songs['Artists']+", Big Sean", other_songs['Artists'])
other_songs['Artists'] = np.where(other_songs['Artists'].str.contains("STATIK KXNG"), other_songs['Artists']+", KXNG Crooked", other_songs['Artists'])
other_songs['Artists'] = np.where(other_songs['Artists'].str.contains("STATIK KXNG"), other_songs['Artists']+", Statik Selektah", other_songs['Artists'])

other_songs['Artists'] = np.where(other_songs['Artists'].str.contains("Run The Jewels"), other_songs['Artists']+", Killer Mike", other_songs['Artists'])
other_songs['Artists'] = np.where(other_songs['Artists'].str.contains("Run The Jewels"), other_songs['Artists']+", El-P", other_songs['Artists'])
other_songs['Artists'] = np.where(other_songs['Artists'].str.contains("Macklemore & Ryan Lewis") & (~other_songs['Artists'].str.contains("Macklemore")), other_songs['Artists']+", Macklemore", other_songs['Artists'])
other_songs['Artists'] = np.where(other_songs['Artists'].str.contains("Macklemore & Ryan Lewis") & (~other_songs['Artists'].str.contains("Ryan Lewis")), other_songs['Artists']+", Ryan Lewis", other_songs['Artists'])
other_songs['Artists'] = np.where(other_songs['Artists'].str.contains("Slaughterhouse") & (~other_songs["Other Songs I Know"].str.contains("R.N.S.")), other_songs['Artists']+''', Royce Da 5'9"''', other_songs['Artists'])
other_songs['Artists'] = np.where(other_songs['Artists'].str.contains("Slaughterhouse") & (~other_songs['Artists'].str.contains("KXNG Crooked")), other_songs['Artists']+", KXNG Crooked", other_songs['Artists'])
other_songs['Artists'] = np.where(other_songs['Artists'].str.contains("Slaughterhouse") & (~other_songs["Other Songs I Know"].str.contains("Asylum")), other_songs['Artists']+", Joe Budden", other_songs['Artists'])
other_songs['Artists'] = np.where(other_songs['Artists'].str.contains("Slaughterhouse") & (~other_songs['Artists'].str.contains("Joell Ortiz")), other_songs['Artists']+", Joell Ortiz", other_songs['Artists'])

other_songs['Artists'] = np.where(other_songs['Artists'].str.contains("Banks & Steelz"), other_songs['Artists']+", RZA", other_songs['Artists'])
other_songs['Artists'] = np.where(other_songs['Artists'].str.contains("Banks & Steelz"), other_songs['Artists']+", Paul Banks", other_songs['Artists'])
other_songs['Artists'] = np.where(other_songs['Artists'].str.contains("Wu-Tang Clan") & (other_songs["Other Songs I Know"].str.contains("Keep Watch")), other_songs['Artists']+", Method Man, Inspectah Deck, GZA, Cappadonna", other_songs['Artists'])
other_songs['Artists'] = np.where(other_songs['Artists'].str.contains("Rae Sremmurd"), other_songs['Artists']+", Swae Lee", other_songs['Artists'])
other_songs['Artists'] = np.where(other_songs['Artists'].str.contains("Rae Sremmurd"), other_songs['Artists']+", Slim Jxmmi", other_songs['Artists'])

other_songs['Artists'] = np.where(other_songs['Artists'].str.contains("Migos") & (~other_songs["Other Songs I Know"].str.contains("Pipe It Up")) , other_songs['Artists']+", Offset, Quavo, Takeoff", other_songs['Artists'])
other_songs['Artists'] = np.where(other_songs['Artists'].str.contains("Migos") & (other_songs["Other Songs I Know"].str.contains("Pipe It Up")) , other_songs['Artists']+", Quavo, Takeoff", other_songs['Artists'])

other_songs['Artists'] = np.where(other_songs['Artists'].str.contains("D12") & (~other_songs["Other Songs I Know"].str.contains("In The Morning|Another Public Service Announcement - Intro|Bugz 97|Fuck Love Twice|Instigator|Leave Dat Boy Alone|Shit Can Happen|Steve Berman|That's How - Skit")) , other_songs['Artists']+", Bizarre", other_songs['Artists'])
other_songs['Artists'] = np.where(other_songs['Artists'].str.contains("D12") & (~other_songs["Other Songs I Know"].str.contains("Bane|Another Public Service Announcement - Intro|Bizarre - Skit|Bizzare - Skit|Bugz 97 - Skit|Desidance|Fuck Love Twice|I Ain't Crazy|Instigator|I Wanna Be Famous|That's How - Skit")), other_songs['Artists']+", Eminem", other_songs['Artists'])
other_songs['Artists'] = np.where(other_songs['Artists'].str.contains("D12") & (~other_songs["Other Songs I Know"].str.contains("American Psycho II|Bugz 97|Just Like U|Steve Berman|That's How - Skit")), other_songs['Artists']+", Kuniva", other_songs['Artists'])
other_songs['Artists'] = np.where(other_songs['Artists'].str.contains("D12") & (~other_songs["Other Songs I Know"].str.contains("40 oz|American Psycho II|Another Public Service Announcement|Bizarre - Skit|Bizzare - Skit|Bugz 97|Dude - Skit|Fuck Love Twice|Git Up|I Wanna Be Famous|Just Like U|Keep Talkin|Pimplikeness|Steve Berman - Skit")), other_songs['Artists']+", Mr. Porter", other_songs['Artists'])
other_songs['Artists'] = np.where(other_songs['Artists'].str.contains("D12") & (~other_songs["Other Songs I Know"].str.contains("In The Morning|American Psycho|Public Service|Bane|Bizzare - Skit|Bugz 97|Dude - Skit|Fuck Love Twice|Git Up|I Wanna Be Famous|Just Like U|Leave Dat Boy|Shit Can Happen|Steve Berman|That's How - Skit")), other_songs['Artists']+", Proof", other_songs['Artists'])
other_songs['Artists'] = np.where(other_songs['Artists'].str.contains("D12") & (~other_songs["Other Songs I Know"].str.contains("40 oz|American Psycho II|Another Public Service Announcement|Bizzare - Skit|Bugz 97|Dude - Skit|Fuck Love Twice|Just Like U|Steve Berman - Skit|That's How - Skit")), other_songs['Artists']+", Swifty McVay", other_songs['Artists'])

other_songs['Artists'] = np.where(other_songs['Artists'].str.contains("Flatbush Zombies"), other_songs['Artists']+", Erick the Architect", other_songs['Artists'])
other_songs['Artists'] = np.where(other_songs['Artists'].str.contains("Flatbush Zombies"), other_songs['Artists']+", Meechy Darko", other_songs['Artists'])
other_songs['Artists'] = np.where(other_songs['Artists'].str.contains("Flatbush Zombies"), other_songs['Artists']+", Zombie Juice", other_songs['Artists'])

other_songs['Artists'] = np.where(other_songs['Artists'].str.contains("Troy") & (other_songs["Other Songs I Know"].str.contains("Get'cha Head|I Can't Take|What I've Been")) , other_songs['Artists']+", Drew Seeley", other_songs['Artists'])
other_songs['Artists'] = np.where(other_songs['Artists'].str.contains("Troy") & (other_songs["Other Songs I Know"].str.contains("Bet On It|You Are the Music")) , other_songs['Artists']+", Zac Efron", other_songs['Artists'])

other_songs = pd.DataFrame(other_songs["Artists"])

other_songs["Artists"] = other_songs["Artists"].str.split(",")
other_songs["Artists"] = other_songs["Artists"].apply(lambda my_list:[x.strip() for x in my_list])
other_songs["Artists"] = other_songs['Artists'].apply(set)
other_songs["Length"] = other_songs["Artists"].str.len()
artists = pd.DataFrame(other_songs['Artists'].values.tolist())
names = artists[0].append(artists[1])
for i in artists.columns[2:]:
	names = names.append(artists[i])
names = names.str.replace("^ ", "")
names = names.str.replace(" $", "")
names = pd.DataFrame(names)
names["Arist"] = "True"

grouped_orig = names.groupby(0).count()
grouped_orig.reset_index(inplace=True)
grouped_orig = grouped_orig.rename(columns = {0:"Artist", "Arist":"Number of Songs"})


loved_songs = pd.read_csv("loved.csv", sep='\t')

loved_songs = pd.DataFrame(loved_songs["Songs I Love"])
loved_songs["Songs I Love"] = loved_songs["Songs I Love"].str.replace("feat. ", ", ")
loved_songs["Songs I Love"] = loved_songs["Songs I Love"].str.replace("Tyler, The Creator", "Tyler The Creator")
loved_songs["Songs I Love"] = loved_songs["Songs I Love"].str.replace("Meechie", "Meechy")
loved_songs["Songs I Love"] = loved_songs["Songs I Love"].str.replace("Nyck @ Knight", "Nyck Caution, Kirk Knight")
loved_songs["Songs I Love"] = loved_songs["Songs I Love"].str.replace("MGK", "Machine Gun Kelly")
loved_songs["Songs I Love"] = loved_songs["Songs I Love"].str.replace("Holly Brook", "Skylar Grey")
loved_songs["Songs I Love"] = loved_songs["Songs I Love"].str.replace("Marina & The Diamonds", "MARINA")
loved_songs["Songs I Love"] = loved_songs["Songs I Love"].str.replace("Seth Avett & Jessica Lea Mayfield", "Seth Avett, Jessica Lea Mayfield")
loved_songs["Songs I Love"] = loved_songs["Songs I Love"].str.replace('Macklemore & Ryan Lewis', 'Macklemore, Ryan Lewis')

loved_songs["Songs I Love"] = np.where(loved_songs["Songs I Love"].str.contains("PRhyme") & (~loved_songs["Songs I Love"].str.contains('''Royce Da 5'9"''')), loved_songs["Songs I Love"]+''', Royce Da 5'9"''', loved_songs["Songs I Love"])
loved_songs["Songs I Love"] = np.where(loved_songs["Songs I Love"].str.contains("PRhyme") & (~loved_songs["Songs I Love"].str.contains("DJ Premier")), loved_songs["Songs I Love"]+", DJ Premier", loved_songs["Songs I Love"])
loved_songs["Songs I Love"] = np.where(loved_songs["Songs I Love"].str.contains("Bad Meets Evil") & (~loved_songs["Songs I Love"].str.contains('''Royce Da 5'9"''')), loved_songs["Songs I Love"]+''', Royce Da 5'9"''', loved_songs["Songs I Love"])
loved_songs["Songs I Love"] = np.where(loved_songs["Songs I Love"].str.contains("Bad Meets Evil") & (~loved_songs["Songs I Love"].str.contains("Eminem")), loved_songs["Songs I Love"]+", Eminem", loved_songs["Songs I Love"])
loved_songs["Songs I Love"] = np.where(loved_songs["Songs I Love"].str.contains("KIDS SEE GHOSTS") & (~loved_songs["Songs I Love"].str.contains("Kanye West")), loved_songs["Songs I Love"]+", Kanye West", loved_songs["Songs I Love"])
loved_songs["Songs I Love"] = np.where(loved_songs["Songs I Love"].str.contains("KIDS SEE GHOSTS") & (~loved_songs["Songs I Love"].str.contains("Kid Cudi")), loved_songs["Songs I Love"]+", Kid Cudi", loved_songs["Songs I Love"])
loved_songs["Songs I Love"] = np.where(loved_songs["Songs I Love"].str.contains("mansionz") & (~loved_songs["Songs I Love"].str.contains("blackbear")), loved_songs["Songs I Love"]+", blackbear", loved_songs["Songs I Love"])
loved_songs["Songs I Love"] = np.where(loved_songs["Songs I Love"].str.contains("mansionz") & (~loved_songs["Songs I Love"].str.contains("Mike Posner")), loved_songs["Songs I Love"]+", Mike Posner", loved_songs["Songs I Love"])

loved_songs["Songs I Love"] = np.where(loved_songs["Songs I Love"].str.contains("Macklemore & Ryan Lewis") & (~loved_songs["Songs I Love"].str.contains("Macklemore")), loved_songs["Songs I Love"]+", Macklemore", loved_songs["Songs I Love"])
loved_songs["Songs I Love"] = np.where(loved_songs["Songs I Love"].str.contains("Macklemore & Ryan Lewis") & (~loved_songs["Songs I Love"].str.contains("Ryan Lewis")), loved_songs["Songs I Love"]+", Ryan Lewis", loved_songs["Songs I Love"])
loved_songs["Songs I Love"] = np.where(loved_songs["Songs I Love"].str.contains("TWENTY88"), loved_songs["Songs I Love"]+", Jhené Aiko", loved_songs["Songs I Love"])
loved_songs["Songs I Love"] = np.where(loved_songs["Songs I Love"].str.contains("TWENTY88"), loved_songs["Songs I Love"]+", Big Sean", loved_songs["Songs I Love"])

loved_songs["Songs I Love"] = np.where(loved_songs["Songs I Love"].str.contains("Run The Jewels"), loved_songs["Songs I Love"]+", Killer Mike", loved_songs["Songs I Love"])
loved_songs["Songs I Love"] = np.where(loved_songs["Songs I Love"].str.contains("Run The Jewels"), loved_songs["Songs I Love"]+", El-P", loved_songs["Songs I Love"])
loved_songs["Songs I Love"] = np.where(loved_songs["Songs I Love"].str.contains("Black Hippy") & (~loved_songs["Songs I Love"].str.contains("ScHoolboy Q")), loved_songs["Songs I Love"]+", ScHoolboy Q", loved_songs["Songs I Love"])
loved_songs["Songs I Love"] = np.where(loved_songs["Songs I Love"].str.contains("Black Hippy") & (~loved_songs["Songs I Love"].str.contains("Kendrick Lamar")), loved_songs["Songs I Love"]+", Kendrick Lamar", loved_songs["Songs I Love"])
loved_songs["Songs I Love"] = np.where(loved_songs["Songs I Love"].str.contains("Black Hippy") & (~loved_songs["Songs I Love"].str.contains("Jay Rock")), loved_songs["Songs I Love"]+", Jay Rock", loved_songs["Songs I Love"])
loved_songs["Songs I Love"] = np.where(loved_songs["Songs I Love"].str.contains("Black Hippy") & (~loved_songs["Songs I Love"].str.contains("Ab-Soul")), loved_songs["Songs I Love"]+", Ab-Soul", loved_songs["Songs I Love"])

loved_songs["Songs I Love"] = np.where(loved_songs["Songs I Love"].str.contains("Slaughterhouse") & (~loved_songs["Songs I Love"].str.contains('''Royce Da 5'9"''')), loved_songs["Songs I Love"]+''', Royce Da 5'9"''', loved_songs["Songs I Love"])
loved_songs["Songs I Love"] = np.where(loved_songs["Songs I Love"].str.contains("Slaughterhouse") & (~loved_songs["Songs I Love"].str.contains("KXNG Crooked")), loved_songs["Songs I Love"]+", KXNG Crooked", loved_songs["Songs I Love"])
loved_songs["Songs I Love"] = np.where(loved_songs["Songs I Love"].str.contains("Slaughterhouse") & (~loved_songs["Songs I Love"].str.contains("Joe Budden")), loved_songs["Songs I Love"]+", Joe Budden", loved_songs["Songs I Love"])
loved_songs["Songs I Love"] = np.where(loved_songs["Songs I Love"].str.contains("Slaughterhouse") & (~loved_songs["Songs I Love"].str.contains("Joell Ortiz")), loved_songs["Songs I Love"]+", Joell Ortiz", loved_songs["Songs I Love"])

loved_songs["Songs I Love"] = np.where(loved_songs["Songs I Love"].str.contains("Banks & Steelz") & (~loved_songs["Songs I Love"].str.contains("RZA")), loved_songs["Songs I Love"]+", RZA", loved_songs["Songs I Love"])
loved_songs["Songs I Love"] = np.where(loved_songs["Songs I Love"].str.contains("Banks & Steelz") & (~loved_songs["Songs I Love"].str.contains("Paul Banks")), loved_songs["Songs I Love"]+", Paul Banks", loved_songs["Songs I Love"])

loved_songs["Songs I Love"] = loved_songs["Songs I Love"].str.split(",")
loved_songs["Songs I Love"] = loved_songs["Songs I Love"].apply(lambda my_list:[x.strip() for x in my_list])
loved_songs["Songs I Love"] = loved_songs["Songs I Love"].apply(set)
loved_songs["Length"] = loved_songs["Songs I Love"].str.len()
artists = pd.DataFrame(loved_songs["Songs I Love"].values.tolist())
names = artists[0].append(artists[1])
for i in artists.columns[2:]:
	names = names.append(artists[i])
names = names.str.replace("^ ", "")
names = names.str.replace(" $", "")
names = pd.DataFrame(names)
names["Arist"] = "True"

grouped_loved = names.groupby(0).count()
grouped_loved.reset_index(inplace=True)
grouped_loved = grouped_loved.rename(columns = {0:"Artist", "Arist":"Number of Songs"})

saved_data = pd.read_csv("saved_songs.csv")
grouped = grouped_orig.merge(saved_data, left_on = "Artist", right_on = "Artist", how = 'outer', suffixes = [" Disliked", None])
grouped = grouped.merge(grouped_loved, left_on = "Artist", right_on = "Artist", how = 'left', suffixes = [None, " Loved"])
grouped = grouped.fillna(0)

queue = pd.read_csv("queue.csv", sep = "\t")
queue = pd.DataFrame(queue["Artists"])
queue["Artists"] = queue["Artists"].str.replace("feat. ", ", ", regex = False)
queue["Artists"] = queue["Artists"].str.replace("Tyler, The Creator", "Tyler The Creator")
queue["Artists"] = queue["Artists"].str.replace("Hank Williams, Jr.", "Hank Williams Jr.", regex = False)
queue["Artists"] = queue["Artists"].str.replace("Bazzi vs.", "Bazzi", regex = False)
queue["Artists"] = queue["Artists"].str.replace("Meechie", "Meechy")
queue["Artists"] = queue["Artists"].str.replace("Nyck @ Knight", "Nyck Caution, Kirk Knight")
queue["Artists"] = queue["Artists"].str.replace("Aloe Blacc X David Correy", "Aloe Blacc, David Correy")
queue["Artists"] = queue["Artists"].str.replace("Mumford & Sons (Remix)", "Mumford & Sons", regex = False)
queue["Artists"] = queue["Artists"].str.replace("Charlie XCX", "Charli XCX")
queue["Artists"] = queue["Artists"].str.replace("Conway the Machine", "Conway")
queue["Artists"] = queue["Artists"].str.replace("nothing,nowhere.", "nothing;nowhere.", regex=False)
queue["Artists"] = queue["Artists"].str.replace("MGK", "Machine Gun Kelly")
queue["Artists"] = queue["Artists"].str.replace("Holly Brook", "Skylar Grey")
queue["Artists"] = queue["Artists"].str.replace("Marina & The Diamonds", "MARINA")
queue["Artists"] = queue["Artists"].str.replace("Seth Avett & Jessica Lea Mayfield", "Seth Avett, Jessica Lea Mayfield")
queue["Artists"] = queue["Artists"].str.replace("Sharpay Evans", "Ashley Tisdale")
queue["Artists"] = queue["Artists"].str.replace("Eric B. & Rakim", "Eric B., Rakim", regex=False)
queue["Artists"] = queue["Artists"].str.replace("Gabriella Montez", "Vanessa Hudgens")
queue["Artists"] = queue["Artists"].str.replace("Dimitri Vegas & Like Mike", "Dimitri Vegas, Like Mike")
queue["Artists"] = queue["Artists"].str.replace("Hamilton Leithauser + Rostam", "Hamilton Leithauser, Rostam")
queue["Artists"] = queue["Artists"].str.replace("Jared Evan & Statik Selektah", "Jared Evan, Statik Selektah")
queue["Artists"] = queue["Artists"].str.replace("Will Butler vs The Knocks", "Will Butler, The Knocks")
queue["Artists"] = queue["Artists"].str.replace('Macklemore & Ryan Lewis', 'Macklemore, Ryan Lewis')
queue["Artists"] = queue["Artists"].str.replace('Denaun', 'Mr. Porter')
queue["Artists"] = queue["Artists"].str.replace('Mr Porter', 'Mr. Porter')
queue["Artists"] = queue["Artists"].str.replace('Kevin Parker', 'Tame Impala')
queue["Artists"] = queue["Artists"].str.replace('Alex Lasarenko', 'Alexander Lasarenko')
queue["Artists"] = queue["Artists"].str.replace('B.o.B.', 'B.o.B', regex=False)
queue["Artists"] = queue["Artists"].str.replace('Jethro Sheeran', 'Alonestar')
queue["Artists"] = queue["Artists"].str.replace('Hannah Montana', 'Miley Cyrus')
queue["Artists"] = queue["Artists"].str.replace('Troi Martin', 'Troi Irons')
queue["Artists"] = queue["Artists"].str.replace('Troi', 'Troi Irons')
queue["Artists"] = queue["Artists"].str.replace('Claire Cottrill', 'Clairo')

queue["Artists"] = np.where(queue["Artists"].str.contains("PRhyme") & (~queue["Artists"].str.contains('''Royce Da 5'9"''')), queue["Artists"]+''', Royce Da 5'9"''', queue["Artists"])
queue["Artists"] = np.where(queue["Artists"].str.contains("PRhyme") & (~queue["Artists"].str.contains("DJ Premier")), queue["Artists"]+", DJ Premier", queue["Artists"])
queue["Artists"] = np.where(queue["Artists"].str.contains("Bad Meets Evil") & (~queue["Artists"].str.contains('''Royce Da 5'9"''')), queue["Artists"]+''', Royce Da 5'9"''', queue["Artists"])
queue["Artists"] = np.where(queue["Artists"].str.contains("Bad Meets Evil") & (~queue["Artists"].str.contains("Eminem")), queue["Artists"]+", Eminem", queue["Artists"])
queue["Artists"] = np.where(queue["Artists"].str.contains("KIDS SEE GHOSTS") & (~queue["Artists"].str.contains("Kanye West")), queue["Artists"]+", Kanye West", queue["Artists"])
queue["Artists"] = np.where(queue["Artists"].str.contains("KIDS SEE GHOSTS") & (~queue["Artists"].str.contains("Kid Cudi")), queue["Artists"]+", Kid Cudi", queue["Artists"])
queue["Artists"] = np.where(queue["Artists"].str.contains("mansionz") & (~queue["Artists"].str.contains("blackbear")), queue["Artists"]+", blackbear", queue["Artists"])
queue["Artists"] = np.where(queue["Artists"].str.contains("mansionz") & (~queue["Artists"].str.contains("Mike Posner")), queue["Artists"]+", Mike Posner", queue["Artists"])
queue["Artists"] = np.where(queue["Artists"].str.contains("Slaughterhouse") & (~queue["Artists"].str.contains('''Royce Da 5'9"''')), queue["Artists"]+''', Royce Da 5'9"''', queue["Artists"])
queue["Artists"] = np.where(queue["Artists"].str.contains("Slaughterhouse") & (~queue["Artists"].str.contains("KXNG Crooked")), queue["Artists"]+ ", KXNG Crooked", queue["Artists"])
queue["Artists"] = np.where(queue["Artists"].str.contains("Slaughterhouse") & (~queue["Artists"].str.contains("Joe Budden")), queue["Artists"]+", Joe Budden", queue["Artists"])
queue["Artists"] = np.where(queue["Artists"].str.contains("Slaughterhouse") & (~queue["Artists"].str.contains("Joell Ortiz")), queue["Artists"]+", Joell Ortiz", queue["Artists"])

queue["Artists"] = np.where(queue["Artists"].str.contains("TWENTY88"), queue["Artists"]+", Jhené Aiko", queue["Artists"])
queue["Artists"] = np.where(queue["Artists"].str.contains("TWENTY88"), queue["Artists"]+", Big Sean", queue["Artists"])
queue["Artists"] = np.where(queue["Artists"].str.contains("Run The Jewels"), queue["Artists"]+", Killer Mike", queue["Artists"])
queue["Artists"] = np.where(queue["Artists"].str.contains("Run The Jewels"), queue["Artists"]+", El-P", queue["Artists"])

queue["Artists"] = np.where(queue["Artists"].str.contains("Rae Sremmurd"), queue["Artists"]+", Swae Lee", queue["Artists"])
queue["Artists"] = np.where(queue["Artists"].str.contains("Rae Sremmurd"), queue["Artists"]+", Slim Jxmmi", queue["Artists"])

queue["Artists"] = np.where(queue["Artists"].str.contains("Macklemore & Ryan Lewis") & (~queue["Artists"].str.contains("Macklemore")), queue["Artists"]+", Macklemore", queue["Artists"])
queue["Artists"] = np.where(queue["Artists"].str.contains("Macklemore & Ryan Lewis") & (~queue["Artists"].str.contains("Ryan Lewis")), queue["Artists"]+", Ryan Lewis", queue["Artists"])
queue["Artists"] = np.where(queue["Artists"].str.contains("Black Hippy") & (~queue["Artists"].str.contains("ScHoolboy Q")), queue["Artists"]+", ScHoolboy Q", queue["Artists"])
queue["Artists"] = np.where(queue["Artists"].str.contains("Black Hippy") & (~queue["Artists"].str.contains("Kendrick Lamar")), queue["Artists"]+", Kendrick Lamar", queue["Artists"])
queue["Artists"] = np.where(queue["Artists"].str.contains("Black Hippy") & (~queue["Artists"].str.contains("Jay Rock")), queue["Artists"]+", Jay Rock", queue["Artists"])
queue["Artists"] = np.where(queue["Artists"].str.contains("Black Hippy") & (~queue["Artists"].str.contains("Ab-Soul")), queue["Artists"]+", Ab-Soul", queue["Artists"])
queue["Artists"] = np.where(queue["Artists"].str.contains("Banks & Steelz") & (~queue["Artists"].str.contains("RZA")), queue["Artists"]+", RZA", queue["Artists"])
queue["Artists"] = np.where(queue["Artists"].str.contains("Banks & Steelz") & (~queue["Artists"].str.contains("Paul Banks")), queue["Artists"]+", Paul Banks", queue["Artists"])

queue['Artists'] = np.where(queue['Artists'].str.contains("STATIK KXNG"), queue['Artists']+", KXNG Crooked", queue['Artists'])
queue['Artists'] = np.where(queue['Artists'].str.contains("STATIK KXNG"), queue['Artists']+", Statik Selektah", queue['Artists'])

queue["Artists"] = queue["Artists"].str.split(",")
queue["Artists"] = queue["Artists"].apply(lambda my_list:[x.strip() for x in my_list])
queue["Artists"] = queue["Artists"].apply(set)
queue["Length"] = queue["Artists"].str.len()
queue = queue[queue["Artists"].notna()]
queue = queue[queue["Artists"] != None]



artists = pd.DataFrame(queue["Artists"].values.tolist())
names = artists[0].append(artists[1])
for i in artists.columns[2:]:
	names = names.append(artists[i])
names = names.str.replace("^ ", "")
names = names.str.replace(" $", "")
names = pd.DataFrame(names)
names = names.rename(columns = {0: "Artist"})
names["Arist"] = "True"

grouped_orig = names.groupby(["Artist"]).count()
grouped_orig.reset_index(inplace=True)
grouped_orig = grouped_orig.rename(columns = {"Arist":"Number of Songs"})
print(grouped_orig.head())
grouped = grouped.merge(grouped_orig, on = "Artist", how = "outer", suffixes = [None, " Undecided"])


queue = pd.read_csv("unheard.csv", sep = "\t")
queue = pd.DataFrame(queue["Artists"])
queue = queue.dropna()

queue["Artists"] = queue["Artists"].str.replace("feat. ", ", ")
queue["Artists"] = queue["Artists"].str.replace("Tyler, The Creator", "Tyler The Creator")
queue["Artists"] = queue["Artists"].str.replace("Hank Williams, Jr.", "Hank Williams Jr.")
queue["Artists"] = queue["Artists"].str.replace("Bazzi vs.", "Bazzi")
queue["Artists"] = queue["Artists"].str.replace("Meechie", "Meechy")
queue["Artists"] = queue["Artists"].str.replace("Nyck @ Knight", "Nyck Caution, Kirk Knight")
queue["Artists"] = queue["Artists"].str.replace("Aloe Blacc X David Correy", "Aloe Blacc, David Correy")
queue["Artists"] = queue["Artists"].str.replace("Mumford & Sons (Remix)", "Mumford & Sons")
queue["Artists"] = queue["Artists"].str.replace("Charlie XCX", "Charli XCX")
queue["Artists"] = queue["Artists"].str.replace("Conway the Machine", "Conway")
queue["Artists"] = queue["Artists"].str.replace("nothing,nowhere.", "nothing;nowhere.")
queue["Artists"] = queue["Artists"].str.replace("MGK", "Machine Gun Kelly")
queue["Artists"] = queue["Artists"].str.replace("Holly Brook", "Skylar Grey")
queue["Artists"] = queue["Artists"].str.replace("Marina & The Diamonds", "MARINA")
queue["Artists"] = queue["Artists"].str.replace("Seth Avett & Jessica Lea Mayfield", "Seth Avett, Jessica Lea Mayfield")
queue["Artists"] = queue["Artists"].str.replace("Sharpay Evans", "Ashley Tisdale")
queue["Artists"] = queue["Artists"].str.replace("Eric B. & Rakim", "Eric B., Rakim")
queue["Artists"] = queue["Artists"].str.replace("Gabriella Montez", "Vanessa Hudgens")
queue["Artists"] = queue["Artists"].str.replace("Dimitri Vegas & Like Mike", "Dimitri Vegas, Like Mike")
queue["Artists"] = queue["Artists"].str.replace("Hamilton Leithauser + Rostam", "Hamilton Leithauser, Rostam")
queue["Artists"] = queue["Artists"].str.replace("Jared Evan & Statik Selektah", "Jared Evan, Statik Selektah")
queue["Artists"] = queue["Artists"].str.replace("Will Butler vs The Knocks", "Will Butler, The Knocks")
queue["Artists"] = queue["Artists"].str.replace('Macklemore & Ryan Lewis', 'Macklemore, Ryan Lewis')
queue["Artists"] = queue["Artists"].str.replace('Mr Porter', 'Mr. Porter')
queue["Artists"] = queue["Artists"].str.replace('Denaun', 'Mr. Porter')
queue["Artists"] = queue["Artists"].str.replace('Kevin Parker', 'Tame Impala')
queue["Artists"] = queue["Artists"].str.replace('Alex Lasarenko', 'Alexander Lasarenko')
queue["Artists"] = queue["Artists"].str.replace('B.o.B.', 'B.o.B' , regex =False)
queue["Artists"] = queue["Artists"].str.replace('Hannah Montana', 'Miley Cyrus')
queue["Artists"] = queue["Artists"].str.replace('Troi Martin', 'Troi Irons')
queue["Artists"] = queue["Artists"].str.replace('Troi', 'Troi Irons')
queue["Artists"] = queue["Artists"].str.replace('Claire Cottrill', 'Clairo')

queue["Artists"] = np.where(queue["Artists"].str.contains("Run The Jewels"), queue["Artists"]+", Killer Mike", queue["Artists"])
queue["Artists"] = np.where(queue["Artists"].str.contains("Run The Jewels"), queue["Artists"]+", El-P", queue["Artists"])
queue["Artists"] = np.where(queue["Artists"].str.contains("TWENTY88"), queue["Artists"]+", Jhené Aiko", queue["Artists"])
queue["Artists"] = np.where(queue["Artists"].str.contains("TWENTY88"), queue["Artists"]+", Big Sean", queue["Artists"])
queue["Artists"] = np.where(queue["Artists"].str.contains("PRhyme") & (~queue["Artists"].str.contains('''Royce Da 5'9"''')), queue["Artists"]+''', Royce Da 5'9"''', queue["Artists"])
queue["Artists"] = np.where(queue["Artists"].str.contains("PRhyme") & (~queue["Artists"].str.contains("DJ Premier")), queue["Artists"]+", DJ Premier", queue["Artists"])
queue["Artists"] = np.where(queue["Artists"].str.contains("Bad Meets Evil") & (~queue["Artists"].str.contains('''Royce Da 5'9"''')), queue["Artists"]+''', Royce Da 5'9"''', queue["Artists"])
queue["Artists"] = np.where(queue["Artists"].str.contains("Bad Meets Evil") & (~queue["Artists"].str.contains("Eminem")), queue["Artists"]+", Eminem", queue["Artists"])
queue["Artists"] = np.where(queue["Artists"].str.contains("KIDS SEE GHOSTS") & (~queue["Artists"].str.contains("Kanye West")), queue["Artists"]+", Kanye West", queue["Artists"])
queue["Artists"] = np.where(queue["Artists"].str.contains("KIDS SEE GHOSTS") & (~queue["Artists"].str.contains("Kid Cudi")), queue["Artists"]+", Kid Cudi", queue["Artists"])
queue["Artists"] = np.where(queue["Artists"].str.contains("mansionz") & (~queue["Artists"].str.contains("blackbear")), queue["Artists"]+", blackbear", queue["Artists"])
queue["Artists"] = np.where(queue["Artists"].str.contains("mansionz") & (~queue["Artists"].str.contains("Mike Posner")), queue["Artists"]+", Mike Posner", queue["Artists"])
queue["Artists"] = np.where(queue["Artists"].str.contains("Slaughterhouse") & (~queue["Artists"].str.contains('''Royce Da 5'9"''')), queue["Artists"]+''', Royce Da 5'9"''', queue["Artists"])
queue["Artists"] = np.where(queue["Artists"].str.contains("Slaughterhouse") & (~queue["Artists"].str.contains("KXNG Crooked")), queue["Artists"]+ ", KXNG Crooked", queue["Artists"])
queue["Artists"] = np.where(queue["Artists"].str.contains("Slaughterhouse") & (~queue["Artists"].str.contains("Joe Budden")), queue["Artists"]+", Joe Budden", queue["Artists"])
queue["Artists"] = np.where(queue["Artists"].str.contains("Slaughterhouse") & (~queue["Artists"].str.contains("Joell Ortiz")), queue["Artists"]+", Joell Ortiz", queue["Artists"])
queue["Artists"] = np.where(queue["Artists"].str.contains("Black Hippy") & (~queue["Artists"].str.contains("ScHoolboy Q")), queue["Artists"]+", ScHoolboy Q", queue["Artists"])
queue["Artists"] = np.where(queue["Artists"].str.contains("Black Hippy") & (~queue["Artists"].str.contains("Kendrick Lamar")), queue["Artists"]+", Kendrick Lamar", queue["Artists"])
queue["Artists"] = np.where(queue["Artists"].str.contains("Black Hippy") & (~queue["Artists"].str.contains("Jay Rock")), queue["Artists"]+", Jay Rock", queue["Artists"])
queue["Artists"] = np.where(queue["Artists"].str.contains("Black Hippy") & (~queue["Artists"].str.contains("Ab-Soul")), queue["Artists"]+", Ab-Soul", queue["Artists"])
queue["Artists"] = np.where(queue["Artists"].str.contains("Macklemore & Ryan Lewis") & (~queue["Artists"].str.contains("Macklemore")), queue["Artists"]+", Macklemore", queue["Artists"])
queue["Artists"] = np.where(queue["Artists"].str.contains("Macklemore & Ryan Lewis") & (~queue["Artists"].str.contains("Ryan Lewis")), queue["Artists"]+", Ryan Lewis", queue["Artists"])

queue["Artists"] = np.where(queue["Artists"].str.contains("Banks & Steelz") & (~queue["Artists"].str.contains("RZA")), queue["Artists"]+", RZA", queue["Artists"])
queue["Artists"] = np.where(queue["Artists"].str.contains("Banks & Steelz") & (~queue["Artists"].str.contains("Paul Banks")), queue["Artists"]+", Paul Banks", queue["Artists"])

queue['Artists'] = np.where(queue['Artists'].str.contains("STATIK KXNG"), queue['Artists']+", KXNG Crooked", queue['Artists'])
queue['Artists'] = np.where(queue['Artists'].str.contains("STATIK KXNG"), queue['Artists']+", Statik Selektah", queue['Artists'])

queue["Artists"] = queue["Artists"].str.split(",")
queue["Artists"] = queue["Artists"].apply(lambda my_list:[x.strip() for x in my_list])
queue["Artists"] = queue["Artists"].apply(set)
queue["Length"] = queue["Artists"].str.len()
queue = queue[queue["Artists"].notna()]
queue = queue[queue["Artists"] != None]

artists = pd.DataFrame(queue["Artists"].values.tolist())
names = artists[0].append(artists[1])
for i in artists.columns[2:]:
	names = names.append(artists[i])
names = names.str.replace("^ ", "")
names = names.str.replace(" $", "")
names = pd.DataFrame(names)
names = names.rename(columns = {0: "Artist"})
names["Arist"] = "True"

grouped_unheard = names.groupby(["Artist"]).count()
grouped_unheard.reset_index(inplace=True)
grouped_unheard = grouped_unheard.rename(columns = {"Arist":"Number of Songs"})
print(grouped_unheard.head())
grouped = grouped.merge(grouped_unheard, on = "Artist", how = "outer", suffixes = [None, " Unheard"])

grouped = grouped.fillna(0)
grouped["Rating"] = grouped["Number of Songs"]*(grouped["Number of Songs"]/(grouped["Number of Songs"]+grouped["Number of Songs Disliked"]) + grouped["Number of Songs Loved"]/grouped["Number of Songs"])
grouped = grouped.fillna(0)
grouped["Number of Songs Disliked"] = grouped["Number of Songs Disliked"].astype(int)
grouped.loc[grouped["Rating"] == 0, "Rating"] = grouped["Number of Songs Disliked"] * -1
grouped.loc[(grouped["Number of Songs"] == 0) & (grouped["Number of Songs Disliked"] == 0), "Rating"] = 0
print(grouped.shape)
grouped = grouped.sort_values(["Rating", "Artist"], ascending = [False, True]).reset_index()
print(grouped.shape)
grouped["Rank"] = grouped.index  +1
print(grouped.shape)
ties = grouped.groupby("Rating")["Rank"].min()
merged = grouped.merge(ties, left_on = "Rating", right_on = "Rating")

del grouped
del ties

merged["Rank_x"] = merged["Rank_x"].astype(str)
merged["Rank_y"] = merged["Rank_y"].astype(str)
merged = merged.loc[merged["Artist"] != "Disney"]
merged = merged.loc[merged["Artist"] != "Sniper Remix"]
merged = merged.loc[merged["Artist"] != "Troy"]
print(merged.shape)
merged.loc[merged["Rank_x"] != merged["Rank_y"], "Rank_y"] = "T"+merged["Rank_y"]
merged = merged.drop(columns = "Rank_x")
merged = merged.rename(columns = {"Rank_y":"Rank"})
merged.loc[("T" +merged["Rank"]).isin(merged["Rank"]), "Rank"] = "T"+merged["Rank"]
merged["Rating"] = merged["Rating"].round(2)
merged = merged[["Rank", "Rating", "Artist", "Number of Songs", "Number of Songs Disliked", "Number of Songs Unheard", "Number of Songs Undecided", "Number of Songs Loved"]]
merged["Number of Songs Undecided"] = (merged["Number of Songs Undecided"] + merged["Number of Songs Unheard"]).astype(int)
merged["Songs In Queue"] = merged["Number of Songs Undecided"] - merged["Number of Songs Unheard"]
merged["Total Songs Reviewed"] = merged["Number of Songs"] + merged["Number of Songs Disliked"]
merged["Remaining Importance"] = (merged["Rating"] * merged["Number of Songs Undecided"]).astype(int)
merged["Unheard Importance"] = (merged["Rating"] * merged["Number of Songs Unheard"]).astype(int)
merged["Inflation Factor"] = ((merged["Number of Songs Undecided"])/merged["Total Songs Reviewed"]).round(2)
merged.loc[merged["Total Songs Reviewed"] == 0, "Inflation Factor"] = merged["Number of Songs Undecided"]
merged.loc[merged["Inflation Factor"] < 0, "Inflation Factor"] = merged["Inflation Factor"]*-1
merged["Number of Songs Loved"] = merged["Number of Songs Loved"].astype(int)
merged["Number of Songs"] = merged["Number of Songs"].astype(int)
merged["Number of Songs Unheard"] = merged["Number of Songs Unheard"].astype(int)
merged["Total Songs Reviewed"] = merged["Total Songs Reviewed"].astype(int)
merged["Lowest Possible Rating"] = merged["Number of Songs"]*(merged["Number of Songs"]/(merged["Number of Songs"]+merged["Number of Songs Undecided"]+merged["Number of Songs Disliked"]) + merged["Number of Songs Loved"]/merged["Number of Songs"])
merged["Highest Possible Rating"] = (merged["Number of Songs"]+merged["Number of Songs Undecided"])*((merged["Number of Songs"]+merged["Number of Songs Undecided"])/(merged["Number of Songs"]+merged["Number of Songs Undecided"]+merged["Number of Songs Disliked"]) + merged["Number of Songs Loved"]/(merged["Number of Songs"]+merged["Number of Songs Undecided"]))
merged["Lowest Possible Rating"] = merged["Lowest Possible Rating"].round(2)
merged = merged.fillna(0)
merged.loc[merged["Lowest Possible Rating"] == 0, "Lowest Possible Rating"] = (merged["Number of Songs Disliked"] + merged["Number of Songs Undecided"])*-1
merged.loc[(merged["Highest Possible Rating"] == 0) & (merged["Number of Songs"] == 0), "Highest Possible Rating"] = merged["Rating"]
merged["Highest Possible Rating"] = merged["Highest Possible Rating"].round(2)
merged = merged[merged["Artist"] != "Artists"]

merged["Lowest Queue Rating"] = merged["Number of Songs"]*(merged["Number of Songs"]/(merged["Number of Songs"]+merged["Songs In Queue"]+merged["Number of Songs Disliked"]) + merged["Number of Songs Loved"]/merged["Number of Songs"])
merged["Highest Queue Rating"] = (merged["Number of Songs"]+merged["Songs In Queue"])*((merged["Number of Songs"]+merged["Songs In Queue"])/(merged["Number of Songs"]+merged["Songs In Queue"]+merged["Number of Songs Disliked"]) + merged["Number of Songs Loved"]/(merged["Number of Songs"]+merged["Songs In Queue"]))

merged = merged.fillna(0)
merged.loc[merged["Lowest Queue Rating"] == 0, "Lowest Queue Rating"] = (merged["Number of Songs Disliked"] + merged["Songs In Queue"])*-1
merged.loc[(merged["Highest Queue Rating"] == 0) & (merged["Number of Songs"] == 0), "Highest Queue Rating"] = merged["Rating"]

merged["Lowest Queue Rating"] = merged["Lowest Queue Rating"].round(2)
merged["Highest Queue Rating"] = merged["Highest Queue Rating"].round(2)

unique = merged["Highest Possible Rating"].unique()
new_high_list = sorted([(merged.iloc[i]["Lowest Possible Rating"]) for i in range(merged.shape[0])], reverse = True)
high_df = pd.DataFrame(unique, columns = ["Highest Possible Rating"])
high_rankings = []
for i in unique:
    if i not in new_high_list:
        new_list = new_high_list.copy()
        new_list.append(i)
        new_list.sort(reverse=True)
        index = new_list.index(i)
        high_rankings.append(index+1)
        new_list.pop(new_list.index(i))
    else:
        index = new_high_list.index(i)
        high_rankings.append(index+1)
high_df["Highest Possible Ranking"] = high_rankings
merged = merged.merge(high_df, how = "inner", on = "Highest Possible Rating")

unique = merged["Lowest Possible Rating"].unique()
new_high_list = sorted([(merged.iloc[i]["Highest Possible Rating"]) for i in range(merged.shape[0])], reverse = True)
high_df = pd.DataFrame(unique, columns = ["Lowest Possible Rating"])
high_rankings = []
for i in unique:
    if i not in new_high_list:
        new_list = new_high_list.copy()
        new_list.append(i)
        new_list.sort(reverse=True)
        index = new_list.index(i)
        high_rankings.append(index)
        new_list.pop(new_list.index(i))
    else:
        index = new_high_list.index(i)
        high_rankings.append(index+1)
high_df["Lowest Possible Ranking"] = high_rankings
merged = merged.merge(high_df, how = "inner", on = "Lowest Possible Rating")

unique = merged["Highest Queue Rating"].unique()
new_high_list = sorted([(merged.iloc[i]["Lowest Queue Rating"]) for i in range(merged.shape[0])], reverse = True)
high_df = pd.DataFrame(unique, columns = ["Highest Queue Rating"])
high_rankings = []
for i in unique:
    if i not in new_high_list:
        new_list = new_high_list.copy()
        new_list.append(i)
        new_list.sort(reverse=True)
        index = new_list.index(i)
        high_rankings.append(index+1)
        new_list.pop(new_list.index(i))
    else:
        index = new_high_list.index(i)
        high_rankings.append(index+1)
high_df["Highest Queue Ranking"] = high_rankings
merged = merged.merge(high_df, how = "inner", on = "Highest Queue Rating")

unique = merged["Lowest Queue Rating"].unique()
new_high_list = sorted([(merged.iloc[i]["Highest Queue Rating"]) for i in range(merged.shape[0])], reverse = True)
high_df = pd.DataFrame(unique, columns = ["Lowest Queue Rating"])
high_rankings = []
for i in unique:
    if i not in new_high_list:
        new_list = new_high_list.copy()
        new_list.append(i)
        new_list.sort(reverse=True)
        index = new_list.index(i)
        high_rankings.append(index)
        new_list.pop(new_list.index(i))
    else:
        index = new_high_list.index(i)
        high_rankings.append(index+1)
high_df["Lowest Queue Ranking"] = high_rankings
merged = merged.merge(high_df, how = "inner", on = "Lowest Queue Rating")


unique = merged["Highest Possible Rating"].unique()
new_high_list = sorted([(merged.iloc[i]["Rating"]) for i in range(merged.shape[0])], reverse = True)
high_df = pd.DataFrame(unique, columns = ["Highest Possible Rating"])
high_rankings = []
for i in unique:
    if i not in new_high_list:
        new_list = new_high_list.copy()
        new_list.append(i)
        new_list.sort(reverse=True)
        index = new_list.index(i)
        high_rankings.append(index+1)
        new_list.pop(new_list.index(i))
    else:
        index = new_high_list.index(i)
        high_rankings.append(index+1)
high_df["Highest Immediate Ranking"] = high_rankings
merged = merged.merge(high_df, how = "inner", on = "Highest Possible Rating")

unique = merged["Lowest Possible Rating"].unique()
new_high_list = sorted([(merged.iloc[i]["Rating"]) for i in range(merged.shape[0])], reverse = True)
high_df = pd.DataFrame(unique, columns = ["Lowest Possible Rating"])
high_rankings = []
for i in unique:
    if i not in new_high_list:
        new_list = new_high_list.copy()
        new_list.append(i)
        new_list.sort(reverse=True)
        index = new_list.index(i)
        high_rankings.append(index+1)
        new_list.pop(new_list.index(i))
    else:
        index = new_high_list.index(i)
        high_rankings.append(index+1)
high_df["Lowest Immediate Ranking"] = high_rankings
merged = merged.merge(high_df, how = "inner", on = "Lowest Possible Rating")



merged = merged.sort_values(["Rating", "Artist"], ascending = [False, True]).reset_index()
merged["Possible Rankings"] = - merged["Highest Possible Ranking"] + merged["Lowest Possible Ranking"] +1
merged["Possible Queue Rankings"] = - merged["Highest Queue Ranking"] + merged["Lowest Queue Ranking"] +1
merged["Possible Immediate Rankings"] = - merged["Highest Immediate Ranking"] + merged["Lowest Immediate Ranking"] +1
merged["Range"] =(merged["Highest Possible Rating"] - merged["Lowest Possible Rating"]).round(2)
merged["Queue Range"] =(merged["Highest Queue Rating"] - merged["Lowest Queue Rating"]).round(2)
merged["League"] = "None"
merged.loc[merged.index < 20, "League"] = "Premier League"
merged.loc[(merged.index < 44) & (merged["League"] == "None"), "League"] = "EFL Championship"
merged.loc[(merged.index < 68) & (merged["League"] == "None"), "League"] = "EFL League One"
merged.loc[(merged.index < 92) & (merged["League"] == "None"), "League"] = "EFL League Two"
merged.loc[(merged.index < 116) & (merged["League"] == "None"), "League"] = "National League"
merged.loc[(merged.index < 138) & (merged["League"] == "None"), "League"] = "National League North"
merged.loc[(merged.index < 160) & (merged["League"] == "None"), "League"] = "National League South"
merged.loc[(merged.index < 182) & (merged["League"] == "None"), "League"] = "Northern Premier League Premier"
merged.loc[(merged.index < 204) & (merged["League"] == "None"), "League"] = "Southern League Premier Central"
merged.loc[(merged.index < 226) & (merged["League"] == "None"), "League"] = "Southern League Premier South"
merged.loc[(merged.index < 248) & (merged["League"] == "None"), "League"] = "Isthmian League Premier"
merged.loc[(merged.index < 268) & (merged["League"] == "None"), "League"] = "Northern Premier League Division One East"
merged.loc[(merged.index < 288) & (merged["League"] == "None"), "League"] = "Northern Premier League Division One Midlands"
merged.loc[(merged.index < 308) & (merged["League"] == "None"), "League"] = "Northern Premier League Division One West"
merged.loc[(merged.index < 328) & (merged["League"] == "None"), "League"] = "Southern League Division One Central"
merged.loc[(merged.index < 348) & (merged["League"] == "None"), "League"] = "Southern League Division One South"
merged.loc[(merged.index < 368) & (merged["League"] == "None"), "League"] = "Isthmian League Division One South Central"
merged.loc[(merged.index < 388) & (merged["League"] == "None"), "League"] = "Isthmian League Division One North"
merged.loc[(merged.index < 408) & (merged["League"] == "None"), "League"] = "Isthmian League Division One South East"

old_power = 7.887
if input("Would you like to update the test rating? ") == "Yes":
	print("You decided to update the test rating. This will take a few minutes.")
	for i in range(78000,80000,1):
		power = i/10000
		merged["Test Rating"] = merged["Number of Songs"]*(merged["Number of Songs"]/(merged["Number of Songs"]+merged["Number of Songs Disliked"]) + merged["Number of Songs Loved"]/merged["Number of Songs"])**power
		merged["Test Rating"] = merged["Test Rating"].round(2)
		merged.loc[merged["Rating"] < 0, "Test Rating"] = merged["Rating"]
		if merged["Test Rating"].max()/100 == merged["Test Rating"].max()//100:
			break
	print(power)
else:
	print("You decided not to update the test rating. Sad.")
	merged["Test Rating"] = merged["Number of Songs"]*(merged["Number of Songs"]/(merged["Number of Songs"]+merged["Number of Songs Disliked"]) + merged["Number of Songs Loved"]/merged["Number of Songs"])**old_power
	merged["Test Rating"] = merged["Test Rating"].round(2)
	merged.loc[merged["Rating"] < 0, "Test Rating"] = merged["Rating"]


#merged.loc[(merged.index < 426) & (merged["League"] == "None"), "League"] = "Combined Counties League Premier Division North"
#merged.loc[(merged.index < 446) & (merged["League"] == "None"), "League"] = "Combined Counties League Premier Division South"
#merged.loc[(merged.index < 446) & (merged["League"] == "None"), "League"] = "Eastern Counties League Premier"
#merged.loc[(merged.index < 467) & (merged["League"] == "None"), "League"] = "Essex Senior League"
#merged.loc[(merged.index < 487) & (merged["League"] == "None"), "League"] = "Hellenic League Premier"
#merged.loc[(merged.index < 506) & (merged["League"] == "None"), "League"] = "Midland League Premier"
#merged.loc[(merged.index < 527) & (merged["League"] == "None"), "League"] = "North West Counties League Premier"
#merged.loc[(merged.index < 547) & (merged["League"] == "None"), "League"] = "Northern Counties East League Premier"
#merged.loc[(merged.index < 567) & (merged["League"] == "None"), "League"] = "Northern League Division One"
#merged.loc[(merged.index < 587) & (merged["League"] == "None"), "League"] = "Southern Counties East League Premier"
#merged.loc[(merged.index < 607) & (merged["League"] == "None"), "League"] = "Spartan South Midlands League Premier"
#merged.loc[(merged.index < 627) & (merged["League"] == "None"), "League"] = "Southern Combination League Premier Division"
#merged.loc[(merged.index < 645) & (merged["League"] == "None"), "League"] = "United Counties League Premier Division North"
#merged.loc[(merged.index < 665) & (merged["League"] == "None"), "League"] = "United Counties League Premier Division South"
#merged.loc[(merged.index < 686) & (merged["League"] == "None"), "League"] = "Wessex League Premier Division"
#merged.loc[(merged.index < 705) & (merged["League"] == "None"), "League"] = "Western League Premier Division"

old = pd.read_csv("artist_ranking.csv")
test_merged = pd.merge(merged, old, on = "Artist", how = "left")
changed = test_merged.loc[(test_merged["Number of Songs Undecided_x"] + test_merged["Total Songs Reviewed_x"]) < (test_merged["Number of Songs Undecided_y"] + test_merged["Total Songs Reviewed_y"])].copy()
print("Artists with Lost Songs:", list(changed["Artist"]))
merged = merged.drop(columns = "index")
merged.to_csv("artist_ranking.csv", encoding = "utf-8", index = False)
print("Check artist_ranking.csv for your updated ranking!!")