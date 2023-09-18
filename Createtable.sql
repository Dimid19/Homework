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
INSERT INTO genre (name) VALUES
    ('Fantasy'),
    ('War'),
    ('Detective'),
    ('Horror'),
    ('Comedy'),
    ('Drama');
INSERT INTO movie (title, tagline, summary, release_year, genre_id)
VALUES
    ('Lord of the Rings','My precission','A journey to save Middle-earth', 2001,1),
    ('The hobbit','Smoge','Bilbo Baggins joins an adventure', 2012,1),
    ('Fury','Is the best joob','Tank crew mission', 2014,2),
    ('Sherloc','ELementarno','Modern-day Sherlock Holmes',2010,3),
    ('Mirors','Don`t see','Supernatural events in a mirror', 2008,4),
    ('Macho and Botan','Anti kisiak','Hilarious misadventures', 2007,5),
    ('Hatiko','Forewer love','Loyal dog tale of devotion', 2009,6);
INSERT INTO people (name, birth_day)
VALUES
     ('Cristofer Li','1990-01-15'),
     ('Bread Pitt','1985-03-20'),
     ('cumberbatch','1985-03-20'),
     ('Emi Smart','1970-07-10'),
     ('Jonnie Depp','1980-05-25'),
     ('Hachiko owner','1988-12-05');
INSERT INTO  movie_people (movie_id, people_id, name_personage, director, screenwriter)
VALUES
    (1,1,'Gendalf grey','Director1','screenwriter1'),
    (2,1, 'Gendalf grey','Director2','screenwriter2'),
    (3,2,'Don Kolnerr','Director3','screenwriter3'),
    (4,3,'Doktor Watsonn','Director4','screenwriter4'),
    (5,4,'Mary','Director5','screenwriter5'),
    (6,5,'Tom Henson','Director6','screenwriter6'),
    (7,6,'THe dog Hatiko','Director7','screenwriter7');