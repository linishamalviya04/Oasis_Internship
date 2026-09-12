# Demo Video Script - Task 1: Cleaning Data

**Duration Target:** 3-5 minutes  
**Format:** Screen recording with voiceover  
**Title Card (2 seconds):** "Oasis Infobyte SIP | Data Analytics Track | Task 1: Cleaning Data | [Your Name]"

---

## SCENE 1: Introduction (30 seconds)
**Visual:** Show GitHub repo structure, then open `cleaning_data.ipynb`
**Script:**
> "Hi, I'm [Your Name] and this is my submission for Task 1: Cleaning Data in the Oasis Infobyte Data Analytics internship. 
> 
> In this task, I demonstrate professional data cleaning skills by taking a deliberately messy customer dataset with 1,050 rows and 12 columns, and systematically transforming it into an analysis-ready dataset."

---

## SCENE 2: Data Quality Report (45 seconds)
**Visual:** Scroll through Cells 1-3 showing null report, duplicates, data types, anomalies
**Script:**
> "First, I perform a comprehensive data quality assessment. The dataset has several issues:
> - 359 total null values across 4 columns: gender, email, city, and subscription status
> - 47 duplicate rows (4.5%)
> - Inconsistent categorical formatting - gender has 6 variations, city has 8, subscription status has 6
> - Outliers: age of 200, negative total_spent of -500, and an extreme value of 999,999"

---

## SCENE 3: Missing Data Handling (45 seconds)
**Visual:** Show Cell 4-5 code and output
**Script:**
> "For missing data, I apply strategic handling per column:
> - Email: Drop rows (10% missing, not needed for core analysis)
> - Gender, City, Subscription Status: Mode imputation to preserve distribution
> 
> After this step, we go from 1,050 to 945 rows with only phone column having nulls."

---

## SCENE 4: Duplicate Removal & Standardization (45 seconds)
**Visual:** Show Cells 6-8
**Script:**
> "Next, I remove 42 duplicate rows, leaving 903 unique records.
> 
> Then standardization: I normalize all inconsistent categorical values - mapping Male/M/male to 'Male', Female/F/female to 'Female', NYC/LA/Chi to full city names, and standardizing subscription statuses. Date columns are converted to datetime, and invalid phone numbers are flagged."

---

## SCENE 5: Outlier Detection & Data Types (45 seconds)
**Visual:** Show Cells 9-11
**Script:**
> "Using the IQR method with 1.5x multiplier:
> - Age: 1 outlier at 200, capped at 100
> - Total spent: 43 outliers, capped at IQR upper bound, negative values set to 0
> - Purchase count: 4 outliers capped
> 
> Finally, I assign correct data types: integers for IDs and counts, floats for monetary, datetime for dates, categories for nominal variables."

---

## SCENE 6: Before vs After Summary (30 seconds)
**Visual:** Show Cell 12 comparison table
**Script:**
> "The results speak for themselves:
> - Rows: 1,050 → 903 (cleaned)
> - Nulls: 359 → 33 (only phone)
> - Duplicates: 47 → 0
> - Data types: Mixed → All correct
> 
> The cleaned dataset is saved as `cleaned_customer_data.csv` - ready for any downstream analysis."

---

## SCENE 7: Conclusion (15 seconds)
**Visual:** Show final conclusion markdown, GitHub repo
**Script:**
> "This completes Task 1. The full pipeline is documented in the Jupyter notebook with every decision justified. Thank you for reviewing!
> 
> #oasisinfobyte #dataanalytics #datacleaning #python #pandas"

---

## Recording Tips
- Record at 1080p minimum
- Use clear microphone audio
- Zoom in on code when explaining
- Pause 2 seconds between sections
- Keep mouse movements smooth