
-- script to create all the tables in the database and populate with test data
-- still need to worry about what happens when users or listings are deleted

USE book_exchange;

-- uncomment the drops below to reset the database
-- DROP TABLE pinned_book;
-- DROP TABLE transaction;
-- DROP TABLE book_for_sale;
-- DROP TABLE school_uses_book;
-- DROP TABLE book;
-- DROP TABLE user;
-- DROP TABLE school;

CREATE TABLE school (
    name varchar(100) NOT NULL,
    city varchar(100) NOT NULL,
    state varchar(100) NOT NULL,
    PRIMARY KEY (name)
);

CREATE TABLE user (
    id int NOT NULL AUTO_INCREMENT, 
    first_name varchar(100) NOT NULL, 
    last_name varchar(100) NOT NULL, 
    phone_number varchar(20) NOT NULL, 
    email varchar(100) NOT NULL, 
    city varchar(100) NOT NULL, 
    state varchar(100) NOT NULL, 
    school varchar(100) NOT NULL, 
    year_in_school varchar(100), 
    major varchar(100), 
    PRIMARY KEY (id), 
    FOREIGN KEY (school) REFERENCES school(name) 
); 

CREATE TABLE book (
    ISBN varchar(14) NOT NULL,
    title varchar(255) NOT NULL,
    edition varchar(100),
    author_first_name varchar(100),
    author_last_name varchar(100),
    subject varchar(100),
    topic varchar(100),
    PRIMARY KEY (ISBN)
);

CREATE TABLE book_for_sale (
    id int NOT NULL AUTO_INCREMENT,
    ISBN varchar(100) NOT NULL,
    seller_id int NOT NULL,
    book_condition varchar(100),
    price float NOT NULL,
    comment tinytext,
    available bool NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (ISBN) REFERENCES book(ISBN),
    FOREIGN KEY (seller_id) REFERENCES user(id)
);

CREATE TABLE pinned_book (
    user_id int NOT NULL,
    book_listing_id int NOT NULL,
    CONSTRAINT PK_PINNED_BOOK PRIMARY KEY (user_id, book_listing_id),
    FOREIGN KEY (user_id) REFERENCES user(id),
    FOREIGN KEY (book_listing_id) REFERENCES book_for_sale(id)
);

CREATE TABLE transaction (
    buyer_id int NOT NULL,
    book_listing_id int NOT NULL,
    time_sold timestamp NOT NULL DEFAULT(CURRENT_TIMESTAMP),
    meeting_location varchar(255),
    CONSTRAINT PK_TRANSACTION PRIMARY KEY (buyer_id, book_listing_id),
    FOREIGN KEY (buyer_id) REFERENCES user(id),
    FOREIGN KEY (book_listing_id) REFERENCES book_for_sale(id)
);

CREATE TABLE school_uses_book (
    school_name varchar(100) NOT NULL,
    ISBN varchar(100) NOT NULL,
    department varchar(100),
    class varchar(100),
    CONSTRAINT PK_SCHOOL_USES_BOOK PRIMARY KEY (school_name, ISBN),
    FOREIGN KEY (school_name) REFERENCES school(name),
    FOREIGN KEY (ISBN) REFERENCES book(ISBN)
);

-- populate the tables with test data

INSERT INTO school VALUES
    ('IIT', 'Chicago', 'Illinois'),
    ('UIC', 'Chicago', 'Illinois');

INSERT INTO user (first_name, last_name, phone_number, email, city, state, school, year_in_school, major) VALUES
    ('Brandon', 'Bennitt', '8158065862', 'bbennitt@hawk.iit.edu', 'Chicago', 'Illinois', 'IIT', 'Senior', 'Computer Engineering'),
    ('Joe', 'Smith', '8158065861', 'jsmith@hawk.iit.edu', 'Chicago', 'Illinois', 'IIT', 'Junior', 'Computer Science'),
    ('Madison', 'Jones', '8158065860', 'mjones@uic.edu', 'Chicago', 'Illinois', 'UIC', 'Senior', 'Computer Engineering'),
    ('Meghan', 'Williams', '8158065863', 'mwilliams@uic.edu', 'Chicago', 'Illinois', 'UIC', 'Freshman', 'Computer Engineering');

INSERT INTO book VALUES
    ('9780857292988', 'Introduction to Artificial Intelligence (Undergraduate Topics in Computer Science)', 'First', 'Wolfgang', 'Ertel', 'Computer Science', 'Artificial Intelligence'),
    ('9781502447968', 'The Missing Link: An Introduction to Web Development and Programming', 'First', 'Michael', 'Mendez', 'Computer Science', 'Web Development'),
    ('9780078022159', 'Database System Concepts', 'Seventh', 'Abraham', 'Silberschatz', 'Computer Science', 'Databases');

INSERT INTO book_for_sale (ISBN, seller_id, book_condition, price, comment, available) VALUES
   ('9780857292988', 1, 'Good', 60.00, 'This book was essential for the class but not used afterwards. Good condition, no tears or missing pages.', FALSE),
   ('9781502447968', 3, 'Fair', 40.00, 'Small damages to the front and back cover but all pages are present.', TRUE),
   ('9781502447968', 4, 'Excellent', 50.00, 'Only used this book a few times. Good as new.', TRUE);

INSERT INTO pinned_book VALUES
    (1, 2),
    (1, 3),
    (2, 1);

INSERT INTO transaction (buyer_id, book_listing_id, meeting_location) VALUES
    (2, 1, 'IIT Library');

INSERT INTO school_uses_book VALUES
    ('IIT', '9780857292988', 'Computer Science', 'CS 480'),
    ('IIT', '9781502447968', 'Computer Science', 'CS 487'),
    ('UIC', '9781502447968', 'Computer Science', 'CS 484');

