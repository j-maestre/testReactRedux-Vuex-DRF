from django.core.exceptions import ValidationError


def validate_rg_length(value):
    if len(value) < 6 or len(value) > 10:
        raise ValidationError(u'%s is not a valid RG.' % value)
    return True


def validate_cpf_length(value):
    if len(value) != 11:
        raise ValidationError(u'%s is not a valid CPF.' % value)
    return True


def validate_cpf(value):
    if value == "11111111111" or \
            value == "22222222222" or \
            value == "33333333333" or \
            value == "44444444444" or \
            value == "55555555555" or \
            value == "66666666666" or \
            value == "77777777777" or \
            value == "88888888888" or \
            value == "99999999999" or \
            value == "00000000000" or\
            not value.isdigit():
        raise ValidationError(u'%s is not a valid CPF' % value)
    numbers = value[:9]
    digits = value[9:11]
    first_digit = get_first_digit(numbers)
    numbers = numbers + str(first_digit)
    second_digit = get_second_digit(numbers)
    verified_digits = str(first_digit) + str(second_digit)
    if verified_digits != digits:
        raise ValidationError(u'%s is not a valid CPF.' % value)
    return True


def get_first_digit(numbers):
    i = 10
    cpfsum = 0
    for x in numbers:
        cpfsum += int(x) * i
        i -= 1
    remainder = (cpfsum * 10) % 11
    if remainder == 10:
        remainder = 0
    return remainder


def get_second_digit(numbers):
    cpfsum = 0
    i = 11
    for x in numbers:
        cpfsum += int(x) * i
        i -= 1
    remainder = (cpfsum * 10) % 11
    if remainder == 10:
        remainder = 0
    return remainder
