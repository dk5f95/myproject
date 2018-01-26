from rest_framework.generics import ( 
   CreateAPIView,
   ListAPIView,
   RetrieveAPIView,
   DestroyAPIView,
   UpdateAPIView,

   )

from shop.models import ( Shop, City, Category, SubCategory)
from .serializers import (
	ShopCreateSerializer,
	ShopDetailSerializer,
    ShopListSerializer,
    CityListSerializer,
    CategoryListSerializer,
    SubCategoryListSerializer,
    )



class ShopCreateAPIView(CreateAPIView):
	queryset = Shop.objects.all()
	serializer_class = ShopCreateSerializer


class ShopDetailAPIView(RetrieveAPIView):
	queryset = Shop.objects.all()
	serializer_class = ShopDetailSerializer

class ShopUpdateAPIView(UpdateAPIView):
	queryset = Shop.objects.all()
	serializer_class = ShopDetailSerializer




class ShopDeleteAPIView(DestroyAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopDetailSerializer




class ShopListAPIView(ListAPIView):
	queryset = Shop.objects.all()
	serializer_class = ShopListSerializer

class CityListAPIView(ListAPIView):
	queryset = City.objects.all()
	serializer_class = CityListSerializer

class CategoryListAPIView(ListAPIView):
	queryset = Category.objects.all()
	serializer_class = CategoryListSerializer

class SubCategoryListAPIView(ListAPIView):
	queryset = SubCategory.objects.all()
	serializer_class = SubCategoryListSerializer