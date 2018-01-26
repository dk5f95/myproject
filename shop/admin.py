from django.contrib import admin
from django import forms
from django.contrib.gis.db import models as gis_models
from mapwidgets.widgets import GooglePointFieldWidget
from shop.models import(
	Shop,
	Category,
	SubCategory,
	City,
	Offer,
	FilterTag,
	Feedback,
	Vote,
	Products,
	Deals,
	)
# Register your models here.


class ShopAdmin(admin.ModelAdmin):
	list_display = ('shopName','isActive','category','city')
	list_filter = ('isActive','city','category')
	list_editable = ('category',)
	search_fields = ('shopName',)
	formfield_overrides = {
        gis_models.PointField: {"widget": GooglePointFieldWidget}
    }
# class ProductsAdmin(admin.ModelAdmin):
# 	list_display = ('product_name','Available','shopName')

# class PricingAdminForm(forms.ModelForm):
#     shop = forms.ModelChoiceField(queryset=Shop.objects.order_by('shopName'))
#     class Meta:
#         model = Pricing
#         fields = '__all__'

# class PricingAdmin(admin.ModelAdmin):
# 	form = PricingAdminForm
# @admin.register(Products,Shop)
# class DefaultAdmin(admin.ModelAdmin):
#     pass
admin.site.register(Shop,ShopAdmin)
# admin.site.register(Products,ProductsAdmin)
admin.site.register([Category,SubCategory,FilterTag,City,Offer,Feedback,Vote,Deals,Products])