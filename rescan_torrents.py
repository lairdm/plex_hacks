import os
from plexapi.server import PlexServer
from plexapi import utils 
from pprint import pprint

from secrets import *

ONLY_DUMP_RATED=False

plex = PlexServer(baseurl, token)

section = plex.library.sectionByID(5)
section.refresh()
