from django.conf.urls import url
from django.contrib import admin

from .views import (
    ShopDeleteAPIView,
    ShopDetailAPIView, 
	ShopListAPIView,
	ShopUpdateAPIView,
	ShopCreateAPIView,
    CityListAPIView,
    CategoryListAPIView,
    SubCategoryListAPIView,
 )



urlpatterns = [
    url(r'^$', ShopListAPIView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', ShopDetailAPIView.as_view(), name='detail'), 
    url(r'^(?P<pk>\d+)/edit$', ShopUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete$', ShopDeleteAPIView.as_view(), name='delete'),
    url(r'^create$', ShopCreateAPIView.as_view(), name='Create'),
    url(r'^cities$',CityListAPIView.as_view(),name="listCity"),
    url(r'^categories$',CategoryListAPIView.as_view(),name="listCategory"),
    url(r'^subcategories$',SubCategoryListAPIView.as_view(),name="listsubCategory")
    ]

