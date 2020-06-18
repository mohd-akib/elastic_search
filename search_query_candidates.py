import json

import requests
import yaml
from models.JobPostsSearchQuery import JobPostsSearchQuery
from models.CandidatesSearchQuery import CandidatesSearchQuery


def get_search_url_for_index(index):
    with open("config.yml", "r") as ymlfile:
        config = yaml.load(ymlfile)
    url = "http://" + config["elastic_search"]["host"] + ":" + str(
        config["elastic_search"]["port"]) + "/" + index + "/_search"
    print(url)
    return url


def query_candidates(search_bar_text, latitude, longitude, distance, last_updated_timestamp, college_tier,
                     required_work_experience):
    headers = {'Content-Type': 'application/json'}
    query_body = CandidatesSearchQuery(search_bar_text=search_bar_text, latitude=latitude, longitude=longitude,
                                       distance=distance, last_updated_timestamp=last_updated_timestamp,
                                       college_tier=college_tier,
                                       required_work_experience=required_work_experience)

    candidate_search_query_json_string = json.dumps(query_body.serialize())
    print(candidate_search_query_json_string)

    resp = requests.request(method='get', url=get_search_url_for_index("candidates"),
                            data=candidate_search_query_json_string, headers=headers)

    return resp


if __name__ == "__main__":
    search_bar_text_1 = "java developers in bangalore"
    latitude_1 = 12.91449
    longitude_1 = 77.666512
    distance_1 = "5km"
    last_updated_timestamp_1 = 1591756300
    college_tier_1 = 3
    required_work_experience_1 = 3
    response = query_candidates(search_bar_text=search_bar_text_1, latitude=latitude_1, longitude=longitude_1,
                                distance=distance_1,
                                last_updated_timestamp=last_updated_timestamp_1, college_tier=college_tier_1,
                                required_work_experience=required_work_experience_1)
    print(response.content)
