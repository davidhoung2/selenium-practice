import time
import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import random
from skimage import io

a = random.randint(2, 3)
type = input("1. 可見光\n"
             "2. 彩色\n"
             "3. 色調強化\n"
             "4. 黑白\n"
             "5. 真實色\n"
             "type of image: ")

area = input("\n1. 全景\n"
             "2. 東亞\n"
             "3. 台灣\n"
             "area size: ")

t = input("\ntime: ")
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.cwb.gov.tw/V8/C/W/OBS_Sat.html")
if type == '1':
    driver.find_element(By.LINK_TEXT, "可見光").click()
elif type == '2':
    driver.find_element(By.LINK_TEXT, "彩色").click()
elif type == '3':
    driver.find_element(By.LINK_TEXT, "色調強化").click()
elif type == '4':
    driver.find_element(By.LINK_TEXT, "黑白").click()
elif type == '5':
    driver.find_element(By.LINK_TEXT, "真實色").click()
time.sleep(a)

if area == '1':
    driver.find_element(By.XPATH, "//label[contains(text(), '全景')]").click()
if area == '2':
    driver.find_element(By.XPATH, "//label[contains(text(), '東亞')]").click()
if area == '3':
    driver.find_element(By.XPATH, "//label[contains(text(), '臺灣')]").click()

#時間表格挑選
obj1 = Select(driver.find_element(By.ID, "selectday"))
#select_by_index
obj1.select_by_visible_text(t)
img_src = driver.find_element(By.XPATH, "//*[@id='link-1']/img").get_attribute("src")
image = io.imread(img_src)
plt.imshow(image)
plt.show()
#2022/05/03 19:20