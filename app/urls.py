from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('back', views.back, name="back"),
    path('log_in', views.log_in_page_render, name="log_in"),
    path('home_page', views.home_page_render, name="home_page"),
    path('register_page', views.register_page_render, name="register_page"),
    path('user_profile_page/<int:user_id>', views.user_profile_page, name="user_profile"),
    path('add_entry_page', views.add_entry_page, name="add_entry_page"),
    path('deities_by_religion/<str:deity_religion>', views.deities_by_religion_page, name="deities_by_religion"),
    path('deities_by_location/<str:deity_location>', views.deities_by_location_page, name="deities_by_religion"),
    path('deity_info_page/<int:deity_id>', views.deity_info_page, name="deity_info"),
    path('register', views.register, name="register"),
    path('logout', views.logout, name="logout"),
    path('login', views.login, name="login"),
    path('searchbar', views.searchbar, name="searchbar"),
    path('add_deity', views.add_deity, name="add_deity"),
    path('deity_edit_page/<int:deity_id>', views.deity_edit_page, name="deity_edit_page"),
    path('edit_deity/<int:deity_id>', views.edit_deity, name="edit_deity"),
    path('genCSV', views.generateCSV, name="genCSV"),
    path('wiki_sum/<str:deity_name>', views.wiki_sum_page, name="wiki_sum"),
    path('wiki_error', views.wiki_error, name="wiki_error")
]