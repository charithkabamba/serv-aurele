from os import name
from django.db import models

# Create your models here.

class Messages(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    subject = models.TextField()
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date']

class Subscribers(models.Model):
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.email
    class Meta:
        ordering = ['-date']
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'
        ordering = ['-date']

class Newsletter(models.Model):
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.email
    class Meta:
        ordering = ['-date']
        verbose_name = 'Newsletter'
        verbose_name_plural = 'Newsletters'
        ordering = ['-date']

class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio_images/')
    tech_stack = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_created']

class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='skill_images/')
    proficiency = models.IntegerField()  # Assuming proficiency is represented as an integer percentage
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date_created']

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='service_images/')  # Assuming image is represented by a file path or similar
    icon = models.CharField(max_length=100)  # Assuming icon is represented by a class name or similar
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date_created']

class ProjectCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date_created']

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/')  # Assuming image is represented by a file path or similar
    category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    module = models.CharField(max_length=100, default='General', blank=True, null=True)
    module1 = models.CharField(max_length=100, default='General', blank=True, null=True)
    module2 = models.CharField(max_length=100, default='General', blank=True, null=True)

    def __str__(self):
        return self.name
    

class Teams(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    skills = models.TextField()
    image = models.ImageField(upload_to='team_images/')  # Assuming image is represented by a file path or similar
    date_created = models.DateTimeField(auto_now_add=True)
    team_module = models.CharField(max_length=100, default='General', blank=True, null=True)
    team_module1 = models.CharField(max_length=100, default='General', blank=True, null=True)
    team_module2 = models.CharField(max_length=100, default='General', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date_created']