from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

website = "https://www.ufc.com/rankings"
path = "D:\chromedriver-win64\chromedriver.exe"
driver = webdriver.Chrome()
driver.get(website)

fighters = driver.find_elements(By.TAG_NAME, 'tr')

go = 1
time.sleep(10)


name = []
rank = []
for i in fighters:
    #if "Rank" in i:
        #i = i[0:-20]
    #print(i.text)
    i = i.text
    if "Rank" in i:
        i = i[0:-20]
    if go <= 9:
        name.append(i[2:])
        rank.append(i[0])
    if go > 9:
        name.append(i[3:])
        rank.append(i[:2])
    if go == 15:
        break
    go +=1

driver.quit()

df = pd.DataFrame({'rank' : rank, 'name': name})
df.to_csv("p4p_rankings.csv", index=False)
print(df)
#print(name)
#print(rank)