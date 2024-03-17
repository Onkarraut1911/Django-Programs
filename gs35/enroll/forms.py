from django import forms


class StudentRegistration(forms.Form):
    name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    text = forms.CharField(widget=forms.Textarea())

    class1 = forms.CharField(
        widget=forms.TextInput(attrs={"class": "somecss1", "id": "uniqueid"})
    )  # this is make a class in html of name somecss1 you can set css using this class '.somecss' , you can set also id

    cookie = forms.CharField(widget=forms.HiddenInput())
    check = forms.CharField(widget=forms.CheckboxInput())
    file = forms.FileField()
    # file1 = forms.CharField(widget=forms.FileField())
