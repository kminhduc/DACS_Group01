import csv
from datetime import datetime
import pandas as pd
import mysql.connector
from sqlalchemy import create_engine, text

import connectDB

# Danh sách dữ liệu cần chèn
english_names = [
    'type', 'Street', 'Ward', 'District', 'Name', 'Description',
    'Road_Surface_Area', 'Floor', 'Bedrooms', 'Parking',
    'Area', 'Size', 'Direction', 'Price', 'Link', 'Day', 'Month', 'Year'
]
current_datetime = datetime.now()
day = current_datetime.day
month = current_datetime.month
year = current_datetime.year
def upData(tinh, itemList):

    connection = connectDB.connect()

    cursor = connection.cursor()

    insert_query = f"INSERT INTO {tinh}({', '.join(['`' + name + '`' for name in english_names])}) " \
                   "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    cursor.execute(insert_query, itemList)

    # Lưu các thay đổi vào cơ sở dữ liệu
    connection.commit()

    # Đóng kết nối và cursor khi hoàn thành
    cursor.close()
    connection.close()

def upDataToCSV(tinh):
    connection = connectDB.connect()
    cursor = connection.cursor()
    query = f"SELECT " \
            f"CASE WHEN `Type` = 1.1 THEN 'Nhà mặt đường' " \
            f"     WHEN `Type` = 1.2 THEN 'Nhà trong hẻm' " \
            f"     WHEN `Type` = 2 THEN 'Mặt bằng' " \
            f"     WHEN `Type` = 3 THEN 'Căn hộ chung cư'" \
            f"     ELSE 'Đất thổ cư, đất ở' " \
            f"END as `Type`, CONCAT(Street, ', ', Ward, ', ', District) AS Location, " \
            f"name, Price, Road_Surface_Area, Floor, Bedrooms, Parking, Area, Size, Direction, Link " \
            f"FROM {tinh};"
    cursor.execute(query)
    result = cursor.fetchall()
    column_names = [i[0] for i in cursor.description]
    csv_file = "UIMaindata.csv"
    df = pd.DataFrame(result, columns=column_names)

    df.to_csv(csv_file, sep='\t', encoding='utf-16', index=False)
    print(f"Dữ liệu đã được lưu vào tệp {csv_file}")

def upDataToCSV2(Type, Street, Ward, District, Floor, Bedrooms, Parking, Area, Price):
    connection = connectDB.connect()
    cursor = connection.cursor()
    query = f"SELECT " \
            f"CASE WHEN `Type` = 1.1 THEN 'Nhà mặt đường' " \
            f"     WHEN `Type` = 1.2 THEN 'Nhà trong hẻm' " \
            f"     WHEN `Type` = 2 THEN 'Mặt bằng' " \
            f"     WHEN `Type` = 3 THEN 'Căn hộ chung cư'" \
            f"     ELSE 'Đất thổ cư, đất ở' " \
            f"END as `Type`, CONCAT(Street, ', ', Ward, ', ', District) AS Location, " \
            f"name, Price, Road_Surface_Area, Floor, Bedrooms, Parking, Area, Size, Direction, Link " \
            f"FROM {District};" \
            f"WHERE Ward = {Ward} and Street = {Street} and Floor = {Floor} and Bedrooms = {Bedrooms}"
    cursor.execute(query)
    result = cursor.fetchall()
    column_names = [i[0] for i in cursor.description]
    csv_file = "UIMaindata.csv"
    df = pd.DataFrame(result, columns=column_names)

    df.to_csv(csv_file, sep='\t', encoding='utf-16', index=False)
    print(f"Dữ liệu đã được lưu vào tệp {csv_file}")


