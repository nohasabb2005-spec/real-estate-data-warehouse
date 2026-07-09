# 🥈 Silver Layer

The **Silver Layer** is responsible for cleaning, validating, and transforming the raw data stored in the Bronze layer. All transformations are implemented using **dbt** to improve data quality and prepare the dataset for analytical modeling.

---

## 📥 Data Source

- Source Table: `BRONZE.RAW_LISTINGS`
- Transformation Tool: **dbt**
- Output Schema: **SILVER**

---

## ⚙️ Data Cleaning Steps

The Silver layer performs the following operations:

### 1. Remove Duplicate Records

Duplicate listings are removed using **listing_id** as the unique identifier.

---

### 2. Handle Missing Values

Missing values are identified and replaced using appropriate techniques depending on the column type.

---

### 3. Correct Data Types

Data types are standardized:

- Convert `price` to numeric
- Convert `surface_m2` to numeric
- Convert `listing_date` to DATE
- Convert `year_built` to INTEGER

---

### 4. Standardize Text Values

Normalize text columns by:

- Removing extra spaces
- Converting values to a consistent format
- Standardizing property types
- Standardizing heating types
- Standardizing parking values

---

### 5. Handle Invalid Data

Detect and remove unrealistic values such as:

- Negative prices
- Extremely high prices
- Invalid surface values
- Incorrect construction years

---

### 6. Create Derived Columns

New analytical columns are generated:

- **price_per_m2**
- **property_age**

---

## 🏗️ Silver Architecture

```text
          Bronze Layer
      BRONZE.RAW_LISTINGS
               │
               ▼
        dbt Silver Models
               │
               ▼
      Data Cleaning & Validation
               │
               ▼
     Standardization & Enrichment
               │
               ▼
      SILVER.CLEAN_LISTINGS
```

---

## 📂 Files Used

```text
dbt/
└── models/
    └── silver/
```

---

## 📋 Output Table

**Schema**

```
SILVER
```

**Table**

```
CLEAN_LISTINGS
```

---

## ✅ Silver Layer Output

- Duplicate records removed.
- Missing values handled.
- Data types corrected.
- Text values standardized.
- Invalid records filtered.
- Derived columns created.
- Clean dataset ready for the Gold Layer.
