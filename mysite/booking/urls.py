from django.urls import path
from .views import HotelViewSets

urlpatterns = [
    path('', HotelViewSets.as_view({'get': 'list','post':'create'}), name='hotel_list'),
    path('<int:pk>/', HotelViewSets.as_view({'get': 'list', 'put': 'update','delete':'destroy'}), name='hotel_detail')
]
