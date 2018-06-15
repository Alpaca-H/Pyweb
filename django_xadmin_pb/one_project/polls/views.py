from django.shortcuts import render
from .models import wew
# Create your views here.



def test(request):

    return render(request,'留言板.html',)

def index(request):
    if request.method == "POST":
        name = request.POST['name']
        message = request.POST['message']
        address = request.POST['address']
        email = request.POST['email']
        wews = wew()
        wews.name = name
        wews.email = email
        wews.message = message
        wews.address = address
        print(wews.name, wews.email, wews.message, wews.address)
        wews.save()
    return  render(request,'留言板.html')