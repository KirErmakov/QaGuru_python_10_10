from demoqa_tests.data import users
from demoqa_tests.model.pages.registration_page import RegistrationPage
import allure
from allure_commons.types import Severity


@allure.tag('DemoQa')
@allure.severity(Severity.CRITICAL)
@allure.label('Owner', 'K1rMac')
@allure.feature('User registration')
@allure.story('Register new user')
@allure.link('https://demoqa.com', name='Testing')
def test_user_registration_form_high_level():
    student = users.student
    registration_page = RegistrationPage()

    with allure.step('Open registration page'):
        registration_page.open()

    with allure.step('Register new user'):
        registration_page.user_registration(student)

    with allure.step('Check form results are correct'):
        registration_page.should_register_user_with(student)
