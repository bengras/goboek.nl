import locale
locale.setlocale(locale.LC_TIME, 'en_US.UTF-8')  # Set to English locale

DEFAULT_LANG = 'en'
AUTHOR = 'Ben Gras'
OUTPUT_PATH = '/var/www/www.shrike-systems.com'
PATH = 'content'
THEME = "/home/beng/pelican-themes/mediumfox"
SITEURL = 'https://www.shrike-systems.com/'
SITENAME = 'Shrike Systems'
TIMEZONE = 'CET'
DELETE_OUTPUT_DIRECTORY = True
FEED_ATOM = 'atom.xml'
FEED_RSS = 'rss.xml'
TWITTER_USERNAME = 'bjg'
STATIC_PATHS = [ 'images' , 'files' ]
