from plyer import notification
import requests
from bs4 import BeautifulSoup
import time



def notifyme(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "E:\\Python\\Project on Covid-19\\icon1.ico",
        timeout = 9
    )

def getData(url):
    r = requests.get(url)
    return r.text

if __name__ == "__main__":
    # notifyme("Hello Dilip","Lets stop this spread of virus together")
    while True:
        myhtmlData = getData('https://www.mohfw.gov.in/')

        soup = BeautifulSoup(myhtmlData, 'html.parser')
        # print(soup.prettify())
        myDataStr = ""
        for tr in soup.find_all('tbody')[7].find_all('tr'):
            myDataStr += tr.get_text()
        
        myDataStr = myDataStr[1:]
        itemlist = myDataStr.split("\n\n")
        
        states = ['Maharashtra','Odisha','Delhi']
        for item in itemlist[0:25]:
            dataList = item.split("\n")
            if dataList[1] in states:
                # print(dataList)
                title = "COVID-19 STATEWISE STATUS\nSTATE: {}".format(dataList[1])
                figures = "Indians: {}\nForeigners: {}\nCured: {}\nDeaths: {}".format(dataList[2],dataList[3],dataList[4],dataList[5])
                notifyme(title, figures)
                time.sleep(3)
        time.sleep(1800)
    



