import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import random
from fake_useragent import UserAgent
import fake_useragent
#import threadingcd 
from concurrent.futures import ProcessPoolExecutor
import concurrent.futures
from seleniumwire import webdriver



path=os.path.dirname(os.path.abspath(__file__))
proxy_list = []
with open(path+'\\config.txt','r') as f:
    config = json.load(f)
    tasks = config["Tasks"]
    site = config["Site"]


def get_proxy():
    proxies = open(path+"\\proxies.txt", 'r').read().splitlines()
    try:
        for line in proxies:
            if len(line.split(':'))==4:
                ip = (line.split(':')[0])
                port = (line.split(':')[1])
                user = (line.split(':')[2])
                ippw = (line.split(':')[3])
                httpline = ('http://{}:{}@{}:{}'.format(user,ippw,ip,port))
                proxy_list.append(httpline)
            else:
                ip = (line.split(':')[0])
                port = (line.split(':')[1])
                httpline = ('http://{}:{}'.format(ip,port))
                proxy_list.append(httpline)
    except:
        print("Proxy Error")

def spoof(lol):
        ranua = UserAgent()
        ua=ranua.random
        if len(proxy_list) > 0:
            PROXY = random.choice(proxy_list)
            proxy_list.remove(PROXY)
        else:
            PROXY = random.choice(proxy_list)
        
        chrome_options = Options()
        chrome_options.add_argument("user-agent="+ua)
        chrome_options.add_argument('--incognito')
        chrome_options.add_argument('--ignore-certificate-errors-spki-list')
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--proxy-server=http://%s' % PROXY)
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=chrome_options,executable_path=path+"\\chromedriver.exe")
        driver.get(site)

def thread():
    with concurrent.futures.ThreadPoolExecutor(max_workers=int(tasks)) as executor:
        executor.map(spoof, range(int(tasks)))
        # x = threading.Thread(target=spoof)
        # x.start()
        # x.join()

if __name__ == "__main__":
    get_proxy()    
    thread()

