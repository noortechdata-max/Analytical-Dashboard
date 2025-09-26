import streamlit as st
import base64

# --- Page Config ---
st.set_page_config(page_title="My App", layout="wide")

# --- Encode local logo as base64 ---
with open("logo.png", "rb") as f:
    logo_bytes = f.read()
logo_base64 = base64.b64encode(logo_bytes).decode()

# --- Load CSV file for download ---
with open("skills_data.csv", "rb") as f:
    csv_bytes = f.read()

# --- Custom CSS ---
st.markdown("""
    <style>
    /* Header container responsive */
    .header-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: nowrap;
        width: 100%;
        margin-bottom: 20px;
    }
    @media (max-width: 768px) {
        .header-container {
            flex-direction: row;
            justify-content: space-between;
        }
    }
    h2 {
        color: black !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- Header: Logo + Download CSV Button ---
st.markdown(
    f"""
    <div class="header-container">
        <img src="data:image/png;base64,{logo_base64}" width="120" alt="Logo">
        <div>
            <a download="skills_data.csv" href="data:text/csv;base64,{base64.b64encode(csv_bytes).decode()}"
               style="text-decoration:none;">
                <button style="
                    background-color:#0065DA;
                    color:white;
                    border:none;
                    border-radius:20px;
                    height:28px;
                    width:128px;
                    font-family:Inter,sans-serif;
                    font-size:14px;
                    cursor:pointer;">
                    Download CSV
                </button>
            </a>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Hero Section ---
st.markdown("""
    <div style="background-color:#0065DA; width:100%; height:auto;
                padding:40px; color:white; box-sizing:border-box;">
        <div style="font-family: Inter, sans-serif; font-size: 20px; line-height: 1.5;">
            <h1 style="font-size:48px; font-weight:800; color:white; margin-bottom:20px;">
                Skills You Can Sell Online as a <br> Freelancer
            </h1>
            <p>
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

# --- Bottom Section: Centered Heading + CSV Button ---
st.markdown(
    "<h2 style='text-align:center; font-size:36px; font-weight:700; margin-top:60px; margin-bottom:20px; font-family:Inter, sans-serif;'>"
    "Download Skills CSV</h2>",
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div style="text-align:center;">
        <a download="skills_data.csv" href="data:text/csv;base64,{base64.b64encode(csv_bytes).decode()}"
           style="text-decoration:none;">
            <button style="
                background-color:#0065DA;
                color:white;
                border:none;
                border-radius:20px;
                height:36px;
                width:160px;
                font-family:Inter,sans-serif;
                font-size:16px;
                cursor:pointer;">
                Download CSV
            </button>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Footer ---
st.markdown("""
    <hr style="border:1px solid #0065DA; margin-top:40px;">
    <p style='text-align:center; color:#0065DA; font-size:16px; font-family:Inter, sans-serif; margin-top:10px;'>
        © 2025 Noor |
        <a href='https://www.linkedin.com/in/noor-fatima-18480a2a6/' target='_blank' style='color:#0065DA; text-decoration:none;'>LinkedIn</a> |
        <a href='https://github.com/noortechdata-max' target='_blank' style='color:#0065DA; text-decoration:none;'>GitHub</a>
    </p>
""", unsafe_allow_html=True)













