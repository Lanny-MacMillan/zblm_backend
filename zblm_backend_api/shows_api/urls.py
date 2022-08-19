from django.urls import path
from . import views

urlpatterns = [
    path('api/shows', views.ShowList.as_view(), name='show_list'), 
    # api/shows will be routed to the ShowList view for handling
    path('api/shows/<int:pk>', views.ShowDetail.as_view(), name='show_detail'), 
    # api/shows will be routed to the ShowDetail view for handling
]