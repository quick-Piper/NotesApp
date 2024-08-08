from typing import Any
from django.shortcuts import render, redirect
from .models import Note
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import UserRegisterForm
from django.core.serializers import serialize
from django.http import JsonResponse
import json
from datetime import datetime, date


class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        return super().default(obj)

class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'document/note_home.html'
    context_object_name = 'notes'
    ordering = ['-modified_at']

    def get_queryset(self):
        return Note.objects.filter(author=self.request.user) 

class NoteDetailView(DetailView):   
    model = Note


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    
class NoteEditView(LoginRequiredMixin, UpdateView):
    model = Note
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)           
 

class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    success_url = '/'
 
 
# register page for user
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in.')
            return redirect('login')
    else:       
        form = UserRegisterForm()
    return render(request, 'document/register.html', {'form': form})
 
 
# logout function
def user_logout(request):
    logout(request)
    return render(request, 'document/logout.html', {})
    



