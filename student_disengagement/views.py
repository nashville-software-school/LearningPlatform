from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
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
def studentDisengagementFormView(request, pk=None):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = StudentDisengagementForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('student_disengagement:disengagement_list'))

    form = StudentDisengagementForm()
    return render(request, 'student_disengagement/withdrawal_form.html', {"form": form})

@login_required
def studentDisengagementListView(request):
    disengagements = get_list_or_404(StudentDisengagement)
    return render(request, 'student_disengagement/studentdisengagement_list.html', {"de_list": disengagements})

@login_required
def studentDisengagementDetailView(request, pk):
    disengagement = get_object_or_404(StudentDisengagement, pk=pk)
    return render(request, 'student_disengagement/studentdisengagement_detail.html', {"de": disengagement})

@login_required
@require_http_methods(["GET", "POST"])
def studentDisengagementEditView(request, pk):
    disengagement = StudentDisengagement.objects.get(pk=pk)
    if request.method == "POST":
        form = StudentDisengagementForm(request.POST, instance=disengagement)
        if form.is_valid():
          form.save()
          return HttpResponseRedirect(reverse('student_disengagement:disengagement', args=[pk]))

    form = StudentDisengagementForm(instance=disengagement)
    return render(request, 'student_disengagement/withdrawal_form.html', {"form": form})



@login_required
def studentDisengagementPDFView(request, pk):
    # disengagement = get_object_or_404(StudentDisengagement, pk=pk)
    # template = "student_disengagement/studentdisengagement_sig.html"

    # pdf = generate_pdf(template, disengagement)
    # if pdf:
    #     filename = f"student_disengagement_{disengagement.student.last_name}_{disengagement.id}.pdf"
    #     disengagement.pdf.save(filename, File(BytesIO(pdf.content)))
    #     send_pdf_email(filename, disengagement)
    #     return redirect(reverse('student_disengagement:disengagement_list'))
    # return HttpResponse("Not found")
    pass
