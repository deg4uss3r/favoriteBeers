#!/usr/bin/env python

#imports
import json
import urllib2
import os

user = raw_input("What's you untapped user name? ")

#getting client secret key:
clientSecretFile = open(os.path.expanduser('~/Dropbox/private/untapped-private-api'), 'r') #have to use os.path.expanduser because of ~
CLIENTSECRET=clientSecretFile.read()
CLIENTID='189BD8671F3124A796C4B9C78BB8FED66DA4C4C9'

#Getting total number of distinct beers checked in 
infoURL='https://api.untappd.com/v4/user/info/' + user + '?&compact=true&client_id='+CLIENTID+'&client_secret='+CLIENTSECRET

result=urllib2.urlopen(infoURL).read()
data = json.loads(result)
totalNumberofBeers=int(data['response']['user']['stats']['total_beers'])
theIndex=50

getbeers='user/beers/' + user + '?&limit='+str(theIndex)+'&offset='
beersURL='https://api.untappd.com/v4/'+getbeers+str(theIndex)+'&client_id='+CLIENTID+'&client_secret='+CLIENTSECRET

#TODO loop over all beers 50 at a time (free API limitation)

#TODO create dictionary of beer styles and ratings
#TODO average ratings and find best rated beer style

myBeers=[]

while (totalNumberofBeers!=0):
    beersURL='https://api.untappd.com/v4/'+getbeers+str(theIndex)+'&client_id='+CLIENTID+'&client_secret='+CLIENTSECRET
    result=urllib2.urlopen(beersURL).read()
    data=json.loads(result)

    x=int(data['response']['beers']['count'])
    x-=1
    while (x >=0):
        beerName=data['response']['beers']['items'][x]['beer']['beer_name']
        myBeers.append(beerName)
        x-=1
    #beerStyle=data['response']['beers']['items'][x]['beer']['beer_style']
    #rating=float(data['response']['beers']['items'][x]['rating_score'])
    #print("%s - %s - %f"%(beerName, beerStyle, rating))

    if(totalNumberofBeers >50):
        theIndex=50
    elif (totalNumberofBeers<50 and totalNumberofBeers >0):
        theIndex=totalNumberofBeers
    else:
        print("fin") #never gets here BUG

    totalNumberofBeers-=theIndex

#print(data['beer_name'])

#TODO: getting an extra twenty beers in this result set not sure why
print(len(myBeers))
