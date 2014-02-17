from django import forms

class Add_volunteer(forms.Form):
	name = forms.CharField(max_length=200)
	email = forms.EmailField(max_length=200)
	phone = forms.CharField(max_length=30)


class Add_project(forms.Form):
	name = forms.CharField(max_length=200)
