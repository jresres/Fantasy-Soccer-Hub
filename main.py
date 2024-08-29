from fasthtml.common import *

def NavBarSection():
    return (
        Div(
            Div(
                A('Home', href='#', cls='btn btn-ghost normal-case text-xl'),
                A('Leaderboard', href='#', cls='btn btn-ghost normal-case text-xl'),
                A('Team Stats', href='#', cls='btn btn-ghost normal-cfase text-xl'),
                A('Player Stats', href='#', cls='btn btn-ghost normal-case text-xl'),
                A('Trades', href='#', cls='btn btn-ghost normal-case text-xl'),
                cls='flex-1'
            ),
            cls='navbar bg-sky-900'
        )
    )

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
                    LeaderboardItem("2", "Jared", "20"),
                    LeaderboardItem("3", "Owen", "18"),
                    cls='p-4 w-1/2'
                ),
                cls='flex justify-center items-center'
            )
        )

# Loading tailwind and daisyui
tlink = Script(src="https://cdn.tailwindcss.com"),
dlink = Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/daisyui@4.11.1/dist/full.min.css")
app = FastHTML(hdrs=(tlink, dlink, picolink))

@app.get("/")
def homepage():
    title = "Fantasy Soccer Hub"

    return (
            Title(title), 
            Main(
                NavBarSection(),
                LeaderboardSection()
            )
            )

serve()