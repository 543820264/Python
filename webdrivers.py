from selenium import webdriver
import threading

def driver(url,browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        driver.get(url)
    if browser == 'firefox':
        driver = webdriver.Firefox()
        driver.get(url)

if __name__ == '__main__':
    url = 'https://github.com'
    threads = []
    t1 = threading.Thread(target=driver, args=(url, 'firefox'))
    threads.append(t1)
    t2 = threading.Thread(target=driver, args=(url, 'chrome'))
    threads.append(t2)
    for t in threads:
        t.start()
    for t in threads:
        t.join()
