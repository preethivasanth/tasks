import urllib2

seed=raw_input('Enter a url : ')

def getAllNewLinksOnPage(page,prevLinks):

response = urllib2.urlopen(page)
html = response.read()

links,pos,allFound=[],0,False
while not allFound:
    aTag=html.find("<a href=",pos)
    if aTag>-1:
        href=html.find('"',aTag+1)
        endHref=html.find('"',href+1)
        url=html[href+1:endHref]
        if url[:7]=="http://":
            if url[-1]=="/":
                url=url[:-1]
            if not url in links and not url in prevLinks:
                links.append(url)     
                print url
        closeTag=html.find("</a>",aTag)
        pos=closeTag+1
    else:
        allFound=True   
return links

toCrawl=[seed]
crawled=[]
while toCrawl:
url=toCrawl.pop()
crawled.append(url)
newLinks=getAllNewLinksOnPage(url,crawled)
toCrawl=list(set(toCrawl)|set(newLinks))

print crawled   
