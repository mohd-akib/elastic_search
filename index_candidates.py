import yaml
import requests
import logging
import json
from models.Candidates import Candidate


def get_url_for_index_and_id(index, id):
    with open("config.yml", "r") as ymlfile:
        config = yaml.load(ymlfile)
    url = "http://" + config["elastic_search"]["host"] + ":" + str(
        config["elastic_search"]["port"]) + "/" + index + "/_doc/" + str(id)
    print(url)
    return url


def index_candidate(candidate, id):
    try:
        headers = {'Content-Type': 'application/json'}
        resp = requests.post(get_url_for_index_and_id(index="candidates", id=id), data=candidate, headers=headers)
        print(resp.json())
        if resp.status_code != 200:
            logging.error("ES: error in indexing data to candidates index")
    except Exception as e:
        logging.error("ES: Exception in indexing data to candidates index %s", e)


if __name__ == "__main__":
    candidate = Candidate(first_name="Mohd",
                          last_name="Akmo",
                          mobile_number="9304850614",
                          email_address="akibk001@gmail.com",
                          skills=["java", "python", "c", "c++", "algorithm", "machine learning",
                                  "competitive programming"],
                          current_address="flat 403 building 670 hsr layout sector3 bangalore, india",
                          work_experience=3,
                          current_domain="software development",
                          college_name="NIT Jamshedpur",
                          college_tier=2,
                          current_company="Medlife",
                          current_ctc=1000000,
                          availability="immediate",
                          keywords=["software", "java", "python", "bangalore", "developer"],
                          title="software engineer",
                          current_location_latitude=12.911862,
                          current_location_longitude=77.644592,
                          resume_link="www.medlife.com",
                          current_location_pin_code=560102,
                          last_updated_timestamp=1592485542
                          )
    candidate_json_string = json.dumps(candidate.serialize())
    index_candidate(candidate=candidate_json_string, id=1)
