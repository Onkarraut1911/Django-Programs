from django import forms


class StudentRegistration(forms.Form):
    name = forms.CharField(
        label="your name", initial="meghana"
    )  # label argument change the label name of the field

    user_name = forms.CharField(
        label_suffix="-"
    )  # label_suffix argument change the label tag ex. Name-  , also it need to write label_tag in template

    last_name = forms.CharField(
        initial="sonam"
    )  # initial argument put the text in field initialy

    middle_name = forms.CharField(
        required=False
    )  # this argument used to field is required or not required to fill

    abc_name = forms.CharField(
        disabled=True
    )  # disabled argument disabled field means cant write in the filed

    user_work = forms.CharField(
        help_text="limit 30 character"
    )  # help_text argument is used to displayed message for the field
