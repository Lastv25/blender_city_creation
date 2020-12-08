import overpy as op
from multiprocessing import Pool


def get_city_info(city_name):
    print(city_name)
    api = op.Overpass()
    r = api.query("""<osm-script output="xml">
                  <id-query {{nominatimArea:"""+city_name+"""}} into="area"/>
                  <query type="way">
                      <has-kv k="highway" regv="motorway|trunk|primary|motorway_link|trunk_link|primary_link"/>
                      <area-query from="area"/>
                  </query>
                  <union>
                    <item />
                      <recurse type="way-node"/>   
                  </union>
                  <print mode="body" order="quadtile"/>
                </osm-script>
                    """)
    print(len(r.nodes))

    coords  = []
    coords += [(float(node.lon), float(node.lat)) 
            for node in r.nodes]
    coords += [(float(way.center_lon), float(way.center_lat)) 
            for way in r.ways]
    coords += [(float(rel.center_lon), float(rel.center_lat)) 
            for rel in r.relations]

    print(coords)
