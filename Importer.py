import msgpack
import argparse
import json
from Common import *

parser = argparse.ArgumentParser(description='Import exported library into Google Play Music.')
parser.add_argument('-e', '--email')
parser.add_argument('-p', '--password')
parser.add_argument('file')

if __name__ == '__main__':
    args = parser.parse_args()
    api = login(args.email, args.password)

    with open(args.file, 'r') as f:
        ids = msgpack.unpackb(f.read())
        print map(api.add_aa_track, ids)
