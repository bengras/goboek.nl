AUTHOR = 'Ben Gras'
OUTPUT_PATH = '/usr/local/www/data/vhosts/www.shrike-systems.com'
PATH = 'content'
SITEURL = 'http://www.shrike-systems.com'
SITENAME = 'Shrike Systems'
TIMEZONE = 'CET'
THEME = '../pelican-themes/zurb-F5-basic'
GOOGLE_ANALYTICS = 'UA-50092958-1'
DELETE_OUTPUT_DIRECTORY = True
FEED_ATOM = 'atom.xml'
FEED_RSS = 'rss.xml'
TWITTER_USERNAME = 'bjg'
FLATTR_USER = 'ben.gras'
STATIC_PATHS = [ 'images' , 'files' ]

PLUGINS = [
    'pelican_youtube',
]

