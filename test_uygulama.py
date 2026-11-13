import csv
import tempfile
import unittest
from pathlib import Path

from uygulama import add_record, save_csv


class KodlamaTestleri(unittest.TestCase):
    def setUp(self):
        self.records = []
        self.counts = {}
        self.names = {}

    def add(self, code="P01", excerpt="Kurgusal alıntı", themes=("Eğitim",), **kwargs):
        return add_record(
            self.records,
            self.counts,
            self.names,
            code,
            excerpt,
            list(themes),
            **kwargs,
        )

    def test_normal_kayit(self):
        ok, _ = self.add()
        self.assertTrue(ok)
        self.assertEqual(self.counts["eğitim"], 1)

    def test_bosluk_harf_farki_ve_yinelenen_tema(self):
        self.add(themes=("Eğitim",))
        ok, _ = self.add(code="P02", themes=(" eğitim ", "EĞİTİM"))
        self.assertTrue(ok)
        self.assertEqual(self.counts["eğitim"], 2)
        self.assertEqual(self.records[-1]["themes"], ["Eğitim"])

    def test_birden_cok_farkli_tema(self):
        ok, _ = self.add(themes=("Eğitim", "Eşitsizlik"))
        self.assertTrue(ok)
        self.assertEqual(self.counts["eğitim"], 1)
        self.assertEqual(self.counts["eşitsizlik"], 1)

    def test_bos_alinti_kaydi_engeller(self):
        ok, _ = self.add(excerpt="   ")
        self.assertFalse(ok)
        self.assertEqual(self.records, [])
        self.assertEqual(self.counts, {})

    def test_tanitici_bilgi_maskelenmediyse_kaydi_engeller(self):
        ok, _ = self.add(has_identifiers=True, sanitized_excerpt="")
        self.assertFalse(ok)
        self.assertEqual(self.records, [])

    def test_maskelenmis_alinti_kaydedilir(self):
        ok, _ = self.add(
            has_identifiers=True,
            sanitized_excerpt="[KİŞİ] [YER] hakkında konuştu.",
        )
        self.assertTrue(ok)
        self.assertIn("[KİŞİ]", self.records[0]["excerpt"])

    def test_gecersiz_takma_kod_kaydi_engeller(self):
        ok, _ = self.add(code="Gerçek Ad")
        self.assertFalse(ok)
        self.assertEqual(self.records, [])

    def test_csv_kayit_ve_tema_toplamini_yazar(self):
        self.add(themes=("Eğitim", "Eşitsizlik"))
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "sonuc.csv"
            save_csv(path, self.records, self.counts, self.names)
            with path.open(encoding="utf-8", newline="") as csv_file:
                rows = list(csv.reader(csv_file))
        self.assertEqual(len(rows), 4)
        self.assertEqual(rows[1][0], "Kayıt")
        self.assertEqual(rows[2][0], "Tema toplamı")
        self.assertEqual(rows[3][0], "Tema toplamı")


if __name__ == "__main__":
    unittest.main(verbosity=2)
