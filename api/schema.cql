CREATE TABLE IF NOT EXISTS news_site (
    link text,
    title text,
    score float,
    summary text,
    PRIMARY KEY (link)
) WITH CLUSTERING ORDER BY (score DESC)