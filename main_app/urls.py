from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_widget/', views.add_widget, name='add_widget'),
    path('delete_widget/<int:widget_id>',
         views.delete_widget,
         name='delete_widget')
    # path('delete_widget/<int:pk>',
    #      views.WidgetDelete.as_view(),
    #      name='delete_widget'),
    # path('', views.WidgetCreate.as_view(), name='create'),
    # path('', views.WidgetDelete.as_view(), name='delete'),
]