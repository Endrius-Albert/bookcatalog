CREATE TABLE api_book (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    description TEXT,
    author VARCHAR(255),
    isbn VARCHAR(13),
    published_date DATE
);
