from inventory_report.reports.simple_report import (
    SimpleReport,
    oldest_manufacture,
    closest_expiration,
    comp_with_more_products,
)
from collections import Counter


def products_in_stock(products):
    company = [product["nome_da_empresa"] for product in products]
    count = Counter(company).items()
    result = ""
    for company in count:
        name, amount = company
        result += f"- {name}: {amount}\n"
    return result


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(products):
        return (
            f"Data de fabricação mais antiga: {oldest_manufacture(products)}\n"
            f"Data de validade mais próxima: {closest_expiration(products)}\n"
            f"Empresa com mais produtos: {comp_with_more_products(products)}\n"
            f"Produtos estocados por empresa:\n{products_in_stock(products)}"
        )
