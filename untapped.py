#!/usr/bin/env python

import json
import urllib2

CLIENTSECRET='FA66F961A03E608386961840D87050915274923C'
CLIENTID='189BD8671F3124A796C4B9C78BB8FED66DA4C4C9'

#Getting total number of distinct beers checked in 
infoURL='https://api.untappd.com/v4/user/info/degausser?&compact=true&client_id='+CLIENTID+'&client_secret='+CLIENTSECRET

result=urllib2.urlopen(infoURL).read()
data = json.loads(result)
totalNumberofBeers=int(data['response']['user']['stats']['total_beers'])
print(totalNumberofBeers)
theIndex=50


#Hard coded method to get my user info
getbeers='user/beers/degausser?&limit='+str(theIndex)+'&offset='
beersURL='https://api.untappd.com/v4/'+getbeers+str(theIndex)+'&client_id='+CLIENTID+'&client_secret='+CLIENTSECRET

#TODO loop over all beers 50 at a time
#TODO create dictionary of beer styles and ratings
#TODO average ratings and find best rated beer style

myBeers=[]

while (totalNumberofBeers!=0):
    print(totalNumberofBeers)
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
        print("fin")

    totalNumberofBeers-=theIndex

#print(data['beer_name'])

#TODO: getting an extra twenty beers in this result set not sure why
print(myBeers)
