import os
import errno

def get_api_key():
    api_key_file = os.getenv('YELP_API_KEY_FILE')
    if api_key_file:
        with open(api_key_file, 'r') as file:
            return file.read().strip()
    else:
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), 'YELP_API_KEY_FILE')
    
