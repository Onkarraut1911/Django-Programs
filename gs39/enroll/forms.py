from django import forms


class StudentRegistration(forms.Form):
    name = forms.CharField(
        min_length=5, max_length=10, strip=False
    )  # This arguments are validetors , strip value default is True
    # strip validator is set True then it used to if you put input with lots of space in starting and ending then it removed spacese

    last_name = forms.CharField(
        empty_value="sonam"
    )  # This field is requierd so you didnt write anything in field then it gives error , empty_value used to set default value in field so we cant get error this value pass in the field

    middle_name = forms.CharField(
        error_messages={"required": "Enter your middle name"}
    )  # if you want to change the error message then use this validator error_message , if requied error is occure then this message show

    Roll = forms.IntegerField(min_value=1, max_value=10, required=False)
    price = forms.DecimalField(
        min_value=1,
        max_value=10,
        max_digits=3,
        decimal_places=1,  # decimal_palces argument is insure only one digit after decimal point
    )  # decimal(flot value) , max_digits ensure the how many digit user put in the field including digits before and after the decimal point maximun 3

    rate = forms.FloatField(min_value=1, max_value=10)
    # defference between DecimalField and FloatField is you entered 5 then decimal print 5 and float field print 5.0

    comment = forms.SlugField()
    email = forms.EmailField(min_length=5, max_length=50)
    website = forms.URLField(min_length=5, max_length=50)
    password = forms.CharField(
        min_length=5, max_length=50, widget=forms.PasswordInput()
    )
    discription = forms.CharField(widget=forms.Textarea())
    feedback = forms.CharField(
        min_length=5,
        max_length=50,
        widget=forms.TextInput(attrs={"class": "somecss1 somecss2", "id": "uniqueid"}),
    )
    notes = forms.CharField(
        min_length=5,
        max_length=50,
        widget=forms.Textarea(
            attrs={"rows": 3, "cols": 50}
        ),  # this rows and cols used to  area of text  this 3 rows and 50 columns like that table but not borders
    )

    agree = forms.BooleanField(label="I Agree")
