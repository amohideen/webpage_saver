
from urllib2 import Request, urlopen, URLError
import os

def download_url(url,filename,count):
	req = Request(line)
	#Start with line no 1
	try:
		response = urlopen(req)
	except URLError as e:
		if hasattr(e, 'reason'):
			print 'Line No:', count, ':',e
		elif hasattr(e, 'code'):
			print 'Line No:', count, ':',e
	else:
		print 'Line No:', count, ' Downloading'+filename
		if not os.path.exists('test_'+str(count)):
			os.makedirs('test_'+str(count))
		f = response.read()
		if filename is None:
			filename = 'index'
		output = open(os.path.join('test_'+str(count), filename), 'wb')
		output.write(f)
		output.close()
		return f


count = 0
with open("urllist.txt", "r") as f:
	for line in f:
		line = line.rstrip()
		count = count+1
		f = download_url(line,'test_'+str(count)+'.html',count)

		from BeautifulSoup import BeautifulSoup, SoupStrainer
		import re
		soup = BeautifulSoup(f)
		for script in soup.findAll(src=re.compile("\w+.js")):
			js=script.get('src')
			if js.startswith('../'):
				js_file_name = js[js.rfind('/')+1::]
				js_file_path = line[:line.rfind('/')+1:]
				download_url(js_file_path+'/'+js_file_name,js_file_name,count)


		for style in soup.findAll(href=re.compile("\w+.css")):
			if style is not None:
				css = style.get('href')
				if css.startswith('../'):
					css_file_name = css[css.rfind('/')+1::]
					css_file_path = line[:line.rfind('/')+1:]
					download_url(css_file_path+'/'+css_file_name,css_file_name,count)
				else:
					pass