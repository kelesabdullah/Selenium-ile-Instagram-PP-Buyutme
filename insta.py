from selenium import webdriver
import time
user = input("write username: ")
driver = webdriver.Opera(executable_path="driver.exe dosyasının klasör konumu buraya")

url = "https://izoomyou.com/tr/user/"+user
driver.get(url)
time.sleep(1)
veri = driver.find_element_by_id("userthumbnail").get_attribute("src")
print(veri)
driver.get(veri)
driver.maximize_window()
time.sleep(10)
driver.quit()