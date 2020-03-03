import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f'https://www.indeed.com/jobs?q=python&limit={LIMIT}'

# 웹사이트의 max page number 반환해주는 함수 정의
def get_last_page():
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, 'html.parser') 
  pagination = soup.find("div",{"class":"pagination"}) 
  links = pagination.find_all('a')
  pages = []
  for link in links[:-1]:
    pages.append(int(link.string)) 
  max_page = pages[-1]
  return max_page

def extract_job(html): #주어진 html문서에서 필요한 정보만 뽑아오는 함수
    title = html.find('div',{'class':'title'}).find('a')['title']
    company = html.find("span",{"class":"company"})
    if company:
      company_anchor = company.find('a')
      if company_anchor is not None:
        company = str(company_anchor.string)
      else:
        company = str(company.string)
      company = company.strip()
    else:
      company = None
    location = html.find("div", {"class":"recJobLoc"})['data-rc-loc']
    job_id = html["data-jk"]
    return{'title': title, 'company':company, 'location':location, 'link':f"https://www.indeed.com/viewjob?jk={job_id}"}


# 각 페이지마다의 html을 추출하고, 그 안의 정보를 extract_job 함수로 추출해서 list에 정리할 함수 extract_jobs
def extract_jobs(last_page):
  jobs = [] 
  for page in range(last_page):
    print(f"Scrapping Indeed: Page {page}")
    result = requests.get(f"{URL}&start={page*LIMIT}") #whole HTML of each page
    soup = BeautifulSoup(result.text, 'html.parser') #whole HTML of each page
    results = soup.find_all("div", {'class': 'jobsearch-SerpJobCard'}) 
    #전체 HTML에서 class name이 Serp어쩌구인 div들을 몽땅 모아 list로 만든 것이 results
    for result in results: #results의 각 element에 대해 아래를 적용해라
      job = extract_job(result)
      jobs.append(job) #job을 jobs에 넣어주기
  return jobs

def get_jobs():
  last_page = get_last_page()
  jobs = extract_jobs(last_page)
  return jobs