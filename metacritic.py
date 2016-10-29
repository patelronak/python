def dict_to_json(content):
	import json
	return json.dumps(content)

def games(name=None):

	from bs4 import BeautifulSoup
	import urllib2

	url              = "http://www.metacritic.com/game/playstation-3"
	list_class       = "list_products"
	list_element     = "ol"
	product_class    = "product"
	product_element  = "li"
	title_class      = "product_title"
	title_element    = "div"
	metascore_class  = "metascore_w"
	metascore_element= "span"
	ad_class         = "ad_unit"
	
	output           = {}

	hdr = {
		'Connection': 'close',
		'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X; de-de) AppleWebKit/523.10.3 (KHTML, like Gecko) Version/3.0.4 Safari/523.10',
		'Accept-Charset': 'ISO-8859-1,UTF-8;q=0.7,*;q=0.7',
		'Cache-Control': 'no-cache',
		'Accept-Language': 'de,en;q=0.7,en-us;q=0.3'
	}

	req      = urllib2.Request(url,headers=hdr)
	response = urllib2.urlopen(req)
	htmlout  = response.read()
	content  = BeautifulSoup(htmlout, "html.parser")
	
	if name:
		title = content.find(title_element, text=name)
		score = (title.parent).find(metascore_element, class_=metascore_class)
		output[(title.text).strip()] = (score.text).strip()
	else:
		gamelist = content.find(list_element, class_=list_class)
		games    = gamelist.find_all(product_element, class_=product_class)
		for game in games:
			if ad_class not in game.attrs['class']:
				title = game.find(title_element, class_=title_class)
				score = game.find(metascore_element, class_=metascore_class)
				output[(title.text).strip()] = (score.text).strip()

	return dict_to_json(output)	