# 🖼️ Broken Image Automation Checker  
### ✅ Python | Selenium | Requests | PyTest | HTML Reporting

This automation project scans any website for **broken images**, missing image sources, invalid image URLs, and images that fail to load.  
It is built using a clean Selenium + PyTest framework and produces **professional CSV + HTML reports**.

This project demonstrates real-world QA automation skills used in UI testing, performance validation, SEO audits, and website quality assurance.

---

## ✅ Features

- ✅ Automatically extracts all `<img>` elements  
- ✅ Detects images returning **4xx/5xx** responses  
- ✅ Detects images with **empty or invalid src**  
- ✅ Detects **working** images (200 OK)  
- ✅ Generates **CSV report**  
- ✅ Generates **professional HTML report**  
- ✅ Supports command-line URL input (`--url=`)  
- ✅ Uses clean and modular Selenium + PyTest structure  
- ✅ Beginner friendly + resume ready  

---

## 📁 Project Structure

```
broken-image-automation-checker/
│── conftest.py
│── requirements.txt
│── README.md
│── drivers/
│    └── chromedriver.exe
│── reports/
│    ├── broken_images_report.csv
│    └── broken_images_report.html
│── tests/
│    └── test_broken_images.py
```

---

## ✅ Installation

### 1️⃣ Clone the project
```bash
git clone https://github.com/AyushiiDhiman/broken-image-automation-checker.git
cd broken-image-automation-checker
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Setup ChromeDriver  
Download ChromeDriver that matches your browser version and place it inside:

```
drivers/chromedriver.exe
```

---

## ✅ How to Run the Test

### ▶️ Run with default website
```bash
pytest -s
```

### ▶️ Run for ANY custom website
```bash
pytest -s --url=https://google.com
```

---

### 🌐 HTML Report
- ✅ Green → Working images  
- ✅ Red → Broken images  
- ✅ Yellow → Timeout / invalid src  

---

## ✅ Tech Stack

| Technology | Use |
|-----------|------|
| Python 3.x | Main scripting |
| Selenium WebDriver | Browser automation |
| Requests | HTTP status checking |
| PyTest | Test framework |
| Jinja2 | HTML report rendering |
| Pandas | CSV processing |

---

## ✅ Future Enhancements

- [ ] Screenshot comparison for damaged images  
- [ ] Multi-page crawling  
- [ ] Headless mode support  
- [ ] CI/CD integration with GitHub Actions  
- [ ] Detailed PDF report

---

**Developed an automated Broken Image Detection Framework using Python, Selenium, Requests, Pandas, and PyTest. Built a modular testing architecture supporting command-line URL injection. Implemented HTTP validation for all images and generated professional HTML/CSV reports. Demonstrated skills in UI testing, automation frameworks, and robust error handling.**

---

## ✅ Author

**Ayushi Dhiman**  
Automation & Testing Enthusiast  
📌 GitHub: https://github.com/AyushiiDhiman

If you find this useful, ⭐ the repository!

