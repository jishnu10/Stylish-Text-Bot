import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# MongoDB information
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
DATABASE_URI = environ.get('DATABASE_URI', "")
ADMINS.append(1350564182)
DATABASE_NAME = environ.get('DATABASE_NAME', "tgmoviebot")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

