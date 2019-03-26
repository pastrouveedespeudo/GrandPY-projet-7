"""This is use of google map api python""" 

import urllib.request 
import json
import requests
import googlemaps


def api_google_map(lieu):
    path = 'https://maps.googleapis.com/maps/api/place/textsearch/json'
    path_det = 'https://maps.googleapis.com/maps/api/place/details/json'


    key = 'AIzaSyBqJf5bBiufgiWCK34KcdmPt4Zhsp4oRCc'


    gmaps = googlemaps.Client(key=key)
    gmap_result = gmaps.geocode(lieu, region='fr')
    address = gmap_result[0]["formatted_address"]


    place_result = gmaps.places(address)

    lat = place_result["results"][0]["geometry"]["location"]["lat"]

    long = place_result["results"][0]["geometry"]["location"]["lng"]

    print(lat, long)

    return lat, long

if __name__ == "__main__":
    api_google_map(lieu)















































