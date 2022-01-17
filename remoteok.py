import tqdm
import request_soup as rs

def extract_jobs(soup):
  jobs=[]
  for job in soup:
    title = job.find('h3', {'itemprop':'name'}).text
    company = job.find('h2', {'itemprop':'title'}).text
    link = "https://remoteok.io" + job.find('a', {'class':'preventLink'})['href']
    job = {
      'site': "RemoteOk",
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
      job_url= f'https://remoteok.com/remote-{job}-jobs'
      soup=rs.requestWithUgerAgent(job_url).find_all('tr', {'class':'job'})
      extract_jobs(soup)
    except:
      return []

