import streamlit as st
import os

# --- Page Config ---
st.set_page_config(page_title="My App", layout="wide")  # full width

# --- Custom CSS ---
st.markdown(
    """
    <style>
    .header-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: nowrap;   /* ✅ same row desktop + mobile */
        margin-bottom: 20px;
        width: 100%;
    }
    .header-container img {
        width: 120px;   /* ✅ fixed logo size */
        height: auto;
    }
    .download-btn {
        background-color: #0065DA;
        color: white;
        border: none;
        border-radius: 20px;
        font-family: Inter, sans-serif;
        font-size: 14px;
        height: 28px;
        width: 128px;
        cursor: pointer;
    }
    .download-btn:hover {
        background-color: #0050b3;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Logo + CSV Button Layout (HTML only) ---
logo_path = "logo.png"       # make sure file exists in same folder
csv_path = "skills_data.csv" # make sure file exists in same folder

st.markdown(
    f"""
    <div class="header-container">
        <img src="{logo_path}" alt="Logo">
        <a href="{csv_path}" download>
            <button class="download-btn">Download CSV</button>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Rectangle with hero layout ---
st.markdown(
    """
    <div style="background-color:#0065DA; width:100%; height:auto; 
                padding:40px; color:white; box-sizing:border-box;">
        <div style="font-family: Inter, sans-serif; font-size: 20px; line-height: 1.5;">
            <h1 style="font-size:48px; font-weight:800; margin-bottom:20px;">
                Skills You Can Sell Online as a <br> Freelancer
            </h1>
            <p style="word-wrap: break-word;">
                Freelancing today runs on practical digital skills, not just degrees. 
                That's why I pulled together a list of 108+ skills you can learn and 
                turn into real income — from design and data analysis to coding, 
                marketing, and AI. These are skills you can pick up and start selling 
                on Fiverr, Upwork, and LinkedIn, moving directly from learning to earning.
                <br><br>
                Over the past five years, I have tracked which skills stay in demand, 
                which fade out, and which are starting to rise. Each one comes with 
                curated resources so you don't waste time figuring out where to start. 
                The research is powered by insights from LinkedIn, Fiverr, and Upwork, 
                and sharpened with tech. The result is a clear, data-backed guide to focus on 
                skills that actually pay.
            </p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# --- Top Paid Skills Heading ---
st.markdown(
    "<h2 style='font-size:36px; font-weight:700; color:#0065DA; "
    "margin-top:40px; margin-bottom:20px; font-family:Inter, sans-serif;'>"
    "Top Paid Skills</h2>", 
    unsafe_allow_html=True
)

# --- Dashboard Table ---
table_html = """
<table style="width:100%; border-collapse: collapse; font-family: Inter, sans-serif; font-size: 16px; margin-top: 10px;">
    <tr>
        <th style="background-color:#0065DA; color:white; padding:12px; text-align:left;">Skill</th>
        <th style="background-color:#0065DA; color:white; padding:12px; text-align:left;">Avg Monthly (USD)</th>
        <th style="background-color:#0065DA; color:white; padding:12px; text-align:left;">Demand</th>
    </tr>
    <tr><td>AI & Machine Learning</td><td>$6500</td><td>High</td></tr>
    <tr><td>Data Science</td><td>$6000</td><td>High</td></tr>
    <tr><td>Cloud Computing</td><td>$5800</td><td>High</td></tr>
    <tr><td>Cybersecurity</td><td>$5500</td><td>High</td></tr>
    <tr><td>Blockchain Development</td><td>$5200</td><td>Medium</td></tr>
</table>
"""
st.markdown(table_html, unsafe_allow_html=True)

# --- Top In-Demand Skills Heading ---
st.markdown(
    "<h2 style='font-size:36px; font-weight:700; color:#0065DA; "
    "margin-top:40px; margin-bottom:20px; font-family:Inter, sans-serif;'>"
    "Top In-Demand Skills</h2>", 
    unsafe_allow_html=True
)

# --- Dashboard Table ---
table_html_demand = """
<table style="width:100%; border-collapse: collapse; font-family: Inter, sans-serif; font-size: 16px; margin-top: 10px;">
    <tr>
        <th style="background-color:#0065DA; color:white; padding:12px; text-align:left;">Skill</th>
        <th style="background-color:#0065DA; color:white; padding:12px; text-align:left;">Demand Level</th>
        <th style="background-color:#0065DA; color:white; padding:12px; text-align:left;">Avg Monthly (USD)</th>
    </tr>
    <tr><td>Generative AI</td><td>Very High</td><td>$6200</td></tr>
    <tr><td>Data Analytics</td><td>High</td><td>$5000</td></tr>
    <tr><td>Cloud Computing</td><td>High</td><td>$5800</td></tr>
    <tr><td>Cybersecurity</td><td>High</td><td>$5500</td></tr>
    <tr><td>UI/UX Design</td><td>Medium</td><td>$4000</td></tr>
</table>
"""
st.markdown(table_html_demand, unsafe_allow_html=True)




