import csv
from datetime import datetime

import mysql.connector

import connectDB


# cmd: mysql --local-infile=1 -u root -p
# load data local infile 'C:\\Users\\LT\\Downloads\\CovidVaccinations.csv' into table covidvaccinations FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS;

# Kết nối đến MySQL
def creTable(tinh):
    mydb = connectDB.connect()
    now = datetime.now()
    month = now.month
    year = now.year

    with open('D:\DACS_Group02\DACS\Book2.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)  # Lấy tiêu đề cột

        # Tạo câu truy vấn SQL để tạo bảng
        create_table_query = f"CREATE TABLE IF NOT EXISTS {tinh}("
        for column in header:
            column = column.replace(" ", "_")
            create_table_query += f"`{column}` VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci default null,"
        create_table_query = create_table_query[:-1] + ")" # Loại bỏ dấu phẩy cuối cùng và thêm dấu đóng ngoặc

        # Thực thi câu truy vấn để tạo bảng
        cursor = mydb.cursor()
        cursor.execute(create_table_query)

        add_column = f"ALTER TABLE {tinh} ADD price_clean DOUBLE;"
        cursor.execute(add_column)

    # Đóng kết nối đến MySQL
    mydb.close()
