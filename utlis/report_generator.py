import os
from datetime import datetime
from fpdf import FPDF

class ReportGenerator:
    def __init__(self, user_name):
        self.user_name = user_name
        self.base_dir = f"reports/{self.user_name}"
        os.makedirs(self.base_dir, exist_ok=True)  # Create reports/username/ if not exists

    def generate_pdf(self, job_title, matched_skills, missing_skills, recommended_resources):
        now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"report_{now}.pdf"
        filepath = os.path.join(self.base_dir, filename)

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", "B", 16)
        pdf.cell(0, 10, f"Skill Gap Report for {self.user_name}", ln=True)

        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, f"Dream Job: {job_title}", ln=True)
        pdf.ln(5)

        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, "Skills You Already Have:", ln=True)
        pdf.set_font("Arial", size=12)
        for skill in matched_skills:
            pdf.cell(0, 10, f"- {skill}", ln=True)

        pdf.ln(5)
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, "Skills You Are Missing:", ln=True)
        pdf.set_font("Arial", size=12)
        for skill in missing_skills:
            pdf.cell(0, 10, f"- {skill}", ln=True)

        pdf.ln(5)
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, "Recommended Resources:", ln=True)
        pdf.set_font("Arial", size=12)
        for skill, link_dict in recommended_resources.items():
            for desc, link in link_dict.items():
                pdf.multi_cell(0, 10, f"{skill}: {link}")

        pdf.output(filepath)
        return filepath

