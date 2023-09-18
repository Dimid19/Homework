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
--CREATE TABLE movie_people
Create table movie_people
(
    PRIMARY KEY (movie_id, people_id)
    movie_id INTEGER REFERENCES movie(id),
    people_id INTEGER REFERENCES people(id),
    name_personage    VARCHAR(255) NOT NULL,
    director          VARCHAR(255) NOT NULL,
    screenwriter      VARCHAR(255) NOT NULL
);