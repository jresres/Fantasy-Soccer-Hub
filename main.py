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
        href="#",
        hx_get=f"/{title.lower().replace(' ','_')}",
        hx_target="#main-content")
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
        cls='collapse collapse-arrow border border-base-300 bg-base-100 rounded-box mt-2 hover:bg-slate-700')
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
            LeaderboardSection(),
            id="main-content")
    )

def LeagueTableTab(LeagueID, LeagueName):
    return (A(
        LeagueName,
        id=f'tab-{LeagueName.lower().replace(' ','-')}', 
        hx_get=f"/league_table/{LeagueID}",
        hx_target="#main-content",
        href='#',
        cls='tab tab-bordered flex-1 focus:border-b-2 hover:bg-gray-800'
    ))

@app.get("/league_table")
def LeagueTable():
    leagues = get_all_leagues()

    return (
        NavBarSection(currTab=1),
        Div(
            Div(
                *[LeagueTableTab(LeagueID=league[0], LeagueName=league[2]) for league in leagues],
                cls='tabs flex justify-center'
            ),
            cls='w-full'
        )
    )

def LeagueStandingsTableRow(team):
    return (
        Tr(
            Td(team[8]),
            Td(team[2]),
            Td(team[9]),
            Td(team[10]),
            Td(team[12]),
            Td(team[11]),
            Td(team[5]),
            Td(team[6]),
            Td(team[7]),
            Td(team[13]),
        )
    )

def LeagueStandingsTable(teams):
    return (
        Table(
            Thead(
                Tr(
                    Th('Rank'),
                    Th('Team'),
                    Th('MP'),
                    Th('W'),
                    Th('D'),
                    Th('L'),
                    Th("GF"),
                    Th('GA'),
                    Th('GD'),
                    Th('Points')
                )
            ),
            Tbody(
                *[LeagueStandingsTableRow(team) for team in teams]
            ),
            cls='table'
        )
    )

@app.get("/league_table/{LeagueID}")
def LeagueTableContent(LeagueID:int):
    teams = get_all_league_teams(LeagueID)
    return (
        LeagueTable(),
        Div(
            LeagueStandingsTable(teams),
            cls='overflox-x-auto'
        )
    )

@app.get("/player_table")
def PlayerTable():
    return (
        NavBarSection(currTab=2)
    )

@app.get("/free_agency_requests")
def FreeAgencyRequests():
    return (
        NavBarSection(currTab=3)
    )

serve()