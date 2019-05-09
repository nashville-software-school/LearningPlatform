from django.shortcuts import render, redirect
from django.contrib import messages

# auth
def auth(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    template = 'student_disengagement/index.html'

    if user is not None:
        login(request, user)
        return render(request, template)
    else:
        msg = "Invalid credentials, please try again"
        return render(request, template, {"message": msg})


# home
def index(request):
    message = None
    if( 'logout_message' in request.session ):
        message = request.session['logout_message']
        del request.session['logout_message']

    template = 'student_disengagement/index.html'
    return render(request, template, {'logout_message': message })
