import requests,tqdm
from bs4 import BeautifulSoup

def extract_jobs(soup):
  jobs=[]
  for job in soup:
    table = job.find_all('li')
    for j in table[:-1]:
      title = j.find('span',{'class':'title'}).text
      company = j.find('span', {'class':'company'}).text
      link=j.find_all('a')[1]['href']
      job = {
        'site': "remote",
        'company':company,
        'title': title,
        'link':f"https://weworkremotely.com{link}",
      }
      print(job)
      jobs.append(job)
  return jobs


def get_jobs(jobs):
  for job in jobs:
    try:
      job_url= f'https://remoteok.com/remote-dev+{job}-jobs'
      soup = BeautifulSoup(requests.get(job_url))
      extract_jobs(soup)
    except:
      return []

