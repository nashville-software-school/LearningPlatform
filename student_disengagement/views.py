from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login, logout

# import model(s) from LearningAPI app
from LearningAPI.models import Instructor, Student, CohortType
from .models import StudentDisengagement, ReasonCode, DisengagementType, StudentNote
from .forms import StudentDisengagementForm, StudentNoteForm

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

def logout_view(request):
    name = request.user.first_name
    logout(request)
    request.session['logout_message'] = f"Bye, {name}"
    return redirect('student_disengagement:index')

# home
def index(request):
    message = None
    if( 'logout_message' in request.session ):
        message = request.session['logout_message']
        del request.session['logout_message']

    template = 'student_disengagement/index.html'
    return render(request, template, {'logout_message': message })

# disengagement views
@login_required
@require_http_methods(["GET", "POST"])
def studentDisengagementFormView(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = StudentDisengagementForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            disengagement = form.save()
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('student_disengagement:disengagement_list'))
    else:
      form = StudentDisengagementForm()
      return render(request, 'student_disengagement/withdrawal_form.html', {"form": form})

@login_required
def studentDisengagementListView(request):
    disengagements = get_list_or_404(StudentDisengagement)
    return render(request, 'student_disengagement/student_disengagement_list.html', {"de": disengagments})
