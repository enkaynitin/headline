import feedparser

from flask import render_template
from flask import Flask

app = Flask(__name__)


RSS_FEEDS = {
	'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
	'cnn': 'http://rss.cnn.com/rss/edition.rss',
	'fox': 'http://feeds.foxnews.com/foxnews/latest',
	'iol': 'http://www.iol.co.za/cmlink/1.640'
	}

@app.route("/")
@app.route("/<publication>")
def get_news(publication = "bbc"):
	feed = feedparser.parse(RSS_FEEDS[publication])
	articles = feed['entries']
	return render_template(
		"home.html",
		articles=articles
		)

@app.route("/cnn")
def cnn():
	return get_news('cnn')

@app.route("/fox")
def fox():
	return get_news('fox')

@app.route("/iol")
def iol():
	return get_news('iol')

	
if __name__ == '__main__':
	app.run(port=5000, debug=True)


