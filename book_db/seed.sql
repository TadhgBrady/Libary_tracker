CREATE TABLE IF NOT EXISTS books (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    genre TEXT,
    year_published INT,
    isbn TEXT UNIQUE,
    rating FLOAT,
    read BOOLEAN DEFAULT FALSE
);

CREATE TABLE IF NOT EXISTS comments (
    id SERIAL PRIMARY KEY,
    content TEXT NOT NULL,
    book_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (book_id) REFERENCES books(id) ON DELETE CASCADE
);

INSERT INTO books (title, author, genre, year_published, isbn, rating, read) VALUES
('The Great Gatsby', 'F. Scott Fitzgerald', 'Fiction', 1925, '978-0-7432-7356-5', 3.9, TRUE),
('To Kill a Mockingbird', 'Harper Lee', 'Fiction', 1960, '978-0-06-112008-4', 4.3, TRUE),
('1984', 'George Orwell', 'Dystopian', 1949, '978-0-451-52493-2', 4.2, FALSE),
('Pride and Prejudice', 'Jane Austen', 'Romance', 1813, '978-0-14-143951-8', 4.6, TRUE),
('The Catcher in the Rye', 'J.D. Salinger', 'Fiction', 1951, '978-0-316-76948-0', 3.8, FALSE);

INSERT INTO comments (content, book_id) VALUES
('A classic that never gets old', 1),
('Amazing story about social injustice', 2),
('Thought-provoking and dystopian', 3);