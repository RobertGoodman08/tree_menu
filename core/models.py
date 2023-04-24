from django.db import models





class Menu(models.Model):
    title = models.CharField(max_length=250)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    url = models.URLField()

    def __str__(self):
        return self.title



    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'