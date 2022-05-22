#!/usr/bin/env python3

import argparse 
import codecs
import http.client
import http.server
import json
import logging
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import webbrowser
import pandas as pd
import numpy as np

logging.basicConfig(level=20, datefmt='%I:%M:%S', format='[%(asctime)s] %(message)s')


class SpotifyAPI:
	
	# Requires an OAuth token.
	def __init__(self, auth):
		self._auth = auth
	
	# Gets a resource from the Spotify API and returns the object.
	def get(self, url, params={}, tries=3):
		# Construct the correct URL.
		if not url.startswith('https://api.spotify.com/v1/'):
			url = 'https://api.spotify.com/v1/' + url
		if params:
			url += ('&' if '?' in url else '?') + urllib.parse.urlencode(params)
	
		# Try the sending off the request a specified number of times before giving up.
		for _ in range(tries):
			try:
				req = urllib.request.Request(url)
				req.add_header('Authorization', 'Bearer ' + self._auth)
				res = urllib.request.urlopen(req)
				reader = codecs.getreader('utf-8')
				return json.load(reader(res))
			except Exception as err:
				logging.info('Couldn\'t load URL: {} ({})'.format(url, err))
				time.sleep(2)
				logging.info('Trying again...')
		sys.exit(1)
	
	# The Spotify API breaks long lists into multiple pages. This method automatically
	# fetches all pages and joins them, returning in a single list of objects.
	def list(self, url, params={}):
		last_log_time = time.time()
		response = self.get(url, params)
		items = response['items']

		while response['next']:
			if time.time() > last_log_time + 15:
				last_log_time = time.time()
				logging.info(f"Loaded {len(items)}/{response['total']} items")

			response = self.get(response['next'])
			items += response['items']
		return items
	
	# Pops open a browser window for a user to log in and authorize API access.
	@staticmethod
	def authorize(client_id, scope):
		url = 'https://accounts.spotify.com/authorize?' + urllib.parse.urlencode({
			'response_type': 'token',
			'client_id': client_id,
			'scope': scope,
			'redirect_uri': 'http://127.0.0.1:{}/redirect'.format(SpotifyAPI._SERVER_PORT)
		})
		logging.info(f'Logging in (click if it doesn\'t open automatically): {url}')
		webbrowser.open(url)
	
		# Start a simple, local HTTP server to listen for the authorization token... (i.e. a hack).
		server = SpotifyAPI._AuthorizationServer('127.0.0.1', SpotifyAPI._SERVER_PORT)
		try:
			while True:
				server.handle_request()
		except SpotifyAPI._Authorization as auth:
			return SpotifyAPI(auth.access_token)
	
	# The port that the local server listens on. Don't change this,
	# as Spotify only will redirect to certain predefined URLs.
	_SERVER_PORT = 43019
	
	class _AuthorizationServer(http.server.HTTPServer):
		def __init__(self, host, port):
			http.server.HTTPServer.__init__(self, (host, port), SpotifyAPI._AuthorizationHandler)
		
		# Disable the default error handling.
		def handle_error(self, request, client_address):
			raise
	
	class _AuthorizationHandler(http.server.BaseHTTPRequestHandler):
		def do_GET(self):
			# The Spotify API has redirected here, but access_token is hidden in the URL fragment.
			# Read it using JavaScript and send it to /token as an actual query string...
			if self.path.startswith('/redirect'):
				self.send_response(200)
				self.send_header('Content-Type', 'text/html')
				self.end_headers()
				self.wfile.write(b'<script>location.replace("token?" + location.hash.slice(1));</script>')
			
			# Read access_token and use an exception to kill the server listening...
			elif self.path.startswith('/token?'):
				self.send_response(200)
				self.send_header('Content-Type', 'text/html')
				self.end_headers()
				self.wfile.write(b'<script>close()</script>Thanks! You may now close this window.')

				access_token = re.search('access_token=([^&]*)', self.path).group(1)
				logging.info(f'Received access token from Spotify: {access_token}')
				raise SpotifyAPI._Authorization(access_token)
			
			else:
				self.send_error(404)
		
		# Disable the default logging.
		def log_message(self, format, *args):
			pass
	
	class _Authorization(Exception):
		def __init__(self, access_token):
			self.access_token = access_token


def main():
	# Parse arguments.
	parser = argparse.ArgumentParser(description='Exports your Spotify playlists. By default, opens a browser window '
	                                           + 'to authorize the Spotify Web API, but you can also manually specify'
	                                           + ' an OAuth token with the --token option.')
	parser.add_argument('--token', metavar='OAUTH_TOKEN', help='use a Spotify OAuth token (requires the '
	                                                         + '`playlist-read-private` permission)')
	parser.add_argument('--dump', default='liked', choices=['liked,playlists', 'playlists,liked', 'playlists', 'liked'],
	                    help='dump playlists or Liked Songs, or both (default: playlists)')
	parser.add_argument('--format', default='txt', choices=['json', 'txt'], help='output format (default: txt)')
	parser.add_argument('file', help='output filename', nargs='?')
	args = parser.parse_args()
	
	# If they didn't give a filename, then just prompt them. (They probably just double-clicked.)
	while not args.file:
		args.file = "saved_list.csv"
		args.format = args.file.split('.')[-1]
	
	# Log into the Spotify API.
	if args.token:
		spotify = SpotifyAPI(args.token)
	else:
		spotify = SpotifyAPI.authorize(client_id='5c098bcc800e45d49e476265bc9b6934',
		                               scope='playlist-read-private playlist-read-collaborative user-library-read')
	
	# Get the ID of the logged in user.
	logging.info('Loading user info...')
	me = spotify.get('me')
	logging.info('Logged in as {display_name} ({id})'.format(**me))

	playlists = []

	# List Artists
	if 'liked' in args.dump:
		logging.info('Loading Artists...')
		liked_tracks = spotify.list('users/{user_id}/tracks'.format(user_id=me['id']), {'limit': 50})
		playlists += [{'name': 'Artists', 'tracks': liked_tracks}]

	# List all playlists and the tracks in each playlist
	if 'playlists' in args.dump:
		logging.info('Loading playlists...')
		playlist_data = spotify.list('users/{user_id}/playlists'.format(user_id=me['id']), {'limit': 50})
		logging.info(f'Found {len(playlist_data)} playlists')

		# List all tracks in each playlist
		for playlist in playlist_data:
			logging.info('Loading playlist: {name} ({tracks[total]} songs)'.format(**playlist))
			playlist['tracks'] = spotify.list(playlist['tracks']['href'], {'limit': 100})
		playlists += playlist_data
	
	# Write the file.
	logging.info('Writing files...')
	with open(args.file, 'w', encoding='utf-8') as f:
		# JSON file.
		if args.format == 'json':
			json.dump(playlists, f)
		
		# Tab-separated file.
		else:
			count = 1
			for playlist in playlists:
				f.write("Liked Songs" + '\tArtists' +'\tID'+ '\tExCol'+ '\r\n')
				for track in playlist['tracks']:
					if track['track'] is None:
						continue
					if count == 1:
						count += 1
					f.write('{name}\t{artists}\t{album}\t{id}\r\n'.format(
						id=track['track']['id'],
						name=track['track']['name'],
						artists=', '.join([artist['name'] for artist in track['track']['artists']]),
						album=track['track']['album']['name']
					))
				f.write('\r\n')
	#logging.info('Wrote raw data file: ' + args.file)
	return args.file

if __name__ == '__main__':
	main = main()
	data = pd.read_csv(main, sep = '\t')
	duplicate_group = data.groupby(["Liked Songs", "Artists"]).count()
	duplicates = duplicate_group[duplicate_group["ExCol"] > 1].copy()
	del duplicate_group
	pd.set_option("display.max_rows", 100, "display.max_columns", None)
	if duplicates.shape != (0,0):
		print(duplicates.sort_values("Artists"))
	else:
		print("Zero Duplicates Found!")

	del duplicates
	print(data.columns)

	data["Artists"] = data["Artists"].str.replace("feat. ", ", ")
	data["Artists"] = data["Artists"].str.replace("Tyler, The Creator", "Tyler The Creator") #might be a more systematic way of making this fix (comes from splitting by commas)
	data["Artists"] = data["Artists"].str.replace("Meechie", "Meechy")
	data["Artists"] = data["Artists"].str.replace("Hank Williams, Jr.", "Hank Williams Jr.")
	data["Artists"] = data["Artists"].str.replace("Bazzi vs.", "Bazzi")
	data["Artists"] = data["Artists"].str.replace("Nyck @ Knight", "Nyck Caution, Kirk Knight")
	data["Artists"] = data["Artists"].str.replace("Aloe Blacc X David Correy", "Aloe Blacc, David Correy")
	data["Artists"] = data["Artists"].str.replace("Mumford & Sons (Remix)", "Mumford & Sons", regex=False)
	data["Artists"] = data["Artists"].str.replace("B.oB", "B.o.B", regex=False)
	data["Artists"] = data["Artists"].str.replace("B.o.B.", "B.o.B", regex=False)
	data["Artists"] = data["Artists"].str.replace("Betatraxx", "BetaTraxx")
	data["Artists"] = data["Artists"].str.replace("Nate Feuerstein", "NF")
	data["Artists"] = data["Artists"].str.replace("Conway the Machine", "Conway")
	data["Artists"] = data["Artists"].str.replace("nothing,nowhere.", "nothing;nowhere.", regex = False)
	data["Artists"] = data["Artists"].str.replace("The Throne", "JAY-Z, Kanye West")
	data["Artists"] = data["Artists"].str.replace("MGK", "Machine Gun Kelly")
	data["Artists"] = data["Artists"].str.replace("Holly Brook", "Skylar Grey")
	data["Artists"] = data["Artists"].str.replace("Marina & The Diamonds", "MARINA")
	data["Artists"] = data["Artists"].str.replace("Macklemore & Ryan Lewis", "Macklemore, Ryan Lewis")
	data["Artists"] = data["Artists"].str.replace("Seth Avett & Jessica Lea Mayfield", "Seth Avett, Jessica Lea Mayfield")
	data["Artists"] = data["Artists"].str.replace("Eric B. & Rakim", "Eric B., Rakim", regex=False)
	data["Artists"] = data["Artists"].str.replace("Boy & Bear and Jess Chalker", "Boy & Bear, Jess Chalker")
	data["Artists"] = data["Artists"].str.replace("Elana Stone & Brian Campeau", "Elana Stone, Brian Campeau")
	data["Artists"] = data["Artists"].str.replace("Gabrielle Huber & Cameron Potts", "Gabrielle Huber, Cameron Potts")
	data["Artists"] = data["Artists"].str.replace('Denaun', 'Mr. Porter')
	data["Artists"] = data["Artists"].str.replace('Mr Porter', 'Mr. Porter')
	data["Artists"] = data["Artists"].str.replace('Kevin Parker', 'Tame Impala')
	data["Artists"] = data["Artists"].str.replace('Alex Lasarenko', 'Alexander Lasarenko')
	data["Artists"] = data["Artists"].str.replace('Jethro Sheeran', 'Alonestar')
	data["Artists"] = data["Artists"].str.replace('Jacquie Lee', 'Jacquie')
	data["Artists"] = data["Artists"].str.replace('Achromatik', 'Peter James')
	data["Artists"] = data["Artists"].str.replace('Meyhem', 'Meyhem Lauren')
	data["Artists"] = data["Artists"].str.replace('Hannah Montana', 'Miley Cyrus')
	data["Artists"] = data["Artists"].str.replace('Troi Martin', 'Troi Irons')
	data["Artists"] = data["Artists"].str.replace('Troi', 'Troi Irons')
	data["Artists"] = data["Artists"].str.replace('Nottz Raw', 'Nottz')
	data["Artists"] = data["Artists"].str.replace('Kate Miller Heidke', 'Kate Miller-Heidke')
	data["Artists"] = data["Artists"].str.replace('Beastcoast', 'Beast Coast')
	data["Artists"] = data["Artists"].str.replace('Planet Vi', 'R. City')
	data["Artists"] = data["Artists"].str.replace('Claire Cottrill', 'Clairo')

	data['Artists'] = np.where(data["Artists"].str.contains("PRhyme"), data["Artists"]+''', Royce Da 5'9"''', data["Artists"])
	data['Artists'] = np.where(data["Artists"].str.contains("PRhyme"), data["Artists"]+", DJ Premier", data["Artists"])
	data['Artists'] = np.where(data["Artists"].str.contains("Bad Meets Evil"), data["Artists"]+''', Royce Da 5'9"''', data["Artists"])
	data['Artists'] = np.where(data["Artists"].str.contains("Bad Meets Evil"), data["Artists"]+", DJ Premier", data["Artists"])
	data['Artists'] = np.where(data["Artists"].str.contains("KIDS SEE GHOSTS"), data["Artists"]+", Kanye West", data["Artists"])
	data['Artists'] = np.where(data["Artists"].str.contains("KIDS SEE GHOSTS"), data["Artists"]+", Kid Cudi", data["Artists"])
	data['Artists'] = np.where(data["Artists"].str.contains("mansionz"), data["Artists"]+", blackbear", data["Artists"])
	data['Artists'] = np.where(data["Artists"].str.contains("mansionz"), data["Artists"]+", Mike Posner", data["Artists"])
	data['Artists'] = np.where(data["Artists"].str.contains("Run The Jewels"), data["Artists"]+", Killer Mike", data["Artists"])
	data['Artists'] = np.where(data["Artists"].str.contains("Run The Jewels"), data["Artists"]+", El-P", data["Artists"])
	data['Artists'] = np.where(data["Artists"].str.contains("TWENTY88"), data["Artists"]+", Jhené Aiko", data["Artists"])
	data['Artists'] = np.where(data["Artists"].str.contains("TWENTY88"), data["Artists"]+", Big Sean", data["Artists"])
	data['Artists'] = np.where(data["Artists"].str.contains("Underachievers"), data["Artists"]+", Issa Gold", data["Artists"])
	data['Artists'] = np.where(data["Artists"].str.contains("Underachievers"), data["Artists"]+", AKTHESAVIOR", data["Artists"])
	data['Artists'] = np.where(data["Artists"].str.contains("Rae Sremmurd"), data["Artists"]+", Swae Lee", data["Artists"])
	data['Artists'] = np.where(data["Artists"].str.contains("Rae Sremmurd"), data["Artists"]+", Slim Jxmmi", data["Artists"])
	data['Artists'] = np.where(data["Artists"].str.contains("Slaughterhouse"), data["Artists"]+''', Royce Da 5'9"''', data["Artists"])
	data['Artists'] = np.where(data["Artists"].str.contains("Slaughterhouse"), data["Artists"]+", KXNG Crooked", data["Artists"])
	data['Artists'] = np.where(data["Artists"].str.contains("Slaughterhouse") & (~data["Liked Songs"].str.contains("Psychopath Killer")) & (~data["Liked Songs"].str.contains("Our House")), data["Artists"]+", Joe Budden", data["Artists"])
	data['Artists'] = np.where(data["Artists"].str.contains("Slaughterhouse") & (~data["Liked Songs"].str.contains("Psychopath Killer")), data["Artists"]+", Joell Ortiz", data["Artists"])


	data['Artists'] = np.where(data["Artists"].str.contains("Black Hippy"), data["Artists"]+", ScHoolboy Q", data["Artists"])
	data['Artists'] = np.where(data["Artists"].str.contains("Black Hippy"), data["Artists"]+", Kendrick Lamar", data["Artists"])
	data['Artists'] = np.where(data["Artists"].str.contains("Black Hippy"), data["Artists"]+", Jay Rock", data["Artists"])
	data['Artists'] = np.where(data["Artists"].str.contains("Black Hippy"), data["Artists"]+", Ab-Soul", data["Artists"])

	data['Artists'] = np.where(data["Artists"].str.contains("Banks & Steelz"), data["Artists"]+", RZA", data["Artists"])
	data['Artists'] = np.where(data["Artists"].str.contains("Banks & Steelz"), data["Artists"]+", Paul Banks", data["Artists"])
	data['Artists'] = np.where(data["Artists"].str.contains("Wu-Tang Clan") & (data["Liked Songs"]=="Crushed Egos"), data["Artists"]+", Raekwon, RZA", data["Artists"])
	data['Artists'] = np.where(data["Artists"].str.contains("Wu-Tang Clan") & (data["Liked Songs"]=="Miracle"), data["Artists"]+", Method Man, Raekwon, Cappadonna, Masta Killa", data["Artists"])
	data['Artists'] = np.where(data["Artists"].str.contains("Wu-Tang Clan") & (data["Liked Songs"]=="A Better Tomorrow"), data["Artists"]+", Raekwon, RZA", data["Artists"])
	data['Artists'] = np.where(data["Artists"].str.contains("Wu-Tang Clan") & (data["Liked Songs"]=="Never Let Go"), data["Artists"]+", RZA, U-God, Inspectah Deck, Method Man, GZA, Masta Killa", data["Artists"])
	data['Artists'] = np.where(data["Artists"].str.contains("Wu-Tang Clan") & (data["Liked Songs"]=="Ruckus in B Minor"), data["Artists"]+", Cappadonna, Ghostface Killah, GZA, Inspectah Deck, Masta Killa, Method Man, Ol' Dirty Bastard, Raekwon, RZA, U-God", data["Artists"])

	data['Artists'] = np.where(data["Artists"].str.contains("Migos") & (data["Liked Songs"].str.contains("Bad and Boujee")), data["Artists"]+", Quavo, Offset", data["Artists"])
	data['Artists'] = np.where(data["Artists"].str.contains("Migos") & (data["Liked Songs"].str.contains("Every City We Go")), data["Artists"]+", Quavo, Offset", data["Artists"])
	data['Artists'] = np.where(data["Artists"].str.contains("Migos") & (data["Liked Songs"].str.contains("Having Our Way")), data["Artists"]+", Quavo, Offset, Takeoff", data["Artists"])
	data['Artists'] = np.where(data["Artists"].str.contains("Migos") & (data["Liked Songs"].str.contains("Irresistible")), data["Artists"]+", Quavo, Takeoff", data["Artists"])
	data['Artists'] = np.where(data["Artists"].str.contains("Migos") & (data["Liked Songs"].str.contains("MotorSport")), data["Artists"]+", Quavo, Offset, Takeoff", data["Artists"])
	data['Artists'] = np.where(data["Artists"].str.contains("Migos") & (data["Liked Songs"].str.contains("Slide")), data["Artists"]+", Quavo, Offset", data["Artists"])
	data['Artists'] = np.where(data["Artists"].str.contains("Migos") & (data["Liked Songs"].str.contains("Straightenin")), data["Artists"]+", Quavo, Offset, Takeoff", data["Artists"])

	data['Artists'] = np.where(data['Artists'].str.contains("D12") & (~data["Liked Songs"].str.contains("Girls")), data['Artists']+", Bizarre", data['Artists'])
	data['Artists'] = np.where(data['Artists'].str.contains("D12"), data['Artists']+", Eminem", data['Artists'])
	data['Artists'] = np.where(data['Artists'].str.contains("D12") & (~data["Liked Songs"].str.contains("Girls")), data['Artists']+", Kuniva", data['Artists'])
	data['Artists'] = np.where(data['Artists'].str.contains("D12") & (~data["Liked Songs"].str.contains("Girls")), data['Artists']+", Mr. Porter", data['Artists'])
	data['Artists'] = np.where(data['Artists'].str.contains("D12") & (~data["Liked Songs"].str.contains("Girls|But Music")), data['Artists']+", Proof", data['Artists'])
	data['Artists'] = np.where(data['Artists'].str.contains("D12") & (~data["Liked Songs"].str.contains("Girls")), data['Artists']+", Swifty McVay", data['Artists'])

	data['Artists'] = np.where(data['Artists'].str.contains("Flatbush Zombies") & (~data["Liked Songs"].str.contains("Ascension|Fly Away|My Jeep")), data['Artists']+", Erick the Architect", data['Artists'])
	data['Artists'] = np.where(data['Artists'].str.contains("Flatbush Zombies") & (~data["Liked Songs"].str.contains("Distance|Spike Lee Joint")), data['Artists']+", Meechy Darko", data['Artists'])
	data['Artists'] = np.where(data['Artists'].str.contains("Flatbush Zombies") & (~data["Liked Songs"].str.contains("Ascension|Dirty Elevator Music|Distance|Fly Away|Last Choir|My Jeep|Snow In The Stadium")), data['Artists']+", Zombie Juice", data['Artists'])

	data['Artists'] = np.where(data['Artists'].str.contains("STATIK KXNG"), data['Artists']+", KXNG Crooked", data['Artists'])
	data['Artists'] = np.where(data['Artists'].str.contains("STATIK KXNG"), data['Artists']+", Statik Selektah", data['Artists'])

	liked_songs = pd.DataFrame(data["Artists"])

	del data

	liked_songs["Artists"] = liked_songs["Artists"].str.split(",")
	liked_songs["Artists"] = liked_songs["Artists"].apply(lambda my_list:[x.strip() for x in my_list])
	liked_songs["Artists"] = liked_songs["Artists"].apply(set)
	liked_songs["Length"] = liked_songs["Artists"].str.len()
	artists = pd.DataFrame(liked_songs["Artists"].values.tolist())
	del liked_songs
	names = artists[0].append(artists[1])
	for i in artists.columns[2:]:
		names = names.append(artists[i])
	names = names.str.replace("^ ", "") #replace space at beginning of string
	names = names.str.replace(" $", "") #replace space at end of string
	names = pd.DataFrame(names)
	names["Arist"] = "True"
	grouped = names.groupby(0).count()
	del artists
	del names
	grouped.reset_index(inplace=True)
	grouped = grouped.rename(columns = {0:"Artist", "Arist":"Number of Songs"})
	grouped = grouped.sort_values(["Number of Songs", "Artist"], ascending = [False, True])
	grouped.reset_index(inplace=True)
	grouped["Rank"] = grouped.index  +1
	grouped = grouped.drop(columns = 'index')
	ties = grouped.groupby("Number of Songs")["Rank"].min()
	merged = grouped.merge(ties, left_on = "Number of Songs", right_on = "Number of Songs")
	del grouped
	del ties
	merged["Rank_x"] = merged["Rank_x"].astype(str)
	merged["Rank_y"] = merged["Rank_y"].astype(str)
	merged.loc[merged["Rank_x"] != merged["Rank_y"], "Rank_y"] = "T"+merged["Rank_y"]
	merged = merged.drop(columns = "Rank_x")
	merged = merged.rename(columns = {"Rank_y":"Rank"})
	merged.loc[("T" +merged["Rank"]).isin(merged["Rank"]), "Rank"] = "T"+merged["Rank"]
	merged.to_csv("saved_songs.csv", encoding = "utf-8", index = False)
	print("Check saved_songs.csv for your saved-only ranking!!")

