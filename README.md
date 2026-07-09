# 🥉 Bronze Layer

The **Bronze Layer** is the first stage of the Medallion Architecture. It stores the raw real estate data exactly as received from the source without any transformations. This layer ensures complete data traceability and serves as the foundation for all downstream processing.

---

## 📥 Data Source

- Source File: `real-estate-raw.csv`
- Format: CSV
- Loaded using: `python/load_bronze.py`

---

## ⚙️ Processing Steps

The Bronze ingestion process performs the following operations:

1. Read the raw CSV dataset.
2. Connect to Snowflake.
3. Create the **BRONZE** schema (if it does not already exist).
4. Create the `RAW_LISTINGS` table.
5. Load the raw data into Snowflake.
6. Add a metadata column named `_loaded_at` to record the loading timestamp.

---

## 🏗️ Bronze Architecture

```text
          real-estate-raw.csv
                   │
                   ▼
      Python Script (load_bronze.py)
                   │
                   ▼
        Snowflake BRONZE Schema
                   │
                   ▼
             RAW_LISTINGS
         + _loaded_at Metadata
```

---

## 📂 Files Used

```text
python/
└── load_bronze.py

dags/
└── data/
    └── real-estate-raw.csv
```

---

## 📋 Bronze Table

**Table Name**

```
BRONZE.RAW_LISTINGS
```

### Main Columns

- listing_id
- property_type
- country
- city
- neighborhood
- surface_m2
- num_rooms
- num_bathrooms
- floor
- year_built
- price
- listing_date
- condition
- heating_type
- parking
- energy_rating
- _loaded_at

---

## ✅ Bronze Layer Output

- Raw data preserved without modification.
- Complete data traceability.
- Metadata added for audit purposes.
- Ready for transformation in the Silver Layer.
