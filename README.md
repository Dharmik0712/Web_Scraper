# 🌐 Lead & Job Web Scraper

An AI-powered Streamlit application that scrapes company websites to extract key lead contact information (emails, phone numbers) and open job postings. Built as part of the Caprae Capital AI-Readiness Pre-Screening Challenge.

---

## 🔗 Live Demo
**[Click here to try the deployed app](https://webscraper-vwbewfdkfzekz2htd7pfwb.streamlit.app/)**

---

## 🧠 Problem Statement
Caprae Capital empowers post-acquisition businesses through AI transformation. This tool helps automate lead generation by scraping and structuring contact details and job data from corporate websites in just one click.

---

## ✨ Features
- 🔍 Scrape contact pages (email, phone, source links)
- 💼 Extract structured job postings (title, tech stack, experience)
- 📥 Download results as CSV (for CRM or sales use)
- 🧠 Simple, intuitive UI with real-time results

---

## ⚙️ How It Works
1. Enter a company's base website URL
2. Click **"Scrape Website"**
3. App scrapes the main site and important subpages (Contact, About, Careers, etc.)
4. Data is presented in tables and can be downloaded instantly

---

## 🛠️ Tech Stack
- **Frontend**: Streamlit
- **Backend**: Python, BeautifulSoup, Requests
- **Other Libraries**: `pandas`, `fake_useragent`, `re`, `base64`

---

## 📂 Folder Structure
```
├── app.py              # Streamlit frontend logic
├── scraper.py          # Core scraping logic
├── utils.py            # Helper functions (regex, download)
├── requirements.txt    # Python dependencies
```

---

## 🚀 Getting Started (Local Setup)
```bash
# 1. Clone the repository
git clone https://github.com/Dharmik0712/Web_Scraper.git
cd Web_Scraper

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the Streamlit app
streamlit run app.py
```

---

## 🧪 Example Use Cases
- Sales prospecting: Find key contact points from a company site
- Talent intelligence: Analyze job trends and hiring signals
- BD Scouting: Combine open roles + tech stack for partnership targeting

---

## 🧾 License
MIT License — feel free to fork and build upon it.

---

## 🙋‍♂️ Author
**Dharmik Sompura**  
For Caprae Capital’s AI-Readiness Internship Challenge  
[GitHub Profile](https://github.com/Dharmik0712)

---

## 🧩 Future Improvements
- LinkedIn and social scraping
- CAPTCHA bypass
- CRM integrations (Salesforce/Hubspot)
- Email validity checks

---

> 💬 *“Don’t just extract data—extract insight.”*
