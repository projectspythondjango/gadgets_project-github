from django.urls import path
from .import views

app_name = 'gadgetsapp'
urlpatterns=[
    path('',views.index,name='index'),
    path('detail/<int:idnumber>/',views.detail,name='detail'),
    path('add/',views.addgadgets,name='addgadgets'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')
]