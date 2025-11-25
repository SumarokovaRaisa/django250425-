from rest_framework.generics import RetrieveUpdateDestroyAPIView

from library.models import Category
from library.serializers import CategorySerializer


class CategoryRetrieveUpdateDestroyGenericView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'name_category'  # Колонка из БД
    lookup_url_kwarg = 'name'  # Название параметра в url (<type:param>)
