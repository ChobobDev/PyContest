import tqdm
import request_soup as rs

def extract_jobs(soup):
  jobs=[]
  for job in soup:
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
      jobs.append(job)
  return jobs


def get_jobs(jobs):
  for job in jobs:
    try:
      job_url=f"https://weworkremotely.com/remote-jobs/search?term={job}"
      soup = rs.requestWithUgerAgent(job_url).find_all('section', {'class':'jobs'})
      return extract_jobs(soup)
    except:
      return []

