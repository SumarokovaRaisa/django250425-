from django.urls import path

from library.views.categories import CategoryRetrieveUpdateDestroyGenericView

urlpatterns = [
    path('<str:name>/', CategoryRetrieveUpdateDestroyGenericView.as_view()),
]
