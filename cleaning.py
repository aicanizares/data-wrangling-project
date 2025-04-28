# Function to clean company names with hypens
def clean_company_hyphens(name):
    if isinstance(name, str):
        name = name.lower()
        name = name.replace("  ", " ")
        name = name.replace(" ", "-")
        name = name.replace(",", "-")
        name = name.replace(".", "-") if not name.endswith(".") else name[:-1]
        name = name.replace("[", "-").replace("]", "-")
        name = name.replace("_", "-")
        name = name.replace("!", "-")
    return name

df_gfi["Company"] = df_gfi["Company"].apply(clean_company_hyphens)


import unicodedata
# Function to remove accent marks and umlauts
def remove_accents(name):
    if isinstance(name, str):
        name = unicodedata.normalize('NFKD', name).encode('ASCII', 'ignore').decode('utf-8')
    return name

df_gfi["Company"] = df_gfi["Company"].apply(remove_accents)


# Function to clean company names by replacing punctuation marks (orthographic)
def clean_company_orthographic(x):
    if isinstance(x, str):
        x = x.replace("&", "")
        x = x.replace("'", "")
        x = x.replace("(", "").replace(")", "")
        x = x.replace(":", "")
    return x

df_gfi["Company"] = df_gfi["Company"].apply(clean_company_orthographic)


# Function to check category presence
def check_cheese(product_types):
    return any("cheese" in p.lower() for p in product_types)

def check_other_dairy(product_types):
    return any("other dairy" in p.lower() for p in product_types)

# Apply transformations to merged_df
merged_df["Product Type"] = merged_df["Product Type"].fillna("").apply(lambda x: x.split(","))