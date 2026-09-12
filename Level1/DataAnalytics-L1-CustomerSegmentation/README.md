# Task 3: Customer Segmentation Analysis

**Track:** Data Analytics - Level 1  
**Internship:** Oasis Infobyte SIP  

## Objective
Apply clustering algorithms to segment an e-commerce company's customer base into distinct groups based on purchasing behaviour, enabling targeted marketing strategies.

## Dataset
- **Source:** Same retail sales data from Task 2 (2,000 orders, 488 unique customers)
- **Period:** January 2022 - March 2022
- **RFM Features Engineered:** Recency, Frequency, Monetary per customer

## Tech Stack
- Python
- pandas
- scikit-learn (KMeans, StandardScaler, silhouette_score)
- matplotlib
- seaborn
- Jupyter Notebook

## Methodology

### 1. RFM Feature Engineering
- **Recency**: Days since last purchase (range: 1-83 days, mean: 20.0)
- **Frequency**: Total number of orders (range: 1-10, mean: 4.1)
- **Monetary**: Total spend (range: $9.50-$2,604, mean: $538.07)

### 2. Data Preprocessing
- StandardScaler applied to normalize all three RFM features
- Zero mean, unit variance achieved

### 3. Optimal Cluster Selection
**Elbow Method & Silhouette Analysis:**
| K | Inertia | Silhouette |
|---|---------|------------|
| 2 | 830.45 | **0.3720** |
| 3 | 568.06 | 0.3542 |
| 4 | 442.72 | 0.3255 |
| 5 | 391.12 | 0.3072 |

**Selected K = 4** (balance between silhouette score and business interpretability)

### 4. K-Means Clustering Results

#### Cluster Profiles (Original Scale)
| Cluster | Recency (days) | Frequency | Monetary ($) | Customers | % |
|---------|----------------|-----------|--------------|-----------|---|
| **0** | 48.5 | 2.35 | 312.58 | 101 | 20.7% |
| **1** | 12.6 | 5.13 | 602.66 | 164 | 33.6% |
| **2** | 13.8 | 2.53 | 245.36 | 144 | 29.5% |
| **3** | 10.4 | 7.05 | 1,225.81 | 79 | 16.2% |

#### Demographic Profiles
| Cluster | Avg Age | Primary Gender | Primary Region | Avg Order Value | Categories/Customer |
|---------|---------|----------------|----------------|-----------------|---------------------|
| 0 | 47.1 | Male | East | $136.39 | 1.98 |
| 1 | 45.0 | Female | North | $126.09 | 3.54 |
| 2 | 46.9 | Male | East | $104.25 | 2.05 |
| 3 | 42.4 | Male | East | $184.00 | 4.25 |

## Cluster Interpretations & Marketing Actions

### Cluster 0: "At-Risk / Dormant Customers" (20.7%)
- **Characteristics**: High recency (48 days), low frequency (2.35), low monetary ($313)
- **Profile**: Older male customers from East, narrow category interest
- **Marketing Action**: **Win-back Campaign** - "We miss you" emails with 15% reactivation offer, personalized product recommendations based on past purchases

### Cluster 1: "Loyal Customers" (33.6%) - LARGEST SEGMENT
- **Characteristics**: Low recency (13 days), high frequency (5.13), good monetary ($603)
- **Profile**: Predominantly female, North region, diverse category interest (3.5 categories)
- **Marketing Action**: **Loyalty Program** - Tiered rewards, early access to new products, referral bonuses, VIP customer service

### Cluster 2: "Occasional / Low-Value Buyers" (29.5%)
- **Characteristics**: Recent (14 days), low frequency (2.53), low monetary ($245)
- **Profile**: Male, East region, low category diversity, low AOV
- **Marketing Action**: **Cross-sell & Upsell** - Bundle offers, "Complete your purchase" recommendations, category exploration incentives, free shipping threshold

### Cluster 3: "Champions / High-Value Customers" (16.2%) - HIGHEST VALUE
- **Characteristics**: Very recent (10 days), very high frequency (7.05), very high monetary ($1,226)
- **Profile**: Younger male, East region, high category diversity (4.25), highest AOV ($184)
- **Marketing Action**: **VIP Treatment** - Exclusive products, dedicated account manager, beta testing access, premium support, birthday/anniversary gifts

## Strategic Recommendations

1. **Retention Priority**: Focus on Cluster 0 (at-risk) and Cluster 3 (champions) - highest revenue impact
2. **Growth Opportunity**: Cluster 1 (loyal) has potential to become champions with right engagement
3. **Volume Play**: Cluster 2 (occasional) represents 29.5% of customers - small AOV increases = significant revenue
4. **Resource Allocation**: 
   - 40% budget → Champion retention (Cluster 3)
   - 30% budget → Win-back (Cluster 0)
   - 20% budget → Loyalty nurturing (Cluster 1)
   - 10% budget → Cross-sell (Cluster 2)

## Files
- `customer_segmentation.ipynb` - Main analysis notebook
- `customer_segmentation_executed.ipynb` - Executed notebook with outputs
- `customer_data_for_segmentation.csv` - Prepared dataset

## Key Learnings
- RFM analysis as foundation for behavioral segmentation
- K-Means clustering with proper feature scaling
- Elbow method + Silhouette score for optimal K selection
- Translating cluster profiles into actionable marketing strategies
- Balancing statistical rigor with business interpretability