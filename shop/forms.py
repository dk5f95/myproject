from django import forms

from .models import Shop

class addshop(forms.ModelForm):
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
