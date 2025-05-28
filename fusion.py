import pandas as pd
import os

# Lire les fichiers CSV
clubs_df = pd.read_csv('./datasetfoot_exploitable/clubs.csv')
competitions_df = pd.read_csv('./datasetfoot_exploitable/competitions.csv')


# Fusionner les deux DataFrames sur l'identifiant de compétition
merged_df = clubs_df.merge(
    competitions_df,
    left_on='domestic_competition_id',
    right_on='competition_id',
    how='left'
)

# Créer un dossier de sortie
output_dir = './clubs_par_competition'
os.makedirs(output_dir, exist_ok=True)

# Sauvegarder un fichier CSV pour chaque compétition
for competition_id, group in merged_df.groupby('competition_id'):
    if pd.isna(competition_id):
        continue
    competition_name = group['competition_code'].iloc[0]  # Nom de la compétition
    safe_name = competition_name.replace('/', '-').replace('\\', '-').replace(' ', '_')
    filename = f"{safe_name}_{competition_id}.csv"
    file_path = os.path.join(output_dir, filename)
    group.to_csv(file_path, index=False)

print(f"Fichiers générés dans : {output_dir}")
