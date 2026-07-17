# Silver Layer

The **Silver Layer** is responsible for cleaning, validating, and enriching the raw data from the Bronze layer using **dbt**. The objective is to produce reliable, standardized datasets ready for analytical modeling in the Gold layer.

---

## Data Cleaning

The following transformations are applied:

- ✅ Remove duplicate records.
- ✅ Handle missing values (`NULL` values).
- ✅ Convert incorrect data types.
- ✅ Normalize property types (Apartment, Villa, House, etc.).
- ✅ Standardize parking values (Yes / No).
- ✅ Standardize heating types.
- ✅ Parse inconsistent date formats.
- ✅ Remove unrealistic property prices.
- ✅ Remove invalid surface values (≤ 0).

---

## Derived Columns

Additional business metrics are created:

| Column | Description |
|---------|-------------|
| `price_per_m2` | Property price divided by surface area. |
| `property_age` | Age of the property calculated from the construction year. |

---

## Data Quality Rules

The Silver layer ensures that:

- No duplicate records exist.
- Required fields are not null.
- Prices are greater than zero.
- Surface values are positive.
- Property types follow a consistent naming convention.
- Parking and heating values are standardized.
- Dates are stored using a consistent format.

---

## Output

The cleaned datasets are stored in the **Silver** schema and are used as the input for the Gold layer, where dimensional models and business metrics are created.

