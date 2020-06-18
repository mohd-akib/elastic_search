from models.JobPost import LatLong


class Candidate:
    def __init__(self, first_name, last_name, mobile_number, email_address, skills, current_address, work_experience,
                 current_domain, college_name, college_tier, current_company, current_ctc,
                 availability, keywords, title, resume_link, current_location_latitude, current_location_longitude,
                 current_location_pin_code, last_updated_timestamp):
        self.first_name = first_name
        self.last_name = last_name
        self.mobile_number = mobile_number
        self.email_address = email_address
        self.skills = skills
        self.current_address = current_address
        self.work_experience = work_experience
        self.current_domain = current_domain
        self.college_name = college_name
        self.college_tier = college_tier
        self.current_company = current_company
        self.current_ctc = current_ctc
        self.availability = availability
        self.keywords = keywords
        self.title = title
        self.current_location_lat_long = LatLong(lat=current_location_latitude, lon=current_location_longitude)
        self.current_location_pin_code = current_location_pin_code
        self.resume_link = resume_link
        self.last_updated_timestamp = last_updated_timestamp

    def serialize(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "mobile_number": self.mobile_number,
            "email_address": self.email_address,
            "skills": self.skills,
            "current_address": self.current_address,
            "work_experience": self.work_experience,
            "current_domain": self.current_domain,
            "college_name": self.college_name,
            "college_tier": self.college_tier,
            "current_company": self.current_company,
            "current_ctc": self.current_ctc,
            "availability": self.availability,
            "keywords": self.keywords,
            "title": self.title,
            "current_location_lat_long": self.current_location_lat_long.serialize(),
            "current_location_pin_code": self.current_location_pin_code,
            "resume_link": self.resume_link,
            "last_updated_timestamp": self.last_updated_timestamp
        }
