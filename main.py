import psycopg2
import pandas as pd

# Подключение к БД
conn = psycopg2.connect(
    dbname="anime_db",
    user="anuar21",
    password="",
    host="localhost",
    port="5432"
)

queries = {
    "top_10_by_episodes": """
        SELECT name, episodes
        FROM anime
        WHERE episodes ~ '^[0-9]+$'
        ORDER BY CAST(episodes AS INTEGER) DESC
        LIMIT 10;
    """,
    "top_10_by_avg_rating": """
        SELECT a.name, ROUND(AVG(r.rating)::numeric, 2) AS avg_rating, COUNT(r.user_id) AS votes
        FROM rating r
        JOIN anime a ON r.anime_id = a.anime_id
        GROUP BY a.name
        HAVING COUNT(r.user_id) > 1000
        ORDER BY avg_rating DESC
        LIMIT 10;
    """,
    "top_10_by_members": """
        SELECT name, members
        FROM anime
        ORDER BY members DESC
        LIMIT 10;
    """,
    "anime_by_type": """
        SELECT type, COUNT(*) AS total
        FROM anime
        WHERE type IS NOT NULL
        GROUP BY type
        ORDER BY total DESC
        LIMIT 10;
    """,
    "top_10_low_rating": """
        SELECT name, rating
        FROM anime
        WHERE rating IS NOT NULL
        ORDER BY rating ASC
        LIMIT 10;
    """,
    "top_10_high_rating": """
        SELECT name, rating
        FROM anime
        WHERE rating IS NOT NULL
        ORDER BY rating DESC
        LIMIT 10;
    """,
    "anime_by_genre": """
        SELECT genre, COUNT(*) AS total
        FROM anime
        WHERE genre IS NOT NULL
        GROUP BY genre
        ORDER BY total DESC
        LIMIT 10;
    """,
    "top_10_shortest": """
        SELECT name, episodes
        FROM anime
        WHERE episodes ~ '^[0-9]+$'
        ORDER BY CAST(episodes AS INTEGER) ASC
        LIMIT 10;
    """,
    "top_10_action": """
        SELECT name, rating, members
        FROM anime
        WHERE genre ILIKE '%Action%' AND rating IS NOT NULL
        ORDER BY rating DESC
        LIMIT 10;
    """,
    "avg_rating_by_type": """
        SELECT type, ROUND(AVG(rating)::numeric, 2) AS avg_rating
        FROM anime
        WHERE rating IS NOT NULL AND type IS NOT NULL
        GROUP BY type
        ORDER BY avg_rating DESC
        LIMIT 10;
    """
}

# Выполняем все запросы
for name, query in queries.items():
    df = pd.read_sql_query(query, conn)
    print(f"=== {name} ===")
    print(df, "\n")
    df.to_csv(f"query_results/{name}.csv", index=False)

conn.close()
print("Готово! Все запросы выполнены и сохранены в папке 'query_results'.")
