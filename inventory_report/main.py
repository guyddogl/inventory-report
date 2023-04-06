import sys
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor


def main():

    if len(sys.argv) <= 2:
        return print("Verifique os argumentos", file=sys.stderr)

    _, path, type = sys.argv

    data = ""

    if path.endswith(".csv"):
        data = InventoryRefactor(CsvImporter)
    if path.endswith(".json"):
        data = InventoryRefactor(JsonImporter)
    if path.endswith(".xml"):
        data = InventoryRefactor(XmlImporter)

    result = data.import_data(path, type)

    print(result, end="")


if __name__ == "__main__":
    main()
