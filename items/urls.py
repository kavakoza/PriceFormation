from items.apps import ItemsConfig
from items.views import ItemCreateAPIView, ItemListAPIView, ItemRetrieveAPIView, ItemDestroyAPIView, ItemUpdateAPIView
from django.urls import path

app_name = ItemsConfig.name

urlpatterns = [
    path('items/', ItemListAPIView.as_view(), name='items_list'),
    path('items/create/', ItemCreateAPIView.as_view(), name='item_create'),
    path('items/<int:pk>/', ItemRetrieveAPIView.as_view(), name='item_detail'),
    path('items/update/<int:pk>', ItemUpdateAPIView.as_view(), name='item_update'),
    path('items/delete/<int:pk>/', ItemDestroyAPIView.as_view(), name='item_delete'),
]
