# Task 2: Unemployment Analysis with Python

**Track:** Data Science  
**Internship:** Oasis Infobyte SIP  

## Objective
Perform exploratory data analysis on unemployment data to uncover regional and temporal trends, with a focus on the impact of the COVID-19 pandemic on unemployment rates in India.

## Dataset
- **Source:** Synthetic dataset (720 records, 15 states, Jan 2019 - Dec 2022)
- **Features:** Date, State, Unemployment Rate, Employment Rate, Labour Participation Rate
- **Based on:** Kaggle "Unemployment in India" dataset structure

## Tech Stack
- Python, pandas, matplotlib, seaborn, Jupyter Notebook

## Analysis Performed

### 1. Regional Analysis
- **Highest unemployment states**: Odisha (12.25%), West Bengal (12.21%), Bihar (11.97%)
- **Lowest unemployment states**: Punjab (3.77%), Delhi (5.89%), Madhya Pradesh (5.78%)
- Significant variation across states (3.77% - 12.25%)

### 2. Temporal Trends
- **Pre-COVID average**: 7.34%
- **COVID peak (Apr-May 2020)**: ~19-20% (3x increase)
- **Post-COVID recovery**: 7.38% (near pre-COVID levels)

### 3. COVID Impact by State
- **Highest increase**: Rajasthan (+9.42%), Gujarat (+8.93%), Kerala (+8.59%)
- **Most affected in absolute terms**: Odisha, West Bengal, Bihar (highest baseline + large increase)

### 4. Correlation Analysis
- **Unemployment ↔ Employment**: -0.94 (strong negative)
- **Unemployment ↔ Labour Participation**: 0.02 (negligible)
- **Employment ↔ Labour Participation**: -0.02 (negligible)

### 5. Recovery Analysis
- Most states recovered to near pre-COVID levels by 2022
- Recovery uneven: industrial states (Maharashtra, Gujarat) recovered faster
- Some states (Bihar, Odisha) still above pre-COVID levels

## Files
- `unemployment_analysis.ipynb` - Main analysis notebook
- `unemployment_analysis_executed.ipynb` - Executed notebook with outputs
- `unemployment_india.csv` - Dataset

## Key Insights
- COVID caused 3x unemployment spike (7.3% → 19.8% peak)
- Recovery nearly complete by 2022 but uneven across states
- Labour participation rate remained stable (~50%) throughout
- Eastern states (Odisha, West Bengal, Bihar) most vulnerable

## Files
- `unemployment_analysis.ipynb` - Main analysis notebook
- `unemployment_analysis_executed.ipynb` - Executed notebook with outputs
- `unemployment_india.csv` - Dataset