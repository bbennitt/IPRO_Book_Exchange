from django.contrib import admin

from .models import User, Book, BookForSale, PinnedBook, School, SchoolUsesBook, Transaction

admin.site.register(User)
admin.site.register(Book)
admin.site.register(BookForSale)
admin.site.register(PinnedBook)
admin.site.register(School)
admin.site.register(SchoolUsesBook)
admin.site.register(Transaction)