from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Companyinfo(models.Model):
    OPTIONS = (
        ("PHUKET", "ภูเก็ต"),
        ("PANGNGA", "พังงา"),
        ("KRABI", "กระบี่"),
        ("RANONG", "ระนอง"),
        ("TRANG", "ตรัง"),
        ("CHUMPORN", "ชุมพร"),
        ("SURAT", "สุราษฎร์ธานี"),
        ("SATUN", "สตูล"),
    )
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True
    )
    logo = models.ImageField(upload_to="images/", blank=True)
    company_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    province = models.CharField(choices=OPTIONS, default="PHUKET", max_length=50)
    phone_number = models.CharField(max_length=12)

    def __str__(self):
        return self.company_name


class JobDetail(models.Model):
    department = (
        ("FRONTOFFICE", "Front Office"),
        ("FOOD_AND_BEVERAGE_SERVICE", "Food and Beverage-Service"),
        ("FOOD_AND_BEVERAGE_KITCHEN", "Food and Beverage-Kitchen"),
        ("HOUSEKEEPING", "Housekeeping"),
        ("SECURITY", "Security"),
        ("ENGINEER", "Engineer"),
        ("LANDSCAPE", "Landscape"),
        ("HUMAN_RESOURCE", "Human Resource"),
        ("SALES_AND_MARKETING", "Sales and Marketing"),
        ("FINANCE", "Finance"),
    )
    maximum_age = (
        ("30", "30"),
        ("40", "40"),
        ("50", "50"),
        ("60", "60"),
        ("NOT SPECIFIC", "not specific"),
    )
    
    jobtitle = models.CharField(max_length=100)
    department = models.CharField(
        choices=department, default="FRONTOFFICE", max_length=50
    )
    maximum_age = models.CharField(choices=maximum_age, default="50", max_length=50)
    
