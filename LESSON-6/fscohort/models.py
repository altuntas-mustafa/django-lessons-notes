from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.IntegerField(blank=True, null=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Student isimli modelin adnı admin panelinde Öğrenciler olarak değiştirdik
#     class Meta:
#         verbose_name_plural = "Öğrencler" 