class LatLong:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def serialize(self):
        return {
            "lat": self.lat,
            "lon": self.lon
        }


class JobPost:
    def __init__(self, job_title, job_type, skills, college_tier, industry, required_work_experience, company_name,
                 pin_code, city, state, country, company_address, posted_date, expiry_date, lat_long, keywords=None,
                 description=None):
        self.job_title = job_title
        self.job_type = job_type
        self.skills = skills
        self.college_tier = college_tier
        self.industry = industry
        self.required_work_experience = required_work_experience
        self.company_name = company_name
        self.pin_code = pin_code
        self.city = city
        self.state = state
        self.country = country
        self.company_address = company_address
        self.posted_date = posted_date
        self.expiry_date = expiry_date
        self.lat_long = lat_long
        self.keywords = keywords
        self.description = description

    def serialize(self):
        return {"job_title": self.job_title,
                "job_type": self.job_type,
                "skills": self.skills,
                "college_tier": self.college_tier,
                "industry": self.industry,
                "required_work_experience": self.required_work_experience,
                "company_name": self.company_name,
                "pin_code": self.pin_code,
                "city": self.city,
                "state": self.state,
                "country": self.country,
                "company_address": self.company_address,
                "posted_date": self.posted_date,
                "expiry_date": self.expiry_date,
                "lat_long": self.lat_long,
                "keywords": self.keywords,
                "description": self.description}
