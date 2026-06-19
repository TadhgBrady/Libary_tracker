CREATE TABLE IF NOT EXISTS books (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    genre TEXT,
    year_published INT
);

INSERT INTO books (title, author, genre, year_published) VALUES
('The Great Gatsby', 'F. Scott Fitzgerald', 'Fiction', 1925),
('To Kill a Mockingbird', 'Harper Lee', 'Fiction', 1960),
('1984', 'George Orwell', 'Dystopian', 1949),
('Pride and Prejudice', 'Jane Austen', 'Romance', 1813),
('The Catcher in the Rye', 'J.D. Salinger', 'Fiction', 1951);