import os
from plexapi.server import PlexServer
from plexapi import utils 
from pprint import pprint

from secrets import *

ONLY_DUMP_RATED=False

plex = PlexServer(baseurl, token)

sections = [section for section in plex.library.sections()]

section = plex.library.section("Music")
for item in section.all():
    for track in item.tracks():
        if track.userRating == None and ONLY_DUMP_RATED:
            continue
        
        rating = 0 if track.userRating == None else track.userRating / 2
        print(f"#EXT-X-RATING:{int(rating)}")
        print(track.media[0].parts[0].file)
