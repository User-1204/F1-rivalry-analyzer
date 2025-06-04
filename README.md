# 🏎️ F1 Head-to-Head Analyzer

**Author:** Sakshi Makwana

**Course Project:** CS50: Introduction to Python

---

## 📌 Overview
F1 Head-to-Head Analyzer is a Python-based command-line application that lets you compare two Formula 1 drivers across multiple seasons using real-time data from the Ergast Developer API.

This tool fetches race results and standings, computes key performance metrics (wins, podiums, DNFs, etc.), and presents both tabular and visual summaries to help users draw insightful comparisons between drivers. It's built as part of an academic project for the CS50 Python course and demonstrates proficiency in API usage, data analysis, and user-friendly CLI interaction.

Whether you're an F1 fan, a data science learner, or simply curious about sports analytics, this tool offers a meaningful and interactive experience.

🔍 Built using:

* **Python** for scripting
* **Pandas** for data processing
* **Matplotlib** for visualization
* **PrettyTable** for formatted terminal output
* **Pytest** for testing

---

## ✨ Features

### Real-Time Data

* Retrieves driver standings and race results from Ergast API
* Handles multiple seasons for a historical view

### Performance Metrics

* Calculates:
  * Wins
  * Podium finishes
  * Pole positions
  * DNFs (Did Not Finish)

### Visual + Tabular Output

* Pretty comparison table using `PrettyTable`
* Line chart of points over time using `Matplotlib`

### Robust Input Handling

* Validates driver IDs and year ranges
* Displays errors clearly if data is not available

---

## 📂 File Structure

```
f1-analyzer/
│
├── main.py             # Main script for execution
├── api.py              # Functions to fetch API data
├── analysis.py         # Summarizes performance stats
├── plot.py             # Points line chart generation
├── test_project.py     # Unit test for stats module
├── requirements.txt    # Dependency list
└── README.md           # Project documentation
```

---

## ⚙️ Installation

1. Clone the repository
2. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run

```bash
python main.py
```

### 💬 User Inputs

* Driver 1 ID (e.g., `hamilton`)
* Driver 2 ID (e.g., `max_verstappen`)
* Start year (e.g., `2015`)
* End year (e.g., `2023`)

The app will:

1. Fetch data 
2. Calculate stats 
3. Display a head-to-head table 
4. Plot seasonal points line graph 

---

## 🧪 Testing

Run unit tests for the stats analysis using:

```bash
pytest test_project.py
```

**Pytest Output Example:**
![Pytest Output](https://github.com/user-attachments/assets/8dd5a8d4-91d5-41ce-9d18-cc1c65119974)

---

## 📷 Screenshots

### ✅ Output:

* Terminal table and points comparison graph

![Proper Output](https://github.com/user-attachments/assets/b348e903-2fd7-4087-804d-adc5ff95609c)

---

### 📉 Line Chart Visualization:

* Side-by-side driver points comparison over seasons

![Line Chart](https://github.com/user-attachments/assets/62a253d5-61ac-49e1-b961-c099b92e8c19)

---

### ⚠️ Error Handling:

* Gracefully handles invalid driver IDs or empty data

![Error Output](https://github.com/user-attachments/assets/8526ef82-73e8-4b97-9dc1-3251ee4a4e7c)

---

## 🛠️ Future Enhancements

* Support for comparing **3+ drivers**
* Add **constructor-level** (team) stats
* Export results as **CSV or PDF**
* Build an interactive **web interface**
* Predict future performance using **ML models**

## 🙏 Acknowledgements

Special thanks to the CS50 teaching staff and the open Ergast F1 API community for providing the resources and support that made this project possible.
