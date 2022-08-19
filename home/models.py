from django.db import models
from autoslug import AutoSlugField

# Create your models here.


class Hero(models.Model):
    Cover = models.ImageField(upload_to="images/")
    cv = models.FileField(upload_to="images/")
    heading = models.CharField(max_length=120)
    # typeing efect
    t1 = models.CharField(max_length=100)
    t2 = models.CharField(max_length=100)
    t3 = models.CharField(max_length=100)
    t4 = models.CharField(max_length=100)

    def __str__(self):
        return self.t1


class About(models.Model):
    name = models.CharField(max_length=100)
    profile = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    about_me = models.TextField()
    photo = models.ImageField(upload_to="images/")
    logo = models.ImageField(upload_to="images/", null=True)
    location = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Skill(models.Model):
    skill = models.CharField(max_length=100)
    percentage = models.CharField(max_length=5)

    def __str__(self):
        return self.skill


class Services(models.Model):
    description = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.description


class Services_list(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Portfolio(models.Model):
    description = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.description


class Portfolio_item(models.Model):
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from="title", null=True, unique=True)
    description = models.TextField()
    Picture = models.ImageField(upload_to="images/")
    category = models.CharField(max_length=100)
    url = models.CharField(max_length=100, null=True)
    project_client = models.CharField(max_length=100, null=True)
    date = models.DateTimeField(auto_now=True)
    slider_one = models.ImageField(upload_to="images/", null=True)
    slider_two = models.ImageField(upload_to="images/", null=True)
    slider_three = models.ImageField(upload_to="images/", null=True)

    def __str__(self):
        return self.title


class Blog(models.Model):
    description = models.TextField(max_length=200, null=True)

    def __str__(self):
        return self.description


class Blog_item(models.Model):
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from="title", null=True, unique=True)
    description = models.TextField()
    Picture = models.ImageField(upload_to="images/")
    category = models.CharField(max_length=100)
    author = models.CharField(max_length=100, null=True)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class Count(models.Model):
    work = models.CharField(max_length=50)
    experience = models.CharField(max_length=50)
    total_client = models.CharField(max_length=50)
    award_won = models.CharField(max_length=50)

    def __str__(self):
        return self.work


class Testimonial(models.Model):
    photo = models.ImageField(upload_to="images/", null=True)
    author = models.CharField(max_length=100)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.author
