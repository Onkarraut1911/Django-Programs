class FourDigitYearConverter:
    regex = "[0-9]{4}"  # this is build in attribute regex it get any number between 0 to 9 of exactly 4 digit

    def to_python(self, value):
        return int(value)  # this is type conversion (casting)

    def to_url(self, value):
        return f"{value:4d}"
        # return "%4d" % value  # this is same as upper line
