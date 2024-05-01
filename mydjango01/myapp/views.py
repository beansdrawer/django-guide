from django.shortcuts import render

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from myapp.models import Item


# def index(request: HttpRequest) -> HttpResponse:
#     return render(
#         request=request,
#         template_name="myapp/index.html",
#         context={},
#     )

def index(request) :

    item_qs = Item.objects.all()

    return render(
        request=request,
        template_name="myapp/index.html",
        context={
            "item_qs" : item_qs
        },
    )