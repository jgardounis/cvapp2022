# Import form modules
from django import forms
from .models import *
# Create class to define the form fields
class DegreeForm(forms.ModelForm):
	title = forms.CharField(label="Τίτλος", max_length=200)	


class PersonForm(forms.ModelForm):    
	LastName = forms.CharField(label="Επώνυμο", max_length=200)
	FirstName = forms.CharField(label="Όνομα", max_length=200)
	email = forms.EmailField(max_length = 200)
	Mobile = forms.CharField(label="Κινητό", max_length=10,required=False)
	Degree = forms.ModelChoiceField(queryset=Degree.objects.all(), empty_label="---",label='Πτυχείο',required=False)
	file = forms.FileField(label='Βιογραφικό',required=False)


	def __init__(self, *args, **kwargs):
		self.app = 'cvapp2022byte'
		super(PersonForm, self).__init__(*args, **kwargs)

	class Meta:
		model = Person
		exclude = ('dateCreated',)  


class DegreeForm(forms.ModelForm):    
	title = forms.CharField(label="Τίτλος", max_length=200)

	def __init__(self, *args, **kwargs):
		self.app = 'cvapp2022byte'
		super(DegreeForm, self).__init__(*args, **kwargs)

	class Meta:
		model = Degree
		exclude = ('created','modified','del_f',) 		