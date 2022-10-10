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


## Database Creation Code <br/><br/>

**Run the code below in a MySQL prompt to create the appropriate tables and columns** <br/><br/>
*Notes:*  <br/><br/>
    - Make sure to edit the code in this file and update other members if we do change the schema so development is on the same page <br/><br/>
    - There is an SQL script included in the GitHub with the code to create the tables in the database and populate with testing data <br/><br/>

Code to create user table: <br/><br/>
CREATE TABLE user ( <br/><br/>
    id int NOT NULL AUTO_INCREMENT, <br/><br/>
    first_name varchar(100) NOT NULL, <br/><br/>
    last_name varchar(100) NOT NULL, <br/><br/>
    phone_number varchar(20) NOT NULL, <br/><br/>
    email varchar(100) NOT NULL, <br/><br/>
    city varchar(100) NOT NULL, <br/><br/>
    state varchar(100) NOT NULL, <br/><br/>
    school varchar(100) NOT NULL, <br/><br/>
    year_in_school varchar(100), <br/><br/>
    major varchar(100), <br/><br/>
    PRIMARY KEY (id), <br/><br/>
    FOREIGN KEY (school) REFERENCES school(name) <br/><br/>
); <br/><br/>


Code to create book table:
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


Code to create book_for_sale table:
CREATE TABLE book_for_sale (
    id int NOT NULL AUTO_INCREMENT,
    ISBN varchar(100) NOT NULL,
    seller_id int NOT NULL,
    book_condition varchar(100),
    price float NOT NULL,
    comment tinytext,
    PRIMARY KEY (id),
    FOREIGN KEY (ISBN) REFERENCES book(ISBN),
    FOREIGN KEY (seller_id) REFERENCES user(id)
);


Code to create pinned_book table:
CREATE TABLE pinned_book (
    user_id int NOT NULL,
    book_listing_id int NOT NULL,
    CONSTRAINT PK_PINNED_BOOK PRIMARY KEY (user_id, book_listing_id),
    FOREIGN KEY (user_id) REFERENCES user(id),
    FOREIGN KEY (book_listing_id) REFERENCES book_for_sale(id)
);


Code to create transaction table:
CREATE TABLE transaction (
    buyer_id int NOT NULL,
    book_listing_id int NOT NULL,
    time_sold timestamp NOT NULL,
    meeting_location varchar(255),
    CONSTRAINT PK_TRANSACTION PRIMARY KEY (buyer_id, book_listing_id),
    FOREIGN KEY (buyer_id) REFERENCES user(id),
    FOREIGN KEY (book_listing_id) REFERENCES book_for_sale(id)
);


Code to create school table:
CREATE TABLE school (
    name varchar(100) NOT NULL,
    city varchar(100) NOT NULL,
    state varchar(100) NOT NULL,
    PRIMARY KEY (name)
);


Code to create school_uses_book table:
CREATE TABLE school_uses_book (
    school_name varchar(100) NOT NULL,
    ISBN varchar(100) NOT NULL,
    department varchar(100),
    class varchar(100),
    CONSTRAINT PK_SCHOOL_USES_BOOK PRIMARY KEY (school_name, ISBN),
    FOREIGN KEY (school_name) REFERENCES school(name),
    FOREIGN KEY (ISBN) REFERENCES book(ISBN)
);


## Inserting Database Values Examples

**These are some examples of inserting data into each of the fields so we can test the database out**
*Note: Make sure that these are updated as the schema is updated*

INSERT INTO user (first_name, last_name, phone_number, email, city, state, school, year_in_school, major)
    ('Brandon', 'Bennitt', '8158065862', 'bbennitt@hawk.iit.edu', 'Chicago', 'Illinois', 'IIT', 'Senior', 'Computer Engineering')
    ('Joe', 'Smith', '8158065861', 'jsmith@hawk.iit.edu', 'Chicago', 'Illinois', 'IIT', 'Junior', 'Computer Science')
    ('Madison', 'Jones', '8158065860', 'mjones@uic.edu', 'Chicago', 'Illinois', 'UIC', 'Senior', 'Computer Engineering')
    ('Meghan', 'Williams', '8158065863', 'mwilliams@uic.edu', 'Chicago', 'Illinois', 'UIC', 'Freshman', 'Computer Engineering')


INSERT INTO book VALUES
    ('978-0857292988', 'Introduction to Artificial Intelligence (Undergraduate Topics in Computer Science)', 'First', 'Wolfgang', 'Ertel', 'Computer Science', 'Artificial Intelligence')