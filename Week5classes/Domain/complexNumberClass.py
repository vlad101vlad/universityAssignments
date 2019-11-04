class ComplexNumber:
    def __init__(self, real_part=0, imaginary_part=0):
        self._real_part = int(real_part)
        self._imaginary_part = int(imaginary_part)

    @property
    def real_part(self):
        return self._real_part

    @property
    def imaginary_part(self):
        return self._imaginary_part

    def set_real_part(self, new_real_part):
        self._real_part = new_real_part

    def set_imaginary_part(self, new_imaginary_part):
        self._imaginary_part = new_imaginary_part

    @property
    def print_form(self):
        string_to_be_printed = ""
        imaginary_part = self._imaginary_part
        real_part = self._real_part

        if real_part:
            string_to_be_printed = string_to_be_printed + str(real_part)

        if imaginary_part:
            if imaginary_part > 0:
                if real_part:
                    string_to_be_printed = string_to_be_printed + "+" + str(imaginary_part) + "i"
                else:
                    string_to_be_printed = string_to_be_printed + str(imaginary_part) + "i"
            else:
                string_to_be_printed = string_to_be_printed + str(imaginary_part) + "i"

        return string_to_be_printed
