from fasthtml.common import *

def LeaderboardItem(place, player_name, points):
    return (Div(
                Div(f'{place}. {player_name}', cls='collapse-title text-xl font-medium'),
                Div(f'Points: {points}', cls='collapse-title text-xl font-medium text-right pr-16'),
                Div(
                    P('Content for item 1.'),
                    cls='collapse-content'
                ),
                tabindex='0',
                cls='collapse collapse-arrow border border-base-300 bg-base-100 rounded-box mt-2'
            ))

def LeaderboardSection():
    return (Div(
                Div(
                    H1("Leaderboard", cls='flex justify-center text-4xl font-bold mt-10 mb-4'),
                    LeaderboardItem("1", "Will", "10"),
                    LeaderboardItem("2", "Jared", "19"),
                    LeaderboardItem("3", "Owen", "18"),
                    cls='p-4 w-1/2'
                ),
                cls='flex justify-center items-center'
            )
        )