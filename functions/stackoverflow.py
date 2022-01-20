from functions import request_soup as rs

def get_pagination(soup):
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
  jobs=[]
  for page in range(1,last_page+1):
    soup=rs.requestWithUgerAgent(f"{job_url}&pg={page}").find_all("div", {"class": "-job"})
    jobs.extend(get_job_detail(soup))
  return jobs

def get_jobs(jobs):
  try:
      job_url=f"https://stackoverflow.com/jobs?q={job}&pg=i"
      soup=rs.requestWithUgerAgent(job_url)
      last_page=get_pagination(soup)
      print(last_page)
      return extract_pages(job_url,last_page)
  except:
    print("Here")
    return []

    