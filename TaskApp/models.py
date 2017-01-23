from django.db import models

# Create your models here.
class Task(models.Model):
    task_name = models.CharField(max_length=20) #oopss :)  #we can extend length :)
    task_desc = models.TextField(max_length=200)
    completed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='Images/',default='Images/None/No-img.jpg')
    doc = models.FileField(upload_to='Doc/',default='Doc/None/No-doc.pdf')

    def __str__(self):
        return  "%s" % self.task_name
    
class User(models.Model):
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	email = models.CharField(max_length=20)
	username = models.CharField(max_length=20) 
	password = models.CharField(max_length=20)

	def __str__(self):
		return "%s" % self.username
