#get the stuff we need--i.e. import the external libraries we need
import nltk
from bs4 import BeautifulSoup
from urllib import request

#stored the url we're using
url = 'https://github.com/humanitiesprogramming/scraping-corpus'

#using the URL we just defined and the following chain of methods, pull all the html at the url we defined
html = request.urlopen(url).read()

#took URL and turned it into a soup object
soup = BeautifulSoup(html, 'lxml')

#this spits back all the text from the url you've saved (print(soup.text)). It's been translated to a variable for later use.
our_text = soup.text

#this defines the variable links as all the links from the soup object according to the parameters here
links = soup.find_all('a')[0:10]

#print(links)

#look in our text and return everything from the first thru 2000 character
#print(our_text[0:2000])

#this should remove all the line breaks with nothing
#print(soup.text.replace('\n', ' '))

links_html = soup.select('td.content a')
this_link = links_html[0]

#at this point we are able tp print only the link text we're interested in
#print(this_link['href'])

urls = []

#when stopping at the first print, it just lists out each of the urls we're interested in
for link in links_html:
    #we need to remove "blob/" from each url in the list, we then turned that into a variable called to_append
    to_append = link['href'].replace('blob/', '')
    #this adds the preceding text plus the link without /blob to the urls list
    urls.append('https://raw.githubusercontent.com' + to_append)

#print(urls)


test_urls = urls[3]
corpus_texts = []

#this is printing out the text from each url in the list
for url in urls:
    html = request.urlopen(url).read()
    soup = BeautifulSoup(html, 'lxml')
    text = soup.text.replace('\n', '')
    corpus_texts.append(text)
    #print('scraping' + url)

    #print(len(corpus_texts))
    #print(len(corpus_texts[0]))

#this breaks the giant string into word units, then analyzes it by word frequency for the 50 most common words
this_text = corpus_texts[0]
process_this_text = nltk.word_tokenize(this_text)
print(process_this_text[0:20])
print(nltk.FreqDist(process_this_text).most_common(50))
