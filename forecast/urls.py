from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
	url(r'^$',views.index,name='index'),
    url(r'^holtwinter$', views.model_form_upload, name='model_form_upload'),
    url(r'^croston$', views.crostonview, name='croston'),
    url(r'^arima$',views.arimaview,name='arima'),
    url(r'^fbprophet$',views.fbprophetview,name='fbprophet'),
    url(r'^decomposition$',views.decompositionview,name='decompose'),

   
]