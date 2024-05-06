from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Product)
admin.site.register(Review)
admin.site.register(UserProfile)
admin.site.register(Cart)
admin.site.register(CartItem)