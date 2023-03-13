from django.urls import path
from . import views

app_name = "catalog"

urlpatterns = [
    path("",views.index,name='index'),
    path('create/',views.BookCreate.as_view(),name='create'),
    path('book_detail/<int:pk>', views.BookDetail.as_view(),name='book_detail')
]
