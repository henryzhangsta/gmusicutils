import gmusicapi
import getpass

def is_aa_track(track, aa_only=False):
    if aa_only and (not track.has_key('trackType') or track['trackType'] != '8'):
        return False

    if track.has_key('nid') and track['nid'].startswith('T'):
        return True
    elif track.has_key('storeId') and track['storeId'].startswith('T'):
        return True
    return False

def get_aa_id(track):
    if track.has_key('nid') and track['nid'].startswith('T'):
        return track['nid']
    elif track.has_key('storeId') and track['storeId'].startswith('T'):
        return track['storeId']
    else:
        raise Exception('Not a valid AllAccess track.')

def login(arg_email, arg_password):
    api = gmusicapi.Mobileclient()
    while True:
        email = arg_email if arg_email else raw_input('Email: ')
        password = arg_password if arg_password else getpass.getpass('Password: ')
        if api.login(email, password):
            return api
        else:
            print 'Invalid email/password combination.'
            if arg_email and arg_password:
                exit()