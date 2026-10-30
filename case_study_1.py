teams = {
    "Team A": [80, 75],
    "Team B": [90, 85],
    "Team C": [70, 70]
}

for team, scores in teams.items():
    print(team, "Total Score:", sum(scores))

ranking = sorted(
    teams.items(),
    key=lambda x: sum(x[1]),
    reverse=True
)

print("\nTeam Rankings:")
for rank, item in enumerate(ranking, 1):
    print(rank, item[0])