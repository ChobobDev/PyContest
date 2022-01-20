from functions import utils as ut

def extract_jobs(soup):
  jobs=[]
  print("Remote Ok")
  for job in soup:
    title = job.find('h3', {'itemprop':'name'}).text
    company = job.find('h2', {'itemprop':'title'}).text
    link = "https://remoteok.io" + job.find('a', {'class':'preventLink'})['href']
    job = {
      'site': "RemoteOk",
      'company':company,
      'location':"N/A",
      'title': title,
      'link':f"{link}",
    }
    jobs.append(job)
  return jobs


def get_jobs(job):
  try:
    job_url= f'https://remoteok.com/remote-{job}-jobs'
    soup=ut.requestWithUgerAgent(job_url).find_all('tr', {'class':'job'})
    return extract_jobs(soup)
  except:
    return []
