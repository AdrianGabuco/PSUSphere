"""
URL configuration for projectsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from studentorg.views import HomePageView, OrganizationList, OrganizationCreateView, OrganizationUpdateView, OrganizationDeleteView, MemberList, MemberCreateView, MemberUpdateView, MemberDeleteView, CollegeList, CollegeCreateView, CollegeUpdateView, CollegeDeleteView, StudentList, StudentCreateView, StudentUpdateView, StudentDeleteView, ProgramList, ProgramCreateView, ProgramUpdateView, ProgramDeleteView
from studentorg import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePageView.as_view(), name='home'),
    path('organization_list', views.OrganizationList.as_view(), name='organization-list'),
    path('organization_list/add', views.OrganizationCreateView.as_view(), name='organization-add'),
    path('organization_list/<pk>', views.OrganizationUpdateView.as_view(), name='organization-edit'),
    path('organization_list/<pk>/delete', views.OrganizationDeleteView.as_view(), name='organization-delete'),
    path('member_list', views.MemberList.as_view(), name='member-list'),
    path('member_list/add', views.MemberCreateView.as_view(), name='member-add'),
    path('member_list/<pk>', views.MemberUpdateView.as_view(), name='member-edit'),
    path('member_list/<pk>/delete', views.MemberDeleteView.as_view(), name='member-delete'),
    path('college_list', views.CollegeList.as_view(), name='college-list'),
    path('college_list/add', views.CollegeCreateView.as_view(), name='college-add'),
    path('college_list/<pk>', views.CollegeUpdateView.as_view(), name='college-edit'),
    path('college_list/<pk>/delete', views.CollegeDeleteView.as_view(), name='college-delete'),
    path('student_list', views.StudentList.as_view(), name='student-list'),
    path('student_list/add', views.StudentCreateView.as_view(), name='student-add'),
    path('student_list/<pk>', views.StudentUpdateView.as_view(), name='student-edit'),
    path('student_list/<pk>/delete', views.StudentDeleteView.as_view(), name='student-delete'),
    path('program_list', views.ProgramList.as_view(), name='program-list'),
    path('program_list/add', views.ProgramCreateView.as_view(), name='program-add'),
    path('program_list/<pk>', views.ProgramUpdateView.as_view(), name='program-edit'),
    path('program_list/<pk>/delete', views.ProgramDeleteView.as_view(), name='program-delete'),
]
