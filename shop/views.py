# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404


from .forms import addshop
from .models import Shop

# Create your views here.





def add_shop(request):
    form = addshop(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        # print (form.cleaned_data.get("title"))
        instance.save()






    # if request.method == "POST":
    #     print request.POST.get("content")
    #     title = request.POST.get("content")
    #     print request.POST.get("title")
    context = {
        "form": form,
    }
    return render(request, "addshop.html", context)
