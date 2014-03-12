#Copyright 2014 Levatas
#Written by Anthony Dreessen

"""
Python integration with Yahoo's BOSS search API
you will need BOSS search API Key and API Secret which require a credit card
in order to use. get to developer.aps.yahoo.com
"""

import urllib2
import oauth2 as oauth #dependency
import time
import json

BASE_URL = "http://yboss.yahooapis.com/ysearch/"

class Searcher(object):
	"""Creates searcher object that can be reused"""
	def __init__(self, api_key, api_secret):
		super(Searcher, self).__init__()
		self.api_key = api_key
		self.api_secret = api_secret
		self.consumer = oauth.Consumer(key=self.api_key,secret=api_secret)
		self.results = []
		self.filter = None
		self.type = None
		self.view = None
		self.abstract = None
		self.title = None
		self.url = None
		self.style = None

	def oauth_request(self,url, params, method="GET"):
	    params['oauth_version'] = "1.0"
	    params['oauth_nonce'] = oauth.generate_nonce()
	    params['oauth_timestamp'] = int(time.time())
	    params['oauth_consumer_key'] = self.consumer.key
	    req = oauth.Request(method=method, url=url, parameters=params)
	    req.sign_request(oauth.SignatureMethod_HMAC_SHA1(), self.consumer, None)

	    return req
		
	def web_search(self,keywords,url_ext='web',_filter=None,_type=None,_view=None,_abstract=None,_title=None,_url=None,_style=None):
		search_url = BASE_URL+url_ext
		params = {}
		params['q'] = keywords
		if _filter != None:
			params['filter'] = _filter
		if _type != None:
			params['type'] = _type
		if _view != None:
			params['view'] = _view
		if _abstract != None:
			params['abstract'] = _abstract
		if _title != None:
			params['title'] = _title
		if _url != None:
			params['url'] = _url
		if _style != None:
			params['style'] = _style
		req = self.oauth_request(search_url,params=params)
		req['q'] = req['q'].encode('utf8')
		req_url = req.to_url().replace('+', '%20')
		print req_url
		result = urllib2.urlopen(req_url)
		bossresponse = []
		for row in result:
			bossresponse.append(row)
		result = json.loads(bossresponse[0])
		self.results.append(result)
		return result

	def limited_web_search(self,keywords):
		return self.web_search(keywords,url_ext='limitedweb',_filter=self.filter,_type=self.type,_view=self.view,_title=self.title,_url=self.url,_style=self.style)
	def image_search(self,keywords):
		return self.web_search(keywords,url_ext='images',_filter=self.filter,_type=self.type,_view=self.view,_title=self.title,_url=self.url,_style=self.style)
	def news_search(self,keywords):
		return self.web_search(keywords,url_ext='news',_filter=self.filter,_type=self.type,_view=self.view,_title=self.title,_url=self.url,_style=self.style)
	def blog_search(self,keywords):
		return self.web_search(keywords,url_ext='blogs',_filter=self.filter,_type=self.type,_view=self.view,_title=self.title,_url=self.url,_style=self.style)
