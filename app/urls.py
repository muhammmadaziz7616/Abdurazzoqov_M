from django.urls import path
from django.conf.urls.static import static

from app.views import  PersonListView ,PersonDeleteView
from root.settings import MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    path('', PersonListView.as_view(), name='index'),
    path('delete/<int:pk>', PersonDeleteView.as_view(), name='delete_product'),
    ]