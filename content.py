def get_all_users(db):
    dt = db.t
    userID_sql = f"""select * from {dt.Users}"""
    return db.q(userID_sql)

NAV_CONTENT = ["Leaderboard", "League Table", "Player Table", "Free Agency Requests"]