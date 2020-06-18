import yaml
import requests
import logging
import json
from models.JobPost import JobPost


def get_url_for_index_and_id(index, id):
    with open("config.yml", "r") as ymlfile:
        config = yaml.load(ymlfile)
    url = "http://" + config["elastic_search"]["host"] + ":" + str(
        config["elastic_search"]["port"]) + "/" + index + "/_doc/" + str(id)
    print(url)
    return url


def index_job_post(job_post, id):
    try:
        headers = {'Content-Type': 'application/json'}
        resp = requests.post(get_url_for_index_and_id(index="job_posts", id=id), data=job_post, headers=headers)
        print(resp.json())
        if resp.status_code != 200:
            logging.error("ES: error in indexing data to job_posts index")
    except Exception as e:
        logging.error("ES: Exception in indexing data to job_posts index %s", e)


if __name__ == "__main__":
    job_post = JobPost(job_title="Java Developer",
                       job_type="fulltime",
                       skills=["Java", "Spring", "Hibernate", "JPA", "Junit"],
                       college_tier=None,
                       industry="Pharmaceutical Industry",
                       required_work_experience=3,
                       company_name="Signant Health",
                       pin_code=500081,
                       city="Hyderabad",
                       state="Telangana",
                       country="India",
                       posted_date=1592224011,
                       expiry_date=1592656011,
                       keywords=["J2EE", "Pharmaceutical", "Health", "Software", "Spring",
                                 "Java", "Soap", "Rest", "microservices", "junit", "agile"])
    job_post_json_string = json.dumps(job_post.serialize())
    index_job_post(job_post=job_post_json_string, id=1)
