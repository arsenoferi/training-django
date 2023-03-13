from  django.urls import path
from . import views


app_name = 'first_app'

urlpatterns=[
    path('',views.simple_view),
    path('number/<int:num_page>/',views.num_page_view),
    path('example_view/',views.example_view, name = 'example-view'),
    path('variable/',views.variable_view, name='variable-view'),
    #path('<int:num1>/<int:num2>/', views.add_value),
]

