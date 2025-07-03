import streamlit as st
import pandas as pd
from scraper import full_scrape
from utils import download_link

st.set_page_config(page_title="Lead & Job Scraper", layout="wide")
st.title("🌐 Website Scraper")
st.sidebar.header("🔗 Scraper Configuration")
url = st.sidebar.text_input("Enter base company website", placeholder="https://example.com")
scrape_button = st.sidebar.button("Scrape Website")

if scrape_button:
    with st.spinner("Scraping contact details and job openings..."):
        leads_df, jobs_df = full_scrape(url)

    if not leads_df.empty:
        st.subheader("📞 Extracted Contact Information")
        st.dataframe(leads_df)
        leads_csv = leads_df.to_csv(index=False)
        st.markdown(download_link(leads_csv, "leads.csv", "📥 Download Leads CSV"), unsafe_allow_html=True)
    else:
        st.warning("No contact info found.")
    if not jobs_df.empty:
        st.subheader("💼 Extracted Job Openings")
        st.dataframe(jobs_df)
        jobs_csv = jobs_df.to_csv(index=False)
        st.markdown(download_link(jobs_csv, "job_openings.csv", "📥 Download Job Openings CSV"), unsafe_allow_html=True)
    else:
        st.warning("No job openings found.")
