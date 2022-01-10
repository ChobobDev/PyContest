import requests,tqdm
from bs4 import BeautifulSoup

def get_pagination(job_url):
  target = requests.get(job_url)
  soup = BeautifulSoup(target.text, "html.parser")
  paginations = soup.find("div", class_="s-pagination").find_all("a")
  last_page = paginations[-2].get_text(strip=True)
  return int(last_page)

def get_job_detail(jobs):
  job = {
    "site": "Stackoverflow",
    "company": ,
    "avatar": ,
    "location": ,
    "title": ,
    "link": f"https://stackoverflow.com{a['href']}",
  }
  return job

def extract_pages(job_url,last_page):
  for page in range(1,last_page+1):
    page_results=requests.get(f"{job_url}&pg={page}")
    soup = BeautifulSoup(page_results.text, "html.parser")
    individual_result= soup.find_all("div", {"class": "-job"})










def get_jobs(jobs):
  for job in jobs:
    try:
      job_url=f"https://stackoverflow.com/jobs?q={job}&sort=i"
      last_page=get_pagination(job_url)
    except:
      return []

