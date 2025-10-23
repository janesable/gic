# Genome Inversions Calculator 🧬

Genome Inversions Calculator is a Python/Flask web application designed to estimate the minimum number of inversions required to transform one permutation of syntenic blocks into another within a single chromosome. It is inspired by the previously available GRIMM (TEsler, G. GRIMM: Genome Rearrangements Web Server. Bioinformatics 2002, 18, 492–493). Unlike the original GRIMM tool (Tesler, 2002), which implements the full Hunnichall–Pevzner algorithm and supports various types of rearrangements (inversions, translocations, fusions, splits), GIC is limited to analysing intrachromosomal inversions. The programme is based on a set of greedy algorithms, which simplifies calculations and provides an intuitive interface. This makes the tool convenient for researchers who do not have training in bioinformatics but work with the results of physical mapping, sequencing, or cytogenetic studies. The programme does not require the installation of additional software, other than that in which the code is implemented, does not use complex graph models, and produces a clear visual result reflecting the sequence of chromosome order transformations. As a result, GIC can be used to demonstrate the logic of chromosomal rearrangements, analyse the evolution of individual chromosomes, and conduct comparative studies of closely related species.

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
_______________________________________________________________
## License

This project, *Genome Inversions Calculator (GIC)*, is licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).  
Rightsholder: Tomsk State University  
Original author: Evgeniya Soboleva

See the [LICENSE](./LICENSE) and [NOTICE](./NOTICE) files for more details.

Please cite the project if used in academic or research contexts.

