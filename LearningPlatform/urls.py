"""LearningPlatform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from rest_framework import routers
from django.contrib import admin
from django.urls import path
from LearningAPI import views

router = routers.DefaultRouter()
router.register(r'nssusers', views.NssUserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'proposals', views.ProposalViewSet)
router.register(r'proposalstatus', views.ProposalStatusViewSet)
router.register(r'capstonetypes', views.CapstoneTypeViewSet)
router.register(r'cohorts', views.CohortViewSet)
router.register(r'nssusercohorts', views.NssUserCohortViewSet)
router.register(r'exercises', views.ExerciseViewSet)
router.register(r'nssuserexercises', views.NssUserExerciseViewSet)
router.register(r'preworkpoints', views.PreworkPointsViewSet)
router.register(r'treehousebadges', views.TreehouseBadgeViewSet)
router.register(r'nssuserbadges', views.NssUserBadgeViewSet)
# router.register(r'users', views.UserViewSet)
router.register(r'companies', views.CompanyViewSet)
router.register(r'contacts', views.ContactViewSet)
router.register(r'leadgentypes', views.LeadGenerationTypeViewSet)
router.register(r'technologies', views.TechnologyViewSet)
router.register(r'jobtypes', views.JobTypeViewSet)
router.register(r'placements', views.PlacementViewSet)
router.register(r'appstagetypes', views.ApplicationStageTypeViewSet)
router.register(r'appstages', views.ApplicationStageViewSet)
router.register(r'students', views.StudentViewSet)
router.register(r'instructors', views.InstructorViewSet)
router.register(r'cohorttypes', views.CohortTypeViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('engagement/', include('student_disengagement.urls')),
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
