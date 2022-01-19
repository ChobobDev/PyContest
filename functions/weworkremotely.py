from tqdm import tqdm
from multiprocessing import Process,Manager
from functions import request_soup as rs

manager = Manager()
job_list = manager.list()

def extract_jobs(soup):
  for job in tqdm(soup):
    table = job.find_all('li')
    for j in table[:-1]:
      title = j.find('span',{'class':'title'}).text
      company = j.find('span', {'class':'company'}).text
      link=j.find_all('a')[1]['href']
      job = {
        'site': "WeWorkRemotely",
        'company':company,
        'location':"N/A",
        'title': title,
        'link':f"https://weworkremotely.com{link}",
      }
      job_list.append(job)


def get_jobs(jobs):
  for job in jobs:
    try:
      job_url=f"https://weworkremotely.com/remote-jobs/search?term={job}"
      soup = rs.requestWithUgerAgent(job_url).find_all('section', {'class':'jobs'})
      wwrp1 = Process(target=extract_jobs, args=(soup,))
      wwrp1.start()
      wwrp1.join()
      return job_list
    except:
      return []

