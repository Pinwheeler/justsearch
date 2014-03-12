Yahoo BOSS Search Engine API Integration
========================================

Provides an easy way to access Yahoo's BOSS search API.

#####Usage
-----
```python
  from justsearch import Searcher

  #Create searcher object using Yahoo-defined API key and secret
  search = Searcher(API_KEY,API_SECRET)
  result = search.web_search("KEYWORDS")
```
+ Result will be a python dictionary object with the contents of the BOSS search
+ The search object can be re-used and no search data will be lost.
+ All searches are automatically stored in the Searcher object's "results" member variable
  + The results field is a python list



#####Other Commands
--------------
Can be used to search different Yahoo search domains

```python
search.limited_web_search("KEYWORDS")
search.news_search("KEYWORDS")
search.image_search("KEYWORDS")
search.blog_search("KEYWORDS")
```


#####Configuration
-------------
Yahoo BOSS search defines several search options that you can use to modify your search results
These can be customized to the Search object as defaults. The possible fields are as follows

more specific information can be found at http://developer.yahoo.com/boss/search/boss_api_guide/webv2_service.html

+ `Searcher.filter` 	  used to filter out violent or pornographic results
+ `Searcher.type` 		  specifies the type of documents in the results (pdf,msoffice,etc)
+ `Searcher.view` 		  identifies the language of the document
+ `Searcher.abstract` 	abstract=long will retrieve an expanded abstract for each entry
+ `Searcher.title` 		returns results with the title argument in the title
+ `Searcher.url` 	  	returns results with the url argument in the url
+ `Searcher.style` 		changes the style of the returned results (style=raw cleans out HTML)
