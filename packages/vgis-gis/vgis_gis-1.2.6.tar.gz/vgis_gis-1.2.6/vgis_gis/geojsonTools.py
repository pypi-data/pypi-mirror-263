"""
===================================
#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
@Author: chenxw
@Email : gisfanmachel@gmail.com
@File: shpTools.py
@Date: Create in 2021/1/22 13:43
@Description: 对geojson文件的操作类
@ Software: PyCharm

===================================
"""

import json
import os

import geopandas as gpd


class GeoJsonHelper:

    def __init__(self):
        pass

    @staticmethod
    # 合并 geojson
    def merge_geojsons(geojson_files_path, merge_result_file):
        index = 0
        all_data = {}
        for file_name in os.listdir(geojson_files_path):
            geojson_file = os.path.join(geojson_files_path, file_name)
            with open(geojson_file, 'r', encoding='utf-8') as fp:
                each_data = json.load(fp)
            if index == 0:
                all_data = each_data
            else:
                all_data["features"] += each_data["features"]
        result_file = open(merge_result_file, "w")
        json.dump(all_data, result_file)

    # 将geojson转换为shp
    @staticmethod
    def convert_geojson_to_shp(geojson_path, shp_path):
        # 读取 GeoJSON 文件
        gdf = gpd.read_file(geojson_path, engine='pyogrio')
        # 保存为 Shapefile
        gdf.to_file(shp_path, driver='ESRI Shapefile', engine='pyogrio')

    # geojson里增加epsg
    @staticmethod
    def add_epsg_value_in_geojson(geojson_path, espg_value):
        data = json.load(open(geojson_path, encoding="utf-8"))
        if "crs" not in data:
            data['crs'] = {"type": "name", "properties": {"name": "urn:ogc:def:crs:EPSG::{}".format(espg_value)}}
        with open(geojson_path, 'w') as fp:
            json.dump(data, fp)

    @staticmethod
    def get_geojson_geometry_info(geojson_path):
        epsg_value, geometry_type = None, None
        data = json.load(open(geojson_path, encoding="utf-8"))
        if "crs" in data:
            epsg_info = data["crs"]["properties"]["name"]
            if "urn:ogc:def:crs:EPSG" in epsg_info:
                epsg_value = epsg_info.split("::")[1]
        if "features" in data:
            features = data["features"]
            if len(features) > 0:
                geometry_type = features[0]["geometry"]["type"]
        return epsg_value, geometry_type


if __name__ == '__main__':
    geojson_path = "e:\\tttt.geojson"
    shp_path = "e:\\tttt.shp"
    # GeoJsonHelper.convert_geojson_to_shp(geojson_path, shp_path)
    print(GeoJsonHelper.get_geojson_geometry_info(geojson_path))
