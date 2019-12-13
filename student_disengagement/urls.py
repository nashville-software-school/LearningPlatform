from django.urls import path
from . import views

app_name = 'student_disengagement'
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.auth, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('disengagement_form', views.studentDisengagementFormView, name='disengagement_form'),
    path('disengagements', views.studentDisengagementListView, name='disengagement_list'),
    path('disengagements/<int:pk>/', views.studentDisengagementDetailView, name='disengagement'),
    path('disengagements/<int:pk>/update', views.studentDisengagementEditView, name='disengagement_edit'),
    # path('disengagements/<int:pk>/signature', views.StudentDisengagementSignatureView, name='disengagement_signature'),
    path('disengagements/<int:pk>/pdf', views.studentDisengagementPDFView, name='disengagement_pdf'),
    path('note', views.studentNoteFormView, name='note_form'),
    # for dynamic loading of updated student list into note_form
    path('load-students/<str:form_type>/<int:instructor_id>', views.load_students, name='ajax_load_students'),
    path('my_notes', views.studentNoteListView, name='note_list'),
]
