#!/usr/bin/python3
# this is a smith configuration file

# override the default folders
# DOCDIR = ["documentation", "web"]

# set the font name and description
APPNAME = 'LekeProposal'

# Get version and authorship information from Regular UFO (canonical metadata); must be first function call:
getufoinfo('source/LekeProposal-Regular.ufo')

designspace('source/LekeProposal.designspace',
    target = "${DS:FILENAME_BASE}.ttf",
    pdf = fret(params='-oi')
)
