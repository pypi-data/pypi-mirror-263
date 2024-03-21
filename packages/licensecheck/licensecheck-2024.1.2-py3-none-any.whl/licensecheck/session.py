import requests_cache
import appdirs

session = requests_cache.CachedSession(appdirs.user_cache_dir("licensecheck","fredhappyface"))
