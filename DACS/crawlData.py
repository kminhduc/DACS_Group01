from datetime import datetime
import mysql
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

import upData


current_datetime = datetime.now()
day = current_datetime.day
month = current_datetime.month
year = current_datetime.year

options = Options()
options.add_argument('--headless')

def createDriver():
    return webdriver.Chrome(ChromeDriverManager().install())

def crawlUpData(driver, tinh, indexTinh, theLoaiNha, trangs):
    for trang in range(trangs):

        driver.get(f"https://alonhadat.com.vn/nha-dat/can-ban/{theLoaiNha}/{indexTinh}/{tinh}/trang--{trang+3}.html")
        
        items = driver.find_elements(By.CLASS_NAME, 'content-item')

        for item in items:
            itemList = []
            if theLoaiNha == 'nha-mat-tien':
                type = 1.1
            elif theLoaiNha == 'nha-trong-hem':
                type = 1.2
            elif theLoaiNha == 'mat-bang':
                type = 2
            elif theLoaiNha == 'can-ho-chung-cu':
                type = 3
            else:
                type = 4
            itemList.append(type)

            name = item.find_element(By.CLASS_NAME, 'ct_title').text

            try:
                des = item.find_element(By.CLASS_NAME, 'ct_brief').text
            except:
                des = "_"

            try:
                roadWidth = item.find_element(By.CLASS_NAME, 'road-width').text
            except:
                roadWidth = "_"

            try:
                floors = item.find_element(By.CLASS_NAME, 'floors').text
            except:
                floors = "_"

            try:
                bedroom = item.find_element(By.CLASS_NAME, 'bedroom').text
            except:
                bedroom = "_"

            try:
                check = item.find_element(By.CLASS_NAME, 'parking')
                parking = "Có chỗ để xe"
            except:
                parking = "_"

            try:
                dtItem = item.find_element(By.CLASS_NAME, 'ct_dt')
                text = dtItem.text
                label = dtItem.find_element(By.TAG_NAME, 'label').text
                dt = text.replace(label, '').strip()
            except:
                dt = "_"

            try:
                ktItem = item.find_element(By.CLASS_NAME, 'ct_kt')
                text = ktItem.text
                label = ktItem.find_element(By.TAG_NAME, 'label').text
                kt = text.replace(label, '').strip()
            except:
                kt = "_"

            try:
                directItem = item.find_element(By.CLASS_NAME, 'ct_direct')
                text = directItem.text
                label = directItem.find_element(By.TAG_NAME, 'label').text
                direct = text.replace(label, '').strip()
            except:
                direct = ""

            try:
                priceItem = item.find_element(By.CLASS_NAME, 'price-dis')
                text = priceItem.text
                label = priceItem.find_element(By.TAG_NAME, 'label').text
                price = text.replace(label, '').strip()

                index1 = price.find("tỷ")
                index2 = price.find("triệu / m2")
                index = max(index2, index1)
                if index != -1:
                    price = price[:index + 2]
            except:
                price = "_"

            locates = item.find_elements(By.CSS_SELECTOR, '.ct_dis a')
            check = 0
            for i in locates:
                if len(locates) < 3 and kt == 0:
                    for j in range(3 - len(locates)):
                        itemList.append("_")
                    check += 1
                try:
                    itemList.append(i.text)
                except:
                    itemList.append("_")

            try:
                href = item.find_element(By.CSS_SELECTOR, '.ct_brief a').get_attribute('href')
                print(f"link --- {href}")
            except:
                href = "_"

            itemList.append(name)
            itemList.append(des)
            itemList.append(roadWidth)
            itemList.append(floors)
            itemList.append(bedroom)
            itemList.append(parking)
            itemList.append(dt)
            itemList.append(kt)
            itemList.append(direct)
            itemList.append(price)
            itemList.append(href)
            itemList.append(day)
            itemList.append(month)
            itemList.append(year)

            print(len(itemList))
            try:
                upData.upData(tinh, itemList)
            except mysql.connector.Error as err:
                print(f"Lỗi 1: {err}")
                continue

