import unittest
import os
import shutil
import pandas as pd

from script import main  # Suppose que ton script est dans un fichier `script.py`

class TestClubCSVGeneration(unittest.TestCase):

    def setUp(self):
        # Créer un dossier temporaire pour les tests
        self.test_input_dir = './test_dataset'
        self.test_output_dir = './clubs_par_competition'
        os.makedirs(self.test_input_dir, exist_ok=True)

        # Fichier clubs.csv
        clubs_data = {
            'club_id': [1, 2],
            'name': ['Club A', 'Club B'],
            'domestic_competition_id': ['C1', 'C1']
        }
        pd.DataFrame(clubs_data).to_csv(f'{self.test_input_dir}/clubs.csv', index=False)

        # Fichier competitions.csv
        competitions_data = {
            'competition_id': ['C1'],
            'competition_code': ['L1']
        }
        pd.DataFrame(competitions_data).to_csv(f'{self.test_input_dir}/competitions.csv', index=False)

        # Remplacer les chemins dans le script si nécessaire
        self.original_clubs_path = './datasetfoot_exploitable/clubs.csv'
        self.original_competitions_path = './datasetfoot_exploitable/competitions.csv'

        os.makedirs('./datasetfoot_exploitable', exist_ok=True)
        shutil.copy(f'{self.test_input_dir}/clubs.csv', self.original_clubs_path)
        shutil.copy(f'{self.test_input_dir}/competitions.csv', self.original_competitions_path)

    def tearDown(self):
        # Nettoyage après chaque test
        shutil.rmtree(self.test_input_dir)
        shutil.rmtree('./datasetfoot_exploitable', ignore_errors=True)
        if os.path.exists(self.test_output_dir):
            shutil.rmtree(self.test_output_dir)

    def test_files_generated(self):
        main()
        # Vérifier que le fichier attendu existe
        expected_file = os.path.join(self.test_output_dir, 'L1_C1.csv')
        self.assertTrue(os.path.exists(expected_file))

        # Vérifier le contenu
        df = pd.read_csv(expected_file)
        self.assertEqual(len(df), 2)
        self.assertIn('club_id', df.columns)
        self.assertIn('competition_code', df.columns)

if __name__ == '__main__':
    unittest.main()
