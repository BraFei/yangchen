from django.db import models


class Blog(models.Model):
    concentration = models.FloatField(max_length=30)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.concentration)

    class Meta:
        ordering = ['-created_time']
        db_table = 'dust_monitor'
