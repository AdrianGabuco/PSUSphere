from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Organization, OrgMember, Student, College, Program
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from studentorg.forms import OrganizationForm, MemberForm, CollegeForm, StudentForm, ProgramForm
from django.urls import reverse_lazy
from typing import Any
from django.db.models.query import QuerySet
from django.db.models import Q, Count
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models.functions import ExtractMonth, ExtractYear


@method_decorator(login_required, name='dispatch')
class HomePageView(ListView):
    model = Organization
    context_object_name = 'home'
    template_name = 'home.html'

class OrganizationList(ListView):
    model = Organization
    context_object_name = 'organization'
    template_name = 'org_list.html'
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        qs = super(OrganizationList, self).get_queryset(*args, **kwargs)
        if self.request.GET.get("q") != None:
            query = self.request.GET.get('q')
            qs = qs.filter(Q(name__icontains=query) 
                           | Q(description__icontains=query)
                           | Q(college__college_name__icontains=query))
        return qs

class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_add.html'
    success_url = reverse_lazy('organization-list')

class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_edit.html'
    success_url = reverse_lazy('organization-list')

class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = 'org_del.html'
    success_url = reverse_lazy('organization-list')

class MemberList(ListView):
    model = OrgMember
    context_object_name = 'member'
    template_name = 'member_list.html'
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        qs = super(MemberList, self).get_queryset(*args, **kwargs)
        if self.request.GET.get("q") != None:
            query = self.request.GET.get('q')
            qs = qs.filter(Q(student__firstname__icontains=query) 
                    | Q(student__lastname__icontains=query) 
                    | Q(organization__name__icontains=query))
        return qs

class MemberCreateView(CreateView):
    model = OrgMember
    form_class = MemberForm
    template_name = 'member_add.html'
    success_url = reverse_lazy('member-list')

class MemberUpdateView(UpdateView):
    model = OrgMember
    form_class = MemberForm
    template_name = 'member_edit.html'
    success_url = reverse_lazy('member-list')

class MemberDeleteView(DeleteView):
    model = OrgMember
    template_name = 'member_del.html'
    success_url = reverse_lazy('member-list')

class CollegeList(ListView):
    model = College
    context_object_name = 'college'
    template_name = 'college_list.html'
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        qs = super(CollegeList, self).get_queryset(*args, **kwargs)
        if self.request.GET.get("q") != None:
            query = self.request.GET.get('q')
            qs = qs.filter(Q(college_name__icontains=query))
        return qs

class CollegeCreateView(CreateView):
    model = College
    form_class = CollegeForm
    template_name = 'college_add.html'
    success_url = reverse_lazy('college-list')

class CollegeUpdateView(UpdateView):
    model = College
    form_class = CollegeForm
    template_name = 'college_edit.html'
    success_url = reverse_lazy('college-list')

class CollegeDeleteView(DeleteView):
    model = College
    template_name = 'college_del.html'
    success_url = reverse_lazy('college-list')

class StudentList(ListView):
    model = Student
    context_object_name = 'student'
    template_name = 'student_list.html'
    paginate_by = 10

    def get_queryset(self, *args, **kwargs):
        qs = super(StudentList, self).get_queryset(*args, **kwargs)
        if self.request.GET.get("q") != None:
            query = self.request.GET.get('q')
            qs = qs.filter(Q(student_id__icontains=query) 
                        | Q(lastname__icontains=query) 
                        | Q(firstname__icontains=query) 
                        | Q(middlename__icontains=query) 
                        | Q(program__prog_name__icontains=query) )
        return qs

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_add.html'
    success_url = reverse_lazy('student-list')

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_edit.html'
    success_url = reverse_lazy('student-list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_del.html'
    success_url = reverse_lazy('student-list')

class ProgramList(ListView):
    model = Program
    context_object_name = 'program'
    template_name = 'program_list.html'
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        qs = super(ProgramList, self).get_queryset(*args, **kwargs)
        if self.request.GET.get("q") != None:
            query = self.request.GET.get('q')
            qs = qs.filter(Q(prog_name__icontains=query) 
                        | Q(college__college_name__icontains=query) )
        return qs

class ProgramCreateView(CreateView):
    model = Program
    form_class = ProgramForm
    template_name = 'program_add.html'
    success_url = reverse_lazy('program-list')

class ProgramUpdateView(UpdateView):
    model = Program
    form_class = ProgramForm
    template_name = 'program_edit.html'
    success_url = reverse_lazy('program-list')

class ProgramDeleteView(DeleteView):
    model = Program
    template_name = 'program_del.html'
    success_url = reverse_lazy('program-list')

class DashboardView(ListView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def get_queryset(self, *args, **kwargs):
        pass

def students_per_college(request):
    data = College.objects.annotate(
        student_count=Count('program__student')
    ).values('college_name', 'student_count')
    return JsonResponse(list(data), safe=False)

def program_distribution(request):
    data = Program.objects.annotate(
        student_count=Count('student')
    ).values('prog_name', 'student_count', 'college__college_name')
    return JsonResponse(list(data), safe=False)

def org_membership(request):
    data = Organization.objects.annotate(
        member_count=Count('orgmember')
    ).values('name', 'member_count')
    return JsonResponse(list(data), safe=False)

def enrollment_trend(request):
    data = Student.objects.annotate(
        month=ExtractMonth('created_at'),
        year=ExtractYear('created_at')
    ).values('month', 'year').annotate(
        count=Count('id')
    ).order_by('year', 'month')
    return JsonResponse(list(data), safe=False)

def college_orgs(request):
    data = College.objects.annotate(
        org_count=Count('organization')
    ).values('college_name', 'org_count')
    return JsonResponse(list(data), safe=False)