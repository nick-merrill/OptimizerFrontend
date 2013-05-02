from django.db import models

class Variable(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(blank=True)

    value = models.CharField(max_length=30)

class Problem(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField(blank=True)
    is_visible = models.BooleanField(default=True)
    url = models.CharField(max_length=11, help_text="MUST BE ONLY ONE WORD LONG, and please lowercase. Also, make it unique from other problems.")

    required_inputs = models.ManyToManyField(Variable)

    inputs = models.TextField(help_text="Use this field to enter the Java commandline arguments line by line.")

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

class Solution(models.Model):
    prob = models.ForeignKey(Problem)

    vars = models.ManyToManyField(Variable)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

class Algorithm(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField(blank=True)
    is_visible = models.BooleanField(default=True)
    url = models.CharField(max_length=11, help_text="MUST BE ONLY ONE WORD LONG, and please lowercase.")

    input = models.TextField(help_text="Use this field to enter the Java commandline arguments line by line. Also, make it unique from other algorithms.")

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
