from email.policy import default
from unicodedata import category
from django.db import models
from autoslug import AutoSlugField
from django.core.validators import FileExtensionValidator
from tinymce.models import HTMLField
from ckeditor.fields import RichTextField


News_Category = (
    ('National','देश'),
    ('InterNational','विदेश'),
    ('Rajasthan','राजस्थान'),
    ('Politics','राजनीति'),
    ('Sports','स्पोर्ट्स'),
    ('Carrier','करिअर'),
    ('Entertainment','मनोरंजन'),
    ('Sikar','सीकर')
)

class Admin(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=100)
    last_login = models.DateTimeField()
    profile_img = models.FileField(upload_to='img/',validators=[FileExtensionValidator( ['jpg','jpeg','png']) ])

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=10)
    message = models.TextField()
    date = models.DateTimeField()

class Magazine(models.Model):
    date = models.DateField()
    image = models.FileField(upload_to='img/magazine/',validators=[FileExtensionValidator( ['jpg','jpeg','png'])])
    magazine = models.FileField(upload_to='pdf/',validators=[FileExtensionValidator( ['pdf'])])
    status = models.BooleanField()

class News(models.Model):
    title = models.CharField(max_length=255)
    heading = models.TextField()
    news = HTMLField()
    image = models.FileField(upload_to='img/news/',validators=[FileExtensionValidator( ['jpg','jpeg','png']) ])
    datetime = models.DateTimeField()
    type = models.CharField(max_length=50,choices=News_Category,default='National')
    status = models.BooleanField()
    news_slug = AutoSlugField(populate_from='title',null=True,unique=True,default=None)

class Photo(models.Model):
    category = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    image = models.FileField(upload_to='img/photo/',validators=[FileExtensionValidator( ['jpg','jpeg','png']) ])
    status = models.BooleanField()

class Video(models.Model):
    category = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    video_id = models.CharField(max_length=100)
    datetime = models.DateTimeField()
    status = models.BooleanField()

class Logo(models.Model):
    logo = models.FileField(upload_to='img/',validators=[FileExtensionValidator( ['jpg','jpeg','png']) ],default=False)
    poster = models.FileField(upload_to='img/',validators=[FileExtensionValidator( ['jpg','jpeg','png']) ],default=False)
    preloader = models.FileField(upload_to='img/',validators=[FileExtensionValidator( ['jpg','jpeg','png']) ],default=False)




