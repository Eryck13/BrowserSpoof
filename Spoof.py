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




path=os.path.dirname(os.path.abspath(__file__))
proxy_list = []
with open(path+'\\config.txt','r') as f:
    config = json.load(f)
    tasks = config["Tasks"]
    site = config["Site"]


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
                #chrome_options = Options()
                chrome_options.add_argument("user-agent="+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36")#ua)
                chrome_options.add_argument('--ignore-certificate-errors-spki-list')
                chrome_options.add_argument('--ignore-certificate-errors')
                chrome_options.add_argument('--disable-plugins-discovery')
                chrome_options.add_experimental_option("detach", True)
                chrome_options.add_experimental_option('useAutomationExtension', False)
                chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
                driver = webdriver.Chrome(options=chrome_options,executable_path=path+"\\chromedriver.exe")
                driver.get("chrome-extension://ggmdpepbjljkkkdaklfihhngmmgmpggp/options.html")
                WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID,"login")))
                driver.maximize_window()
                driver.implicitly_wait(5)
                a=driver.find_element_by_id("login")
                a.send_keys(user)
                b=driver.find_element_by_id("password")
                b.send_keys(password)
                c=driver.find_element_by_id("retry")
                c.clear()
                d=driver.find_element_by_id("retry")
                d.send_keys("2")
                e=driver.find_element_by_id("save")
                e.click()
                driver.get(str(site))
            else: 
                chrome_options = Options()
                chrome_options.add_argument("--proxy-server=http://{}".format(PROXY))
                #chrome_options = Options()
                #chrome_options.add_argument('--incognito')
                chrome_options.add_argument("user-agent="+"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36")#ua)
                chrome_options.add_argument('--ignore-certificate-errors-spki-list')
                chrome_options.add_argument('--ignore-certificate-errors')
                chrome_options.add_argument('--disable-plugins-discovery')
                chrome_options.add_experimental_option("detach", True)
                chrome_options.add_experimental_option('useAutomationExtension', False)
                chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
                driver = webdriver.Chrome(options=chrome_options,executable_path=path+"\\chromedriver.exe")
                driver.get(str(site))
#spoof(site,count)

def thread(tasks,site):
    count = 0
    get_proxy(count)    

    # with concurrent.futures.ThreadPoolExecutor(max_workers=int(tasks)) as executor:
    #      executor.map(spoof(site,count), range(int(tasks)))
    #      count+=1
    while int(count)<int(tasks):
            x = threading.Thread(target=spoof,args=(site,count))
            x.start()
            count+=1

# if __name__ == "__main__":
    #thread(tasks,site,count)
