# Database Information

## Setup and Django Configuration

Once configuring the django project locally, you need to edit the database settings to use a mysql database. I recommend installing mysql first and creating the database and a non-root user with all privileges to the database. After that, you can add the database to the Django project by editing the settings.py and migrate. The default user and password in our Django configuration is 'user1' and 'GroupE3!'


## Database Schema Description

After further thought and discussion, it was decided it's best to create 6 different tables in our database. We will have a user table, book table, pinned_books, transactions table, school table, and school_uses_book table. These are not set in stone but a good starting point.

A description of each of the tables is below.
1. **user:** Each user has one entry in the user table with a variety of information. 
  - *PK:* 'id'

2. **book:** Each book has one entry in the book table with seller field as the id of the seller. 
- *PK:* 'id' 
- *Foreign key:* 'user_id' references 'id' in user table

3. **pinned_books:** Row is created when a user pins/saves a book for later. 
- *PK:* 'user_id', 'book_id'
- *Foreign key:* 'user_id' references 'id' in user table, 'book_id' references 'id' in book table

4. **transaction:** A row is created for each book once it has been sold.
- *PK:* 'buyer_id', 'seller_id', 'book_id'
- *Foreign key:* 'buyer_id' references 'id' in user table, 'seller_id' references 'id' in user table, 'book_id' references 'id' in book table

5. **school:** Each school has multiple students, but each student only has one school (defined constraint we are creating for right now). School will have city and state information so an algorithm can run to calculate the distance between schools if users don't live at their school, but would sell to other users near their school.
- *PK:* 'id'

6. **school_uses_book:** This is used for filtering books by school or other things we may want to include. Gives us valuable insights to display.
- *PK:* 'school_id', 'book_id'
- *Foreign Key:* 'school_id' references 'id' in school table, 'book_id' references 'id' in book table


### Other Notes

- We are going to have a field in the book table that is a boolean named 'available' that will be set to true until it is sold or taken down. For that reason, we will never be deleting books that are at one time posted. This makes sure we don't have to delete on cascade when we don't want to (pinned_books). Create an icon to be displayed to indicated available or not when displaying books. Default search to only show books that are available but can search for previously posted books as well (just have to change the query in the Python code).

- This schema is a work in progress and does not have to be final. As we see fit we can add tables, fields, views, etc.


## Database Creation Code

**Run the code below in a MySQL prompt to create the database with appropriate tables and columns**
*Note: Make sure to edit the code in this file and update other members if we do change the schema so local development is on the same page.*

Code to create user table:
CREATE TABLE user (
    first_name varchar(100),
    last_name varchar(100),
    city varchar(100),
    state varchar(100),
    College varchar(100)
);


Code to create book table:
CREATE TABLE book (
    Name varchar(100),
    Edition varchar(100),
    ISBN varchar(100),
    AuthorFirstName varchar(100),
    AuthorLastName varchar(100),
    Genre varchar(100),
    Topic varchar(100),
    Book_condition` varchar(100),
    Price float,
    Comment tinytext
);


Code to create transaction table:
CREATE TABLE transaction (

);


Code to create school table:
CREATE TABLE school (

);


Code to create pinned_books view:
CREATE VIEW pinned_books (
    user_id int,
    book_id int,
    Primary key (both of these)
);


## Inserting Database Values Examples

**These are some examples of inserting data into each of the fields so we can test the database out**
*Note: Make sure that these are updated as the schema is updated*
