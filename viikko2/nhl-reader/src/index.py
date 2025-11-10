from rich.table import Table
from rich.console import Console

from player_reader import PlayerReader
from player_stats import PlayerStats


def main():
    console = Console()
    season = input("Season [2018-19, 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26]: ")
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"

    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    nationalities = stats.get_nationalities()

    while True:
        nationality = input(f"Nationality [{nationalities}]").upper()
        players = stats.top_scorers_by_nationality(nationality)




        table = Table(title=f"[italic]Season {season} players from {nationality}[/italic]")

        table.add_column("Name", style="cyan")
        table.add_column("Teams", style="green")
        table.add_column("Goals", justify="right")
        table.add_column("Assists", justify="right")
        table.add_column("Points", justify="right")



        for p in players:
            table.add_row(p.name, p.team, str(p.goals), str(p.assists), str(p.goals + p.assists))

        console.print(table)


if __name__ == "__main__":
    main()
