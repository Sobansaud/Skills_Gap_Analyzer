import json

class SkillDatabase:
    def __init__(self,file_path):
        with open(file_path,"r") as f:
            self.job_data = json.load(f)

    def get_required_skills(self,job_title):
        return self.job_data.get(job_title,[])
    
    def get_all_jobs(self):
        return list(self.job_data.keys())