from django.shortcuts import render

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# def index(request: HttpRequest) -> HttpResponse:
#     return render(
#         request=request,
#         template_name="myapp/index.html",
#         context={},
#     )

def index(request) :
    return render(
        request=request,
        template_name="myapp/index.html",
        context={
            "content" : "This is the content."
        },
    )