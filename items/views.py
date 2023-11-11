from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from items.paginators import ItemPagination
from items.models import Item
from items.serializers import ItemSerializer
from items.services import total_price


class ItemCreateAPIView(generics.CreateAPIView):
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        data = self.request.data
        price = float(data['price'])
        final_price = total_price(price)
        print(final_price)
        serializer.save(final_price=final_price)

        user = self.request.user
        serializer.save(user=user)


class ItemListAPIView(generics.ListAPIView):
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = ItemPagination

    queryset = Item.objects.all()


class ItemRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]
    queryset = Item.objects.all()


class ItemUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]
    queryset = Item.objects.all()


class ItemDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]
    queryset = Item.objects.all()
