import geopandas as gpd
from shapely.geometry import Point
import numpy as np

def generate_geojson():
    data = []
    for i in range(100):
        lat = 28.0 + np.random.rand() * 0.5
        lon = -82.0 + np.random.rand() * 0.5

        data.append({
            "rainfall": np.random.randint(0, 100),
            "traffic": np.random.randint(0, 100),
            "distance_to_road": np.random.rand() * 10,
            "geometry": Point(lon, lat)
        })

    gdf = gpd.GeoDataFrame(data, crs="EPSG:4326")
    gdf.to_file("data/geo_data.geojson", driver="GeoJSON")

if __name__ == "__main__":
    generate_geojson()
    print("GeoJSON generated")
