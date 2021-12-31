import os
from plexapi.server import PlexServer
from plexapi import utils 
from pprint import pprint

from secrets import * 

plex = PlexServer(baseurl, token)

playlists = [pl for pl in plex.playlists()]
playlist = utils.choose('Choose Playlist', playlists, lambda pl: '%s' % pl.title)

for photo in playlist.items():
    photomediapart = photo.media[0].parts[0]
    print ('\tDownload File: %s' % photomediapart.file)
    url = plex.url('%s?download=1' % photomediapart.key)
#    print(photo.__dict__)
#    print(dir(photo))

    artist = photo.grandparentTitle
    if photo.originalTitle:
        artist = photo.originalTitle
    filename = "{} - {}.{}".format(artist, photo.title, photo.media[0].container)
    print(filename)
    utils.download(url, token, filename)
