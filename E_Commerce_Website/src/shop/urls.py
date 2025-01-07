from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name = 'ShopHome'),
    path('about',views.about, name = 'AboutUs'),
    path('contact',views.contact,name = 'ContactUS'),
    path('search',views.search,name = 'Search'),
    path('tracker',views.tracker,name = 'TrackingStatus'),
    path('checkout',views.checkout,name = 'Checkout'),
    path('products<int:myid>',views.productView,name = 'Products'),
    path('add_contacts',views.add_contacts,name='add_contacts'),
    path('show_contacts',views.show_contacts,name='show_contacts')

]