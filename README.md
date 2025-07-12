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

## 📁 Folder Structure

```
browserstack_assignment/
├── README.md                # Complete project documentation
├── requirements.txt         # Python dependencies
├── .gitignore               # Optional (ignore venv, __pycache__)
├── browserstack_runner.py   # BrowserStack parallel testing code
├── main.py                  # Scraper + Translator + Word Frequency logic
├── screenshots/             # Folder for scraped article images
│   ├── image1.jpg
│   ├── image2.jpg
│   └── ...
├── browserstack.yaml        # Optional: used only if you use BStack SDK
└── venv/                    # Your virtual environment (should be .gitignored)
```




---

### 🚀 4. How to Run (Local + BrowserStack)

```md
## 🚀 How to Run

### ▶️ Run Locally

1. Install dependencies  
   `pip install -r requirements.txt`
2. Run main scraper logic  
   `python main.py`

### ☁️ Run on BrowserStack

1. Open `browserstack_runner.py`
2. Replace `USERNAME` and `ACCESS_KEY` with your own credentials (already done)
3. Run script  
   `python browserstack_runner.py`

You should see live session logs on [BrowserStack Automate Dashboard](https://automate.browserstack.com/projects/Default+Project/builds/MultiBrowser+Android+Build/1?tab=tests&testListView=spec&public_token=691b8f210d9931726adc0ba01201c598355c9d4ab52d79c0463e156dbd0d1627)

Dashboard Summary (https://automate.browserstack.com/projects/Default+Project/builds/MultiBrowser+Android+Build/1?public_token=691b8f210d9931726adc0ba01201c598355c9d4ab52d79c0463e156dbd0d1627)

---

## 🛠️ Tools & Technologies Used

- Python 3.x
- Selenium WebDriver
- BrowserStack Automate
- Google Translate API (or any free alternative)

---

## 📸 Screenshots

> 🔗 Screenshot of Build Running: [View on Google Drive](https://drive.google.com/drive/folders/1ittltRg_Cy81hZDesYt6jIKj4JUKQgHB?usp=sharing)


