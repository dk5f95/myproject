from rest_framework.serializers import ModelSerializer

from shop.models import ( Shop, City, Category, SubCategory)


class ShopListSerializer(ModelSerializer):
	class Meta:
		model = Shop
		fields = [
          'city',
          'category',
          'subCategory',
          'shopName',
          'tagline',
          'bannerImage',
          'email',
          'mobileNo',
          'alternateMobileNo',
          'location',
          'ownerName',
          'shopAddress',
          'shopPinCode',
          'openingTime',
          'closingTime',
          'closingDay',
          ]

class ShopDetailSerializer(ModelSerializer):
     class Meta:
          model = Shop
          fields = [
          'city',
          'category',
          'subCategory',
          'shopName',
          'tagline',
          'bannerImage',
          'email',
          'mobileNo',
          'alternateMobileNo',
          'location',
          'ownerName',
          'shopAddress',
          'shopPinCode',
          'openingTime',
          'closingTime',
          'closingDay',
          ]

class ShopCreateSerializer(ModelSerializer):
     class Meta:
          model = Shop
          fields = [
          'city',
          'category',
          'subCategory',
          'shopName',
          'tagline',
          'bannerImage',
          'email',
          'mobileNo',
          'alternateMobileNo',
          'location',
          'ownerName',
          'shopAddress',
          'shopPinCode',
          'openingTime',
          'closingTime',
          'closingDay',
          'isActive'
          ]


class CityListSerializer(ModelSerializer):
     class Meta:
          model = City
          fields = [
               'id',
               'city',
               'state',
               'country',
               'cityImg',
          ]
class CategoryListSerializer(ModelSerializer):
     class Meta:
          model = Category
          fields = [
               'name',
               'catImg',
               'id',
          ]
class CategorySerializerHelper(ModelSerializer):
     class Meta:
          model = Category
          fields = [
               'id',
               'name',
          ]
class SubCategoryListSerializer(ModelSerializer):
     category = CategorySerializerHelper()
     class Meta:
          model = SubCategory
          fields = [
               'category',
               'id',
               'name',
               'subCatImg'
          ]


