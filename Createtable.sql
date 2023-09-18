DROP TABLE IF EXISTS movie CASCADE;
CREATE TABLE genre
(
    id      SERIAL PRIMARY KEY,
    name    VARCHAR(255) NOT NULL
);
CREATE TABLE movie
(
    id      SERIAL PRIMARY KEY,
    title   VARCHAR(255) NOT NULL CHECK (length(title) > 0),
    tagline VARCHAR(255),
    summary TEXT NOT NULL,
    release_year INT,
    genre_id INTEGER REFERENCES genre(id)
);
CREATE TABLE people
(
    id      SERIAL PRIMARY KEY,
    name    VARCHAR(255) NOT NULL,
    birth_day DATE
);