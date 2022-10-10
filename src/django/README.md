# Database Information

## Setup and Django Configuration

Once configuring the django project locally, you need to edit the database settings to use a mysql database. I recommend installing mysql first and creating the database and a non-root user with all privileges to the database. After that, you can add the database to the Django project by editing the settings.py and migrate. The default user and password in our Django configuration is 'user1' and 'GroupE3!'


## Database Schema Description

After further thought and discussion, it was decided it's best to create 7 different tables in our database. We will have a user table, book table, book_for_sale table, pinned_book table, transactions table, school table, and school_uses_book table. These are not set in stone but a good starting point.

A description of each of the tables is below.
1. **user:** Each user has one entry in the user table with a variety of information. 
    - *PK:* 'id'
    - *Foreign Key:* 'school' references 'name' in school table

2. **book:** Each book ever listed on the website (or added by admin) has an entry in the book table regardless of if it is currently being sold. The user can do this to set notifications for if a book is posted that they're looking for but is not currently listed. Helps with overall schema of DB.
    - *PK:* 'ISBN'

3. **book_for_sale:** Each book that is listed for sale gets added to this table.
    - *PK:* 'id'
    - *Foreign key:* 'ISBN' references 'ISBN' in book table, 'seller_id' references 'id' in user table

4. **pinned_book:** Row is created when a user pins/saves a book that is listed for sale. 
    - *PK:* 'user_id', 'book_listing_id'
    - *Foreign key:* 'user_id' references 'id' in user table, 'book_listing_id' references 'id' in book_for_sale table

5. **transaction:** A row is created for each book transaction on the website (book is sold).
    - *PK:* 'buyer_id', 'book_listing_id'
    - *Foreign key:* 'buyer_id' references 'id' in user table, 'book_listing_id' references 'id' in book_for_sale table

6. **school:** Each school has multiple students, but each student only has one school (defined constraint we are creating for right now). School will have city and state information so an algorithm can run to calculate the distance between schools if users don't live at their school, but would sell to other users near their school.
    - *PK:* 'name'

7. **school_uses_book:** This is used for filtering books by school or other things we may want to include. Gives us valuable insights to display.
    - *PK:* 'school_name', 'ISBN'
    - *Foreign Key:* 'school_name' references 'name' in school table, 'ISBN' references 'ISBN' in book table


### Other Notes

- This schema is a work in progress and does not have to be final. As we see fit we can add tables, fields, views, etc.


## Database Creation Code

**Run the code below in a MySQL prompt to create the appropriate tables and columns**  
*Notes:*  
    - Make sure to edit the code in this file and update other members if we do change the schema so development is on the same page  
    - There is an SQL script named create_and_populate.sql included in the this directory with the code to create the tables in the database and populate with testing data  


Code to create school table:
```sql
CREATE TABLE school (
    name varchar(100) NOT NULL,
    city varchar(100) NOT NULL,
    state varchar(100) NOT NULL,
    PRIMARY KEY (name)
);
```

Code to create user table:
```sql
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
```

Code to create book table:
```sql
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
```

Code to create book_for_sale table:
```sql
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
```

Code to create pinned_book table:
```sql
CREATE TABLE pinned_book (
    user_id int NOT NULL,
    book_listing_id int NOT NULL,
    CONSTRAINT PK_PINNED_BOOK PRIMARY KEY (user_id, book_listing_id),
    FOREIGN KEY (user_id) REFERENCES user(id),
    FOREIGN KEY (book_listing_id) REFERENCES book_for_sale(id)
);
```

Code to create transaction table:
```sql
CREATE TABLE transaction (
    buyer_id int NOT NULL,
    book_listing_id int NOT NULL,
    time_sold timestamp NOT NULL DEFAULT(CURRENT_TIMESTAMP),
    meeting_location varchar(255),
    CONSTRAINT PK_TRANSACTION PRIMARY KEY (buyer_id, book_listing_id),
    FOREIGN KEY (buyer_id) REFERENCES user(id),
    FOREIGN KEY (book_listing_id) REFERENCES book_for_sale(id)
);
```

Code to create school_uses_book table:
```sql
CREATE TABLE school_uses_book (
    school_name varchar(100) NOT NULL,
    ISBN varchar(100) NOT NULL,
    department varchar(100),
    class varchar(100),
    CONSTRAINT PK_SCHOOL_USES_BOOK PRIMARY KEY (school_name, ISBN),
    FOREIGN KEY (school_name) REFERENCES school(name),
    FOREIGN KEY (ISBN) REFERENCES book(ISBN)
);
```


## Inserting Database Values Examples

**These are some examples of inserting data into each of the fields so we can test the database out**  
*Note: Make sure that these are updated as the schema is updated*  

```sql
INSERT INTO school VALUES
    ('IIT', 'Chicago', 'Illinois'),
    ('UIC', 'Chicago', 'Illinois');
```

```sql
INSERT INTO user (first_name, last_name, phone_number, email, city, state, school, year_in_school, major) VALUES
    ('Brandon', 'Bennitt', '8158065862', 'bbennitt@hawk.iit.edu', 'Chicago', 'Illinois', 'IIT', 'Senior', 'Computer Engineering'),
    ('Joe', 'Smith', '8158065861', 'jsmith@hawk.iit.edu', 'Chicago', 'Illinois', 'IIT', 'Junior', 'Computer Science'),
    ('Madison', 'Jones', '8158065860', 'mjones@uic.edu', 'Chicago', 'Illinois', 'UIC', 'Senior', 'Computer Engineering'),
    ('Meghan', 'Williams', '8158065863', 'mwilliams@uic.edu', 'Chicago', 'Illinois', 'UIC', 'Freshman', 'Computer Engineering');
```

```sql
INSERT INTO book VALUES
    ('9780857292988', 'Introduction to Artificial Intelligence (Undergraduate Topics in Computer Science)', 'First', 'Wolfgang', 'Ertel', 'Computer Science', 'Artificial Intelligence'),
    ('9781502447968', 'The Missing Link: An Introduction to Web Development and Programming', 'First', 'Michael', 'Mendez', 'Computer Science', 'Web Development'),
    ('9780078022159', 'Database System Concepts', 'Seventh', 'Abraham', 'Silberschatz', 'Computer Science', 'Databases');
```

```sql
INSERT INTO book_for_sale (ISBN, seller_id, book_condition, price, comment, available) VALUES
   ('9780857292988', 1, 'Good', 60.00, 'This book was essential for the class but not used afterwards. Good condition, no tears or missing pages.', FALSE),
   ('9781502447968', 3, 'Fair', 40.00, 'Small damages to the front and back cover but all pages are present.', TRUE),
   ('9781502447968', 4, 'Excellent', 50.00, 'Only used this book a few times. Good as new.', TRUE);
```

```sql
INSERT INTO pinned_book VALUES
    (1, 2),
    (1, 3),
    (2, 1);
```

```sql
INSERT INTO transaction (buyer_id, book_listing_id, meeting_location) VALUES
    (2, 1, 'IIT Library');
```

```sql
INSERT INTO school_uses_book VALUES
    ('IIT', '9780857292988', 'Computer Science', 'CS 480'),
    ('IIT', '9781502447968', 'Computer Science', 'CS 487'),
    ('UIC', '9781502447968', 'Computer Science', 'CS 484');
```
