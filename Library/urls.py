from django.contrib import admin
from django.urls import path

from Book import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('home/', views.homepage),
    path('home/', views.homepage, name = "Welcome"),
    path('save-book/', views.save_book),
    path('edit-book/<int:id>/', views.edit_book),
    path('delete-book/<int:pk>/', views.delete_book),
    path('show-deleted-data/', views.show_deleted_data),
    path('h-delete-book/<int:pk>/', views.hard_delete_book),
    path('restore/<int:id>/', views.restore_book),
    path('delete-all/', views.delete_all_book),
    path('restore-all/', views.restore_all_book),
    
]
