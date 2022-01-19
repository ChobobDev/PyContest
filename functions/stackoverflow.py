from tqdm import tqdm
from multiprocessing import Process,Manager
from functions import request_soup as rs

manager = Manager()
job_list = manager.list()

def get_pagination(soup):
  pagination = soup.find("div", class_="s-pagination").find_all("a")
  last_page = pagination[-2].get_text(strip=True)
  return int(last_page)

def get_job_detail(jobs_table):
  for job in tqdm(jobs_table):
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
    job_list.append(job)
  

def extract_pages(job_url,last_page):
  job_from_page=[]
  for page in tqdm(range(1,last_page+1)):
    soup=rs.requestWithUgerAgent(f"{job_url}&pg={page}").find_all("div", {"class": "-job"})
    sop2 = Process(target=get_job_detail(soup))
    sop2.start()
    sop2.join()

def get_jobs(jobs):
  for job in jobs:
    try:
      job_url=f"https://stackoverflow.com/jobs?q={job}&sort=i"
      soup=rs.requestWithUgerAgent(job_url)
      last_page=get_pagination(soup)
      sop1 = Process(target=extract_pages, args=(job_url,last_page))
      sop1.start()
      sop1.join()
      return job_list
    except:
      print("Here")
      return []
