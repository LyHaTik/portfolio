from django.contrib import admin

from .models import Client, ChildPhoto, NowPhoto, FuturePhoto


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'pub_date', 'username', 'contact')
    
    
class ChildPhotoAdmin(admin.ModelAdmin):
    list_display = ('photo1', 'photo2', 'photo3', 'photo4')


class NowPhotoAdmin(admin.ModelAdmin):
    list_display = ('photo1', 'photo2', 'photo3', 'photo4')


class FuturePhotoAdmin(admin.ModelAdmin):
    list_display = ('photo1', 'photo2', 'photo3', 'photo4')





admin.site.register(Client, ClientAdmin)
admin.site.register(ChildPhoto, ChildPhotoAdmin)
admin.site.register(NowPhoto, NowPhotoAdmin)
admin.site.register(FuturePhoto, FuturePhotoAdmin)
