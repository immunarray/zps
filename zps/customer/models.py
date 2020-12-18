from django.db import models, AutoField

class Customer(models.Model):
    customer_pk = AutoField.BigAutoField() # Primany Key for Customer
    customer_name = models.CharField(max_lenght=500) # Customer Name
    create_date = models.DateTimeField('date created') # Date customer was created non editable
    customer_status = models.BooleanField() # Customer status 
    customer_credit_terms = [('COD','Cash On Delivery'),('N30','Net 30'), ('N10','Net 10')]
# Create your models here.
