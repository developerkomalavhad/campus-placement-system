from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from users.decorators import role_required

from .forms import JobApplicationForm
from .models import JobApplication


@login_required
def application_list(request):
    applications = JobApplication.objects.select_related("student", "job").all()
    return render(
        request, "applications/application_list.html", {"applications": applications}
    )


@login_required
@role_required(["ADMIN", "STUDENT"])
def application_create(request):
    form = JobApplicationForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Application submitted.")
        return redirect("application_list")
    return render(
        request,
        "applications/application_form.html",
        {"form": form, "title": "Apply for Job"},
    )


@login_required
@role_required(["ADMIN", "STUDENT"])
def application_update(request, pk):
    application = get_object_or_404(JobApplication, pk=pk)
    form = JobApplicationForm(request.POST or None, instance=application)
    if form.is_valid():
        form.save()
        messages.success(request, "Application updated.")
        return redirect("application_list")
    return render(
        request,
        "applications/application_form.html",
        {"form": form, "title": "Edit Application"},
    )


@login_required
@role_required(["ADMIN", "STUDENT"])
def application_delete(request, pk):
    application = get_object_or_404(JobApplication, pk=pk)
    if request.method == "POST":
        application.delete()
        messages.success(request, "Application removed.")
        return redirect("application_list")
    return render(
        request, "applications/application_confirm_delete.html", {"application": application}
    )
