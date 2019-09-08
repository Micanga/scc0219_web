from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.

class Author(models.Model):
	# fields
	user = models.ForeignKey(
		get_user_model(),
		on_delete=models.CASCADE,
		primary_key = True,
	)
	bio = models.CharField(max_length = 300, help_text='Escreva uma descricao para voce!')

	class Meta: 
		ordering = ['-user']

	# methods
	def __str__(self):
		return self.user.username

	def get_absolute_url(self):
		"""Returns the url to access a detail record for this book."""
		return reverse('blogger-detail', args=[str(self.user.id)])

class Blog(models.Model):
	# fields
	title = models.CharField(max_length=50, help_text='Escreva o assunto que deseja postar.')
	content = models.CharField(max_length=1000, help_text='No que você esta pensando?')
	author = models.ForeignKey(
		'Author',
		on_delete=models.SET('Usuario Desvinculado'),
	)
	date = models.DateTimeField(auto_now_add=True)

	class Meta: 
		ordering = ['-date']

	# methods
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		"""Returns the url to access a detail record for this book."""
		return reverse('blog-detail', args=[str(self.id)])

class Comment(models.Model):
	# fields
	message = models.CharField(max_length=300, help_text='Deixe um comentario.')
	commenter = models.ForeignKey(
		get_user_model(),
		on_delete=models.SET('Usuario Desvinculado'),
		)
	blog = models.ForeignKey(
		'Blog',
		on_delete=models.CASCADE,
	)
	date = models.DateTimeField(auto_now_add=True)

	class Meta: 
		ordering = ['-date']

	# methods
	def __str__(self):
		return self.message