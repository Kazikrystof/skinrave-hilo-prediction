import json
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

# Načtení JSONu
with open("stats.json", "r", encoding="utf-8") as f:
    data = json.load(f)

console.print(
    Panel.fit(
        f"[bold cyan]Celkem záznamů:[/bold cyan] {data['total_records']}",
        title="Hi-Lo Statistiky",
    )
)

table = Table(show_header=True, header_style="bold magenta")

table.add_column("Karta", justify="center")
table.add_column("Výskyt", justify="right")
table.add_column("↑ Vyšší", justify="right", style="green")
table.add_column("↓ Nižší", justify="right", style="red")
table.add_column("= Stejná", justify="right", style="yellow")
table.add_column("% Vyšší", justify="right", style="green")
table.add_column("% Nižší", justify="right", style="red")
table.add_column("% Stejná", justify="right", style="yellow")

cards = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

for card in cards:
    s = data[card]["stats"]
    total = s["count"]

    higher = s["next_higher"] / total * 100
    lower = s["next_lower"] / total * 100
    equal = s["equal"] / total * 100

    table.add_row(
        card,
        str(total),
        str(s["next_higher"]),
        str(s["next_lower"]),
        str(s["equal"]),
        f"{higher:.1f}%",
        f"{lower:.1f}%",
        f"{equal:.1f}%"
    )

console.print(table)