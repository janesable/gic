# Genome Inversions Calculator 🧬

This is a Python/Flask web application for calculating the **minimum number of inversions** between rearranged chromosomes of different species.  
Inspired by the previously available GRIMM tool  
(*Tesler, G. GRIMM: Genome Rearrangements Web Server. Bioinformatics, 2002, 18, 492–493*).

---

## 🚀 How to run locally

#### 1. Clone the repository

```bash
git clone https://github.com/janesable/gic.git
cd gic
```

#### 2. Install dependencies

```bash
pip install -r requirements.txt
```

#### 3. Start the application

```bash
python app.py
```

#### 4. Open in your browser

[http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 💻 How to use it

#### 1. Enter the names and sequences of syntenic blocks (e.g., `1 -3 2 5 4`).  
Negative values indicate reversed orientation of syntenic blocks.

#### 2. Click **Count**.

#### 3. The app will display all inversion steps and the **minimum number of rearrangements** required.

#### 4. You can add or remove genomes using the buttons, if you want to compare more than two species.

---

## 📁 Project structure

```bash
genomic-inversion-calculator/
├── app.py                  # Flask backend
├── templates/
│   └── index.html          # Web interface
├── static/
│   └── style.css           # CSS styles
├── requirements.txt        # List of dependencies
└── README_EN.md            # This file
```

---

## 🧠 About the project

Lovingly developed ❤️ for analyzing genome structural rearrangements  
(in my case, in malaria mosquitoes).

If you use this tool in your research or publication — a citation or mention would be deeply appreciated 😌

---

## 📬 Feedback

Found a bug? Want to suggest a feature?  
Reach out on Telegram: [@janesable](https://t.me/janesable)  
Or be a grown-up and email me: **jane.sable.me@gmail.com**
