from rich.console import Console
from rich.table import Table
from scraper import search_products


def create_table():
    products = search_products('teclado mecanico rgb')

    table = Table(title="Resultados")
    table.add_column("Produto",  style="cyan")
    table.add_column("Preço", style="magenta")
    table.add_column("Loja",style="green")
    table.add_column("Link",  style="purple")

    for product in products:
        table.add_row(
            product['title'],
            (product['price']),
            product['store'],
            f"[link={product['link'].replace(' ', '%20')}]Ver produto[/link]"
        )

    console = Console()
    console.print(table)

create_table()



