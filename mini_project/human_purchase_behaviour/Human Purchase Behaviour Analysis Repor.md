1. Introduction

This report analyzes a dataset containing customer purchase behaviour.
The dataset has 72,637 rows and 3 columns.
The goal is to understand customer segments based on life stage and premium status.

2. Dataset Overview
Feature	Description
Loyalty_card_id:- Unique customer ID
LIFESTAGE :-	Customer life-stage group
PREMIUM_CUSTOMER :-	Type of customer (Budget /Mainstream / Premium)



3. Data Quality Checks
Check	Result
Missing Values	None (0 nulls)
Duplicates	None
Data Types	All correct
Summary Statistics (Loyalty_card_id)
Metric	Value
Mean	136,185.9
Median	134,040
Std Dev	89,892.93
Min	1,000
Max	2,373,711
4. Data Cleaning & Manipulation

Renamed LYLTY_CARD_NBR → Loyalty_card_id

Converted all LIFESTAGE text to lowercase

Sorted the data by LIFESTAGE and PREMIUM_CUSTOMER

Checked for missing values using df.isnull() → None found

Used df.fillna(df.mean()), but no values required filling

5. Customer Distribution
LIFESTAGE Counts

Young Singles/Couples — highest

Young Families

Midage Singles/Couples

Older Singles/Couples

Older Families

Distribution is fairly balanced across life stages.

PREMIUM_CUSTOMER Tier
Tier	Approx %
Budget	~35–40%
Mainstream	~40–45%
Premium	~15–20%

Most customers belong to Budget and Mainstream groups.

6. Key Insights

Younger customers are more Budget-focused

Older families show the highest interest in Premium

Premium is the smallest customer segment but valuable


7. Visual representation Created

Pie chart for LIFESTAGE distribution

Histogram for PREMIUM_CUSTOMER

Grouped bar chart comparing PREMIUM tier across life stages

Scatter plot (converted categories into numbers)

8. Business Recommendations

Provide discounts and offers for Young customers to increase spending

Promote premium  plans to Older Families

Strengthen customer by retention programs 

Create targeted marketing by life stage groups

9. Conclusion

The dataset contains  and complete records for 72,637 customers.
The analysis shows a  mix of life stages and a pyramid-style spending pattern.
There is clear opportunity to increase premium customers, especially in older age groups.
