from django.db import models

# Create your models here.

class Reporter(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	# full_name = models.CharField(max_length=200, default=first_name + last_name)
	def __str__(self):
		return self.first_name + ' ' + self.last_name

class Article(models.Model):
	pub_date = models.DateField()
	heading = models.CharField(max_length=100)
	content = models.TextField()
	reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

	def __str__(self):
		return self.heading