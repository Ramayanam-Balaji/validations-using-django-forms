from django import forms
def check_for_a(value):
    if value[0].lower()=='s':
        raise forms.ValidationError('not valid')
def check_for_b(value):
    if len(value)==10:
        raise forms.ValidationError('not valid')
        

class StudentForm(forms.Form):
    sname=forms.CharField(max_length=100,validators=[check_for_a,check_for_b])
    sid=forms.IntegerField()
    sage=forms.IntegerField()
    semail=forms.EmailField(validators=[check_for_a,check_for_b])