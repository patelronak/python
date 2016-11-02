
# games: 
# input: optional - Name of the game
# input: optional - url to scrape
# this function will get title and metascore for games
# if name is provided it will get metascore about the game
def games(name=None, url=None):

	from bs4 import BeautifulSoup
	import urllib2

	# default url
	if not url:
		url          = "http://www.metacritic.com/game/playstation-3"

	# elements and classes defined in the page for product list and products and ads if applicable.
	list_class       = "list_products"
	list_element     = "ol"
	product_class    = "product"
	product_element  = "li"
	ad_class         = "ad_unit"
	
	# empty array
	output_list      = []

	# header to pass to the request.
	hdr = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X; de-de) AppleWebKit/523.10.3 (KHTML, like Gecko) Version/3.0.4 Safari/523.10',
	}

	# get the content from the site
	req      = urllib2.Request(url,headers=hdr)
	response = urllib2.urlopen(req)
	htmlout  = response.read()
	content  = BeautifulSoup(htmlout, "html.parser")

	# more error checking is required here to see if we are getting valid
	# output from scraping the site and respond appropriately.
	if name:		
		output_list.append(get_product_title_score(content,name))
	else:
		gamelist = content.find(list_element, class_=list_class)
		if gamelist:
			games = gamelist.find_all(product_element, class_=product_class)
			for game in games:
				if ad_class not in game.attrs['class']:
					output_list.append(get_product_title_score(game))
	return  output_list
	
def get_product_title_score(content,name=None):
	
	import collections
	
	title_class      = "product_title"
	title_element    = "div"
	metascore_class  = "metascore_w"
	metascore_element= "span"
	
	output = collections.OrderedDict()
	score_text = -1
	error_message = None
	
	if name:
		title = content.find(title_element, text=name)
	else:
		title = content.find(title_element, class_=title_class)
	
	if title:
		title_text = (title.text).strip()
		score = (title.parent).find(metascore_element, class_=metascore_class)
		if score:
			score_text = int((score.text).strip())
	else:
		if name:
			error_message = name + " - title not found"
		else:
			error_message = "Undefined title"

	if error_message:
		output['error'] = error_message
	else:
		output['title'] = title_text
		output['score'] = score_text

	return output