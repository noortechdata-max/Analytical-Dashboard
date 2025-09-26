import streamlit as st
import base64

# --- Page Config ---
st.set_page_config(page_title="My App", layout="wide")

# --- Encode local logo as base64 ---
with open("logo.png", "rb") as f:
    logo_bytes = f.read()
logo_base64 = base64.b64encode(logo_bytes).decode()

# --- Load CSV File ---
with open("skills_data.csv", "rb") as f:
    csv_data = f.read()

# --- Custom CSS ---
st.markdown("""
    <style>
    .stDownloadButton button {
        background-color: #0065DA !important;
        color: white !important;
        border: none !important;
        border-radius: 20px !important;
        font-family: Inter, sans-serif !important;
        font-size: 14px !important;
        height: 28px !important;
        width: 128px !important;
        cursor: pointer !important;
    }
    .stDownloadButton button:hover {
        background-color: #0050b3 !important;
    }
    .header-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: nowrap;
        width: 100%;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- Header: Logo + Download CSV Button ---
col1, col2 = st.columns([6, 1])
with col1:
    st.markdown(f"<img src='data:image/png;base64,{logo_base64}' width='120' alt='Logo'>", unsafe_allow_html=True)
with col2:
    st.download_button(
        label="Download CSV",
        data=csv_data,
        file_name="skills_data.csv",
        mime="text/csv",
        key="header_csv",
    )

# --- Hero Section with original white heading ---
st.markdown("""
    <div style="background-color:#0065DA; width:100%; height:auto;
                padding:40px; color:white; box-sizing:border-box;">
        <div style="font-family: Inter, sans-serif; font-size: 20px; line-height: 1.5;">
            <h1 style="font-size:48px; font-weight:800; color:white; margin-bottom:20px;">
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
    <div style="width:100%; margin-top:60px; margin-bottom:20px; text-align:center;">
        <h2 style="font-family:Inter, sans-serif; color:black; font-size:36px; font-weight:700; margin-bottom:20px;">
            Download Skills CSV
        </h2>
    </div>
""", unsafe_allow_html=True)

st.download_button(
    label="Download CSV",
    data=csv_data,
    file_name="skills_data.csv",
    mime="text/csv",
    key="footer_csv",
)

# --- Footer ---
st.markdown("""
    <hr style="border:1px solid #0065DA;">
    <p style='text-align:center; color:#0065DA; font-size:16px; font-family:Inter, sans-serif; margin-top:10px;'>
        © 2025 Noor |
        <a href='https://www.linkedin.com/in/noor-fatima-18480a2a6/' target='_blank' style='color:#0065DA; text-decoration:none;'>LinkedIn</a> |
        <a href='https://github.com/noortechdata-max' target='_blank' style='color:#0065DA; text-decoration:none;'>GitHub</a>
    </p>
""", unsafe_allow_html=True)


      
                




















