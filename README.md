Voici la version mise à jour du `README.md` avec la mention claire que les données proviennent d’un **web scraping de Transfermarkt** :

---

````markdown
# 📊 Regroupement des Clubs de Football par Compétition

Ce projet Python permet de fusionner deux fichiers CSV contenant :
- la liste de **tous les clubs professionnels mondiaux**
- la liste de **toutes les compétitions nationales**

Le but est de **regrouper les clubs par compétition nationale** et de générer automatiquement un fichier CSV pour chaque ligue (Ligue 1, Premier League, Serie A, etc.).

---

## 📁 Source des données

Les données utilisées dans ce projet sont issues d’un **web scraping du site [Transfermarkt](https://www.transfermarkt.com/)**, une référence mondiale pour les informations sur les clubs, joueurs, transferts et compétitions de football.

---

## 📁 Fichiers d'entrée

Les fichiers doivent être placés dans le dossier `./datasetfoot_exploitable/` :

- `clubs.csv` : contient les informations des clubs avec un champ `domestic_competition_id`
- `competitions.csv` : contient les compétitions avec un champ `competition_id` et `name`

---

## ⚙️ Fonctionnement du script

Le script `fusion.py` :

1. Charge les deux fichiers CSV avec **pandas**
2. Fusionne les deux tables via l’identifiant `domestic_competition_id`
3. Regroupe les clubs par compétition
4. Génère un fichier CSV par compétition dans un dossier de sortie

---

## 🏁 Lancer le script

Assurez-vous d’avoir **Python 3** et **pandas** installés :

```bash
pip install pandas
````

Puis exécutez :

```bash
python3 datasetfoot_exploitable/fusion.py
```

Les fichiers seront générés dans le dossier : `/mnt/data/clubs_par_competition`

---

## 📦 Exemple de sortie

* `Premier_League_ENG.csv`
* `Ligue_1_FRA.csv`
* `Bundesliga_GER.csv`

Chaque fichier contient toutes les informations du club (nom, pays, compétition, etc.).

---

## 🧾 Auteurs

* 🧑‍💻 Projet développé par \[Ton Nom] pour organiser les données des clubs mondiaux par ligue.

---

## 📜 Licence

Ce projet est open source sous licence MIT.


