from fasthtml.common import *

def TopBarSection():
    return Div()

def LeaderboardItem(player_name, points):
    return Label(f"{player_name}: {points}")


def LeaderboardSection():
    return (Div(
                H1('Leaderboard'),
                Div(
                    LeaderboardItem("Player 1", "0 Points")
                )
            ))

hdrs = []

app,rt = fast_app(live=True)

# Homepage
@rt('/')
def get():
    title = "Fantasy Soccer Hub"

    return (
            Title(title), 
            Main(
                TopBarSection(),
                LeaderboardSection()
            )
            )

serve()