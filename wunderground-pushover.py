import feedparser, httplib, urllib, re
import localconfig

# General Pushover config
PUSHOVER_URL = "api.pushover.net:443"
PUSHOVER_PATH = "/1/messages"

# Wunderground RSS items
CURRENT_CONDITION_ITEM = 0
TODAY_ITEM = 1
TONIGHT_ITEM = 2
TOMORROW_ITEM = 3



print "Parsing RSS feed..."
rss_url = localconfig.RSS_URL
feed = feedparser.parse(rss_url)

message = ""

weatherItem = feed["items"][TODAY_ITEM]
message = weatherItem['description']

message = message.replace("&deg;","")
p = re.compile(r'<.*?>')
message = p.sub('', message)

# Send message to Pushover
print "Sending message to pushover..."
conn = httplib.HTTPSConnection(PUSHOVER_URL)
conn.request("POST", PUSHOVER_PATH,
  urllib.urlencode({
    "title": "Today's Weather",
    "token": localconfig.APP_TOKEN,
    "user": localconfig.USER_TOKEN,
    "message": message,
    "url": localconfig.LINK_URL,
    "url_title": "Weather Details"
  }), { "Content-type": "application/x-www-form-urlencoded" })

# Debugging - see the response
#httpresp = conn.getresponse()
#print httpresp.status
#print httpresp.reason