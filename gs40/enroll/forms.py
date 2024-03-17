from django import forms


class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

    def clean_name(
        self,
    ):  # which field you have validation that field name gives after clean_....... , here i want validatio in name field

        valname = self.cleaned_data[
            "name"
        ]  # submited form data accessing using cleaned_data  and it get data in the dictionary form , here i write name key so it gives me name value means user typed in the feiled of name and store in valname variable

        if len(valname) < 4:
            raise forms.ValidationError("Enter more than or equal 4 characters ")

        return valname
