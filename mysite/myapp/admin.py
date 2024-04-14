from django.contrib import admin
from .models import Tour, Order, Review, Buscket

admin.site.register(Tour)
admin.site.register(Buscket)
admin.site.register(Order)
admin.site.register(Review)
