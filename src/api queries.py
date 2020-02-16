import dotenv
import json
import os
import requests
from dotenv import load_dotenv
load_dotenv()

def asGeoJSON(lat,lng):
    try:
        lat = float(lat)
        lng = float(lng)
        if not math.isnan(lat) and not math.isnan(lng):
            return {
                "type":"Point",
                "coordinates":[lng,lat]
            }
    except Exception:
        print("Invalid data")
        return None


def fourSquareStarbucksLat (lat, long):

CLIENT_ID = os.getenv("CLIENT_ID")
token = os.getenv("CLIENT_SECRET")
    
    url = 'https://api.foursquare.com/v2/venues/explore'

    params = dict(
      client_id=CLIENT_ID,
      client_secret=token,
      v='20200210',
      ll=lat+ "," + long,
      query="Starbucks",
      limit=1
    )
    
    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)

    latitud = data['response']['groups'][0]['items'][0]['venue']['location']['lat']

    return latitud

cleanData['StarbucksLat']=cleanData.apply(lambda x: fourSquareStarbucksLat(str(x.latitude), str(x.longitude)), axis=1)
cleanData.head()

def fourSquareStarbucksLong (lat, long):
    
    url = 'https://api.foursquare.com/v2/venues/explore'

    params = dict(
      client_id=CLIENT_ID,
      client_secret=token,
      v='20200210',
      ll=lat+ "," + long,
      query="Starbucks",
      limit=1
    )

    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)

    longitude = data['response']['groups'][0]['items'][0]['venue']['location']['lng']

    return longitude

cleanData['StarbucksLong']=cleanData.apply(lambda x: fourSquareStarbucksLong(str(x.latitude), str(x.longitude)), axis=1)
cleanData.head()

def fourSquareStarbucks (lat, long):
    
    url = 'https://api.foursquare.com/v2/venues/explore'

    params = dict(
      client_id=CLIENT_ID,
      client_secret=token,
      v='20200210',
      ll=lat+ "," + long,
      query="Starbucks",
      limit=1
    )

    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)
   
    latitud = data['response']['groups'][0]['items'][0]['venue']['location']['lat']
    longitude = data['response']['groups'][0]['items'][0]['venue']['location']['lng']

    return {
        "type":"Point",
        "coordinates":[float(latitud),float(longitude)]}


cleanData['Starbucks']=cleanData.apply(lambda x: fourSquareStarbucks(str(x.latitude), str(x.longitude)), axis=1)
cleanData.head()

cleanData = cleanData.rename(columns={"latitude":"lat_comp", "longitude":"long_comp"})
cleanData.head()