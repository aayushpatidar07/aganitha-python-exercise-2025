## 📘 2. **report.pdf** (Yeh PDF file hogi — form me upload karni hoti hai)

### ✅ Ready-to-Use Report (You can copy to Notepad first)

```markdown
# Aganitha - Python Take Home Exercise 2025

## 👋 Introduction
This take-home assignment involved writing a Python program that fetches PubMed research papers for a user-specified keyword, filters papers based on author affiliation, and saves the results in CSV format.

## 🧠 Objective
- Use PubMed API to fetch paper metadata
- Filter papers with at least one non-academic author
- Save valid entries to `filtered_output.csv`   '''




////

## ⚙️ Tools and Libraries
- Python 3.13
- `requests` – for HTTP requests
- `pandas` – for working with CSV and data filtering
- PubMed E-utilities API

## 🔍 Approach
1. Prompt user for keyword input
2. Fetch 20 paper IDs via PubMed API
3. Fetch XML metadata for those IDs
4. Extract titles and affiliations
5. Filter out papers where all affiliations are academic
6. Save valid paper titles and affiliations to CSV

## ✅ Sample Query
> Input: `machine learning in healthcare`

> Output File: `filtered_output.csv`
Output File: `filtered_output.csv

## 📌 Result
The resulting CSV contains only those research papers with at least one non-academic author, ensuring proper filtering.

## 🧑‍💻 Author
**Aayush Patidar**  
Email: patidaraayush.62@gmail.com  
Candidate ID: Naukri072025

