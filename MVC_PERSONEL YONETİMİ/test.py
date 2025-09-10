import unittest
import sqlite3
import os
from model import create_table, add_personel, get_all_personeller, update_personel, delete_personel, calculate_maas

class TestPersonelManagement(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Test sınıfı başlatıldığında veritabanı ve tablo oluşturulur."""
        create_table()

    def setUp(self):
        """Her testten önce veritabanını temizler."""
        self.conn = sqlite3.connect('personel_veritabanı.db', timeout=10)
        self.cursor = self.conn.cursor()
        self.cursor.execute("DELETE FROM personeller")
        self.conn.commit()
        self.conn.close()

    def test_add_personel(self):
        """Personel ekleme test."""
        add_personel("Ali", 100)
        personeller = get_all_personeller()
        self.assertEqual(len(personeller), 1)
        self.assertEqual(personeller[0][1], "Ali")
        self.assertEqual(personeller[0][5], 100)

    def test_get_all_personeller(self):
        """Tüm personelleri alma test."""
        add_personel("Ali", 100)
        add_personel("Ayşe", 150)
        personeller = get_all_personeller()
        self.assertEqual(len(personeller), 2)
        self.assertEqual(personeller[0][1], "Ali")
        self.assertEqual(personeller[1][1], "Ayşe")

    def test_update_personel(self):
        """Personel güncelleme test."""
        add_personel("Ali", 100)
        personeller = get_all_personeller()
        personel_id = personeller[0][0]
        update_personel(personel_id, "Ali Veli", None,None,0)
        updated_personeller = get_all_personeller()
        self.assertEqual(updated_personeller[0][1], "Ali Veli")
       
        self.assertTrue(updated_personeller[0][5])

    def test_delete_personel(self):
        """Personel silme test."""
        add_personel("Ali", 100)
        personeller = get_all_personeller()
        personel_id = personeller[0][0]
        delete_personel(personel_id)
        personeller_after_delete = get_all_personeller()
        self.assertEqual(len(personeller_after_delete), 0)

    def test_calculate_maas(self):
        """Maaş hesaplama test."""
        add_personel("Ayşe", 100)
        personeller = get_all_personeller()
        personel_id = personeller[0][0]
        update_personel(personel_id, "Ayşe", "2025-06-12T09:00:00", None, 0)
        maas = calculate_maas(personel_id)
        self.assertAlmostEqual(maas, 100.0)

    @classmethod
    def tearDownClass(cls):
        """Test sınıfı bittiğinde veritabanı dosyasını siler."""
        if os.path.exists('personel_veritabanı.db'):
            os.remove('personel_veritabanı.db')
   
# Test sınıfı, unittest modülü ile testleri çalıştırmak için kullanılır.
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)