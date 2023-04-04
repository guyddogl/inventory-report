from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        "01",
        "Deco X60",
        "TP-Link",
        "04/04/2023",
        "não há",
        "134004042023",
        "Ambiente refrigerado",
    )

    assert product.id == "01"
    assert product.nome_do_produto == "Deco X60"
    assert product.nome_da_empresa == "TP-Link"
    assert product.data_de_fabricacao == "04/04/2023"
    assert product.data_de_validade == "não há"
    assert product.numero_de_serie == "134004042023"
    assert product.instrucoes_de_armazenamento == "Ambiente refrigerado"
