from django.contrib import admin
from .models import Neighbour,Business,Police,Profile,Post

# Register your models here.
admin.site.register(Neighbour)
admin.site.register(Business)
admin.site.register(Police)
admin.site.register(Profile)
admin.site.register(Post)