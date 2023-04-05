import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def import_data(path):
        if path.endswith(".csv"):
            with open(path) as file:
                data = csv.DictReader(file)
                return [row for row in data]
        else:
            raise ValueError("Arquivo inválido")
