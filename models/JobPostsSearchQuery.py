from models.JobPost import LatLong
import time


class JobPostsSearchQuery:
    def __init__(self, search_bar_text, latitude, longitude, distance, posted_time_timestamp, college_tier,
                 work_experience):
        self.bool_query = Bool(search_bar_text, latitude, longitude, distance, posted_time_timestamp, college_tier,
                               work_experience)

    def serialize(self):
        return {
            "query": {
                "bool": self.bool_query.serialize()
            }
        }


class MultiMatchQuery:
    def __init__(self, text):
        self.multi_match = MultiMatchNestedQuery(text)

    def serialize(self):
        return {
            "multi_match": self.multi_match.serialize()
        }


class MultiMatchNestedQuery:
    def __init__(self, text):
        self.text_query = text
        self.fields = ["*"]
        self.type = "bool_prefix"

    def serialize(self):
        return {
            "query": self.text_query,
            "fields": self.fields,
            "type": self.type
        }


class Bool:
    def __init__(self, search_bar_text, latitude, longitude, distance, posted_time_timestamp, college_tier,
                 required_work_experience):
        self.filters = Filters(distance=distance, latitude=latitude, longitude=longitude,
                               required_work_experience=required_work_experience,
                               college_tier=college_tier,
                               posted_time_timestamp=posted_time_timestamp)
        self.must = MultiMatchQuery(text=search_bar_text)

    def serialize(self):
        return {
            "must": self.must.serialize(),
            "filter": self.filters.serialize()
        }


class GeoDistanceRadiusFilter:
    def __init__(self, latitude, longitude, distance):
        self.distance = distance
        self.lat_long = LatLong(latitude, longitude)

    def serialize(self):
        return {
            "distance": self.distance,
            "lat_long": self.lat_long.serialize()
        }


class RequiredWorkExperienceFilter:
    def __init__(self, required_work_experience):
        self.gte = required_work_experience

    def serialize(self):
        return {
            "gte": self.gte
        }


class PostedDateTimestampFilter:
    def __init__(self, low, hi):
        self.gte = low
        self.lte = hi

    def serialize(self):
        return {
            "gte": self.gte,
            "lte": self.lte
        }


class CollegeTierFilter:
    def __init__(self, college_tier):
        self.lte = college_tier

    def serialize(self):
        return {
            "lte": self.lte
        }


class Filters:
    def __init__(self, distance, latitude, longitude, required_work_experience, college_tier, posted_time_timestamp):
        self.geo_distance = GeoDistanceRadiusFilter(latitude=latitude, longitude=longitude, distance=distance)
        self.required_work_experience = RequiredWorkExperienceFilter(required_work_experience=required_work_experience)
        self.college_tier = CollegeTierFilter(college_tier=college_tier)
        self.posted_date_timestamp = PostedDateTimestampFilter(low=posted_time_timestamp, hi=time.time())

    def serialize(self):
        return [
            {"geo_distance": self.geo_distance.serialize()},
            {"range": {"required_work_experience": self.required_work_experience.serialize()}},
            {"range": {"college_tier": self.college_tier.serialize()}},
            {"range": {"posted_date_timestamp": self.posted_date_timestamp.serialize()}}
        ]
