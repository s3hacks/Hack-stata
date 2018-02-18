import httplib
from bs4 import BeautifulSoup
import json,io
#fil=open("file.html",'w')
#fil.write(the_page)
#fil.close()
def findallhackathons(domain,page):
	hackathons=[]
	hackathonnames=[]
	locationcity=[]
	locationstate=[]
	c = httplib.HTTPSConnection(domain)
	c.request("GET",page)
	response = c.getresponse()
	data = response.read()
	the_page =BeautifulSoup(data,"html.parser")
	for div in the_page.find_all('h3'):
		hackathonnames.append(div.string)
	for span in the_page.find_all('span'):
		if(span.get('itemprop')=='addressLocality'):
			locationcity.append(span.string)
		if(span.get('itemprop')=='addressRegion'):
			locationstate.append(span.string)
	for i in range(len(hackathonnames)):
		dictionary={}
		dictionary['name']=hackathonnames[i]
		dictionary['city']=locationcity[i]
		dictionary['state']=locationstate[i]
		hackathons.append(dictionary)
	return hackathons
def find_eachhackathon(domain,name):
	urls=[]
	locations=[]
	dates=[]
	names=[]
	page="/hackathons?utf8=&search=%s&challenge_type=all&sort_by=Recently+Added"%('+'.join(name.split()))
	print domain,page
	c = httplib.HTTPSConnection(domain)
	c.request("GET",page)
	response = c.getresponse()
	data = response.read()
	the_page =BeautifulSoup(data,"html.parser")
	for h2 in the_page.find_all('h2'):
		try:
			if(h2.get('class')[0]=='title'):
				names.append(h2.string.strip())
		except:
			continue
	for a in the_page.find_all('a'):
		try:
			if(a.get('data-role')=='featured_challenge'):
				urls.append(a.get('href'))
		except:
			continue
	for p in the_page.find_all('p'):
		try:
			if(p.get('class')[0]=='challenge-location'):
				locations.append(p.contents[2].strip())
		except:
			continue
	for span in the_page.find_all('span'):
		try:
			if(span.get('class')[0]=='value' and span.get('class')[1]=='date-range'):
				dates.append(span.string)
		except:
			continue
	#print urls,dates,locations
	if(len(urls)==len(dates)==len(locations)==len(names)):
		return urls,dates,locations,names
	else:
		return [],[],[],[]
def find_submissions(url):
	url=url.split("/")
	domain=url[2]
	names=[]
	urls=[]
	#winners=[]
	c = httplib.HTTPSConnection(domain)
	c.request("GET","/submissions")
	response = c.getresponse()
	data = response.read()
	the_page =BeautifulSoup(data,"html.parser")
	for a in the_page.find_all('a'):
		try:
			if('link-to-software' in a.get('class')):
				urls.append(a.get('href'))
		except:
			continue
	for h5 in the_page.find_all('h5'):
		try:
			div=h5.find_parent('div')
			if("software-entry-name" in div.get('class')):
				#print div.string
				names.append(h5.string.strip())
		except:
			continue
	data=dict()
	data['names']=names
	#data['winners']=winners
	data['urls']=urls
	data['projectdata']=[]
	for url in urls:
		data['projectdata'].append(find_users_techologies(url))
	return data
def find_users_techologies(link):
	#print link
	ur=link.split("/")
	domain=ur[2]
	page="/"+"/".join(ur[3:])
	#print domain,page
	users=[]
	userlinks=[]
	technologies=[]
	locations=[]
	c = httplib.HTTPSConnection(domain)
	c.request("GET",page)
	response = c.getresponse()
	data = response.read()
	the_page =BeautifulSoup(data,"html.parser")
	for a in the_page.find_all('a'):
		#print a.get('class')
		try:
			if(a.get('class')[0]=="user-profile-link"):
				if(a.string!=None):
					userlinks.append(a.get('href'))
					users.append(a.string)
		except:
			continue
	for a in the_page.find_all('a'):
		span=a.find_parent('span')
		try:
			#print span.get('class')
			if((span.get('class')[0]=='cp-tag') and (span.get('class')[1]=='recognized-tag')):
				technologies.append(a.string)
		except:
			continue
	for url in userlinks:
		#print url
		locations.append(find_location(url))
	a={'users':users,'links':userlinks,'technologies':technologies,'locations':locations,'winner':find_winner(link)}
	#print a
	return a
def find_winner(url):
	url=url.split("/")
	domain=url[2]
	page="/"+"/".join(url[3:])
	#print domain,page
	c = httplib.HTTPSConnection(domain)
	c.request("GET",page)
	response = c.getresponse()
	data = response.read()
	the_page =BeautifulSoup(data,"html.parser")
	for span in the_page.find_all('span'):
		#print span.get('class')
		#print span.get('class')
		try:
			if((span.get('class')[0]=='winner') and (span.get('class')[1]=='label')):
				return True
				#return li.string
		except:
			continue
	return False
def find_location(url):
	url=url.split("/")
	domain=url[2]
	page="/"+"/".join(url[3:])
	#print domain,page
	c = httplib.HTTPSConnection(domain)
	c.request("GET",page)
	response = c.getresponse()
	data = response.read()
	the_page =BeautifulSoup(data,"html.parser")
	for span in the_page.find_all('span'):
		#print span.get('class')
		try:
			if((span.get('class')[0]=='ss-icon') and (span.get('class')[1]=='ss-location')):
				li=span.find_parent('li')
				#print li
				#li=li.split('<')[-2].split('>')
				return li.contents[2].strip()
				#return li.string
		except:
			continue
def foreachhackathon(hackathons):
	total=[]
	for i in range(5):
		print i
		print hackathons[i]
		urls,dates,locations,names=find_eachhackathon('devpost.com',hackathons[i]['name'])
		print urls
		print dates
		print locations
		print names
		print len(urls),len(dates),len(locations),len(names)
		print "------------------------------------------"
		print hackathons[i]['name']
        for j in range(len(urls)):
            a=dict()
            a['name']=names[j]
            a['date']=dates[j]
            a['location']=locations[j]
            a['data']=find_submissions(urls[j])
            print ("-----------------------------")
            print (a)
            with open('file.json', 'w') as f:
                f.write(json.dumps(a))
                f.write('\n')


hackathons= findallhackathons('mlh.io','/seasons/na-2018/events')
#urls,dates,locations=find_eachhackathon('devpost.com',hackathons[0]['name'])
#print urls
#print dates
#print locations

foreachhackathon(hackathons)
#print find_winner('https://devpost.com/software/cache-it-in')
#print find_users_techologies('https://devpost.com/software/cache-it-in')
#print find_submissions(urls[1])

#print names,winners
#users,userlinks,technologies,locations=find_users_techologies(newurls[0])







