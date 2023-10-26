from django.db import models

# Create your models here.
class Payment_info(models.Model):
    s_no=models.AutoField(primary_key=True)
    card_no=models.CharField(max_length=16)
    exp_date=models.CharField(max_length=5)
    cvv=models.CharField(max_length=3)
    name=models.CharField(max_length=255)
    time_stamp=models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.card_no
    



