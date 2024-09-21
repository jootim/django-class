from django.shortcuts import redirect, render

from .form import CompanyInfo


# Create your views here.
def companyinfoadd(request):
    form = CompanyInfo()
    if request.method == "POST":
        form = CompanyInfo(request.POST)
        if form.is_valid():
            start_save = form.save()
            start_save.created_by = request.user
            start_save.save()
            return redirect("home")

    context = {"form": form}
    return render(request, "base/company_info_form.html", context)
