from ast import Try
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from stores import models
from stores.forms import StoreItemForm
from django.http import Http404


def get_store_items(request: HttpRequest) -> HttpResponse:
    store_items: list[models.StoreItem] = list(models.StoreItem.objects.all())
    context = {
        "store_items": store_items,
    }
    return render(request, "store-item-list.html", context)

def create_store_item(request):
    form = StoreItemForm()
    if request.method == "POST":
        form = StoreItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("store_item_list")
    context = {
        "form": form,
    }
    return render(request, "create-store-item.html", context )

def update_store_item(request, item_id):
    store_item = models.StoreItem.objects.get(id=item_id)
    form = StoreItemForm(instance=store_item)
    if request.method == "POST":
        form = StoreItemForm(request.POST, instance=store_item)
        if form.is_valid():
            form.save()
            return redirect("store_item_list")
    context = {
        "store_item": store_item,
        "form": form,
    }
    return render(request, "update-store-item.html", context)

def delete_store_item(request, item_id):
    try:
        store_item = models.StoreItem.objects.get(id=item_id)
    except models.StoreItem.DoesNotExist:
        raise Http404()
    store_item.delete()
    return redirect("store_item_list")




