from django.shortcuts import redirect, render

from .forms import OrderForm,RegisterForm,LoginForm
from .models import Customer, Order,Product
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request,'core/homes.html')

@login_required(login_url='login')
def dashboard(request):
    data = Customer.objects.all()
    order = Order.objects.all()
    totalorder = order.count()
    orderdelivered = Order.objects.filter(status='Delivered').count()
    orderpending = Order.objects.filter(status='Pending').count()
    orderpacked = Order.objects.filter(status='Packed').count()

    context = {
        'data': data,
        'order': order,
        'totalorder': totalorder,
        'orderdelivered': orderdelivered,
        'orderpending': orderpending,
        'orderpacked':orderpacked
    }
    return render(request, 'core/dashboard.html', context)

@login_required(login_url='login')
def customerdetail(request, id):
    data = Customer.objects.get(id=id)
    order = data.order_set.all()
    total_order = order.count()
    context = {
        'data': data,
        'totalorder': total_order,
        'order': order,
    }
    return render(request, 'core/details.html', context)

@login_required(login_url='login')
def updateorder(request, id):
    if request.method == "POST":
        order = Order.objects.get(id=id)
        data = OrderForm(request.POST, instance=order)
        if data.is_valid():
            data.save()
            return redirect('/dashboard/')
    order = Order.objects.get(id=id)
    form = OrderForm(instance=order)
    context = {
        'form': form,
    }
    return render(request, 'core/updateorder.html', context)

@login_required(login_url='login')
def deleteorder(request, id):
    if request.method == "POST":
        order = Order.objects.get(id=id)
        order.delete()
        return redirect('/dashboard/')
    order = Order.objects.get(id=id)
    context = {
        'order': order,
    }
    return render(request, 'core/delete.html', context)

def product(request):
    product = Product.objects.all()
    context = {
        'product': product
    }
    return render(request, 'core/product.html', context)


def registerform(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Registered.')
    else:
        form=RegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'core/register.html',context)


def loginform(request):
    if request.method == "POST":
        fm = LoginForm(data=request.POST)
        if fm.is_valid():
            fname = fm.cleaned_data['username']
            ps = fm.cleaned_data['password']
            user = authenticate(username=fname, password=ps)
        # username = request.POST['username']
        # password = request.POST['password']
        # user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        fm = LoginForm()
    return render(request, 'core/login.html', {'form': fm})


def logoutform(request):
    logout(request)
    return redirect('/login/')





