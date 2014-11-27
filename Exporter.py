import msgpack
import argparse
import json
from Common import *

parser = argparse.ArgumentParser(description='Export Google Play Music library for importing later.')
parser.add_argument('-e', '--email')
parser.add_argument('-p', '--password')
parser.add_argument('-o', '--output')
parser.add_argument('-aa', action='store_const', const=True, default=False)

if __name__ == '__main__':
    args = parser.parse_args()
    api = login(args.email, args.password)
    songs = api.get_all_songs()

    ids = map(get_aa_id, filter(lambda x: is_aa_track(x, args.aa), songs))
    if args.output:
        with open(args.output, 'w') as f:
            f.write(msgpack.packb(ids))
    else:
        print json.dumps(ids)