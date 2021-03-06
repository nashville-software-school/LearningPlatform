from io import BytesIO
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login, logout
from django.core.files import File
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group

# import model(s) from LearningAPI app. No need to do HTTP calls to the API. Cool.
from LearningAPI.models import Instructor, Student, CohortType
from .models import StudentDisengagement, ReasonCode, DisengagementType, StudentNote
from .forms import StudentDisengagementForm, StudentNoteForm
from .helpers import generate_pdf, send_pdf_email

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
    disengagement = get_object_or_404(StudentDisengagement, pk=pk)
    template = "student_disengagement/studentdisengagement_sig.html"

    pdf = generate_pdf(template, disengagement)
    if pdf:
        filename = f"student_disengagement_{disengagement.student.last_name}_{disengagement.id}.pdf"
        disengagement.pdf.save(filename, File(BytesIO(pdf.content)))
        send_pdf_email(filename, disengagement)
        return redirect(reverse('student_disengagement:disengagement_list'))
    return HttpResponse("Not found")

# note views
def group_test(self):
    """test user must pass to get access to /note view"""

    group =  Group.objects.get(name='instructors')
    return group in self.groups.all()

@user_passes_test(group_test)
@require_http_methods(["GET", "POST"])
def studentNoteFormView(request):
    if request.method == "POST":
          # create a form instance and populate it with data from the request:
          form = StudentNoteForm(request.POST)
          # check whether it's valid:
          if form.is_valid():
              form.save()
              # redirect to a new URL:
              return HttpResponseRedirect(reverse('student_disengagement:note_list'))

    form = StudentNoteForm(request.user)
    form.fields['instructor'].initial = Instructor.objects.get(pk=request.user.id)
    return render(request, 'student_disengagement/note_form.html', {"form": form})

@user_passes_test(group_test)
def studentNoteListView(request):
    notes = get_list_or_404(StudentNote.objects.order_by('student'), instructor=request.user.id)
    return render(request, 'student_disengagement/note_list.html', {"notes": notes})


def load_disengagement_students(request, instructor_id):
  pass

def load_note_students(request, instructor_id):
  pass

# based on: https://simpleisbetterthancomplex.com/tutorial/2018/01/29/how-to-implement-dependent-or-chained-dropdown-list-with-django.html
def load_students(request, form_type, instructor_id):
    """student note view helper: dynamically loading new Student list when Instructor is changed in form"""

    # values_list returns a QuerySet that returns list of tuples, rather than model instances
    # flat=True will remove the tuples and return the list
    student_list = Instructor.objects.get(pk=instructor_id).students.all().values_list('id', flat=True)
    students = Student.objects.filter(id__in=student_list).distinct()

    return render(request, 'student_disengagement/student_dropdown_list_options.html', {'students': students})

# if using this view to load students for a disengagement, select only students who have no related disengagement or have a disengagement that is a leave of absence -- because leave of absence students can still have a permanent disengagement created
    # students = Student.objects.filter(Q(disengaged_student__isnull=True) | Q(disengaged_student__disengagement_type=2))
