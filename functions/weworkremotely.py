from functions import utils as ut

def extract_jobs(soup):
  jobs=[]
  for job in soup:
    title = job.find("span", {"class": "title"}).get_text().strip()
    company = job.find("span", {"class": "company"}).get_text().strip()
    location = job.find("span", {"class": "region company"}).get_text().strip()
    link = "https://weworkremotely.com/" + job.find("a")["href"]
    job = {
      'site': "WeWorkRemotely",
      'company':company,
      'location':location,
      'title': title,
      'link':link,
    }
    print(job)
    jobs.append(job)
  return jobs


async def get_jobs(job):
  try:
    job_url=f"https://weworkremotely.com/remote-jobs/search?term={job}"
    soup = await ut.requestWithUgerAgent(job_url).find_all("li", {"class": "feature"})  
    return extract_jobs(soup)
  except:
    return []
