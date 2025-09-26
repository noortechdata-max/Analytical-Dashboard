import streamlit as st
import base64

# --- Page Config ---
st.set_page_config(page_title="My App", layout="wide")

# --- Encode local logo as base64 ---
with open("logo.png", "rb") as f:
    logo_bytes = f.read()
logo_base64 = base64.b64encode(logo_bytes).decode()

# --- Read your real CSV file ---
with open("skills_data.csv", "rb") as f:
    csv_file = f.read()

# --- Custom CSS ---
st.markdown("""
    <style>
    .stDownloadButton>button {
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
    .stDownloadButton>button:hover {
        background-color: #0050b3;
    }
    .center-btn>button {
        background-color:#0065DA !important;
        color:white !important;
        border:none !important;
        border-radius:20px !important;
        height:36px !important;
        width:160px !important;
        font-family:Inter,sans-serif !important;
        font-size:16px !important;
        cursor:pointer !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- Header: Logo + Download CSV Button ---
col1, col2 = st.columns([1, 5])
with col1:
    st.markdown(f'<img src="data:image/png;base64,{logo_base64}" width="120" alt="Logo">', unsafe_allow_html=True)
with col2:
    st.download_button(
        label="Download CSV",
        data=csv_file,
        file_name="skills_data.csv",
        mime="text/csv",
        key="header_csv"
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
                Freelancing today runs on practical digital skills, not just degrees...
            </p>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- Bottom Section: Centered Heading + CSV Button ---
st.markdown("""
    <div style="width:100%; margin-top:60px; margin-bottom:20px; text-align:center;">
        <h2 style="font-family:Inter, sans-serif; color:black; font-size:36px; font-weight:700; margin-bottom:20px;">
            Download Skills CSV
        </h2>
    </div>
""", unsafe_allow_html=True)

# Centered Button
st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
st.download_button(
    label="Download CSV",
    data=csv_file,
    file_name="skills_data.csv",
    mime="text/csv",
    key="bottom_csv"
)
st.markdown("</div>", unsafe_allow_html=True)

# --- Footer ---
st.markdown("""
    <hr style="border:1px solid #0065DA;">
    <p style='text-align:center; color:#0065DA; font-size:16px; font-family:Inter, sans-serif; margin-top:10px;'>
        © 2025 Noor |
        <a href='https://www.linkedin.com/in/noor-fatima-18480a2a6/' target='_blank' style='color:#0065DA; text-decoration:none;'>LinkedIn</a> |
        <a href='https://github.com/noortechdata-max' target='_blank' style='color:#0065DA; text-decoration:none;'>GitHub</a>
    </p>
""", unsafe_allow_html=True)



      
                






















