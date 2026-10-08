# SWYNEX Exploratory Data Analysis

## Project Overview

This project was completed as part of the **SWYNEX Data Science Internship – Task 2: Exploratory Data Analysis**.

The objective of this task is to analyze a prepared Netflix Movies and TV Shows dataset using statistical analysis and data visualization. The analysis focuses on content distribution, ratings, countries, genres, movie durations, TV show seasons, yearly content trends, and data quality.

## Dataset

The dataset contains information about Netflix Movies and TV Shows.

* Total records: 8,807
* Total features: 12
* Duplicate rows: 0
* Duplicate show IDs: 0
* Release year range: 1925–2021
* Missing `date_added` values: 98

### Dataset Columns

* `show_id`
* `type`
* `title`
* `director`
* `cast`
* `country`
* `date_added`
* `release_year`
* `rating`
* `duration`
* `listed_in`
* `description`

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Jupyter Notebook

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
```

## EDA Process

The analysis covers:

1. Dataset loading
2. Dataset structure inspection
3. Data type analysis
4. Missing-value analysis
5. Duplicate-value validation
6. Content type analysis
7. Rating distribution analysis
8. Yearly content addition analysis
9. Country-level analysis
10. Genre analysis
11. Movie duration analysis
12. TV show season analysis
13. Statistical summaries
14. Data visualization
15. Exporting analysis reports

## Key Findings

### 1. Content Type Distribution

The dataset contains:

* Movies: 6,131 (69.62%)
* TV Shows: 2,676 (30.38%)

Movies represent the larger share of the catalog. This distribution can be useful for content segmentation and recommendation analysis.

### 2. Rating Distribution

The most common ratings are:

* TV-MA: 3,207 titles
* TV-14: 2,160 titles

The distribution shows a significant concentration of mature and teenage-oriented content.

### 3. Content Addition Trend

The number of titles added increased substanti
