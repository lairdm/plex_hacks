import os
from plexapi.server import PlexServer
from plexapi import utils 

from secrets import *

plex = PlexServer(baseurl, token)

#movies = plex.library.section('Movies')
#for video in movies.search(unwatched=True):
#    print(video.title)

for client in plex.clients():
    print(client.title)
