# from django.contrib import admin
from django.urls import path
from converter.views import CurrencyConverterView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/', CurrencyConverterView.as_view()),
]
