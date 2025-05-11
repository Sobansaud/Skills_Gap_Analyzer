import streamlit as st
from models.user_profile import User_Profile
from models.job_role import Job_Role
from models.analyzer import Analyzer
from models.skill_database import SkillDatabase
from models.resource_recommender import ResourceRecommender
from utlis.report_generator import ReportGenerator
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Wedge
from io import BytesIO
import time
import requests  # for LinkedIn API scraping (you may need additional API for actual implementation)

# Page config
st.set_page_config(page_title="🤹‍♀️ Skill Gap Analyzer", layout="centered")

# Persistent tab memory
if "active_tab" not in st.session_state:
    st.session_state.active_tab = "🧠 Analyze Skills"

# Welcome message
if 'welcome_shown' not in st.session_state:
    st.session_state['welcome_shown'] = True
    placeholder = st.empty()
    with placeholder.container():
        st.markdown("""
            <style>
                .welcome-container {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                }
                .welcome-box {
                    background-color: #ffffff;
                    padding: 40px 50px;
                    border-radius: 20px;
                    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
                    text-align: center;
                    animation: fadeIn 1s ease-in-out;
                }
                .welcome-box h2 {
                    font-size: 2.5rem;
                    color: #1f77b4;
                    margin-bottom: 10px;
                }
                .welcome-box p {
                    font-size: 1.1rem;
                    color: #333333;
                }
                @keyframes fadeIn {
                    from { opacity: 0; }
                    to { opacity: 1; }
                }
            </style>
            <div class="welcome-container">
                <div class="welcome-box">
                    <h2>👋 Welcome to Skill Gap Analyzer for Dream Job</h2>
                    <p>This AI tool helps you match your skills to your dream job.</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
    time.sleep(1.5)
    placeholder.empty()

st.title("🎯 Skill Gap Analyzer for Dream Job")

# Initialize components
db = SkillDatabase("data/job_role.json")
recommender = ResourceRecommender()

# User inputs
name = st.text_input("🖋 Enter Your Name : ")
current_skills = st.text_input("Enter Your Current Skills (comma separated): ")
selected_job = st.selectbox("Choose Your Dream Job Role : ", db.get_all_jobs())

# Skill Level Detection
skill_level = st.selectbox("Select Your Skill Level : ", ["Beginner", "Intermediate", "Advanced"])

# LinkedIn Profile (Optional for scraping)
linkedin_url = st.text_input("Enter Your LinkedIn Profile URL (optional): ")

if name:
    st.markdown(f"👋 Welcome, **{name}**! Let's analyze your skills and see how ready you are for your dream job as a **{selected_job}**.")
else:
    st.markdown("👋 Welcome! Please enter your name to get started.")

# Tabs
tab_options = ["🧠 Analyze Skills", "📊 Your Score", "📚 Resources"]
selected_tab = st.selectbox("Navigation", tab_options, index=tab_options.index(st.session_state.active_tab))
st.session_state.active_tab = selected_tab

completion_percentage = 0  # default

# ------------------- TAB 1: Analyze Skills -------------------
if selected_tab == "🧠 Analyze Skills":
    if st.button("🔍 Analyze Skills Now"):
        if name and current_skills:
            user_skills = [s.strip().capitalize() for s in current_skills.split(",") if s.strip()]
            required_skills = db.get_required_skills(selected_job)

            user_skills_lower = [s.lower() for s in user_skills]
            required_skills_lower = [s.lower() for s in required_skills]

            matched = [skill for skill in user_skills if skill.lower() in required_skills_lower]
            missing = [skill for skill in required_skills if skill.lower() not in user_skills_lower]

            matched_count = len(matched)
            total_required = len(required_skills)
            completion_percentage = (matched_count / total_required) * 100 if total_required else 0

            # Add progress bar
            st.progress(int(completion_percentage))

            st.success(f"Hi {name}, here's your skill report for **{selected_job}**")
            st.markdown(f"**✅ You already know:** {', '.join(matched) if matched else 'None'}")
            st.markdown(f"**❌ You still need to learn:** {', '.join(missing) if missing else 'None'}")

            st.session_state.update({
                "name": name,
                "selected_job": selected_job,
                "matched": matched,
                "missing": missing,
                "completion_percentage": completion_percentage
            })

# ------------------- TAB 2: Your Score -------------------
elif selected_tab == "📊 Your Score":
    if "completion_percentage" in st.session_state:
        score = int(st.session_state['completion_percentage'])
        st.markdown(f"### 🎯 Readiness Score for **{st.session_state['selected_job']}**")
        st.markdown(f"📈 Your current readiness is: **{score}%**")

        # Circle visualization
        fig, ax = plt.subplots(figsize=(3, 3), dpi=80)
        ax.set_xlim(-1.2, 1.2)
        ax.set_ylim(-1.2, 1.2)
        ax.set_xticks([])  # remove x-axis ticks
        ax.set_yticks([])  # remove y-axis ticks
        ax.add_artist(plt.Circle((0, 0), 1, color='lightgrey', edgecolor='white', lw=6))
        angle = 360 * (score / 100)
        wedge = Wedge((0, 0), 1, 0, angle, color='green', lw=0, alpha=0.7)
        ax.add_patch(wedge)
        ax.add_artist(plt.Circle((0, 0), 1, color='none', edgecolor='white', lw=4))
        ax.text(0, 0, f"{score}%", fontsize=20, color='white', ha='center', va='center', fontweight='bold')

        buf = BytesIO()
        plt.savefig(buf, format="png")
        buf.seek(0)
        st.image(buf)

        if score == 100:
            st.success("🎉 You are 100% ready for this job!")
        elif score >= 50:
            st.info("🟡 You are on track! Keep going.")
        else:
            st.warning("🔴 You need to improve your skills for this role.")
    else:
        st.warning("Please analyze your skills in the first tab.")

# ------------------- TAB 3: Resources -------------------
elif selected_tab == "📚 Resources":
    if "missing" in st.session_state and st.session_state["missing"]:
        st.markdown("### 📘 Recommended Learning Resources:")
        for skill in st.session_state["missing"]:
            link = recommender.get_resource(skill)
            if link:
                st.markdown(f"**📘 {skill}** - [Learn here]({link})")
            else:
                st.warning(f"No resource found for: **{skill}**")
    else:
        st.warning("No missing skills found. Please analyze first.")

# ------------------- PDF Report Button -------------------
if "matched" in st.session_state:
    if st.button("📄 Generate PDF Report"):
        report = ReportGenerator(st.session_state["name"])
        pdf_path = report.generate_pdf(
            st.session_state["selected_job"],
            st.session_state["matched"],
            st.session_state["missing"],
            st.session_state.get("recommended_resources", {})
        )
        with open(pdf_path, "rb") as f:
            pdf_bytes = f.read()
            st.download_button(
                label="⬇️ Download PDF Report",
                data=pdf_bytes,
                file_name=pdf_path.split("/")[-1],
                mime="application/pdf"
            )
