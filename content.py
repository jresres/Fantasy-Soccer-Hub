import sqlite3

DB_NAME = "data/fantasy_soccer.db"

def get_all_users():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Users ORDER BY UserTeamPoints DESC")
    users = cursor.fetchall()

    conn.commit()
    conn.close()

    return users

def get_users_teams(UserID):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT TeamName, TeamPoints FROM Teams WHERE UserID =? ORDER BY TeamPoints DESC", (UserID,))
    user_teams = cursor.fetchall()

    conn.commit()
    conn.close()

    return user_teams

def get_all_leagues():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Leagues ORDER BY LeagueID ASC")
    leagues = cursor.fetchall()

    conn.commit()
    conn.close()

    return leagues

def get_all_players():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Players")
    players = cursor.fetchall()

    conn.commit()
    conn.close()

    return players

def get_all_league_teams(LeagueID):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Teams WHERE LeagueID =? ORDER BY TeamRank ASC", (LeagueID,))
    league_teams = cursor.fetchall()

    conn.commit()
    conn.close()

    return league_teams

NAV_CONTENT = ["Leaderboard", "League Table", "Player Table", "Free Agency Requests"]