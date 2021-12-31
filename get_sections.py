import os
from plexapi.server import PlexServer
from plexapi import utils 
from pprint import pprint

from secrets import *

ONLY_DUMP_RATED=False

plex = PlexServer(baseurl, token)

sections = [section for section in plex.library.sections()]

pprint(sections)
