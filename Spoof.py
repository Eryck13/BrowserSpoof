import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import random
from fake_useragent import UserAgent
import fake_useragent
from concurrent.futures import ProcessPoolExecutor
import concurrent.futures
from selenium import webdriver
import threading
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from tkinter import *

path=os.path.dirname(os.path.abspath(__file__))

root= Tk()
root.title('BoringBrowser')
root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file=path+'\\BoringBot.png'))
x=IntVar()
y=StringVar()
Label1=Label(root,text="Tasks")
Label2=Label(root,text="Site")
entry1 = Entry(root,textvariable=x)
entry2 = Entry(root,textvariable=y) 
Label1.grid(row=0,column=0)
entry1.grid(row=0,column=1)
Label2.grid(row=1,column=0)
entry2.grid(row=1,column=1)    
button1 = Button(text='Launch', command=lambda:thread(x.get(),y.get()))
button1.grid(row=2,column=0)

path=os.path.dirname(os.path.abspath(__file__))
proxy_list = []
def get_proxy(count):
    proxies = open(path+"\\proxies.txt", 'r').read().splitlines()
    try:
        for line in proxies:
            if len(line.split(':'))==4:
                ip = (line.split(':')[0])
                port = (line.split(':')[1])
                user = (line.split(':')[2])
                ippw = (line.split(':')[3])
                httpline = ('{}:{}@{}:{}'.format(user,ippw,ip,port))
                proxy_list.append(httpline)
            else:
                ip = (line.split(':')[0])
                port = (line.split(':')[1])
                httpline = ('{}:{}'.format(ip,port))
                proxy_list.append(httpline)
    except:
        print("Proxy Error")

def spoof(site,count):
            ranua = UserAgent()
            ua=ranua.random
            
            if len(proxy_list) > 0:
                PROXY = random.choice(proxy_list)
                proxy_list.remove(PROXY)
            else:
                PROXY = random.choice(proxy_list)
            
            if '@' in PROXY:
                split=PROXY.split("@")
                PROXY = split[1]
                PROXY2=split[0].split(":")
                user=PROXY2[0]
                password=PROXY2[1]
                chrome_options = Options()
                chrome_options.add_extension(path+"\\Proxy Auto Auth.crx")
                chrome_options.add_argument("--proxy-server=http://{}".format(PROXY))
                chrome_options.add_argument("user-agent="+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36")#ua)
                chrome_options.add_argument('--ignore-certificate-errors-spki-list')
                chrome_options.add_argument('--ignore-certificate-errors')
                chrome_options.add_argument('--disable-plugins-discovery')
                chrome_options.add_experimental_option("detach", True)
                chrome_options.add_experimental_option('useAutomationExtension', False)
                chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
                driver = webdriver.Chrome(options=chrome_options,executable_path=path+"\\chromedriver.exe")
                wait = WebDriverWait(driver, 10)
                a=wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="login"]')))
                b=wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="password"]')))
                c=wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="retry"]')))
                d=wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="retry"]')))
                e=wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="save"]')))
                a.send_keys(user)
                b.send_keys(password)
                c.clear()
                d.send_keys("2")
                e.click()
                driver.get(str(site))
            else: 
                chrome_options = Options()
                chrome_options.add_argument("--proxy-server=http://{}".format(PROXY))
                chrome_options.add_argument("user-agent="+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36")#ua)
                chrome_options.add_argument('--ignore-certificate-errors-spki-list')
                chrome_options.add_argument('--ignore-certificate-errors')
                chrome_options.add_argument('--disable-plugins-discovery')
                chrome_options.add_experimental_option("detach", True)
                chrome_options.add_experimental_option('useAutomationExtension', False)
                chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
                driver = webdriver.Chrome(options=chrome_options,executable_path=path+"\\chromedriver.exe")
                driver.get(str(site))

def thread(tasks,site):
    count = 0
    get_proxy(count)    
    while int(count)<int(tasks):
            x = threading.Thread(target=spoof,args=(site,count))
            x.start()
            count+=1
root.mainloop()

