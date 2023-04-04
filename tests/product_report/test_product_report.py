from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        "01",
        "Deco X60",
        "TP-Link",
        "04/04/2023",
        "28/11/2023",
        "134004042023",
        "em ambiente refrigerado",
    )

    repr = product.__repr__()

    result = (
        "O produto Deco X60 fabricado em 04/04/2023"
        " por TP-Link com validade até 28/11/2023"
        " precisa ser armazenado em ambiente refrigerado."
    )

    assert repr == result
