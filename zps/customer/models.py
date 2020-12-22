from django.db import models, AutoField


class Customer(models.Model):
    customer_status = models.BinaryField
    customer_name = models.CharField(max_length=500, help_text="Customer Name")
    customer_create_date = models.DateField()
    customer_last_modified_date = models.DateField()
    customer_address
    customer_created_by
    customer_updated_by_

# Create your models here.:q!:
