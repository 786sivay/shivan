from django.db import models

# Create your models here.
class  blog(models.Model):
	title=models.CharField(max_length=200)
	pub_date=models.DateTimeField()
	body = models.TextField()
	image= models.ImageField(upload_to='images1/')

	def summary(self):
		return self.body[:100]

	def pub(self):
		return self.pub_date.strftime('%b %e %Y')

	def __str__(self):
		return self.title
