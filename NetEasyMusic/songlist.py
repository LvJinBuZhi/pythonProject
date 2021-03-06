from selenium import webdriver
url = "https://music.163.com/#/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset=0"
browser = webdriver.Chrome() #用Chorme接口创建一个webdriver

while url != 'javascript:void(0)':
    browser.get(url)
    browser.switch_to.frame("contentFrame")
    data = browser.find_element_by_id("m-pl-container").find_elements_by_tag_name("li")
    for i in range(len(data)):
        num = data[i].find_element_by_class_name("nb").text
        if '万'in num and int(num.split('万')[0])>1000:
            msk=data[i].find_element_by_css_selector("a.msk")
            with open("list.txt",'a',encoding='utf-8') as f:
                f.write(' '.join([msk.get_attribute('title'),num,msk.get_attribute('href')])+'\n'+'='*50+'\n')
    url = browser.find_element_by_css_selector("a.zbtn.znxt").get_attribute("href")
browser.close()