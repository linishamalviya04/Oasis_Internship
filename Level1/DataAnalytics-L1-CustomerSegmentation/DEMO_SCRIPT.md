# Demo Video Script - Task 3: Customer Segmentation Analysis

**Duration Target:** 4-6 minutes  
**Format:** Screen recording with voiceover  
**Title Card (2 seconds):** "Oasis Infobyte SIP | Data Analytics Track | Task 3: Customer Segmentation | [Your Name]"

---

## SCENE 1: Introduction (30 seconds)
**Visual:** Show repo, open `customer_segmentation.ipynb`, show RFM concept
**Script:**
> "Hi, I'm [Your Name] presenting Task 3: Customer Segmentation Analysis. 
> 
> Using the same retail data from Task 2, I apply RFM analysis - Recency, Frequency, Monetary - combined with K-Means clustering to segment 488 customers into 4 distinct behavioral groups, enabling targeted marketing strategies."

---

## SCENE 2: RFM Feature Engineering (45 seconds)
**Visual:** Cells 1-3: Customer stats, RFM calculation, distributions
**Script:**
> "First, I compute RFM features per customer:
> - Recency: Days since last purchase (mean 20 days, max 83)
> - Frequency: Total orders (mean 4.1, max 10)
> - Monetary: Total spend (mean $538, max $2,604)
> 
> Distributions are right-skewed, so I apply StandardScaler to normalize before clustering."

---

## SCENE 3: Optimal K Selection (45 seconds)
**Visual:** Cell 5: Elbow plot and Silhouette score chart
**Script:**
> "To find optimal clusters, I use Elbow Method and Silhouette Analysis testing K=2 to 10.
> 
> Silhouette peaks at K=2 (0.372), but K=4 provides better business interpretability with 0.326 score. The elbow shows diminishing returns after K=4. I select K=4 for actionable segments."

---

## SCENE 4: Cluster Results & Visualization (60 seconds)
**Visual:** Cells 6-7: Cluster centers table, 2D/3D scatter plots
**Script:**
> "K-Means with K=4 produces four segments:
> 
> **Cluster 0** (21%): High recency (48 days), low frequency (2.3), low monetary ($313) → 'At-Risk'
> 
> **Cluster 1** (34%): Low recency (13 days), high frequency (5.1), good monetary ($603) → 'Loyal Customers'
> 
> **Cluster 2** (30%): Recent (14 days), low frequency (2.5), low monetary ($245) → 'Occasional Buyers'
> 
> **Cluster 3** (16%): Very recent (10 days), very high frequency (7.1), very high monetary ($1,226) → 'Champions'
> 
> The 3D visualization shows clear separation in RFM space."

---

## SCENE 5: Cluster Profiling & Demographics (45 seconds)
**Visual:** Cells 8-10: Cluster profiles, demographic breakdown, bar chart
**Script:**
> "Adding demographics reveals:
> - Cluster 0: Older males (47), East region, narrow interests (2 categories)
> - Cluster 1: Female-dominant (45), North region, diverse (3.5 categories)  
> - Cluster 2: Males (47), East, low diversity (2 categories), low AOV ($104)
> - Cluster 3: Younger males (42), East, high diversity (4.25 categories), high AOV ($184)"

---

## SCENE 6: Marketing Recommendations (60 seconds)
**Visual:** Cells 11-12: Interpretation markdown, recommendations table
**Script:**
> "Targeted actions per segment:
> 
> **At-Risk (Cluster 0)**: Win-back campaign with 15% reactivation offer, personalized recommendations
> 
> **Loyal (Cluster 1)**: Tiered loyalty program, early access, referral bonuses, VIP support
> 
> **Occasional (Cluster 2)**: Bundle offers, cross-sell recommendations, free shipping thresholds
> 
> **Champions (Cluster 3)**: Exclusive products, dedicated manager, beta access, premium support, gifts
> 
> Budget allocation: 40% Champions, 30% Win-back, 20% Loyalty, 10% Cross-sell"

---

## SCENE 7: Strategic Summary (30 seconds)
**Visual:** Cell 13: Conclusion
**Script:**
> "This segmentation transforms 488 anonymous customers into 4 actionable segments with specific strategies. Champions (16% of customers) likely drive disproportionate revenue - retaining them is priority. At-risk segment needs immediate intervention. The framework is repeatable monthly."

---

## SCENE 8: Conclusion (15 seconds)
**Visual:** GitHub repo, executed notebook
**Script:**
> "Complete analysis with code, visualizations, and business recommendations in the notebook. Thank you!
> 
> #oasisinfobyte #dataanalytics #customersegmentation #RFM #KMeans #clustering"

---

## Recording Tips
- Explain RFM concept briefly for non-technical viewers
- Highlight cluster centers table when discussing segments
- Show 3D plot rotation if possible
- Emphasize business value over technical details
- Connect each recommendation to specific cluster metrics