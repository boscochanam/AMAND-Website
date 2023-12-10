from googlesearch import search
import pandas as pd

def google_search(query, num_results=10):
    links = []
    for j in search(query, num_results=num_results):
        if 'youtube' in j:
            continue
        links.append(j)
    return links

# Example: searching for "AMAND" with "pune" or "manipur"
query = 'AMAND pune OR AMAND manipur'

# Number of results to retrieve
num_results = 100

# Perform Google search
search_results = google_search(query, num_results)

# Create a DataFrame with the results
df = pd.DataFrame({'News Link': search_results, 'Website': ['Google Search'] * len(search_results)})

# Save the DataFrame to a CSV file
df.to_csv('google_search_results.csv', index=False)
