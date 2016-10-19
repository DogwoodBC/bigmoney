from platform import node

from bigmoney.settings_base import *

server = node()

if 'badger' in server:
    from bigmoney.settings_badger import *
# This may be unnecessary since it's also specified in .ebextensions/02_python.config:
elif 'ip-172-31-9-116' in server:
    from bigmoney.settings_staging import *
elif 'ip-172-31-21-189' in server:
    from bigmoney.settings_endpoint import *
else:
    raise Exception("Problem in settings.py.")
