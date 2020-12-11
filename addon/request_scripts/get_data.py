import subprocess
import json
import osm2geojson
import geojson
import requests
from multiprocessing import Pool


def convert_geojson_to_svg(input_folder, output_folder):
        subprocess.run(['svgis', 'draw', input_folder, '-o', output_folder])

def get_city_info(city_name, output_folder):
        query= '[out:json];area[name="'+city_name+'"];(way["highway"~"motorway|trunk|primary|motorway_link|trunk_link|primary_link"](area);>;);out body qt;'
        url = 'http://overpass-api.de/api/interpreter'  # Overpass API URL

        try:
                r = requests.get(url, params={'data': query})
                geojson_r = osm2geojson.json2geojson(r.json())
                with open(output_folder,mode="w+") as f:
                        geojson.dump(geojson_r,f)
                print('Download finished')
                print('Conversion to svg')
                convert_geojson_to_svg(output_folder, '/Users/hgmnjx/Desktop/test.svg')
                print('Conversion finished')
        except:
                print('City not Found')
                #print(r.content)
