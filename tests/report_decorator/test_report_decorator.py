from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport


def test_decorar_relatorio():
    mock = [
        {
            "id": "1",
            "nome_do_produto": "Deco X60",
            "nome_da_empresa": "TP-Link",
            "data_de_fabricacao": "2023-04-04",
            "data_de_validade": "2023-11-28",
            "numero_de_serie": "134004042023",
            "instrucoes_de_armazenamento": "em ambiente refrigerado",
        },
        {
            "id": "2",
            "nome_do_produto": "Deco M5",
            "nome_da_empresa": "TP-Link",
            "data_de_fabricacao": "2023-01-01",
            "data_de_validade": "2023-11-15",
            "numero_de_serie": "042023134004",
            "instrucoes_de_armazenamento": "em ambiente refrigerado",
        },
    ]

    colored = ColoredReport(SimpleReport)
    result = colored.generate(mock)

    assert result == (
        "\033[32mData de fabricação mais antiga:\033[0m"
        " \033[36m2023-01-01\033[0m\n"
        "\033[32mData de validade mais próxima:\033[0m"
        " \033[36m2023-11-15\033[0m\n"
        "\033[32mEmpresa com mais produtos:\033[0m \033[31mTP-Link\033[0m"
    )
