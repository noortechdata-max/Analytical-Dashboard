import streamlit as st
import base64

# --- Page Config ---
st.set_page_config(page_title="My App", layout="wide")

# --- Encode local logo as base64 ---
with open("logo.png", "rb") as f:
    logo_bytes = f.read()
logo_base64 = base64.b64encode(logo_bytes).decode()

# --- Encode hero image as base64 ---
hero_image_path = "hero_image.png"  # Replace with your image path
with open(hero_image_path, "rb") as f:
    hero_bytes = f.read()
hero_base64 = base64.b64encode(hero_bytes).decode()

# --- Custom CSS ---
st.markdown("""
    <style>
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
    .header-container {
        display: flex;
        justify-content: space-between;
        align-items: center; /* vertical align logo & button */
        flex-wrap: nowrap;   /* prevents stacking on mobile */
        width: 100%;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- Header: Logo + Download CSV Button ---
st.markdown(f"""
    <div class="header-container">
        <img src="data:image/png;base64,{logo_base64}" width="120" alt="Logo">
        <a href="skills_data.csv" download="skills_data.csv">
            <button class="download-btn">Download CSV</button>
        </a>
    </div>
""", unsafe_allow_html=True)

# --- Hero Section: Text Left + Image Right ---
st.markdown(f"""
<div style="
    display: flex; 
    flex-wrap: wrap; 
    align-items: center; 
    justify-content: space-between; 
    background-color:#0065DA; 
    padding:40px; 
    box-sizing:border-box;
">
    <!-- Text Column -->
    <div style="
        flex: 1 1 300px; 
        margin-right:20px; 
        color:white; 
        font-family:Inter, sans-serif;
        min-width: 280px;
    ">
        <h1 style="font-size:48px; font-weight:800; margin-bottom:20px;">
            Skills You Can Sell Online as a <br> Freelancer
        </h1>
        <p style="font-size:20px; line-height:1.5;">
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

    <!-- Image Column -->
    <div style="
        flex: 1 1 300px; 
        min-width: 280px; 
        text-align:center;
        margin-top:20px;
    ">
        <img src="data:image/png;base64,{hero_base64}" style="max-width:100%; height:auto; border-radius:10px;">
    </div>
</div>
""", unsafe_allow_html=True)


    <!-- Image Column -->
    <div style="flex:1; min-width:300px; text-align:right;">
        <img src="data:image/png;base64,{hero_base64}" style="max-width:100%; height:auto; border-radius:10px;">
    </div>
</div>
""", unsafe_allow_html=True)

# --- Top Paid Skills Heading (black) ---
st.markdown(
    "<h2 style='font-size:36px; font-weight:700; color:black; "
    "margin-top:40px; margin-bottom:20px; font-family:Inter, sans-serif;'>"
    "Top Paid Skills</h2>", 
    unsafe_allow_html=True
)

# --- Dashboard Table: Top Paid Skills ---
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

# --- Top In-Demand Skills Heading (black) ---
st.markdown(
    "<h2 style='font-size:36px; font-weight:700; color:black; "
    "margin-top:40px; margin-bottom:20px; font-family:Inter, sans-serif;'>"
    "Top In-Demand Skills</h2>", 
    unsafe_allow_html=True
)

# --- Dashboard Table: Top In-Demand Skills ---
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

# --- Bottom Section: Centered Heading + CSV Button (heading black) ---
st.markdown("""
    <div style="width:100%; margin-top:60px; margin-bottom:60px; text-align:center;">
        <h2 style="font-family:Inter, sans-serif; color:black; font-size:36px; font-weight:700; margin-bottom:20px;">
            Download Skills CSV
        </h2>
        <a href="skills_data.csv" download="skills_data.csv">
            <button style="
                background-color:#0065DA; 
                color:white; 
                border:none; 
                border-radius:20px; 
                height:28px; 
                width:128px; 
                font-family:Inter,sans-serif; 
                font-size:14px;
                cursor:pointer;
            ">Download CSV</button>
        </a>
    </div>
""", unsafe_allow_html=True)

# --- Footer ---
st.markdown("""
    <hr style="border:1px solid #0065DA;">
    <p style='text-align:center; color:#0065DA; font-size:16px; font-family:Inter, sans-serif; margin-top:10px;'>
        © 2025 Noor | 
        <a href='https://www.linkedin.com/in/noor-fatima-18480a2a6/' target='_blank' style='color:#0065DA; text-decoration:none;'>LinkedIn</a> | 
        <a href='https://github.com/noortechdata-max' target='_blank' style='color:#0065DA; text-decoration:none;'>GitHub</a>
    </p>
""", unsafe_allow_html=True)

      
                


















