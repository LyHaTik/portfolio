from django.db import models


class Client(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    contact = models.CharField(max_length=30, blank=True, null=True)
    dacoin_general = models.BooleanField(default=False)
    dacoin_foto = models.BooleanField(default=False)
    dacoin_pay = models.BooleanField(default=False)
    dacoin_bot = models.BooleanField(default=False)
    dacoin_like = models.BooleanField(default=False)
    dacoin_otzivi = models.BooleanField(default=False)
    dacoin_clean = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.username}'


class ChildPhoto(models.Model):
    photo1 = models.ImageField('Фото1', blank=True, null=True, default='images2.jpeg', upload_to='data_photo/')
    photo2 = models.ImageField('Фото2', blank=True, null=True, default='images2.jpeg', upload_to='data_photo/')
    photo3 = models.ImageField('Фото3', blank=True, null=True, default='images2.jpeg', upload_to='data_photo/')
    photo4 = models.ImageField('Фото4', blank=True, null=True, default='images2.jpeg', upload_to='data_photo/')
    description = models.TextField(
        default='Описание фото',
        max_length=400,
        blank=True,
        null=True)
    additional_info = models.TextField(default='Доп. информации нет', blank=True, null=True)


class NowPhoto(models.Model):
    photo1 = models.ImageField('Фото1', blank=True, null=True, default='images2.jpeg', upload_to='data_photo/')
    photo2 = models.ImageField('Фото2', blank=True, null=True, default='images2.jpeg', upload_to='data_photo/')
    photo3 = models.ImageField('Фото3', blank=True, null=True, default='images2.jpeg', upload_to='data_photo/')
    photo4 = models.ImageField('Фото4', blank=True, null=True, default='images2.jpeg', upload_to='data_photo/')
    description = models.TextField(
        default='Описание фото',
        max_length=400,
        blank=True,
        null=True)
    additional_info = models.TextField(default='Доп. информации нет', blank=True, null=True)
    

class FuturePhoto(models.Model):
    photo1 = models.ImageField('Фото1', blank=True, null=True, default='images2.jpeg', upload_to='data_photo/')
    photo2 = models.ImageField('Фото2', blank=True, null=True, default='images2.jpeg', upload_to='data_photo/')
    photo3 = models.ImageField('Фото3', blank=True, null=True, default='images2.jpeg', upload_to='data_photo/')
    photo4 = models.ImageField('Фото4', blank=True, null=True, default='images2.jpeg', upload_to='data_photo/')
    description = models.TextField(
        default='Описание фото',
        max_length=400,
        blank=True,
        null=True)
    additional_info = models.TextField(default='Доп. информации нет', blank=True, null=True)


class Like(models.Model):
    like = models.IntegerField(default=0)


class Otziv(models.Model):
    username = models.CharField(max_length=40)
    text = models.TextField()


class Discount(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    percent = models.IntegerField(default=0)