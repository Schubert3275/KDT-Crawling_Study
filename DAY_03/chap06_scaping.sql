-- Active: 1706666516440@@127.0.0.1@3306@scraping
CREATE DATABASE scraping;

USE scraping;

DROP TABLE IF EXISTS pages;

CREATE TABLE
    pages (
        id BIGINT(7) NOT NULL AUTO_INCREMENT,
        title VARCHAR(200),
        content VARCHAR(10000),
        created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (id)
    );

DESCRIBE pages;

INSERT INTO
    pages (title, content)
VALUES
    ('Test page title', 'This is some test page content. It can be up to 10,000 characters long.');

INSERT INTO
    pages (title, content)
VALUES
    ('Second page title', 'This is the second test page content');

SELECT
    *
FROM
    pages
WHERE
    id = 2;

SELECT
    *
FROM
    pages
WHERE
    title LIKE '%test%';

SELECT
    id,
    title,
    created
FROM
    pages
WHERE
    content LIKE '%second%';

DELETE FROM pages
WHERE
    id = 1;

SELECT
    *
FROM
    pages;

UPDATE pages
SET
    title = 'A new title',
    content = 'Some new content'
WHERE
    id = 2;

SELECT
    *
FROM
    pages;
