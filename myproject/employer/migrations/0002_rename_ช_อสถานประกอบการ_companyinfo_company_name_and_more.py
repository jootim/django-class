# Generated by Django 5.0.7 on 2024-08-19 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companyinfo',
            old_name='ชื่อสถานประกอบการ',
            new_name='company_name',
        ),
        migrations.RenameField(
            model_name='companyinfo',
            old_name='ที่ตั้ง',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='companyinfo',
            old_name='โลโก้',
            new_name='logo',
        ),
        migrations.RenameField(
            model_name='companyinfo',
            old_name='เบอร์ติดต่อ',
            new_name='phone_number',
        ),
        migrations.RenameField(
            model_name='companyinfo',
            old_name='จังหวัด',
            new_name='province',
        ),
    ]
