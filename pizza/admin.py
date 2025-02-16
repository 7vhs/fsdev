from django.contrib import admin
from django import forms
from .models import Pizza, Topping, PizzaSize, PizzaCrust, PizzaSauce, PizzaCheese

class PizzaSizeAdmin(admin.ModelAdmin):
    list_display = ('name',)

class PizzaCrustAdmin(admin.ModelAdmin):
    list_display = ('name',)

class PizzaSauceAdmin(admin.ModelAdmin):
    list_display = ('name',)

class PizzaCheeseAdmin(admin.ModelAdmin):
    list_display = ('name',)

class PizzaAdmin(admin.ModelAdmin):
    list_display = ('size', 'crust', 'sauce', 'cheese')  
    search_fields = ['size__name', 'crust__name', 'sauce__name', 'cheese__name']
    filter_horizontal = ('toppings',)

admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Topping)
admin.site.register(PizzaSize, PizzaSizeAdmin)
admin.site.register(PizzaCrust, PizzaCrustAdmin)
admin.site.register(PizzaSauce, PizzaSauceAdmin)
admin.site.register(PizzaCheese, PizzaCheeseAdmin)