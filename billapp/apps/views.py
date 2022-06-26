from urllib import request
from django.shortcuts import render, redirect
from .models import App
from django.contrib import messages
from django.views.generic import (
    ListView,
    CreateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


class AppCreateView(LoginRequiredMixin, CreateView):
    model = App
    fields = ['app_name', 'app_image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AppListView(LoginRequiredMixin, ListView):
    model = App
    template_name = 'apps/apps.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'app_list'
    ordering = ['-date_published']

    def get_queryset(self):
        queryset = super().get_queryset().filter(author=self.request.user)
        return queryset



@login_required
def delete_app(request, slug):
    app = App.objects.filter(slug=slug).first()
    if request.user == app.author:
        app.delete()
        messages.success(request, f'Sucessfully deleted app')
        return redirect('apps')
    else :
        messages.warning(request, f"You are not authorized to do this action")
    return redirect('apps')


