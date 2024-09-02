from fasthtml.common import *
from content import *

# Loading tailwind and daisyui
tlink = Script(src="https://cdn.tailwindcss.com"),
dlink = Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/daisyui@4.11.1/dist/full.min.css")

app = FastHTML(hdrs=(tlink, dlink))
db = database("data/fantasy_soccer.db")

def NavButton(title, is_active=False):
    classes = "btn btn-ghost normal-case text-xl"
    inactive = f"{classes}"
    active = f"{classes} bg-sky-700"

    return (A(
        title, 
        id=f'link-{title.lower().replace(' ','-')}', 
        cls=active if is_active else inactive,
        href=f"/{title.lower().replace(' ','_')}")
    )

def NavBarSection(currTab):
    return (Div(
        Div(
            *[NavButton(title, i==currTab) for i, title in enumerate(NAV_CONTENT)],
            cls='flex-1'
        ),
        cls='navbar bg-sky-900')
    )

def LeaderboardTeamTableItem(team_name, team_points):
    return (
        Td(team_name),
        Td(team_points)
    )

def LeaderboardTeamTable(UserID):
    user_teams = get_users_teams(UserID)
    return (
        Table(
            Thead(
                Tr(
                    Th('Team'),
                    Th('Points')
                )
            ),
            Tbody(
                *[Tr(LeaderboardTeamTableItem(team[0], team[1])) for team in user_teams]
            ),
            cls='table'
        )
    )

def LeaderboardItem(user, user_points=0):
    return (Div(
        Div(f'{user['UserName']}', cls='collapse-title text-xl font-medium'),
        Div(f'Points: {user_points}', cls='collapse-title text-xl font-medium text-right pr-16'),
        Div(
            Div(
                LeaderboardTeamTable(user['UserID']),
                cls='overflow-x-auto'
            ),
            cls='collapse-content'
        ),
        tabindex=0,
        cls='collapse collapse-arrow border border-base-300 bg-base-100 rounded-box mt-2')
    )

def LeaderboardSection():
    users = get_all_users(db)
    return (Div(
        Div(
            H1("Leaderboard", cls='flex justify-center text-4xl font-bold mt-6 mb-4'),
            *[LeaderboardItem(user) for user in users],
            cls='p-4 w-3/4'
        ),
        cls='flex justify-center')
    )

def LeagueTableTab(tabIndex, leagueName):
    checked_input = Input(type='radio', name='league_tabs', role='tab', aria_label=f'{leagueName}', cls='tab flex-1 text-center', checked='checked')
    unchecked_input = Input(type='radio', name='league_tabs', role='tab', aria_label=f'{leagueName}', cls='tab flex-1 text-center')

    return (
        (checked_input if tabIndex == 0 else unchecked_input)
        # Div(f'HERE', role='tabpanel', cls='tab-content'),
    )

@app.get("/")
def Home():
    return Leaderboard()

@app.get("/leaderboard")
def Leaderboard():
    title = "Fantasy Soccer Hub"
    return (
        Title(title), 
        Main(
            NavBarSection(currTab=0),
            LeaderboardSection())
    )

@app.get("/league_table")
def LeagueTable():
    leagues = get_all_leagues()

    return (
        NavBarSection(currTab=1),
        Div(
            *[LeagueTableTab(i, league[2]) for i, league in enumerate(leagues)],
            role='tablist',
            cls='tabs tabs-bordered flex justify-center'
        )
    )

@app.get("/player_table")
def LeagueTable():
    return (
        NavBarSection(currTab=2)
    )

@app.get("/free_agency_requests")
def LeagueTable():
    return (
        NavBarSection(currTab=3)
    )

serve()