from django import forms

class ContactCourse(forms.Form):
	"""docstring for ContactCourse"""
	name = forms.CharField(label='Nome',max_length='100')
	email = forms.EmailField(label='Email')
	message = forms.CharField(label='Mensagem/Duvida',widget=forms.Textarea)
	 

