from instaloader import Instaloader
# import os

def getIgConnection():
    L = Instaloader()
    # igUsername = os.getenv('IG_USERNAME')
    # L.load_session_from_file(igUsername,f'session-{igUsername}')
    return L.context