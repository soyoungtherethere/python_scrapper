from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('C:/Users/user/Downloads/chromedriver')
driver.implicitly_wait(3)
driver.get('https://nid.naver.com/nidlogin.login')
driver.find_element_by_name('id').send_keys('type your naver id here')
driver.find_element_by_name('pw').send_keys('type your naver password here')
# 이 사이에서 자동 입력 방지로 인해 자동입력방지 문자를 손으로 입력해줘야 했다..
driver.find_element_by_xpath('//*[@id="new.save"]').click()

# Naver 페이 들어가기
driver.get('https://order.pay.naver.com/home')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
boughtitems = soup.find_all("p",{"class":"name"}) #구매 항목 이름들어 있는 태그들 긁어오기

for n in boughtitems:
    print(n.text.strip().lstrip('포인트플러스').strip()) #필요한 텍스트만 추출
