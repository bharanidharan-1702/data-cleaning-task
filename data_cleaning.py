import pandas as pd

# STEP 1: Load dataset
df = pd.read_csv("netflix_titles.csv")

# STEP 2: Check sample (for your understanding)
print(df['date_added'].head())

# STEP 3: FIX DATE COLUMN (THIS IS THE REAL FIX)
df['date_added'] = df['date_added'].str.strip()

df['date_added'] = pd.to_datetime(
    df['date_added'],
    format='%B %d, %Y',   # <-- THIS MATCHES YOUR DATASET
    errors='coerce'
)

# Fill missing values
df['date_added'].fillna(method='ffill', inplace=True)

# STEP 4: Handle missing values
df['director'].fillna("Unknown", inplace=True)
df['cast'].fillna("Not Available", inplace=True)
df['country'].fillna("Unknown", inplace=True)
df['rating'].fillna("Not Rated", inplace=True)

# STEP 5: Remove duplicates
df.drop_duplicates(inplace=True)

# STEP 6: Standardize text
df['type'] = df['type'].str.lower()
df['country'] = df['country'].str.title()

# STEP 7: Clean spaces
df['title'] = df['title'].str.strip()
df['director'] = df['director'].str.strip()

# STEP 8: Rename columns
df.columns = df.columns.str.lower().str.replace(" ", "_")

# STEP 9: Save cleaned dataset
df.to_csv("cleaned_netflix_data.csv", index=False)

print("✅ DONE — Your cleaned file is ready!")