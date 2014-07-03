#!/usr/bin/env python
import Spotify
import sys


def app():
    spotify = Spotify.Spotify()

    if len(sys.argv) > 1:
        if sys.argv[1] == '-n':
            spotify.next()

        elif sys.argv[1] == '-p':
            spotify.prev()

        elif sys.argv[1] == '-pp':
            spotify.play_pause()

        elif sys.argv[1] == '-s':
            spotify.stop()

        elif sys.argv[1] == '-m':
            spotify.meta()

        elif sys.argv[1] == '-h':
            print """
            -n for next song
            -p for previous song
            -pp for pause and play song
            -s to stop song
            """

        else:
            print """
            See -h for help
            """

    else:
        print """
############################################################
#            _____             _   _  __                   #                      
#           / ____|           | | (_)/ _|                  #
#          | (___  _ __   ___ | |_ _| |_ _   _             #
#           \___ \| '_ \ / _ \| __| |  _| | | |            #
#           ____) | |_) | (_) | |_| | | | |_| |            #
#          |_____/| .__/ \___/ \__|_|_|  \__, |            #
#                 | |                     __/ |            #
#                 |_|                    |___/             #
#                                                          #  
# by bjarneo <http://www.github.com/bjarneo/PythonSpotify> #
#                                                          #
############################################################
"""

        while 1:
            search_input = raw_input('What artist / song are you searching for?\n> ')
            if search_input:
                spotify.search(search_input)
                spotify.list(10)
                spotify.print_history()

                song_input = raw_input('\nType song number and press <enter> to play. Press <enter> for new search.\n> ')
                if song_input:
                    print spotify.listen(int(song_input))
                else:
                    continue

if __name__ == '__main__':
    app()
