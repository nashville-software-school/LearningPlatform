from django import forms
from django.forms import ModelForm
from django.forms.widgets import SelectDateWidget
from django.db.models import Q
from bootstrap_datepicker_plus import DatePickerInput
from .models import StudentDisengagement, ReasonCode, DisengagementType, StudentNote
# import model(s) from nss_users_api app
from LearningAPI.models import Instructor, Student, CohortType

# Create the form class.
class StudentDisengagementForm(ModelForm):
    # adding widget=forms.Select(attrs={'class':'hidden'}) to reason works to hide the input, but I need to hide the whole div created by Crispy Form. Went with JS solution to hide them after they are in the DOM, which is not ideal at all.
    reason = forms.ModelChoiceField(required=False, queryset=ReasonCode.objects.all(), empty_label="Reason for disengagement")
    disengagement_type = forms.ModelChoiceField(queryset=DisengagementType.objects.all(), empty_label="Type of disengagement")
    cohort_type = forms.ModelChoiceField(queryset=CohortType.objects.all(), empty_label="Cohort type")

    class Meta:
        model = StudentDisengagement
        fields = ['instructor', 'student', 'disengagement_type', 'disengagement_detail', 'reason', 'cohort_type', 'effective_date', 'last_attendance_date', 'intended_return_date', 'return_conditions']
        widgets = {
            'effective_date': DatePickerInput(),
            'last_attendance_date': DatePickerInput(),
            'intended_return_date': DatePickerInput()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['student'].empty_label = 'Select student name'
        self.fields['student'].label = "Student name"

        self.fields['student'].queryset = Student.objects.none()
        self.fields['instructor'].empty_label = 'Select instructor name'
        self.fields['instructor'].label = 'Instructor name'

class StudentNoteForm(ModelForm):

    class Meta:
        model = StudentNote
        fields = '__all__'

    # user arg is passed in from the view when form is instantiated
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        student_list = user.instructor.students.all().values_list('id', flat=True)
        student_queryset = Student.objects.filter(id__in=student_list).distinct()
        self.fields['student'].empty_label = 'Select student name'
        self.fields['student'].label = "Student name"
        self.fields['student'].queryset = student_queryset
        self.fields['instructor'].empty_label = 'Select instructor name'
        self.fields['instructor'].label = 'Instructor name'
