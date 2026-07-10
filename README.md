# 🥉 Couche Bronze

La **Couche Bronze** constitue la première étape de l’architecture **Medallion**. Elle stocke les données immobilières brutes exactement telles qu’elles sont reçues depuis la source, sans aucune transformation. Cette couche garantit une traçabilité complète des données et sert de base pour tous les traitements ultérieurs.

---

## 📥 Source des données

* Fichier source : `real-estate-raw.csv`
* Format : CSV
* Chargement effectué par : `python/load_bronze.py`

---

## ⚙️ Étapes de traitement

Le processus d’ingestion de la couche Bronze réalise les opérations suivantes :

1. Lecture du jeu de données CSV brut.
2. Connexion à Snowflake.
3. Création du schéma **BRONZE** (s’il n’existe pas déjà).
4. Création de la table `RAW_LISTINGS`.
5. Chargement des données brutes dans Snowflake.
6. Ajout d’une colonne de métadonnées nommée `_loaded_at` afin d’enregistrer la date et l’heure du chargement.

---

## 🏗️ Architecture Bronze

```text
          real-estate-raw.csv
                   │
                   ▼
      Script Python (load_bronze.py)
                   │
                   ▼
      Schéma BRONZE dans Snowflake
                   │
                   ▼
             RAW_LISTINGS
      + Métadonnée _loaded_at
```

---

## 📂 Fichiers utilisés

```text
python/
└── load_bronze.py

dags/
└── data/
    └── real-estate-raw.csv
```

---

## 📋 Table Bronze

**Nom de la table**

```text
BRONZE.RAW_LISTINGS
```

### Colonnes principales

* listing_id
* property_type
* country
* city
* neighborhood
* surface_m2
* num_rooms
* num_bathrooms
* floor
* year_built
* price
* listing_date
* condition
* heating_type
* parking
* energy_rating
* _loaded_at

---

## ✅ Résultat de la Couche Bronze

* Conservation des données brutes sans modification.
* Traçabilité complète des données.
* Ajout de métadonnées à des fins d’audit et de suivi.
* Données prêtes à être transformées dans la **Couche Silver**.
