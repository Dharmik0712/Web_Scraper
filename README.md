# 🌐 Website Scraper

This is a web-based scraper built with **Streamlit** that extracts:

* 📞 Contact information (emails & phone numbers)
* 💼 Job openings (job title, description, experience, and tech stack)

from a given company website.

Live App: [https://webscraper-vwbewfdkfzekz2htd7pfwb.streamlit.app/](https://webscraper-vwbewfdkfzekz2htd7pfwb.streamlit.app/)

---

## 🚀 Features

* ✏️ Simple UI to enter company website URLs
* 🔗 Automatically finds relevant internal links (contact, careers, etc.)
* 📣 Extracts emails, phone numbers, and page URLs from the website
* 🔮 Detects and extracts job-related content using keyword heuristics
* 📚 Identifies job title, experience, and tech stack (e.g., Python, React)
* 📄 Download extracted contact and job data as CSV files
* ⏳ Shows loading spinner while scraping is in progress
* ⚠ Displays warnings if no data is found
* 🌐 Completely client-side interaction with no data logging

---

## 🛠 Tech Stack

* **Frontend**: Streamlit
* **Backend**: Python, BeautifulSoup, Requests
* **Libraries**: pandas, fake\_useragent

---

## 📦 Installation

1. **Clone the repo**

```bash
git clone https://github.com/your-username/web-scraper.git
cd web-scraper
```

2. **Create a virtual environment (optional but recommended)**

```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the App Locally

```bash
streamlit run app.py
```

Then open the provided URL in your browser (usually `http://localhost:8501`).

---

## 🗉 File Structure

```
.
├── app.py            # Main Streamlit app
├── scraper.py        # Contains web scraping logic
├── utils.py          # Utility functions (email/phone extraction, download link)
├── requirements.txt  # Dependencies
└── README.md         # This file
```

---

## 📄 Output

* Leads data (`leads.csv`)
* Job openings (`job_openings.csv`)

Each can be downloaded directly through the web app.

---

## ⚠️ Disclaimer

This tool is intended for educational or internal company use only. Always ensure scraping is allowed on the target website as per their **robots.txt** and **terms of service**.

---

## ✨ Credits

Developed by Dharmik Sompura \[[dharmiksompura1212@gmail.com](mailto:dharmiksompura1212@gmail.com)].
