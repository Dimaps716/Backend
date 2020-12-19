# Django
from django.db import models

# creation of the database model its fields and parameters
class studen(models.Model):
    photo = models.URLField(max_length=500)
    name = models.CharField(max_length=80)
    career = models.CharField(max_length=80)
    status = models.CharField(max_length=300)
    exp = models.IntegerField()
    lv = models.IntegerField()



# Return name
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'studen'
        verbose_name_plural = 'students'
        ordering = ['id']

class technologi(models.Model):
    studen_id = models.ForeignKey(studen, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    badge = models.URLField()


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'technologie'
        verbose_name_plural = 'technologies'
        ordering = ['id']


class project(models.Model):
    studen_id = models.ForeignKey(studen, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=400)
    repository = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'project'
        verbose_name_plural = 'projects'
        ordering = ['id']



class courses(models.Model):
    name = models.CharField(max_length=300)
    ur_local = models.URLField(max_length=500)
    time = models.IntegerField()
    week = models.CharField(max_length=80)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'
        ordering = ['id']

class milestone(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=600)


    def __str__(self):
        return self.milestone

    class Meta:
        verbose_name = 'name'
        verbose_name_plural = 'names'
        ordering = ['id']
