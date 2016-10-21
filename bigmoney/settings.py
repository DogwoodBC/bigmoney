from platform import node
try:
    server = node()

    # Normally EB should skip bigmoney.settings and load bigmoney.settings_eb_staging directly,
    # but in case bigmoney.settings is getting loaded by manage.py on the EB server:
    if 'ip-172-31-30-24' in server:
        from bigmoney.settings_eb_staging import *

    else:
        from bigmoney.settings_base import *

        if 'badger' in server:
            from bigmoney.settings_badger import *
        elif 'ip-172-31-21-189' in server:
            from bigmoney.settings_endpoint import *

except:
    raise Exception("Problem in settings.py.")
