class Analyzer:
    def __init__(self,user_profile,job_role):
        self.user = user_profile
        self.job = job_role


    def analyze(self):
        matched = list(set(self.user.current_skills) & set(self.job.required_skills))
        missing = list(set(self.job.required_skills) - set(self.user.current_skills))

        return matched , missing
    