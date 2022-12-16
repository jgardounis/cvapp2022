from django.db import models
from django.utils import timezone

class Degree(models.Model):
	'''
	Πτυχείο
	'''
	title = models.CharField('Τίτλος Πτυχείου(*)',max_length=500)
	created   =  models.DateTimeField(default=timezone.now,verbose_name='Ημερ. Δημιουργίας')
	modified  =  models.DateTimeField(auto_now=True)
	del_f = models.BooleanField("Διαγραμμένο", default=False)

	class Meta:
		verbose_name = 'Πτυχείο'
		app_label = 'cvapp2022byte'
		verbose_name_plural = 'Πτυχεία'



	def save(self, *args, **kwargs):
		''' On save, update timestamps '''
		if not self.id:
			self.created = timezone.now()
		self.modified = timezone.now()
		return super(Degree, self).save(*args, **kwargs)
	def get_absolute_url(self):
		from django.urls import reverse_lazy
		return reverse_lazy('cvapp2022byte:data-update', kwargs={'is_list':0,'myapp':'cvapp2022byte','table':'Degree','form':'DegreeForm','pk':self.pk})
	
	def __str__(self):
		return self.title



class Person(models.Model):
	'''
	Άτομο
	'''
	LastName		=  models.CharField('Επώνυμο',max_length=200)
	FirstName		=  models.CharField('Όνομα',max_length=200)
	email			=  models.EmailField('E-mail',max_length=200,unique=True)
	Mobile			=  models.CharField('Κινητό',max_length=100,null=True,blank=True)
	Degree			=  models.ForeignKey(Degree, verbose_name='Πτυχείο',null=True,blank=True, on_delete=models.CASCADE)
	file 			=  models.FileField('Βιογραφικό',max_length=255)
	dateCreated   =  models.DateTimeField(auto_now_add=True,verbose_name='Ημερ. Δημιουργίας')
	modified  =  models.DateTimeField(auto_now=True)
	class Meta:
		app_label = 'cvapp2022byte'
		verbose_name = 'Βιογραφικό'
		verbose_name_plural = 'Βιογραφικά'		
