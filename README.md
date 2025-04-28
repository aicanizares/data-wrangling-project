# Plant-Based Companies in Europe

## Introduction
This project explores plant-based food companies in Europe, analyzing their presence in media articles and industry trends. The analysis leverages data from The Good Food Institute (GFI) Europe and a vegan business magazine (Vegconomist) to extract meaningful insights.

## Data Sources
- **The Good Food Institute (GFI) Europe**: Provides a dataset of plant-based food companies.
- **Vegconomist**: Articles in the "Marketing & Media" category mentioning plant-based companies.
- **Web Scraping**: Extracted article data from Vegconomist.

## Challenges, Strengths, and Weaknesses
### Challenges:
- Web scraping feasibility and handling infinite scrolling.
- Standardizing company names across sources.

### Strengths:
- Diverse data sources enable a broader perspective on the industry.

### Weaknesses:
- Low number of matches in company names between both datasets.

## Key Questions & Conclusions
### 1. **Does Vegconomist favor European companies in their articles?**
**Conclusion**: No, only 2/10 top-ranked companies in article count were European.

### 2. **Have more plant-based companies been founded year after year since 2000?**
**Conclusion**: No, although there was a rise in company formations from 2017-2020, the trend declined afterward.

### 3. **Do plant-based cheese manufacturers also produce vegan yoghurt and butter in Germany & the Netherlands?**
**Conclusion**: No, most manufacturers focus on a single product category.

### 4. **Are Germany and the Netherlands leading in plant-based cheese and dairy alternatives?**
**Conclusion**: While both countries rank in the top three, neither is the top leader in the sector.

## Methodology
1. **Data Cleaning**:
   - Filtering missing values (e.g., “Year Founded”).
   - Removing duplicates by standardizing company names.
   - Formatting text (case adjustments, accents, punctuation).

2. **Web Scraping**:
   - Extracted company names from Vegconomist articles using Beautiful Soup.
   - Counted occurrences of each company in articles.

3. **Data Merging & Analysis**:
   - Outer join of datasets.
   - Grouped and filtered values to assess trends.
   - Created bar charts and time-series plots for visualization.

## Lessons Learned & Adjustments
- **Merging datasets yielded low business value due to few matches (only 24 companies).**
- **Future approaches should emphasize insights from the GFI dataset alone.**
- **Avoid pre-planning hypotheses based on web scraping results without verifying data availability.**

## Further Questions
- How do European plant-based companies compare financially to their American counterparts?
- What are the key factors driving consumer adoption of plant-based products in different regions?

## Links to Data Sources
- [Vegconomist - Marketing & Media](https://vegconomist.com/category/marketing-and-media/)
- [GFI Europe Company Database](https://gfieurope.org/industry/#company-database)
- [Slides Presentation](https://docs.google.com/presentation/d/1Ay197tIcD_tBU6K3gSM9w_v3Qw4mQaZQYeD60XzZ1qk/edit?usp=sharing)

## How to Run This Project
Clone this repository and open the Jupyter Notebook:

```sh
git clone https://github.com/yourusername/plant-based-companies.git
cd plant-based-companies
