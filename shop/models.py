#!/usr/bin/python
# -*- coding: utf-8 -*-
# Create your models here.
from django.db import models
from django.contrib.gis.db import models as gis_models
from django.contrib.postgres.fields import ArrayField
from django.conf import settings
from django.db.models.signals import pre_save
from django.utils.text import slugify
from multiselectfield import MultiSelectField
CITYNAME = (('raebareli', 'Raebareli'), ('lucknow', 'Lucknow'),('new delhi', 'New Delhi'),)
STATENAME = (('uttar_pradesh', 'Uttar Pradesh'),('delhi','Delhi'),)
DAYS = (
    ('sunday', 'Sunday'),
    ('monday', 'Monday'),
    ('tuesday', 'Tuesday'),
    ('wednesday', 'Wednesday'),
    ('thursday', 'Thursday'),
    ('friday', 'Friday'),
    ('saturday', 'Saturday'),
    ('Not any day', 'None'),
       )
placeholder = ('description of product')

def upload_location(instance, filename):
    return 'shop/%s-%s/%s' % (instance.shopName, instance.id, filename)



class City(models.Model):
    cityImg = models.ImageField(upload_to='cityImg/',
                           default='cityImg/default.png',
                           width_field='widthField',
                           height_field='heightField')
    heightField = models.IntegerField(default=0)
    widthField = models.IntegerField(default=0)

    city = models.CharField(max_length=120, choices=CITYNAME)
    state = models.CharField(max_length=120, choices=STATENAME)
    country = models.CharField(max_length=120, default='india')

    def __str__(self):
        return '%s - %s' % (self.city, self.state)

    class Meta:
        ordering = ('city',)
        unique_together = ('city','state')
        verbose_name_plural = "Cities"



class Category(models.Model):
    name = models.CharField(max_length=120, unique=True)
#    slug = models.SlugField(unique=True, blank=True)
    desc = models.TextField(blank=True)
    catImg = models.FileField(upload_to='catImg/',
                               default='catImg/None/default.svg',)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class SubCategory(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, unique=True)
#    slug = models.SlugField(unique=True, blank=True)
    desc = models.TextField(blank=True)
    subCatImg = models.FileField(upload_to='subCatImg/',
                                  default='subCatImg/None/default.png')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "SubCategories"


class FilterTag(models.Model):

    subCategory = models.ForeignKey(SubCategory,
                                    on_delete=models.CASCADE)
    tag = models.CharField(max_length=120)
#    slug = models.SlugField(unique=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tag +"-"+str(self.subCategory)
    class Meta:
        ordering = ('tag',)

class Shop(models.Model):


    city = models.ForeignKey(City, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # will change on_dlt method soon
    subCategory = models.ManyToManyField(SubCategory)
    filterTags = models.ManyToManyField(FilterTag, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,default=1)

    slug = models.SlugField(unique=True, blank=True)
    shopName = models.CharField(max_length=250)
    tagline = models.CharField(blank=True, max_length=500)


    bannerImage = models.ImageField(upload_to=upload_location,
                                    default='shop/defaultimage/default.png',
                                    width_field='widthField',
                                    height_field='heightField')
    widthField = models.IntegerField(default=0)
    heightField = models.IntegerField(default=0)

    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    email = models.EmailField(blank=True)
    mobileNo = models.CharField(max_length=14)
    alternateMobileNo = models.CharField(max_length=15, blank=True)
    location = gis_models.PointField(u'longitude/latitude',
            geography=True, blank=True, null=True)


    ownerName = models.CharField(blank=True,max_length=250)
    shopAddress = models.TextField()
    shopPinCode = models.PositiveIntegerField()

   

    openingTime = models.TimeField()
    closingTime = models.TimeField()
    closingDay = MultiSelectField(choices=DAYS,default=DAYS[7][0])

 
    isActive = models.BooleanField(default=0)
    updatedAt = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    gis = gis_models.GeoManager()
    objects = models.Manager()

    def __str__(self):
        return self.shopName 


class Vote(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1)
    liked = models.NullBooleanField()
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.shop) +' - '+str(self.user)

class Offer(models.Model):

    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    desc = models.TextField(blank=True)
    endDate = models.DateField(blank=True)

    def __str__(self):
        return self.title

class Feedback(models.Model):
    shop = models.ForeignKey(Shop,on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.shop) +' - '+str(self.user)
class Products(models.Model):
    shop = models.ForeignKey(Shop,on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    product_name = models.CharField(max_length=50)
    Available = models.BooleanField(default=True)
    description = models.TextField(default=placeholder)
    ProductImage = models.ImageField(upload_to=upload_location,
                                    default='shop/None/default.png',
                                    )
   
    def __str__(self):
        return self.product_name
    class Meta:
        verbose_name_plural = "Products"
class Deals(models.Model):
    shop = models.ForeignKey(Shop,on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    Deal = models.CharField(max_length=50)
   
    def __str__(self):
        return self.Deal +'-'+str(self.shop)
    class Meta:
        verbose_name_plural = "Deals"

def create_slug(instance, newSlug=None):
    slug = slugify(instance.shopName)
    if newSlug is not None:
        slug = newSlug
    qs = Shop.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = '%s-%s' % (slug, qs.first().id)
        return create_slug(instance, newSlug=new_slug)
    return slug

#


def pre_save_shop_receiver(
    sender,
    instance,
    *args,
    **kwargs
    ):
    if not instance.slug:
        instance.slug = create_slug(instance)



pre_save.connect(pre_save_shop_receiver, sender=Shop)

 