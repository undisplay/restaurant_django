from django.shortcuts import render

def sale_view(request):
    return render(request,"ordered/index.html")