# Executive Summary

Our analysis of nearly 100,000 orders confirms that delivery delays are directly damaging our customer ratings, especially in the Northeast. While our average late rate is 7.9%, states like Alagoas and Maranhão are seeing much higher delays, which is causing a significant drop in satisfaction. The data shows a clear slide from 4.25 stars for on-time deliveries down to just 1.86 stars for "super late" orders. To turn this around and stop the influx of negative reviews, we need to refine our logistics in these struggling regions and provide customers with more realistic delivery timelines.

# Project Links

* **Link to Notebook:** (https://colab.research.google.com/drive/1l1J89750bLJ15O9ws_moYGJYAMTXe-LX?usp=sharing)
* **Link to Dashboard:**  
* **Link to Presentation:** (https://docs.google.com/presentation/d/1YvFE2e0fsKKB1bF5hopiSmQ2cBFkJyOs/edit?usp=drive_link&ouid=106166006012251092933&rtpof=true&sd=true)


# Technical Explanation

## Data Cleaning
Our data cleaning process ensured accurate analysis by addressing several key issues. We identified and resolved 551 duplicate reviews by calculating the average review score for orders with multiple reviews, consolidating 99,224 review records into 98,673 unique order reviews. We properly handled 1,234 canceled or unavailable orders by flagging them as "Not Delivered" rather than including them in delay calculations, which prevented these non-delivery cases from skewing our late delivery statistics. For the product category analysis, we successfully joined order data with product information for 96,778 orders (97% of total orders), with the remaining 3% lacking complete product details. Additionally, we converted all date fields to proper datetime formats to enable accurate day-difference calculations between estimated and actual delivery dates.



# Project Brief: The "Last Mile" Logistics Auditor

**Client:** Veridi Logistics (Global E-Commerce Aggregator)  
**Deliverable:** Public Dashboard, Code Notebook & Insight Presentation

---

## 1. Business Context
**Veridi Logistics** manages shipping for thousands of online sellers. Recently, the CEO has noticed a spike in negative customer reviews. She has a "gut feeling" that the problem isn't just that packages are late, but that the estimated delivery dates provided to customers are wildly inaccurate (i.e., we are over-promising and under-delivering).

She needs you to audit the delivery data to find the root cause. She specifically wants to know: **"Are we failing specific regions, or is this a nationwide problem?"**

Your job is to build a "Delivery Performance" audit tool that connects the dots between **Logistics Data** (when a package arrived) and **Customer Sentiment** (how they rated the experience).

## 2. The Data
You will use the **Olist E-Commerce Dataset**, a real commercial dataset from a Brazilian marketplace. This is a relational database dump, meaning the data is split across multiple CSV files.

* **Source:** [Kaggle - Olist Brazilian E-Commerce Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
* **Key Files to Use:**
    * `olist_orders_dataset.csv` (The central table)
    * `olist_order_reviews_dataset.csv` (Sentiment)
    * `olist_customers_dataset.csv` (Location)
    * `olist_products_dataset.csv` (Categories)

## 3. Tooling Requirements
You have the flexibility to choose your development environment:

* **Option A (Recommended):** Use a cloud-hosted notebook like **Google Colab**, or **Deepnote**, etc.
* **Option B:** Use a local **Jupyter Notebook** or **VS Code**.
    * *Condition:* If you choose this, you must ensure your code is reproducible. Do not reference local file paths (e.g., `C:/Downloads/...`). Assume the dataset is in the same folder as your notebook.
* **Dashboarding:** The final output must be a **publicly accessible link** (e.g., Tableau Public, Google Looker Studio, Streamlit Cloud, or PowerBI Web, etc.).

---

## 4. User Stories & Acceptance Criteria

### Story 1: The Schema Builder
**As a** Data Engineer,  
**I want** to join the Orders, Reviews, and Customers tables into a single master dataset,  
**So that** I can analyze a customer's location and their review score in the same row.

* **Acceptance Criteria:**
    * Load the raw CSVs into your notebook.
    * Perform the correct joins (e.g., join Reviews to Orders on `order_id`, join Customers to Orders on `customer_id`).
    * **Check:** Ensure you don't accidentally duplicate rows (a common error with 1-to-many joins).

### Story 2: The "Real" Delay Calculator
**As a** Logistics Manager,  
**I want** to know the difference between the "Estimated Delivery Date" and the "Actual Delivery Date,"  
**So that** I can see how often we are lying to customers.

* **Acceptance Criteria:**
    * Create a new calculated column: `Days_Difference` = `order_estimated_delivery_date` - `order_delivered_customer_date`.
    * Classify orders into statuses: "On Time", "Late", and "Super Late" (> 5 days late).
    * Handle missing values: Some orders were never delivered (`order_status` = 'canceled' or 'unavailable'). These should be excluded or flagged separately.

### Story 3: The Geographic Heatmap
**As a** Regional Director,  
**I want** to see which specific States (`customer_state`) have the highest percentage of late deliveries,  
**So that** I can focus my repair efforts on the worst regions.

* **Acceptance Criteria:**
    * Calculate the % of late orders per State.
    * Visualize this on a map or a bar chart.
    * **Insight:** Identify if "Remote" states (far from the distribution center) are disproportionately affected.

### Story 4: The Sentiment Correlation
**As a** Customer Success Lead,  
**I want** to see if late deliveries actually cause bad reviews,  
**So that** I can prove to the CEO that logistics is the problem.

* **Acceptance Criteria:**
    * Create a visualization comparing "Delivery Delay (Days)" vs "Average Review Score (1-5)".
    * Show the average review score for "On Time" orders vs. "Late" orders.

---

## 5. Bonus User Story: The "Translation" Challenge
**As a** Global Analyst,  
**I want** to see product categories in **English**, not Portuguese,  
**So that** I can understand if "Furniture" is harder to ship than "Electronics".

* **Acceptance Criteria:**
    * The `product_category_name` is in Portuguese (e.g., `cama_mesa_banho`).
    * Use the `product_category_name_translation.csv` file included in the dataset (or create your own mapping) to translate these into English for your final dashboard.

---

## 6. The "Candidate's Choice" Challenge
**As a** Creative Problem Solver,  
**I want** to include one extra feature or analysis that adds specific business value,  
**So that** I can demonstrate my ability to think beyond the basic requirements.

* **Instructions:**
    * Add one more metric, chart, or drill-down.
    * **Requirement:** You must justify *why* this feature matters to the business in your README.

---

## 7. Submission Guidelines
Please edit this `README.md` file in your forked repository to include the following three sections at the top:

### A. The Executive Summary
* A 3-5 sentence summary of your findings.

### B. Project Links
* **Link to Notebook:** (e.g., Google Colab, etc.). *Ensure sharing permissions are set to "Anyone with the link can view".*
* **Link to Dashboard:** (e.g., Tableau Public, etc.).
* **Link to Presentation:** A link to a short slide deck (PDF/PPT) AND (Optional) a 2-minute video walkthrough (YouTube) explaining your results.

### C. Technical Explanation
* Briefly explain how you handled the "Data Cleaning".
* Explain your "Candidate's Choice" addition.

**Important Note on Code Submission:**
* Upload your `.ipynb` notebook file to the repo.
* **Crucial:** Also upload an **HTML or PDF export** of your notebook so we can see your charts even if GitHub fails to render the notebook code.
* Once you are ready, please fill out the [Official Submission Form Here](https://forms.office.com/e/heitZ9PP7y) with your links

---

## 🛑 CRITICAL: Pre-Submission Checklist

**Before you submit your form, you MUST complete this checklist.**

> ⚠️ **WARNING:** If you miss any of these items, your submission will be flagged as "Incomplete" and you will **NOT** be invited to an interview. 
>
> **We do not accept "permission error" excuses. Test your links in Incognito Mode.**

### 1. Repository & Code Checks
- [ ] **My GitHub Repo is Public.** (Open the link in a Private/Incognito window to verify).
- [ ] **I have uploaded the `.ipynb` notebook file.**
- [ ] **I have ALSO uploaded an HTML or PDF export** of the notebook.
- [ ] **I have NOT uploaded the massive raw dataset.** (Use `.gitignore` or just don't commit the CSV).
- [ ] **My code uses Relative Paths.** 

### 2. Deliverable Checks
- [ ] **My Dashboard link is publicly accessible.** (No login required).
- [ ] **My Presentation link is publicly accessible.** (Permissions set to "Anyone with the link can view").
- [ ] **I have updated this `README.md` file** with my Executive Summary and technical notes.

### 3. Completeness
- [ ] I have completed **User Stories 1-4**.
- [ ] I have completed the **"Candidate's Choice"** challenge and explained it in the README.

**✅ Only when you have checked every box above, proceed to the submission form.**

---
