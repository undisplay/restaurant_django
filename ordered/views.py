from django.shortcuts import render,redirect
from .models import DrinkOrderedLine, MealOrderedLine, WashOrderedLine, Ordered,Drink,Meal,Wash

def sale_view(request):
    
    if request.method == "POST":
        Ordered.objects.create(employe = request.user,client = request.POST["client"])
        return redirect("sale_view")
    else:
        try:
            ordereds = Ordered.objects.all().filter(is_complete=False).order_by("-updated_at")
        except :
            ordereds = []
            
        try:
            meals = Meal.objects.all().order_by("name")
        except :
            meals = []
            
        try:
            drinks = Drink.objects.all().order_by("name")
        except :
            drinks = []
            
        try:
            washes = Wash.objects.all().order_by("type")
        except :
            washes = []
        
        return render(request,"ordered/index.html",{
            "ordereds":ordereds,
            "meals":meals,
            "drinks":drinks,
            "washes":washes
        })
        
def sale_line(request):
    
    if request.method == "POST":
        try:
            ordered = Ordered.objects.get(id = request.POST["ordered_id"])
        except :
            ordered = None
                
        if request.POST["product"] == "drink":  
            try:
                drink = Drink.objects.get(id = request.POST["id"])
            except :
                drink = None
            
            if ordered and drink:
                DrinkOrderedLine.objects.create(ordered = ordered,drink = drink, quantity = request.POST["quantity"])
                ordered.save()
                
        if request.POST["product"] == "meal":  
            try:
                meal = Meal.objects.get(id = request.POST["id"])
            except :
                meal = None
            
            if ordered and meal:
                MealOrderedLine.objects.create(ordered = ordered,meal = meal, quantity = request.POST["quantity"])
                ordered.save()
                
        if request.POST["product"] == "wash":  
            try:
                wash = Wash.objects.get(id = request.POST["id"])
            except :
                wash = None
            
            if ordered and wash:
                WashOrderedLine.objects.create(ordered = ordered,wash = wash, quantity = request.POST["quantity"])
                ordered.save()
            
        return redirect("sale_view")
    else:
        return redirect("sale_view")