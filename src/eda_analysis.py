from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# =========================
# PROJECT PATHS
# =========================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_PATH = PROJECT_ROOT / "data" / "netflix_titles_cleaned.csv"

OUTPUT_DIR = PROJECT_ROOT / "outputs"
CHARTS_DIR = OUTPUT_DIR / "charts"
REPORTS_DIR = OUTPUT_DIR / "reports"

CHARTS_DIR.mkdir(parents=True, exist_ok=True)
REPORTS_DIR.mkdir(parents=True, exist_ok=True)


# =========================
# LOAD DATA
# =========================

print("Loading dataset...")

df = pd.read_csv(DATA_PATH)

print(f"Dataset loaded successfully.")
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")


# Convert date_added
df["date_added"] = pd.to_datetime(
    df["date_added"],
    errors="coerce"
)


# =========================
# 1. CONTENT TYPE ANALYSIS
# =========================

content_type = (
    df["type"]
    .value_counts()
    .reset_index()
)

content_type.columns = ["type", "count"]

content_type["percentage"] = (
    content_type["count"] / len(df) * 100
).round(2)

content_type.to_csv(
    REPORTS_DIR / "content_type_summary.csv",
    index=False
)


# Chart
plt.figure(figsize=(8, 5))

sns.barplot(
    data=content_type,
    x="type",
    y="count"
)

plt.title("Netflix Content Type Distribution")
plt.xlabel("Content Type")
plt.ylabel("Number of Titles")
plt.tight_layout()

plt.savefig(
    CHARTS_DIR / "content_type_distribution.png",
    dpi=300
)

plt.close()


# =========================
# 2. RATING ANALYSIS
# =========================

rating_summary = (
    df["rating"]
    .value_counts()
    .reset_index()
)

rating_summary.columns = ["rating", "count"]

rating_summary.to_csv(
    REPORTS_DIR / "rating_summary.csv",
    index=False
)


plt.figure(figsize=(10, 6))

sns.barplot(
    data=rating_summary.head(10),
    x="count",
    y="rating"
)

plt.title("Top 10 Netflix Ratings")
plt.xlabel("Number of Titles")
plt.ylabel("Rating")
plt.tight_layout()

plt.savefig(
    CHARTS_DIR / "rating_distribution.png",
    dpi=300
)

plt.close()


# =========================
# 3. CONTENT ADDED BY YEAR
# =========================

yearly_content = (
    df.dropna(subset=["date_added"])
    .assign(
        added_year=lambda x: x["date_added"].dt.year
    )
    .groupby(["added_year", "type"])
    .size()
    .reset_index(name="count")
)

yearly_content.to_csv(
    REPORTS_DIR / "yearly_content_summary.csv",
    index=False
)


plt.figure(figsize=(12, 6))

sns.lineplot(
    data=yearly_content,
    x="added_year",
    y="count",
    hue="type",
    marker="o"
)

plt.title("Netflix Content Added by Year")
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.tight_layout()

plt.savefig(
    CHARTS_DIR / "content_added_by_year.png",
    dpi=300
)

plt.close()


# =========================
# 4. COUNTRY ANALYSIS
# =========================

country_df = df[
    df["country"].notna()
    & (df["country"] != "Not Specified")
].copy()

country_df["country"] = country_df["country"].str.split(",")

country_df = country_df.explode("country")

country_df["country"] = (
    country_df["country"]
    .str.strip()
)

country_summary = (
    country_df["country"]
    .value_counts()
    .reset_index()
)

country_summary.columns = ["country", "count"]

country_summary.to_csv(
    REPORTS_DIR / "country_summary.csv",
    index=False
)


plt.figure(figsize=(10, 7))

sns.barplot(
    data=country_summary.head(15),
    x="count",
    y="country"
)

plt.title("Top 15 Countries by Netflix Titles")
plt.xlabel("Number of Titles")
plt.ylabel("Country")
plt.tight_layout()

plt.savefig(
    CHARTS_DIR / "top_15_countries.png",
    dpi=300
)

plt.close()


# =========================
# 5. GENRE ANALYSIS
# =========================

genre_df = df[
    df["listed_in"].notna()
].copy()

genre_df["listed_in"] = genre_df["listed_in"].str.split(",")

genre_df = genre_df.explode("listed_in")

genre_df["listed_in"] = (
    genre_df["listed_in"]
    .str.strip()
)

genre_summary = (
    genre_df["listed_in"]
    .value_counts()
    .reset_index()
)

genre_summary.columns = ["genre", "count"]

genre_summary.to_csv(
    REPORTS_DIR / "genre_summary.csv",
    index=False
)


plt.figure(figsize=(10, 7))

sns.barplot(
    data=genre_summary.head(15),
    x="count",
    y="genre"
)

plt.title("Top 15 Netflix Genres")
plt.xlabel("Number of Titles")
plt.ylabel("Genre")
plt.tight_layout()

plt.savefig(
    CHARTS_DIR / "top_15_genres.png",
    dpi=300
)

plt.close()


# =========================
# 6. MOVIE DURATION ANALYSIS
# =========================

movies = df[
    df["type"] == "Movie"
].copy()

movies["duration_minutes"] = (
    movies["duration"]
    .astype(str)
    .str.extract(r"(\d+)")
    .astype(float)
)

movie_duration_summary = (
    movies["duration_minutes"]
    .describe()
    .reset_index()
)

movie_duration_summary.columns = [
    "statistic",
    "value"
]

movie_duration_summary.to_csv(
    REPORTS_DIR / "movie_duration_summary.csv",
    index=False
)


plt.figure(figsize=(10, 6))

sns.histplot(
    movies["duration_minutes"].dropna(),
    bins=30,
    kde=True
)

plt.title("Movie Duration Distribution")
plt.xlabel("Duration (minutes)")
plt.ylabel("Number of Movies")
plt.tight_layout()

plt.savefig(
    CHARTS_DIR / "movie_duration_distribution.png",
    dpi=300
)

plt.close()


# =========================
# 7. TV SHOW SEASONS
# =========================

tv_shows = df[
    df["type"] == "TV Show"
].copy()

tv_shows["seasons"] = (
    tv_shows["duration"]
    .astype(str)
    .str.extract(r"(\d+)")
    .astype(float)
)

tv_seasons_summary = (
    tv_shows["seasons"]
    .value_counts()
    .sort_index()
    .reset_index()
)

tv_seasons_summary.columns = [
    "seasons",
    "count"
]

tv_seasons_summary.to_csv(
    REPORTS_DIR / "tv_seasons_summary.csv",
    index=False
)


plt.figure(figsize=(10, 6))

sns.barplot(
    data=tv_seasons_summary,
    x="seasons",
    y="count"
)

plt.title("TV Shows by Number of Seasons")
plt.xlabel("Number of Seasons")
plt.ylabel("Number of TV Shows")
plt.tight_layout()

plt.savefig(
    CHARTS_DIR / "tv_show_seasons_distribution.png",
    dpi=300
)

plt.close()


# =========================
# 8. DATA QUALITY ANALYSIS
# =========================

missing_values = (
    df.isna()
    .sum()
    .reset_index()
)

missing_values.columns = [
    "column",
    "missing_count"
]

missing_values["missing_percentage"] = (
    missing_values["missing_count"]
    / len(df)
    * 100
).round(2)


data_quality = pd.DataFrame({
    "metric": [
        "Rows",
        "Columns",
        "Duplicate Rows",
        "Duplicate show_id",
        "Missing date_added",
        "Minimum release year",
        "Maximum release year"
    ],
    "value": [
        len(df),
        df.shape[1],
        df.duplicated().sum(),
        df["show_id"].duplicated().sum(),
        df["date_added"].isna().sum(),
        df["release_year"].min(),
        df["release_year"].max()
    ]
})

data_quality.to_csv(
    REPORTS_DIR / "data_quality_summary.csv",
    index=False
)


# =========================
# COMPLETION
# =========================

print()
print("=" * 50)
print("EDA ANALYSIS COMPLETED SUCCESSFULLY")
print("=" * 50)

print(f"Charts saved to: {CHARTS_DIR}")
print(f"Reports saved to: {REPORTS_DIR}")

print()
print("Generated charts:")
for file in sorted(CHARTS_DIR.glob("*.png")):
    print("-", file.name)

print()
print("Generated reports:")
for file in sorted(REPORTS_DIR.glob("*.csv")):
    print("-", file.name)