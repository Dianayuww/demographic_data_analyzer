import unittest
import demographic_data_analyzer
import pandas as pd

class UnitTests(unittest.TestCase):
    def test_calculate_demographic_data(self):
        actual = demographic_data_analyzer.calculate_demographic_data()
        
        self.assertAlmostEqual(actual['average_age_men'], 39.4, places=1)
        self.assertAlmostEqual(actual['percentage_bachelors'], 16.4, places=1)
        self.assertAlmostEqual(actual['higher_education_rich'], 46.5, places=1)
        self.assertAlmostEqual(actual['lower_education_rich'], 17.4, places=1)
        self.assertEqual(actual['min_work_hours'], 1)
        self.assertAlmostEqual(actual['rich_percentage'], 10.0, places=1)
        self.assertEqual(actual['highest_earning_country'], 'Iran')
        self.assertAlmostEqual(actual['highest_earning_country_percentage'], 41.9, places=1)
        self.assertEqual(actual['top_IN_occupation'], 'Prof-specialty')
