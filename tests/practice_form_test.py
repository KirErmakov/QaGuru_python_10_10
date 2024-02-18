from tests import users
from tests.registration_page import RegistrationPage


def test_user_registration_form_high_level():
    student = users.student
    registration_page = RegistrationPage()
    registration_page.open()

    registration_page.user_registration(student)

    registration_page.should_register_user_with(student)