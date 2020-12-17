import csv

import selenium
from selenium import webdriver
import time
import json

executable_path1 = 'chromedriver.exe'
driver = webdriver.Chrome(executable_path=executable_path1)     # 创建Chrome对象.
with open('scrapy--master/test100/test100/spiders/shushan.csv','r') as csvfile:
    reader = csv.DictReader(csvfile)
    column = [row['project_name'] for row in reader]
flag = 0
for i in column:
    # 操作这个对象.
    t ='https://github.com'+i
    driver.get(t)     # get方式访问
    print(t)
    time.sleep(1)
    if flag ==0:
        #sign in
        el = driver.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/div[2]/a[1]")
        el.click()
        time.sleep(3)
        el = driver.find_element_by_xpath("/html/body/div[3]/main/div/form/div[4]/input[1]")
        el.send_keys("sdufrancis@163.com")
        time.sleep(3)
        el = driver.find_element_by_xpath("/html/body/div[3]/main/div/form/div[4]/input[2]")
        el.send_keys("Lsq19980215!")
        time.sleep(3)
        el = driver.find_element_by_xpath("//*[@id=\"login\"]/form/div[4]/input[12]")
        el.click()
        time.sleep(3)
    flag = 1

    el = driver.find_element_by_xpath("/html/body/div[4]/div/main/div[2]/div[1]/ul/li[1]/notifications-list-subscription-form/details/summary")
    el.click()
    time.sleep(3)
    el = driver.find_element_by_xpath("/html/body/div[4]/div/main/div[2]/div[1]/ul/li[1]/notifications-list-subscription-form/details/details-menu/div/div/button")
    el.click()
    time.sleep(3)
    el = driver.find_element_by_xpath("/html/body/div[4]/div/main/div[2]/div[1]/ul/li[1]/notifications-list-subscription-form/details/details-dialog/div/form/fieldset/div[3]/label/input")
    el.click()
    time.sleep(3)
    try:
        el = driver.find_element_by_xpath("/html/body/div[4]/div/main/div[2]/div[1]/ul/li[1]/notifications-list-subscription-form/details/details-dialog/div/form/div/button[1]")
    except selenium.common.exceptions.NoSuchElementException:
        print("did")
    else:
        el.click()

    time.sleep(3)
    print("finished")
driver.quit()   # 使用完, 记得关闭浏览器, 不然chromedriver.exe进程为一直在内存中.