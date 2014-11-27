import msgpack
import argparse
import json
from Common import *

parser = argparse.ArgumentParser(description='Dedupe All Access Tracks if the full track is purchased.')
parser.add_argument('-e', '--email')
parser.add_argument('-p', '--password')
parser.add_argument('-o', '--output')

if __name__ == '__main__':
    args = parser.parse_args()
    api = login(args.email, args.password)
    songs = api.get_all_songs()

    purchased = filter(lambda x: not is_aa_track(x, True), songs)
    aa = filter(lambda x: is_aa_track(x, True), songs)
    
    todelete = []
    for track in purchased:
        for aa_track in aa:
            if aa_track['album'] == track['album'] and aa_track['title'] == track['title']:
                print track['album'] + ' - ' + track['title']
                todelete.append(aa_track['id'])
                break

    print api.delete_songs(todelete)