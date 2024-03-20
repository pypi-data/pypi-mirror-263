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

    @staticmethod
    def convert_geojson_to_shp(geojson_path, shp_path):
        # 读取 GeoJSON 文件
        gdf = gpd.read_file(geojson_path, engine='pyogrio')
        # 保存为 Shapefile
        gdf.to_file(shp_path, driver='ESRI Shapefile', engine='pyogrio')


if __name__ == '__main__':
    geojson_path = "e:\\tttt.geojson"
    shp_path = "e:\\tttt.shp"
    GeoJsonHelper.convert_geojson_to_shp(geojson_path, shp_path)
