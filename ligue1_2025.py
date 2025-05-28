import pandas as pd

# Charger le fichier CSV
df = pd.read_csv('./clubs_par_competition/ligue-1_FR1.csv')

# Filtrer les lignes où last_season est 2024
filtered_df = df[df['last_season'] == 2024]

count = 0
for n in filtered_df:
    count+=1

print(count)


# Enregistrer le nouveau fichier
#filtered_df.to_csv("clubs_saison_2025.csv", index=False)

#print("Fichier 'clubs_saison_2024.csv' créé avec succès.")
