from twitter import Twitter, OAuth
t = Twitter(auth=OAuth(\
	'1036085480-ngl7ubg1UqDCNh2vIKuKML0dcn04EkaoBZYgff5',\
	'C8HuiUmqVsSWh9djv7cbenG28Yizj1B6sxBaEnTzKu76y',\
	'OkDe2m9IJKDDnnbKd7NFha6cZ',\
	'c0qJld5PPHlqSGaeWXgyKv93s1NubX29TT0xDjl7wIXhAlQ50I'))
pythonTweets = t.search.tweets(q = "#python")
print(pythonTweets)