# IPRO 497 Fall 2022 – Group E's Product Design Document 

## Problem Statements

With the ever increasing cost of attending college, students are struggling to justify spending hundreds of extra dollars every semester on new textbooks that they will use for one class and then never look at again. To aid in reducing the overall costs of required textbooks, college students can use our solution to help them buy and sell used textbooks for better prices than are offered by campus bookstores and existing e-retailers. 


## Customer
### Description
-   Users: College students that need better access to textbooks
-   Need: Easier access to textbooks (cheaper and faster delivery)
-   Merit: Decrease textbook piracy, provide easier access to textbooks

### Other customer(s) or stakeholder(s)
-   Stakeholder: Campus Administrators
-   Competitors: Campus Bookstores, Online Bookstores, Publishers

## Application type (web app, mobile, website, native client, …)
Website

### Tech stack

| Member | Langugages | FE Frameworks | BE Frameworks | Databases |
| ----------- | ----------- | ----------- | ----------- | ----------- |
| Fenglian Li | Java | NA | NA | NA |
| Calvin Teng | Python, HTML/CSS | NA | NA | NA |
| Adrian Grabowski | Java, Python, HTML/CSS | Bootstrap | NA | MySQL |
| Brandon Bennitt | Python, C++, Java, HTML/CSS | Bootstrap | Flask (very little) | Postgresql |
| Ali Guzelyel | Java, Python, C#,HTML/CSS | React | .Net Core | Postgresql |

#### Client Tech
-   Languages: HTML, CSS, Javascript
-   Frontend: Bootstrap

#### Server Tech
-   Backend: Python, Django
-   Database: MySQL (?MySQL for Django)

## Top Application Capabilities
1. Search for books with search bar (ISBN, name, author, edition) 
2. Set up a pick-up or meeting location at a bookstore between the seller and buyer.
    - Seller can drop books to the bookstore(?other places) and buyer can pick it up later.
3. Buyer can save book for later, pin it, or get notification about it. (sold, etc.)
4. Buyer can change the radius for location (search for books in longer distances.)
5. Account system for buyers and sellers. (past history, rating)
6. Optimize access from phone (users can use website from phone without problems.) 
7. Implement a messaging system, buyer and seller can communicate.
8. Show past prices for books, or prices from other sellers and bookstore/amazon. (price history for the book)
9. If we don’t have the book, suggest to buy an older version from the bookstore.

## Top Two to Three Scenarios
### Persona 1
Demographics: age:18, college student, phone user, from out of state, on a tight budget
Psychographics: Looking for good deals on required textbooks for his first semester of college
Goal: Wants to buy used textbooks from older students on his campus for as cheap as possible

### Scenario 1
Peter is a freshman college student majoring in computer science. Since he is coming straight from high school and does not have a lot of money, he is overwhelmed by the amount of money that textbooks cost. To save money on his limited budget, Peter decides to visit the book exchange website on his phone to see if he can get a good deal on his textbooks. On the book exchange, he sees that a seller is offering to sell the book for $50 less than the campus bookstore. Since he believes this is a good deal, he messages the seller and they decide on a meeting place to exchange the book and payment. Peter is relieved that he was able to save $50 by visiting the book exchange website and is happy with his purchase since he knows he has the proper textbook needed for class.

### Persona 2
Name: Nate
Demographics: age - 21, senior college student in suburbs, took a lot of classes in previous years and has a surplus of textbooks sitting at home.
Pschographics: wants to sell textbooks to make room at home and earn some extra money.

### Scenario 2
Nate is a senior college student living in the suburbs. Over the years he took a lot of classes, and his library has accumulated a lot of textbooks that he doesn’t read. He wants to open up some space and earn some extra cash. He heard from his friends that there is an app he can put the textbooks on. Since he lives in suburbs, going downtown to college campuses takes a while, and he wants to sell the books in a closer location. He goes on the app, puts his books, and sets a meet-up location to a close-by public library and soon he finds a buyer. 

### Persona 3
Name: Lucy
Demographics: age - 20, Junior in college, knows people on campus but not close friends with them
Psychographics: Entrepreneurial and looking to sell her old textbooks in order to buy her new textbooks for this coming semester
Goal: Pay no more for new textbooks than she can sell her old textbooks for

### Scenario 3
Lucy is a rising junior in college and is looking forward to her upcoming semester. After the first week of classes she realizes she has to buy 4 textbooks for this semester, all of which are priced at over $100 on Amazon. Since Lucy has a business mindset and is willing to reduce her costs of school, she is ok with buying used textbooks for cheaper. She also realizes that she never plans on looking at her old textbooks anymore and if she doesn’t sell them, then she will end up throwing them away. Lucy would like to sell her old textbooks to younger students on campus and buy her new textbooks from older students on campus, but doesn’t know anyone that is not the same age as her. Lucy decides to open up the book exchange website and check what other sellers are selling their old textbooks for. After she realizes she’ll be able to sell all of her old textbooks and purchase her new textbooks for the same price, she is happy to list her old books on the book exchange. Once the younger students realize Lucy is selling her books at a reasonable price, they message her to meet up and exchange the books and payment. Lucy then buys the new textbooks from multiple sellers and meets them on campus. In the process, Lucy was able to make some new friends by meeting them while exchanging books and payment.


## Team Members
| Name | Email | Discord | Location | Time Zone Offset | 
| ----------- | ----------- | ----------- | ----------- | ----------- |
| Fenglian Li | fli27@hawk.iit.edu  | NA | China | 13 |
| Calvin Teng | cteng2@hawk.iit.edu | NA | UTC+8 | 13 |
| Brandon Bennitt | bbennitt@hawk.iit.edu | NA | Chicago | 0 |
| Ali Guzelyel | aguzelyel@hawk.iit.edu  | NA | Chicago | 0 |
| Adrian Grabowski | agrabowski@hawk.iit.edu  | NA | Chicago | 0 |

## Team Working Agreement (All team members)
### What do we want to accomplish/learn together?

### Tools
* We will use Github and keep items updated as progress is made
* If we need to meet outside of class we will use the following tool/tech for meetings: Discord/Zoom
* When we are not meeting together we will use the following tool/tech for communications: Discord
* If we need to meet outside of class we will refer to the group availability table at: https://www.when2meet.com/?16700807-Ax5JR for deciding a time to meet.

### Requested Approach/Behavior 
* Any change to the repository needs to be communicated on Discord
* Each story should be a separate branch. Before merging the branches, the story owner requests a Pull Request. After PR, the story owner can merge the branch.
* Acknowledge everyone’s work.
* No questions asked should be considered silly.
* Respect needs to be present at all times.

### Unacceptable behavior
* Removing or changing code related to previous stories without informing the original developer who wrote the code
* Being a dictator of the repository
* Not being present during group collaboration and sprint review without prior notice

### How will we productively solve disagreement
* If 100% of the group does not agree with some decision after 10 minutes of discussion, a poll will be made

## Sprint Schedule

| Week | Sprint Leader |
| --------  | ------------------- |
| 1 - Problem Framing                                 | Fenglian |
| 2 - Problem Framing                                 | Fenglian |
| 3 - Problem Framing                                 | Ali |
| 4 - Problem Framing                                 | Ali |
| 5 - Think, build, test, and demo for midterm        | Brandon |
| 6 - Think, build, test, and demo for midterm        | Brandon |
| 7 - Think, build, test, and demo for midterm        | Adrian |
| 8 - Think, build, test, and demo for midterm        | Adrian |
| 9 - Thanksgiving Break
| 10 - Think, build, test, and demo for final	      | Calvin |
| 11 - Think, build, test, and demo for final         | Calvin |
| 12 - Think, build, test, and demo for final         | Fenglian |
| 13 - Presentation dry run                           | Fenglian |
| 14 - Presentation                                   | Ali |
