from django.shortcuts import redirect, render

from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html',)

def signup(request):
    
    if request.method=='POST':
        print("sigup")
        fname=request.POST.get('First Name',False)
        # lname=request.POST['Last Name']
        # phone=request.POST['Phone Number']
        # address=request.POST['Address']
        # city=request.POST['City']
        # country=request.POST['Country']
        # pcode=request.POST['Postal Code']
        # email=request.POST['Email']
        # password=request.POST['passwordSignup']
        # password1=request.POST['passwordConfirm']
        print(fname)
        return redirect('/login')
    else:
        return render(request, 'signup.html')

