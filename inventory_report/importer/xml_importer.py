import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        if path.endswith(".xml"):
            with open(path) as file:
                data = file.read()
                return [
                    row for row in xmltodict.parse(data)["dataset"]["record"]
                ]
        else:
            raise ValueError("Arquivo inválido")
