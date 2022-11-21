from django.contrib import admin

from .models import User, Book, PinnedBook, School, Transaction

admin.site.register(User)
admin.site.register(Book)
admin.site.register(PinnedBook)
admin.site.register(School)
admin.site.register(Transaction)