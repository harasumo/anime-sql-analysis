-- 1. Топ-10 аниме по количеству серий
SELECT name, episodes
FROM anime
WHERE episodes ~ '^[0-9]+$'
ORDER BY CAST(episodes AS INTEGER) DESC
LIMIT 10;

-- 2. Топ-10 аниме по среднему рейтингу (у которых хотя бы 1000 участников)
SELECT a.name, ROUND(AVG(r.rating)::numeric, 2) AS avg_rating, COUNT(r.user_id) AS votes
FROM rating r
JOIN anime a ON r.anime_id = a.anime_id
GROUP BY a.name
HAVING COUNT(r.user_id) > 1000
ORDER BY avg_rating DESC
LIMIT 10;

-- 3. Топ-10 самых популярных аниме по количеству участников (members)
SELECT name, members
FROM anime
ORDER BY members DESC
LIMIT 10;

-- 4. Количество аниме по типу
SELECT type, COUNT(*) AS total
FROM anime
WHERE type IS NOT NULL
GROUP BY type
ORDER BY total DESC
LIMIT 10;

-- 5. Топ-10 аниме с самым низким рейтингом (без NULL)
SELECT name, rating
FROM anime
WHERE rating IS NOT NULL
ORDER BY rating ASC
LIMIT 10;

-- 6. Топ-10 аниме с самым высоким рейтингом (без NULL)
SELECT name, rating
FROM anime
WHERE rating IS NOT NULL
ORDER BY rating DESC
LIMIT 10;

-- 7. Топ-10 жанров по количеству аниме
SELECT genre, COUNT(*) AS total
FROM anime
WHERE genre IS NOT NULL
GROUP BY genre
ORDER BY total DESC
LIMIT 10;

-- 8. Топ-10 самых коротких аниме (по эпизодам, фильтруем Unknown)
SELECT name, episodes
FROM anime
WHERE episodes ~ '^[0-9]+$'
ORDER BY CAST(episodes AS INTEGER) ASC
LIMIT 10;

-- 9. Топ-10 аниме жанра "Action" по рейтингу
SELECT name, rating, members
FROM anime
WHERE genre ILIKE '%Action%' AND rating IS NOT NULL
ORDER BY rating DESC
LIMIT 10;

-- 10. Средний рейтинг по типу аниме
SELECT type, ROUND(AVG(rating)::numeric, 2) AS avg_rating
FROM anime
WHERE rating IS NOT NULL AND type IS NOT NULL
GROUP BY type
ORDER BY avg_rating DESC
LIMIT 10;
