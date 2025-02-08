from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .models import Product,Order
from .forms import ProductForm

# Create your views here.
def home(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        data = Product.objects.all()
    data = Product.objects.all()
    orders = Order.objects.all()
    form =  ProductForm()
    return render(request,'electronics/home.html',{'data':data,'orders': orders,'form':form})