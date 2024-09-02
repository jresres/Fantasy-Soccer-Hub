import sqlite3

DB_NAME = "data/fantasy_soccer.db"

def get_all_users(db):
    dt = db.t
    userID_sql = f"""select * from {dt.Users}"""
    return db.q(userID_sql)

def get_users_teams(UserID):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT TeamName, TeamPoints FROM Teams WHERE UserID =?", (UserID,))
    user_teams = cursor.fetchall()

    conn.commit()
    conn.close()

    return user_teams

def get_all_leagues():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Leagues")
    leagues = cursor.fetchall()

    conn.commit()
    conn.close()

    return leagues

NAV_CONTENT = ["Leaderboard", "League Table", "Player Table", "Free Agency Requests"]