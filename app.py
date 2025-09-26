import streamlit as st
import base64

# --- Page Config ---
st.set_page_config(page_title="My App", layout="wide")

# --- Load Logo (convert to base64 so HTML <img> works everywhere) ---
def get_base64_image(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

logo_base64 = get_base64_image("logo.png")   # apni logo image ka path do

# --- Load CSV file for download ---
with open("skills_data.csv", "rb") as f:
    csv_bytes = f.read()

# --- Custom CSS ---
st.markdown(
    """
    <style>
        /* Header Flexbox */
        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            width: 100%;
            margin-bottom: 30px;
        }
        .header img {
            height: 50px;
        }
        /* Center Section */
        .centered {
            text-align: center;
            margin-top: 50px;
        }
        h2 {
            color: black !important;
        }
        /* Footer */
        .footer {
            margin-top: 80px;
            padding: 20px;
            text-align: center;
            font-size: 14px;
        }
        .footer a {
            color: #0065DA;
            text-decoration: none;
            margin: 0 10px;
        }
        .footer a:hover {
            text-decoration: underline;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# --- HEADER SECTION (Logo + Button in same line) ---
col1, col2 = st.columns([1, 0.25])
with col1:
    st.markdown(
        f"""
        <div class="header">
            <img src="data:image/png;base64,{logo_base64}" alt="Logo">
        </div>
        """,
        unsafe_allow_html=True
    )
with col2:
    st.download_button(
        label="Download CSV",
        data=csv_bytes,
        file_name="skills_data.csv",
        mime="text/csv",
        key="header-btn"
    )

# --- HERO SECTION ---
st.markdown(
    """
    <h2 class="centered">Welcome to My Skills App</h2>
    <p style="text-align:center; max-width: 600px; margin: auto;">
        This is a hero section with logo and CSV download option.<br>
        You can explore, analyze, and download the dataset easily.
    </p>
    """,
    unsafe_allow_html=True
)

# --- SECOND DOWNLOAD SECTION (Heading + Centered Button) ---
st.markdown('<div class="centered"><h2>Download the CSV File</h2></div>', unsafe_allow_html=True)

st.markdown('<div class="centered">', unsafe_allow_html=True)
st.download_button(
    label="Download CSV",
    data=csv_bytes,
    file_name="skills_data.csv",
    mime="text/csv",
    key="bottom-btn"
)
st.markdown('</div>', unsafe_allow_html=True)

# --- FOOTER SECTION ---
st.markdown(
    """
    <div class="footer">
        <p>Connect with me:</p>
        <a href="https://www.linkedin.com/in/noor-fatima-18480a2a6/" target="_blank">LinkedIn</a> |
        <a href="https://github.com/noortechdata-max" target="_blank">GitHub</a>
    </div>
    """,
    unsafe_allow_html=True
)












