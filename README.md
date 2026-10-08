# SWYNEX Exploratory Data Analysis

## Project Overview

This project was completed as part of the SWYNEX Data Science Internship, Task 2: Exploratory Data Analysis.

The objective of this task is to analyze a prepared Netflix Movies and TV Shows dataset using statistical analysis and visualizations. The analysis focuses on understanding content distribution, ratings, countries, genres, movie durations, TV show seasons, yearly content trends, and overall data quality.

## Dataset

The dataset contains Netflix Movies and TV Shows information.

- Total records: 8,807
- Total features: 12
- Duplicate rows: 0
- Duplicate show IDs: 0
- Release year range: 1925–2021
- Missing date_added values: 98

### Dataset Columns

- show_id
- type
- title
- director
- cast
- country
- date_added
- release_year
- rating
- duration
- listed_in
- description

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

## Project Structure

```text
SWYNEX-Exploratory-Data-Analysis/
├── data/
│   └── netflix_titles_cleaned.csv
├── notebooks/
│   └── eda_analysis.ipynb
├── outputs/
│   ├── charts/
│   │   ├── content_added_by_year.png
│   │   ├── content_type_distribution.png
│   │   ├── movie_duration_distribution.png
│   │   ├── rating_distribution.png
│   │   ├── top_15_countries.png
│   │   ├── top_15_genres.png
│   │   └── tv_show_seasons_distribution.png
│   └── reports/
│       ├── content_type_summary.csv
│       ├── country_summary.csv
│       ├── data_quality_summary.csv
│       ├── genre_summary.csv
│       ├── movie_duration_summary.csv
│       ├── rating_summary.csv
│       ├── tv_seasons_summary.csv
│       └── yearly_content_summary.csv
├── src/
│   └── eda_analysis.py
├── .gitignore
├── requirements.txt
└── README.md