from .forms import *
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.timezone import now
from datetime import timedelta

def index(request):
    return render(request, 'index.html')

def create(request):
    return render(request, 'create.html')

def delivery(request):
    return render(request, 'delivery.html')

def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                login(request, user)
                return redirect('previous')
            else:
                error_message = "Invalid email or password. Please try again."
        except User.DoesNotExist:
            error_message = "Invalid email or password. Please try again."
    
    return render(request, 'login.html', {'error_message': error_message if 'error_message' in locals() else None})

def logout_view(request):
    logout(request)  # Log out the user
    return redirect('index')

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)  # Directly save the user
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save(update_fields=['password'])  # Update the password field
            return redirect('login')
    else:
        form = UserForm()

    return render(request, 'signup.html', {'form': form})


def create_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()  
            return redirect('created')  # Use a redirect for better UX
    else:
        form = UserForm()

    return render(request, 'signup.html', {'form': form})

def update_user(request, userem):
    user = get_object_or_404(User, email=userem)
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            return redirect('update_confirmation')  # Redirect after successful update
    else:
        form = UserForm(instance=user)
        
    return render(request, 'update_user.html', {'form': form, 'user': user})

def create_pizza(request):
    if request.method == 'POST':
        form = PizzaForm(request.POST)
        if form.is_valid():
            pizza = form.save()
            return redirect('delivery')

    else:
        form = PizzaForm()
    
    return render(request, 'create.html', {'form': form})

def delivery(request):
    if request.method == 'POST':
        form = DeliveryForm(request.POST)
        
        if form.is_valid():
            pizza = Pizza.objects.last()
            
            order = Order(
                user=request.user,
                pizza=pizza,
                delivery_name=form.cleaned_data['name'],
                delivery_address=form.cleaned_data['address_line_1'],
                delivery_time=timezone.now() + timedelta(hours=1),
                payment_info=form.cleaned_data['card_number'],
            )
            order.save()
            
            request.session['delivery_id'] = order.id
            
            return redirect('final')

    else:
        form = DeliveryForm()

    return render(request, 'delivery.html', {'form': form})

def final(request):
    delivery_id = request.session.get('delivery_id')
    
    if delivery_id:
        try:
            order = Order.objects.get(id=delivery_id)
            pizza = order.pizza

            context = {
                'order': order,
                'pizza': pizza,
                'delivery_name': order.delivery_name,
                'delivery_address': order.delivery_address,
                'delivery_time': order.delivery_time,
            }
            return render(request, 'final.html', context)

        except Order.DoesNotExist:
            return redirect('index')

    return redirect('index')

def previous(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'previous.html', {'orders': orders})