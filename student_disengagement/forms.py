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
        fields = ['student', 'disengagement_type', 'disengagement_detail', 'reason', 'cohort_type', 'instructor', 'effective_date', 'last_attendance_date', 'intended_return_date', 'return_conditions']
        widgets = {
            'effective_date': DatePickerInput(),
            'last_attendance_date': DatePickerInput(),
            'intended_return_date': DatePickerInput()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['student'].empty_label = 'Select student name'
        self.fields['student'].label = "Student name"
        # select only students who have no related disengagement or have a disengagement that is a leave of absence -- because leave of absence students can still have a permanent disengagement created
        self.fields['student'].queryset = Student.objects.filter(Q(disengaged_student__isnull=True) | Q(disengaged_student__disengagement_type=2))
        self.fields['instructor'].empty_label = 'Select instructor name'
        self.fields['instructor'].label = 'Instructor name'


class StudentNoteForm(ModelForm):

    class Meta:
        model = StudentNote
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['student'].empty_label = 'Select student name'
        self.fields['student'].label = "Student name"
        self.fields['instructor'].empty_label = 'Select instructor name'
        self.fields['instructor'].label = 'Instructor name'
