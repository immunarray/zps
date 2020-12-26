from django.db import models, AutoField


class Customer(models.Model):
    customer_status = models.BinaryField
    customer_name = models.CharField(max_length=500, help_text="Customer Name")
    customer_create_date = models.DateField()
    customer_last_modified_date = models.DateField()
    customer_address = models.CharField(max_length=500, help_text="Customer Address")
    customer_created_by = models.CharField(max_length=200, help_text="Created By")
    customer_updated_by = models.DateField()

# Create your models here.:q!:
