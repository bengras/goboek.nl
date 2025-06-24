import locale
locale.setlocale(locale.LC_TIME, 'en_US.UTF-8')  # Set to English locale

DEFAULT_LANG = 'nl'
AUTHOR = 'René Kuiper'
OUTPUT_PATH = 'docs/'
PATH = 'content'
THEME = "pelican-themes/mediumfox"
THEME = 'bootstrap2'
SITEURL = 'https://www.goboek.nl'
SITENAME = 'Gezond Ouder Worden'
TIMEZONE = 'CET'
DELETE_OUTPUT_DIRECTORY = True
FEED_ATOM = 'atom.xml'
FEED_RSS = 'rss.xml'
STATIC_PATHS = [ 'images' , 'files' ]
LOCALE = ('nl_NL.UTF-8',)  # Use Dutch locale
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = [('Home', '/'), ('Over deze site', '/pages/over-deze-site.html')]
