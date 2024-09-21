from django.forms import ModelForm

from .models import Companyinfo


class CompanyInfo(ModelForm):
    class Meta:
        model = Companyinfo
        fields = ["company_name", "location", "province", "phone_number"]
