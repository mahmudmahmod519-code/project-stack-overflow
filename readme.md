$$ StackOverflow Questions Scraper$$


![alt](20251202_2346_Web-Scraper-Logo_simple_compose_01kbggdcxneqx90rn9vv7epwky.png)

A Python script that scrapes the latest questions from the StackOverflow Questions page and extracts useful information such as titles, descriptions, tags, authors, views, votes, and timestamps.  
The results are saved automatically as **Excel (.xlsx)** and **CSV (.csv)** files.

---

## Description

This project uses **BeautifulSoup**, **Requests**, and **Pandas** to collect structured data from:

https://stackoverflow.com/questions  

The script extracts the following for each question:

- Question title  
- Short description/excerpt  
- Tags (tools)  
- Username of the author  
- Time posted  
- Number of views  
- Number of votes  
- Number of times the question was asked  
- Direct question link  

All data is stored in a clean table and exported for further analysis.

---

## Tech Stack

- ![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)
- ![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup4-WebScraping-green)
- ![Requests](https://img.shields.io/badge/Requests-HTTP-orange)
- ![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-blueviolet)
- ![License](https://img.shields.io/badge/License-MIT-yellow)

---

## Features

- Scrapes all questions listed on the StackOverflow questions homepage  
- Extracts detailed information for each question  
- Saves results in both Excel and CSV formats  
- Easy to extend with additional fields or pagination  
- Beginner-friendly and clean code  
 
---

## Installation

```bash
   git clone https://github.com/mahmudmahmod519-code/project-stack-overflow.git
   cd project-stack-overflow
   pip install -r requirements.txt
   python fetch_questions.py
```

## Usage
After running the script, you will find two new files in the project folder:

- questions.xlsx

- questions.csv

These contain the collected questions and all extracted data in table format.

## Future Improvements 

- Add pagination to scrape multiple question pages

- Improve error handling

- Store data in a database (SQLite, MongoDB, etc.)

- Create a simple GUI or API endpoint

- Add filtering or search features

## Additional Notes

- Make sure your internet connection is active during scraping

- StackOverflow may change its HTML structure in the future

- If something breaks, updating selectors in the code will fix it

<br>


