from django.db import models
from django.utils import timezone

class Habits(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField("date pub")
    strike_count = models.IntegerField(default=0)
    last_checked = models.DateField(default=timezone.now)  # дата останнього відмічення
    is_checked_today = models.BooleanField(default=False)  # чи була звичка виконана сьогодні
