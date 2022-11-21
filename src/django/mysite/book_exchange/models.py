from configparser import ExtendedInterpolation
from email.policy import default
from django.db import models
from django.forms import IntegerField
from django.db import models

# some of these fields we may want a drop down to select. How do we do this?
# See this stack overflow to implement: https://stackoverflow.com/questions/18676156/how-to-properly-use-the-choices-field-option-in-django
# auto increment id does not need to be added as per: https://docs.djangoproject.com/en/4.1/topics/db/models/#automatic-primary-key-fields

class School(models.Model):
    school_name = models.CharField(max_length=100, primary_key=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    def __str__(self):
        return self.school_name

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    school_name = models.ForeignKey(School, on_delete=models.PROTECT)
    year = models.IntegerField(default=0)
    major = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Book(models.Model):
    ISBN = models.CharField(max_length=100, primary_key=True)
    title = models.CharField(max_length=255)
    edition = models.IntegerField(default=0)
    author_first_name = models.CharField(max_length=100)
    author_last_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    book_condition = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    comment = models.TextField()
    available = models.BooleanField(default=True)
    cover = models.ImageField(upload_to="book_exchange/media/covers/", default="book_exchange/media/covers/default.jpg")

    def __str__(self):
        return "ISBN: " + self.ISBN + "\nSeller: " + self.seller.first_name + " " + self.seller.last_name

#class BookForSale(models.Model):
#    ISBN = models.ForeignKey(Book, on_delete=models.RESTRICT)
#    seller = models.ForeignKey(User, on_delete=models.CASCADE)
#    book_condition = models.CharField(max_length=100)
#    price = models.FloatField(default=0)
#    comment = models.TextField()
#    available = models.BooleanField(default=True)
#    cover = models.ImageField(upload_to="book_exchange/media/covers/", default="book_exchange/media/covers/default.jpg")
#    #id = models.CharField(max_length=1000, primary_key=True, unique=True, editable=False)
#
#    def __str__(self):
#        return "ISBN: " + self.ISBN.ISBN + "\nSeller: " + self.seller.first_name + " " + self.seller.last_name

class PinnedBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book_listing = models.ForeignKey(Book, on_delete=models.RESTRICT)

    def __str__(self):
        return "User: " + self.user.__str__() + " pinned " + self.book_listing.__str__()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user_id', 'book_listing_id'], name='unique_user_book_listing_combination'
            )
        ]

class Transaction(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    book_listing = models.ForeignKey(Book, on_delete=models.PROTECT)
    time_sold = models.DateField('Transaction Date')

    def __str__(self):
        return self.book_listing.__str__() + " sold on " + str(self.time_sold) + " to " + self.buyer.__str__()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['buyer_id', 'book_listing_id'], name='unique_buyer_book_listing_combination'
            )
        ]

class SchoolUsesBook(models.Model):
    school_name = models.ForeignKey(School, on_delete=models.CASCADE)
    ISBN = models.ForeignKey(Book, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    course = models.CharField(max_length=100)

    def __str__(self):
        return self.school_name.__str__() + " uses " + self.ISBN.__str__()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['school_name', 'ISBN'], name='unique_school_ISBN_combination'
            )
        ]

