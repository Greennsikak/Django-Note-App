from django.urls import path

from . import views

app_name = "Note"

urlpatterns = [
    path('', views.topic, name='topic'),
    path('topic/<int:topic_id>/', views.topics, name='topics'),
    path('topic/new_topic/', views.new_topic, name='new_topic'),
    path('topic/<int:topic_id>/delete', views.del_topic, name='del_topic'),
    path('topic/<int:topic_id>/new_entry/', views.new_entry, name='new_entry'),
    path('topic/<int:entry_id>/edit_entry/', views.edit_entry, name='edit_entry')

]


