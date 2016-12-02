from django.db import models

class Release(models.Model):
	artist = models.CharField(max_length=200)
	title = models.CharField(max_length=200)
	release_date = models.DateField(auto_now=False)
	cover = models.ImageField(upload_to='releases/cover_images', default='releases/cover_images/no_img.jpg')

	def create(self):
		self.save()

	def __str__(self):
		return "{} - {}".format(self.artist, self.title)

