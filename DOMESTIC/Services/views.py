from django.shortcuts import render,HttpResponse,redirect
from .models import Cleaning,Electics,Plumbing,Carpenter,Review
from datetime import date

# Create your views here.

# For Cleanning Services page and reviews.
def cleanning(request):
    if request.method=="POST":
        uname=request.POST.get('rtext')
        comment=request.POST.get('comment')
        rating=str(request.POST.get('rating'))
        today=date.today()
        dt=today.strftime("%Y-%m-%d")
        review=Review(uname=uname,comment=comment,rating=rating,dt=dt)
        review.save()
        return redirect('cleanning')
    info=Review.objects.all()[:6]
    services = Cleaning.objects.all()
    params ={'cleaning':services,'info':info}
    return render(request, 'cleanning.html',params)

# For Carpenter Services page and reviews.
def carpenter(request):
    carpenter = Carpenter.objects.all()
    if request.method=="POST":
        uname=request.POST.get('rtext')
        comment=request.POST.get('comment')
        rating=str(request.POST.get('rating'))
        today=date.today()
        dt=today.strftime("%Y-%m-%d")
        review=Review(uname=uname,comment=comment,rating=rating,dt=dt)
        review.save()
        return redirect('carpenter')
    info=Review.objects.all()[:6]
    params = {'carpenter':carpenter,'info':info}
    return render(request, 'carpenter.html',params)

# For Electrics Services page and reviews.
def electrics(request):
    electrics = Electics.objects.all()
    if request.method=="POST":
        uname=request.POST.get('rtext')
        comment=request.POST.get('comment')
        rating=str(request.POST.get('rating'))
        today=date.today()
        dt=today.strftime("%Y-%m-%d")
        review=Review(uname=uname,comment=comment,rating=rating,dt=dt)
        review.save()
        return redirect('electrics')
    info=Review.objects.all()[:6]
    param = {'electrics':electrics,'info':info}
    return render(request, 'electrics.html',param)

# For Plumbing Services Page and Reviews.
def plumbing(request):
    plumbing = Plumbing.objects.all()
    if request.method=="POST":
        uname=request.POST.get('rtext')
        comment=request.POST.get('comment')
        rating=str(request.POST.get('rating'))
        today=date.today()
        dt=today.strftime("%Y-%m-%d")
        review=Review(uname=uname,comment=comment,rating=rating,dt=dt)
        review.save()
        return redirect('plumbing')
    info=Review.objects.all()[:6]
    params = {'plumbing':plumbing,'info':info}
    return render(request, 'plumbing.html',params)

# Add service to cart logic.
def add_to_cart(request,cat,sno):
    if request.method=="POST":
        item=cat+'-'+str(sno)
        cart = request.session.get('cart')
        if cart:
            if item in cart:
                pass
            else:
                cart[item]=1
        else:
            cart={}
            cart[item]=1
        request.session['cart']=cart
        # print("cart :- ",request.session.get('cart'))
        if cat=="Cleaning":
            return redirect("/cleanning")
        elif cat=="Carpenter":
            return redirect("/carpenter")
        elif cat=="Electrics":
            return redirect("/electrics")
        elif cat=="Plumbing":
            return redirect("/plumbing")
        else:
            return redirect("/")

# Remove service from the cart logic.
def remove_item(request):
    if request.method=="POST":
        cart = request.session.get('cart')
        sno=request.POST.get('itemid')
        if sno in cart:
            del cart[sno]
        request.session['cart']=cart
        return redirect('/cart')