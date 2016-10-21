from platform import node

from bigmoney.settings_base import *

print('Loading settings.')

try:
    server = node()

    if 'badger' in server:
        from bigmoney.settings_badger import *
    elif 'ip-172-31-21-189' in server:
        from bigmoney.settings_endpoint import *
    # Otherwise assume (for now) that this is the staging Elastic Beanstalk environment.
    else:
        from bigmoney.settings_template import *

except:
    raise Exception("Problem in settings.py.")
