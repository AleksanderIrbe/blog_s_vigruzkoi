from django.db import models

# Create your models here.
class Post(models.Model):
	CATEGORIES = [
		('rockets', 'ракеты'),
		('science', 'наука'), 
	]
	slug =models.SlugField(unique=True)
	google_doc_id = models.CharField('id гугл документа', max_length=100, null=True, blank=True, db_index=True)
	category = models.CharField('категория', max_length=20, choices=CATEGORIES, db_index=True)

	title = models.CharField('заголовок', max_length=100)
	teaser_text = models.TextField('тизер', blank=True)
	teaser_image = models.ImageField('картинка тизера', null=True, blank=True)

	html = models.TextField('текст', blank=True, help_text='HTML')
	source_title = models.CharField('первоисточник', blank=True, max_length=100 )
	source_link = models.URLField('ссылка на первоисточник', blank=True )
	published = models.DateField('опубликовано', null=True, blank=True,
		help_text='оставьте пустым, чтобы скрыть из выдачи. Можно поставить будущее время')

	def __str__(self):
		return self.slug
		