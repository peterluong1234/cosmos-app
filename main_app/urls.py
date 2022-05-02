from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('events/', views.EventList.as_view(), name='events_list'),
    path('events/create/', views.EventCreate.as_view(), name='events_create'),
    path('events/<int:pk>/', views.EventDetail.as_view(), name='events_detail'),
    # path('events/<int:pk>/update/', views.EventUpdate.as_view(), name='events_update'),
]