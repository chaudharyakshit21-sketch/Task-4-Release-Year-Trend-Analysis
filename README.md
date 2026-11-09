# Task 4 (Medium) - Trend Analysis by Release Year
**Auspify Technologies - Data Analysis Using Python Internship** | Intern: Akshit Kumar

**Description:** Analyze how Netflix content production has changed over time.

## Task workflow (from the official task list)
1. Organize content by release year
2. Calculate yearly content releases
3. Identify growth and decline trends
4. Create trend visualizations
5. Interpret business patterns

The cleaned dataset from Task 1 is already included in `data/processed/`, so this project runs on its own.

## Folder structure
```
src/          Python source (task4_trend_analysis.py + netflix_utils.py)
notebooks/    executed Jupyter notebook with outputs
data/         raw Dataset.csv and cleaned dataset
outputs/      charts, screenshots, dashboards, reports, metrics
run.py        run the task with one command
```

## How to run
```bash
pip install -r requirements.txt
python run.py
```
Or open `notebooks/task4_trend_analysis.ipynb` in Jupyter (outputs are already saved).

---
## Results summary
# Task 4 – Trend Analysis by Release Year: Business Patterns

| Period | Titles released | Avg / year |
|---|---|---|
| 2000-2009 | 807 | 80.7 |
| 2010-2014 | 1,250 | 250.0 |
| 2015-2018 | 3,630 | 907.5 |
| 2019-2021 (2021 partial) | 2,574 | 858.0 |

## Trends identified
1. **Rapid growth 2010-2018** – annual releases grew at a **25.0% CAGR** from 192 (2010) to 1144 (2018);
   the peak year was **2018** with 1144 titles. The four years 2015-2018 hold **41.3%** of the whole catalogue.
2. **Decline after the peak is a movie story** – total releases fell **17%** between 2018 and 2020,
   but that is driven by movies (-32.5%) while TV shows actually grew (+15.3%).
   2021 is a partial year (data ends September 2021) and should not be read as a collapse. The 2020 dip coincides with COVID-19
   production disruption, but the dataset cannot prove that cause.
3. **Thin back-catalogue** – only 525 titles (6.0%) were released before 2000: the library is overwhelmingly modern.
4. **Mix shift** – TV shows were 20% of 2010 releases vs 46% in 2020; series are a growing part of production.
5. **Freshness** – the median age of a title when added to Netflix moved from 0 year(s) in 2014 to 1 in 2020;
   66% of 2016 additions were released within the prior year vs 55% in 2020.
6. **Seasonality** – additions are highest in Dec and lowest in Feb (2016-2020 totals), useful for scheduling launches.

## Business interpretation
* Netflix's catalogue was built mainly through a 2015-2019 content-expansion cycle; maintaining that volume requires continued high investment.
* Total releases are below the 2018 peak while TV output is still growing, so the catalogue mix is moving toward series rather than films.
* Back-catalogue titles are a small part of the library (6%); the catalogue in this dataset is dominated by recent content.

*Data: `outputs/reports/task4_yearly_releases.csv`*

