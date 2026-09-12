# Demo Video Script - Task 2: EDA on Retail Sales Data

**Duration Target:** 4-6 minutes  
**Format:** Screen recording with voiceover  
**Title Card (2 seconds):** "Oasis Infobyte SIP | Data Analytics Track | Task 2: EDA on Retail Sales Data | [Your Name]"

---

## SCENE 1: Introduction (30 seconds)
**Visual:** Show repo, open `eda_retail_sales.ipynb`, show dataset overview
**Script:**
> "Hi, I'm [Your Name] presenting Task 2: Exploratory Data Analysis on Retail Sales Data for the Oasis Infobyte Data Analytics internship.
> 
> I analyze a synthetic retail dataset with 2,000 orders across 488 customers over 3 months, uncovering patterns in sales trends, customer demographics, product performance, regional differences, and discount effectiveness."

---

## SCENE 2: Data Loading & Quality (30 seconds)
**Visual:** Cells 1-3: shape, dtypes, null check, descriptive stats
**Script:**
> "The dataset has 13 columns including order details, customer demographics, product info, and pricing. I found 100 missing values across 3 columns - age, gender, and category - which I imputed using median and mode. No duplicates found. Total revenue is $262,578 with average order value of $131."

---

## SCENE 3: Time Series Analysis (45 seconds)
**Visual:** Cell 5: Monthly and quarterly trend charts
**Script:**
> "Monthly sales show a declining trend: January at $99.9K, February at $90.1K, March at $72.6K - a 27% drop over 3 months. This signals potential seasonality or customer churn that needs investigation. Quarterly view confirms Q1 total of $262.6K."

---

## SCENE 4: Customer Demographics (45 seconds)
**Visual:** Cell 7: Age histogram, gender pie, age-gender boxplot, spend by age group
**Script:**
> "Customer age follows a roughly normal distribution centered at 46 years. Gender split is nearly even - 54% male, 46% female. The 26-35 age group has the highest average spend at $137, followed by 65+ at $136. This identifies our core high-value demographic."

---

## SCENE 5: Product & Category Analysis (45 seconds)
**Visual:** Cell 9: Top 10 products bar chart, category revenue chart
**Script:**
> "Top product is Product_58 generating $5,800 from 31 orders. Electronics leads categories at 23% of revenue ($60.3K), followed by Clothing at 20.5% ($53.9K). Top 2 categories drive 43.5% of total revenue - classic Pareto principle."

---

## SCENE 6: Correlation & Regional Analysis (45 seconds)
**Visual:** Cell 11: Correlation heatmap, Cell 13: Regional charts
**Script:**
> "Strongest correlation is unit_price to total_amount at 0.83 - expected since price drives revenue. Quantity correlates at 0.42. Regionally, North leads with $77.7K revenue and 341 customers. West has highest AOV at $134.76 but lowest volume."

---

## SCENE 7: Discount Impact (45 seconds)
**Visual:** Cell 15: Discount analysis charts
**Script:**
> "Critical finding: higher discounts erode average order value without proportional volume gains. No discount yields $135 AOV; 20% discount drops to $106. Revenue at 0% discount is $159.5K vs only $10.6K at 20%. This suggests limiting discounts to 5% maximum."

---

## SCENE 8: Business Recommendations (45 seconds)
**Visual:** Cell 17: Conclusion markdown with 3 recommendations
**Script:**
> "My three data-driven recommendations:
> 
> 1. **Target High-Value Segments**: Focus marketing on 26-35 age group, North region, Electronics/Clothing categories
> 
> 2. **Optimize Discounts**: Cap at 5%, avoid 15-20% which destroys margins
> 
> 3. **Reverse March Decline**: Launch Q2 retention campaign for Q1 buyers, investigate root cause of 27% drop"

---

## SCENE 9: Conclusion (15 seconds)
**Visual:** GitHub repo, notebook
**Script:**
> "All analysis is in the executed notebook with visualizations and markdown observations. Thank you for watching!
> 
> #oasisinfobyte #dataanalytics #EDA #retailanalytics #python"

---

## Recording Tips
- Narrate chart insights as they appear
- Use annotations/highlights on key numbers
- Keep pace steady - don't rush charts
- Show code briefly, focus on outputs