from django.core.exceptions import ValidationError
import unittest
from users.validations import validate_cpf, validate_cpf_length, validate_rg_length


class TestValidations(unittest.TestCase):
    def test_cpf_validation(self):
        self.assertEqual(validate_cpf("87061066091"), True)#normal
        self.assertRaises(ValidationError, validate_cpf, "00000000000")
        self.assertEqual(validate_cpf("43730747800"), True)#remainder 10
        self.assertRaises(ValidationError, validate_cpf, "111")
        self.assertRaises(ValidationError, validate_cpf, "isnotdigit")

    def test_cpf_length(self):
        self.assertEqual(validate_cpf_length("87061066091"), True)
        self.assertRaises(ValidationError, validate_cpf_length, "870610660911")
        self.assertRaises(ValidationError, validate_cpf_length, "111")
        self.assertRaises(ValidationError, validate_cpf_length, "")

    def test_rg_length(self):
        self.assertEqual(validate_rg_length("1234567"), True)
        self.assertRaises(ValidationError, validate_rg_length, "12345")
        self.assertRaises(ValidationError, validate_rg_length, "12345678901")
        self.assertRaises(ValidationError, validate_rg_length, "")
