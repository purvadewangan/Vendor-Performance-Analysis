# Vendor-Performance-Analysis

A complete end-to-end analytics project exploring vendor and brand performance across a large retail dataset. This project handles 12M+ sales records and six interconnected datasets, combining SQL, Python, and Power BI to deliver actionable business insights.

<br>

**Project Overview**

This project focuses on understanding how vendors and brands contribute to overall profitability. It evaluates sales performance, purchasing behavior, inventory movement, and pricing patterns using large-scale data.

The analysis was developed in Jupyter Notebook, connected to a MySQL server to efficiently process high-volume tables. After transforming and merging all datasets into a consolidated summary table, the key findings were visualized and explained through Power BI dashboards.

<br>

**Dataset Summary**

Six raw datasets were used, totaling millions of records:

   - Begin Inventory – 206K rows
    
  -  End Inventory – 224K rows
    
  -  Purchase Prices – 12K rows
    
  -  Purchases – 2.37M rows
    
  -  Sales – 12.8M rows
  
  -  Vendor Invoice – 5.5K rows

 <br>

A final aggregated dataset, vendor_sales_summary, was prepared with 10,692 records and 18 feature columns, combining sales, purchases, pricing, inventory turnover, and profit metrics.

<br>
<br>
  
**Tools & Technologies**

- Python: Pandas, NumPy, Matplotlib, Seaborn

- MySQL: Data extraction, cleaning, and summary table creation

- Power BI: Dashboarding and insight visualization

- Jupyter Notebook: EDA, merging, transformation, analysis

<br>
 <br>

**EDA Approach**

The analysis pipeline included:

- Connecting MySQL with Python to load and inspect each dataset.

- Reviewing initial and final records to understand data distribution and quality.

- Identifying relevant columns for the business problem.

- Creating a consolidated summary table using pandas and SQL.

- Running statistical analysis and correlation checks.

- Preparing clean, structured outputs for visualization in Power BI.

This approach ensured accurate processing of large datasets and reliable insights.

<br>
 <br>

**Key Analytical Highlights**
 <br>
 *Summary Statistics*

- Wide variation in monetary fields shows vendors operate at very different scales.

- Negative gross profit and zero-sales rows indicate pricing issues and slow-moving items.

- Large gaps between mean and max values reflect premium products and cost inconsistencies.

- Turnover varies heavily, pointing to both fast-selling and stagnant inventory.

 <br>
 
*Correlation Insights*

- Pricing has minimal impact on sales revenue or gross profit.

- Strongest correlation: Purchase Quantity ↔ Sales Quantity, confirming effective inventory flow.

- Higher sales prices tend to reduce profit margins due to competitive pressures.

- Turnover speed shows almost no relationship with profitability.

<br>
 <br>

📌 **Business Insights by Question**
1. Identify Brands Needing Promotion or Pricing Adjustment 

- *198 brands show low sales but strong margins—clear opportunities for marketing or pricing optimization.*
  <br>

2. Which Vendors and Brands Drive the Most Sales?

- *A small group dominates revenue.*
- *Diageo North America and Jack Daniel’s No. 7 lead at vendor and brand levels, highlighting where demand is strongest.*
  <br>

3. Which Vendors Contribute Most to Purchase Dollars?

- *Spending is highly concentrated.*
- *Diageo alone accounts for 16% of total purchases.*
  <br>

4. Procurement Dependence on Top Vendors

- *65.69% of purchases come from a limited vendor group.*
- *This dependency increases supply-chain risk and needs diversification.*
  <br>

5. Does Bulk Purchasing Reduce Unit Costs?

- *Yes—large orders reduce unit cost by ~72%, making bulk buying the most cost-efficient volume.*
  <br>

6. Vendors With Low Inventory Turnover

- *About $2.71M is tied up in unsold inventory, largely associated with a few vendors.*
- *These require better demand forecasting and optimized ordering.*
  <br>

7. How Much Capital Is Locked in Unsold Inventory?

- *A handful of vendors—Diageo, Jim Beam, Pernod Ricard—contribute the most to dormant stock value.*
  <br>

8. 95% Confidence Interval for Profit Margins

  Top vendors: 30.7% – 31.6%

- *Low vendors: 40.5% – 42.6%*
- *Low-volume vendors maintain high margins but lack reach.*
  <br>

9. Profit Margin Difference Between Top and Low Vendors

- *Hypothesis testing confirms a significant margin difference.*
- *High-volume vendors rely on competitive pricing, while low-volume vendors rely on higher margins.*

<br>
 <br>

**Business Recommendations**

- Boost growth for high-margin, low-volume brands
  *Targeted marketing and pricing adjustments can lift sales without hurting profitability.*  <br>

- Strengthen relationships with top-performing vendors
  *Key partners like Diageo and Jack Daniel’s drive major revenue and should remain a focus.*  <br>

- Reduce procurement risk by diversifying vendors
  *Spread purchasing across more suppliers to avoid over-dependency.*  <br>

- Use bulk purchasing strategically
  *Leverage volume discounts but align them with accurate demand planning.*  <br>

- Address slow-moving inventory
  *Improve forecasting, adjust purchase quantities, and consider clearance strategies.*  <br>

- Balance pricing between high-volume and high-margin vendors
  *High-volume vendors should refine cost structures, while low-volume vendors need marketing and distribution support.*

<br>
 <br>

 ![Dashboard Preview](https://github.com/purvadewangan/Vendor-Performance-Analysis/blob/main/Vendor%20Performance%20Analysis_page-0001.jpg)
 ![Dashboard Preview](https://github.com/purvadewangan/Vendor-Performance-Analysis/blob/main/Vendor%20Performance%20Analysis_page-0002.jpg)

 <br>
 <br>

As a data analyst, this project allowed me to demonstrate my ability to work with large, complex datasets and manage the full analytics process end-to-end. <br>
Handling more than twelve million records across multiple sources strengthened my skills in **SQL**, **Python**, and **data modeling**. <br>
Building the final insights in **Power BI** helped me translate technical work into clear business outcomes. 
*I’m confident working with high-volume data, blending tools, and delivering analysis that supports real decision-making. If my work aligns with what you’re looking for, I’d be glad to connect.*
