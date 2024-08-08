from django.urls import path
from .views import (
    NoteListView, 
    NoteDetailView, 
    NoteCreateView,
    NoteEditView,
    NoteDeleteView,
)

urlpatterns = [
    path('', NoteListView.as_view(), name='note-list'),
    path('note/<int:pk>/', NoteDetailView.as_view(), name='note-detail'),
    path('note/new/', NoteCreateView.as_view(), name='note-create'),
    path('note/<int:pk>/edit/', NoteEditView.as_view(), name='note-edit'),
    path('note/<int:pk>/delete/', NoteDeleteView.as_view(), name='note-delete'),
]
