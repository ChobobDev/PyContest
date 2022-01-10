import requests,tqdm
from bs4 import BeautifulSoup

def get_pagination(job_url):
  target = requests.get(job_url)
  soup = BeautifulSoup(target.text, "html.parser")
  pagination = soup.find("div", class_="s-pagination").find_all("a")
  last_page = pagination[-2].get_text(strip=True)
  return int(last_page)

def get_job_detail(jobs_table):
  jobs = []
  for job in jobs_table:
    a = job.find("h2").a
    title,link=a['title'],a['href']
    company,location=map(str,job.find("h3", {"class": "fs-body1"}).get_text(strip=True).split("•"))
    job = {
      "site": "StackOverflow",
      "company":company,
      "location":location,
      "title": title,
      "link": f"https://stackoverflow.com{link}",
    }
    jobs.append(job)
  return jobs

def extract_pages(job_url,last_page):
  for page in range(1,last_page+1):
    page_results=requests.get(f"{job_url}&pg={page}")
    soup = BeautifulSoup(page_results.text, "html.parser")
    jobs_table= soup.find_all("div", {"class": "-job"})
    get_job_detail(jobs_table)



def get_jobs(jobs):
  for job in jobs:
    try:
      job_url=f"https://stackoverflow.com/jobs?q={job}&sort=i"
      last_page=get_pagination(job_url)
      extract_pages(job_url,last_page)
    except:
      return []

