from django.urls import path
from . import views



urlpatterns = [
    
    path('', views.home, name='home'),
    path('PAPYRUS/Shop', views.shop, name='PAPYRUS/Shop'),
    path('PAPYRUS/Events', views.events, name='PAPYRUS/Events'),
    path('Blog/Post', views.blog, name='Blog/Post'),
    path('About-Us', views.about, name='About-Us'),
    path('Our-Team', views.team, name='Our-Team'),
    path('Our-Partiners', views.partiners, name='Our-Partiners'),
    path('Get-In-Touch', views.contact, name='Get-In-Touch'),
    path('Shop', views.shop, name='shop'),
    path('Food | Gallary', views.food_gallary, name='Food | Gallary'),
    path('Our Story', views.our_story, name='Our Story'),
    


]