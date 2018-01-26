from django.conf.urls import url, include
from django.contrib import admin
from django_private_chat import urls as django_private_chat_urls
from django.views.generic.base import TemplateView
from ang.views import AngularTemplateView


urlpatterns = [
    url(r'^posts/', include("posts.urls")),
	url(r'^admin/', admin.site.urls),
    url(r'^', include('django_private_chat.urls')),
    url(r'^api/shop/', include("shop.api.urls", namespace='shop-api')),
    url(r'^api/templates/(?P<item>[A-Za-z0-9\_\-\.\/]+)\.html$', AngularTemplateView.as_view())
]

urlpatterns += [ 
       url(r'',TemplateView.as_view(template_name='ang/index.html'))
       ]

                                           
