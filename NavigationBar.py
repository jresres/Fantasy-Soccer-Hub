from fasthtml.common import *

def NavBarSection():
    return (
        Div(
            Div(
                A('Leaderboard', href='#', cls='btn btn-ghost normal-case text-xl'),
                A('League Table', href='#', cls='btn btn-ghost normal-case text-xl'),
                A('Player Table', href='#', cls='btn btn-ghost normal-cfase text-xl'),
                A('Free Agency Requests', href='#', cls='btn btn-ghost normal-case text-xl'),
                cls='flex-1'
            ),
            cls='navbar bg-sky-900'
        )
    )