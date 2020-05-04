from django import forms
# 

class SubmitForm(forms.Form):
	  query=forms.CharField(max_length=200)
