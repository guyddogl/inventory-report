from datetime import datetime
from collections import Counter


def oldest_manufacture(products):
    return min([product["data_de_fabricacao"] for product in products])


def closest_expiration(products):
    list = []
    for product in products:
        data_de_validade = datetime.strptime(
            product["data_de_validade"], "%Y-%m-%d"
        )
        if data_de_validade > datetime.now():
            list.append(product["data_de_validade"])
    return min(list)


def comp_with_more_products(products):
    company = [product["nome_da_empresa"] for product in products]
    return Counter(company).most_common(1)[0][0]


class SimpleReport:
    @staticmethod
    def generate(products):
        return (
            f"Data de fabricação mais antiga: {oldest_manufacture(products)}\n"
            f"Data de validade mais próxima: {closest_expiration(products)}\n"
            f"Empresa com mais produtos: {comp_with_more_products(products)}"
        )
