import time
from functions import stackoverflow as so ,weworkremotely as wwr,remoteok as ro

def scrape_selected(job_name,site):
    start_time = time.time()
    for site in selected_site:
        if site=="so":
            jobs.extend(so.get_jobs([job_name]))
        if site=="wwr":
            jobs.extend(wwr.get_jobs([job_name]))
        if site=="ro":
            jobs.extend(ro.get_jobs([job_name]))
    print("--- %s seconds ---" % (time.time() - start_time))

def scrape_all(job_name):
    jobs=[]
    jobs.extend(so.get_jobs([job_name]))
    jobs.extend(wwr.get_jobs([job_name]))
    jobs.extend(ro.get_jobs([job_name]))
    return jobs

def clear_all():
    so.reset_memory()
    wwr.reset_memory()
    ro.reset_memory()
