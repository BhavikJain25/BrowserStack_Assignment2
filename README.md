# BrowserStack_Assignment2

# 🌐 BrowserStack Automation Assignment – El País Web Scraper

This project is created as part of the **BrowserStack Round 2 Technical Assignment**. It demonstrates a combination of **web scraping**, **translation API integration**, **text processing**, and **cross-browser test automation** using **Selenium with Python**.

---

## ✅ Project Highlights

- Scrapes the first **5 articles** from the [El País - Opinion Section](https://elpais.com/opinion/)
- Extracts article **titles**, **content**, and **cover images**
- Translates Spanish titles to English using a **translation API**
- Analyzes **repeated words** across translated titles
- Executes the entire workflow across **5 browsers in parallel** using **BrowserStack Automate**

---

## 🗂️ Folder Structure

'''browserstack_assignment/
├── README.md # Complete project documentation
├── requirements.txt # Python dependencies
├── .gitignore # Ignore venv, pycache, etc.
├── browserstack_runner.py # Parallel test file using BrowserStack
├── main.py # Scraper + Translator + Word Frequency logic
├── screenshots/ # Folder for scraped article images
│ ├── image1.jpg
│ ├── image2.jpg
│ └── ...
├── browserstack.yaml # Optional: For BrowserStack CLI SDK
└── venv/ # Your virtual environment (should be .gitignored)'''
