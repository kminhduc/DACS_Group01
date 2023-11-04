import math
import threading

import crawlData
import taoTable
import upData

theLoaiNha = ['nha-mat-tien', 'nha-trong-hem', 'mat-bang', 'can-ho-chung-cu', 'dat-tho-cu-dat-o']

trangs = 5
tinh = "hanoi"
def main():
    # taoTable.creTable(tinh)
    driver = crawlData.createDriver()
    for i in theLoaiNha:
        crawlData.crawlUpData(driver, tinh, i, trangs)
    upData.upDataToCSV('hanoi')


if __name__ == "__main__":
    main()