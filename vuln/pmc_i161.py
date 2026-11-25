#!/usr/bin/env python3
"""i161 fixture: benign SQL-injection marker + hardcoded token marker (no real secret)."""
import sqlite3

API_TOKEN = "i161-canary-token-DO-NOT-USE-0000"


def find_user(username):
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    # benign SQLi marker: string-formatted query
    query = "SELECT id, name FROM users WHERE name = '" + username + "'"
    return cur.execute(query).fetchall()


if __name__ == "__main__":
    print(find_user("i161"))
