# Task 2: EDA on Retail Sales Data

**Track:** Data Analytics - Level 1  
**Internship:** Oasis Infobyte SIP  

## Objective
Perform a thorough Exploratory Data Analysis on a retail sales dataset to uncover patterns, customer behaviour trends, and actionable business insights.

## Dataset
- **Source:** Synthetic retail sales dataset (2,000 orders, 488 unique customers)
- **Period:** January 2022 - March 2022 (3 months)
- **Features:** 13 columns including order details, customer demographics, product info, pricing, region

## Tech Stack
- Python
- pandas
- matplotlib
- seaborn
- Jupyter Notebook

## Analysis Performed

### 1. Data Quality Check
- Missing values: customer_age (50), customer_gender (30), category (20)
- No duplicates found
- All missing values imputed (median for age, mode for gender/category)

### 2. Descriptive Statistics
- Mean order value: $131.29
- Total revenue: $262,577.74
- Average customer age: 45.8 years
- Gender split: 53.6% Male, 46.4% Female

### 3. Time Series Analysis
- **Monthly trends**: January ($99,888) → February ($90,053) → March ($72,637)
- **Quarterly**: Q1 2022 total: $262,578
- Declining trend observed over the 3-month period

### 4. Customer Demographics
- **Age distribution**: Roughly normal, centered around 46 years
- **Gender**: Near-even split (Male: 1,071 orders, Female: 929 orders)
- **Age group spending**: 26-35 group highest avg spend ($137.39), 65+ close ($136.03)

### 5. Product Analysis
**Top 10 Products by Revenue:**
1. Product_58: $5,799 (31 orders)
2. Product_97: $4,751 (23 orders)
3. Product_20: $4,427 (21 orders)

**Revenue by Category:**
1. Electronics: $60,302 (23.0%)
2. Clothing: $53,914 (20.5%)
3. Books: $41,062 (15.6%)
4. Home & Garden: $40,916 (15.6%)
5. Sports: $38,969 (14.8%)
6. Beauty: $27,414 (10.4%)

### 6. Correlation Analysis
- **Strongest correlation**: unit_price ↔ total_amount (r = 0.83)
- **Moderate correlation**: quantity ↔ total_amount (r = 0.42)
- Other variables show weak/no correlation

### 7. Regional Analysis
| Region | Revenue | Avg Order Value | Orders | Customers |
|--------|---------|-----------------|--------|-----------|
| North | $77,670 | $131.64 | 590 | 341 |
| South | $68,653 | $131.02 | 524 | 316 |
| East | $62,353 | $128.30 | 486 | 299 |
| West | $53,903 | $134.76 | 400 | 266 |

### 8. Discount Impact Analysis
- No discount (0%): $159,552 revenue, AOV $135.21
- 5% discount: $42,596 revenue, AOV $134.37
- 10% discount: $23,830 revenue, AOV $126.08
- 15% discount: $26,021 revenue, AOV $121.59
- 20% discount: $10,579 revenue, AOV $105.79

**Key Insight:** Higher discounts reduce average order value without proportionally increasing volume.

## Business Recommendations

1. **Focus Marketing on High-Value Segments**
   - Target 26-35 age group (highest spenders)
   - North region customers (highest revenue & customer count)
   - Electronics & Clothing categories (43.5% of revenue)

2. **Optimize Discount Strategy**
   - Limit discounts to ≤5% (maintains AOV while driving volume)
   - Avoid 15-20% discounts (significant margin erosion)
   - Test targeted discounts for low-performing categories (Beauty, Sports)

3. **Address Declining Monthly Trend**
   - Investigate March decline (27% drop from January)
   - Launch Q2 promotional campaign
   - Implement customer retention program for Q1 buyers

## Files
- `eda_retail_sales.ipynb` - Main analysis notebook
- `eda_retail_sales_executed.ipynb` - Executed notebook with outputs
- `retail_sales_data.csv` - Dataset used

## Key Learnings
- End-to-end EDA workflow from data loading to business insights
- Time series visualization for trend identification
- Multi-dimensional analysis (demographics, products, regions, pricing)
- Translating statistical findings into actionable business recommendations