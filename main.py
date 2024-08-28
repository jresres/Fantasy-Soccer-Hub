from fasthtml.common import *
from fa6_icons import svgs,dims

def NavBarSection():
    return (
        Div(
            Div(
                A('Home', href='#', cls='btn btn-ghost normal-case text-xl'),
                A('Leaderboard', href='#', cls='btn btn-ghost normal-case text-xl'),
                A('Team Stats', href='#', cls='btn btn-ghost normal-case text-xl'),
                A('Player Stats', href='#', cls='btn btn-ghost normal-case text-xl'),
                A('Trades', href='#', cls='btn btn-ghost normal-case text-xl'),
                cls='flex-1'
            ),
            cls='navbar bg-sky-900'
        )
    )

def LeaderboardSection():
    return (Div(
                Div(
                    Div('Will', cls='collapse-title text-xl font-medium'),
                    Div(
                        P('Content for item 1.'),
                        cls='collapse-content'
                    ),
                    tabindex='0',
                    cls='collapse collapse-arrow border border-base-300 bg-base-100 rounded-box'
                ),
                Div(
                    Div('Jared', cls='collapse-title text-xl font-medium'),
                    Div(
                        P('Content for item 2.'),
                        cls='collapse-content'
                    ),
                    tabindex='0',
                    cls='collapse collapse-arrow border border-base-300 bg-base-100 rounded-box mt-2'
                ),
                Div(
                    Div('Owen', cls='collapse-title text-xl font-medium'),
                    Div(
                        P('Content for item 3.'),
                        cls='collapse-content'
                    ),
                    tabindex='0',
                    cls='collapse collapse-arrow border border-base-300 bg-base-100 rounded-box mt-2'
                ),
                cls='p-4'
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