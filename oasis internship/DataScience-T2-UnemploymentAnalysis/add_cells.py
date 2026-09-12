import json

with open('unemployment_analysis.ipynb', 'r') as f:
    nb = json.load(f)

new_cells = [
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "# Pre-COVID vs Post-COVID comparison\n",
            "# Define periods: Pre-COVID (Jan 2019 - Feb 2020), COVID (Mar 2020 - Sep 2020), Post-COVID (Oct 2020 - Dec 2022)\n",
            "df['Period'] = pd.cut(df['Date'], \n",
            "    bins=[pd.Timestamp('2019-01-01'), pd.Timestamp('2020-03-01'), pd.Timestamp('2020-10-01'), pd.Timestamp('2023-01-01')],\n",
            "    labels=['Pre-COVID', 'COVID', 'Post-COVID'],\n",
            "    right=False\n",
            ")\n",
            "\n",
            "period_avg = df.groupby('Period')['Unemployment_Rate'].mean().reset_index()\n",
            "print('=== PRE-COVID vs COVID vs POST-COVID ===')\n",
            "display(period_avg)\n",
            "\n",
            "# State-wise comparison\n",
            "state_period = df.groupby(['State', 'Period'])['Unemployment_Rate'].mean().reset_index()\n",
            "state_pivot = state_period.pivot(index='State', columns='Period', values='Unemployment_Rate').reset_index()\n",
            "state_pivot['COVID_Increase'] = state_pivot['COVID'] - state_pivot['Pre-COVID']\n",
            "state_pivot['Recovery'] = state_pivot['COVID'] - state_pivot['Post-COVID']\n",
            "state_pivot = state_pivot.sort_values('COVID_Increase', ascending=False)\n",
            "\n",
            "print('\\n=== STATE-WISE COVID IMPACT ===')\n",
            "display(state_pivot.round(2))\n",
            "\n",
            "# Visualization\n",
            "fig, axes = plt.subplots(1, 2, figsize=(14, 6))\n",
            "\n",
            "# Period comparison\n",
            "sns.barplot(data=period_avg, x='Period', y='Unemployment_Rate', palette=['blue', 'red', 'green'], ax=axes[0])\n",
            "axes[0].set_title('Average Unemployment Rate by Period', fontweight='bold')\n",
            "axes[0].set_ylabel('Unemployment Rate (%)')\n",
            "for i, v in enumerate(period_avg['Unemployment_Rate']):\n",
            "    axes[0].text(i, v + 0.1, f'{v:.2f}%', ha='center', fontweight='bold')\n",
            "\n",
            "# Top 5 states with highest COVID increase\n",
            "top5_increase = state_pivot.nlargest(5, 'COVID_Increase')\n",
            "sns.barplot(data=top5_increase, x='COVID_Increase', y='State', palette='Reds_r', ax=axes[1])\n",
            "axes[1].set_title('Top 5 States - COVID Unemployment Increase', fontweight='bold')\n",
            "axes[1].set_xlabel('Increase from Pre-COVID (%)')\n",
            "\n",
            "plt.tight_layout()\n",
            "plt.show()"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## 7. Month-wise Trends by Year"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "# Monthly trends faceted by year\n",
            "monthly_yearly = df.groupby(['Year', 'Month'])['Unemployment_Rate'].mean().reset_index()\n",
            "monthly_yearly['Month_Name'] = monthly_yearly['Month'].map({1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',7:'Jul',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'})\n",
            "\n",
            "fig, axes = plt.subplots(2, 2, figsize=(14, 10))\n",
            "axes = axes.flatten()\n",
            "\n",
            "for i, year in enumerate([2019, 2020, 2021, 2022]):\n",
            "    year_data = monthly_yearly[monthly_yearly['Year'] == year]\n",
            "    axes[i].plot(year_data['Month'], year_data['Unemployment_Rate'], marker='o', linewidth=2, label=str(year))\n",
            "    axes[i].set_title(f'Unemployment Rate - {year}', fontweight='bold')\n",
            "    axes[i].set_xlabel('Month')\n",
            "    axes[i].set_ylabel('Unemployment Rate (%)')\n",
            "    axes[i].set_xticks(range(1, 13))\n",
            "    axes[i].set_xticklabels(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'], rotation=45)\n",
            "    axes[i].grid(True, alpha=0.3)\n",
            "    if year == 2020:\n",
            "        axes[i].axvspan(3.5, 9.5, alpha=0.2, color='red', label='COVID Lockdown')\n",
            "        axes[i].legend()\n",
            "\n",
            "plt.tight_layout()\n",
            "plt.show()"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## 8. Conclusion"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### Summary\n",
            "\n",
            "1. **Dataset**: 720 records across 15 states from Jan 2019 - Dec 2022 (48 months)\n",
            "\n",
            "2. **Regional Analysis**: \n",
            "   - Top states by unemployment identified\n",
            "   - Significant variation across states\n",
            "\n",
            "3. **Temporal Trends**:\n",
            "   - Clear seasonal patterns in unemployment\n",
            "   - Dramatic spike during COVID-19 lockdown (Apr-Sep 2020)\n",
            "   - Gradual recovery post-lockdown\n",
            "\n",
            "3. **COVID Impact**:\n",
            "   - Unemployment rate increased significantly during lockdown months\n",
            "   - Some states more affected than others\n",
            "   - Recovery trajectory varies by state\n",
            "\n",
            "4. **Correlations**:\n",
            "   - Negative correlation between unemployment and employment rates\n",
            "   - Labour participation shows weak correlation\n",
            "\n",
            "5. **Recovery**: Most states show gradual improvement post-COVID but not yet at pre-COVID levels\n",
            "\n",
            "### Key Insights\n",
            "\n",
            "- COVID-19 caused unprecedented unemployment spike in India\n",
            "- Maharashtra, Delhi, and other industrial states most affected\n",
            "- Recovery has been gradual and uneven across states\n",
            "- Labour participation rate remained relatively stable\n",
            "\n",
            "### Recommendations\n",
            "\n",
            "1. Targeted employment programs for worst-affected states\n",
            "2. Focus on sectors hit hardest by lockdowns\n",
            "3. Monitor labour participation for long-term trends\n",
            "4. Build resilience for future economic shocks"
        ]
    }
]

nb['cells'].extend(new_cells)

with open('unemployment_analysis.ipynb', 'w') as f:
    json.dump(nb, f, indent=2)
print('Notebook updated with all cells')