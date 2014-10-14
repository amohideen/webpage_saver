This Code is supposed to take a list of urls as input and download all the webpages along with their javascripts and css and store in seperate folders also replacing the code in the html pages.

Tech Stack :
Python 2.7
urllib2
beautifulsoup

This for now works only with urls ending with .com and .org.
Also static files with absolute and ../ are not considered.
Only assets with urls like /static/css/somefile.css are considered.
Example url : https://wiki.python.org/moin/Python2orPython3