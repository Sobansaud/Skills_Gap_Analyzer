Streamlit Link: {}

👨‍💻 Made with ❤️ by Muhammad Soban Saud

Skill Gap Analyzer - 1$ Challenge


Overview :-

The Skill Gap Analyzer is a web tool developed as part of the 1$ Challenge by Sir Asharib and Sir Hamza. The tool leverages Object-Oriented Programming (OOP) techniques to help users analyze their skills against their desired job roles. By identifying gaps in skills, the tool provides personalized suggestions and resources to help users bridge these gaps, improving their chances of landing their dream job.

This tool is built with modularity and scalability in mind, ensuring it’s both efficient and easy to maintain.

(Features):-
1. User Input & Skill Detection
Users can enter their name and skills.

Skills are categorized into Technical Skills and Soft Skills, and matched with the requirements of the chosen job role.

2. Skill Gap Analysis
The tool compares the user's current skills with the ideal skills for the selected job role.

It calculates the percentage of skills the user has compared to the total required skills for the role.

3. Progress Visualization
The progress is visualized using dynamic progress bars to represent how many skills the user possesses and how many they need to learn.

4. Personalized Resource Recommendations
Based on the skills the user is missing, the tool provides learning resources (e.g., courses, tutorials) to help fill the gaps.

5. PDF Report Generation
A downloadable PDF report is generated, summarizing the user’s skill gap, progress, and recommended resources.

How It Works (Using OOP Principles)
1. User Profile & Skill Input
Users input their personal information and list their skills in the input fields.

The UserProfile class stores this information and prepares it for analysis.

2. Skill Matching
The JobRole class contains a list of skills required for each role.

The tool compares the user's input skills with the required skills for the chosen job.

3. Skill Gap Calculation
The Analyzer class performs the skill gap analysis by calculating the percentage of skills the user has compared to the required ones.

4. Resource Recommendations
The ResourceRecommender class provides links to relevant resources (such as online courses) to help the user improve their missing skills.

5. PDF Report Generation
The ReportGenerator class generates a PDF report summarizing the user’s skill gap, progress, and recommended resources.

(Technologies Used):
Streamlit: For building the web app and displaying the interactive user interface.

Python: The core programming language, with Object-Oriented Programming (OOP) principles used for code modularity and organization.

Pandas: For handling and analyzing the skill data.

Plotly: For creating interactive charts and visualizing the user's progress in skill acquisition.

Matplotlib: Used for visualizing the data, including charts and graphs.

Fpdf: For generating the PDF report for users.

Object-Oriented Programming (OOP):

UserProfile: A class that stores user details and current skills.

JobRole: A class that contains the required skills for each job role.

Analyzer: A class that analyzes the user’s skills and compares them to the requirements.

ResourceRecommender: A class that provides personalized learning resources.

ReportGenerator: A class that generates the downloadable PDF report.

(How to Use):-
Upload Your Information:

Enter your name and skills in the provided fields on the homepage.

Choose Your Dream Job:

Select the job role you're interested in from the dropdown list.

Analyze Your Skills:

Click the Analyze Skills Now button to analyze your skill gap.

The tool will display a dynamic progress bar indicating the percentage of skills you possess.

Explore Your Results:

View the Skill Gap Analysis, where the missing skills are shown, and recommended resources are provided.

Generate PDF Report:

If you want to download a report, click on the Generate PDF Report button to get a detailed summary of your skill gap and resources.

Class Structure
1. UserProfile
Stores the user’s personal data, including name and skills.

2. JobRole
Contains the required skills for different job roles (e.g., Software Engineer, Data Scientist).

3. Analyzer
Analyzes the user’s skills and compares them with the required skills for the selected job.

Calculates the percentage of skills the user has versus the skills needed.

4. ResourceRecommender
Suggests learning resources (courses, tutorials, articles) for the skills the user is lacking.

5. ReportGenerator
Creates a PDF report summarizing the user's analysis, including their skill gap and recommendations.



Conclusion:-
The Skill Gap Analyzer is a powerful tool that helps individuals identify the gaps in their skills and provides personalized learning resources to help them grow. The use of Object-Oriented Programming (OOP) ensures that the tool is modular, scalable, and easy to maintain.

By using Streamlit and Python, this project provides an interactive and user-friendly experience for users aiming to improve their skills and land their dream jobs