from selene import browser, command, have, be
from selene.support.shared.jquery_style import s
from selenium.webdriver import Keys
from tests.resources import resource
from tests.users import User


class RegistrationPage:
    def __init__(self):
        self.first_name = s('#firstName')
        self.last_name = s('#lastName')
        self.date_of_birth = s('#dateOfBirthInput')
        self.email = s('#userEmail')
        self.gender = browser.all('[for^=gender-radio]')
        self.mobile = s('#userNumber')
        self.subject = s('#subjectsInput')
        self.hobby = browser.all('[for^=hobbies-checkbox]')
        self.picture = s('#uploadPicture')
        self.current_address = s('#currentAddress')
        self.state_dropdown = browser.all('[id^=react-select][id*=option]')
        self.city_dropdown = browser.all('[id^=react-select][id*=option]')
        self.submit_button = s('#submit')

    def open(self):
        browser.open('/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).should(
            have.size_greater_than_or_equal(3))
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
        browser.element('[aria-label="Consent"]').click()

    def fill_first_name(self, user: User):
        self.first_name.should(be.blank).type(user.first_name)
        return self

    def fill_last_name(self, user: User):
        self.last_name.should(be.blank).type(user.last_name)
        return self

    def fill_date_of_birth(self, user: User):
        self.date_of_birth.send_keys(Keys.CONTROL, 'a').type(user.date_of_birth).press_enter()
        return self

    def fill_email(self, user: User):
        self.email.should(be.blank).type(user.email)
        return self

    def select_gender(self, user: User):
        self.gender.element_by(have.exact_text(user.gender.value)).click()
        return self

    def fill_mobile_number(self, user: User):
        self.mobile.type(user.mobile_num)
        return self

    def fill_subject(self, user: User):
        self.subject.type(user.subjects).press_enter()
        return self

    def select_hobby(self, user: User):
        self.hobby.element_by(have.exact_text(user.hobbies.value)).click()
        return self

    def upload_picture(self, user: User):
        self.picture.set_value(resource.path(user.photo))
        return self

    def fill_current_address(self, user: User):
        self.current_address.should(be.blank).perform((command.js.set_value(user.current_address)))
        return self

    def select_state(self, user: User):
        s('#state').click()
        self.state_dropdown.element_by(have.exact_text(user.state)).click()
        return self

    def select_city(self, user: User):
        s('#city').click()
        self.city_dropdown.element_by(have.exact_text(user.city)).click()
        return self

    def submit(self):
        self.submit_button.perform(command.js.click)

    def user_registration(self, user: User):
        self.fill_first_name(user) \
            .fill_last_name(user) \
            .fill_email(user) \
            .select_gender(user) \
            .fill_mobile_number(user) \
            .fill_date_of_birth(user) \
            .fill_subject(user) \
            .select_hobby(user) \
            .upload_picture(user) \
            .fill_current_address(user) \
            .select_state(user) \
            .select_city(user) \
            .submit()



    def should_register_user_with(self, user: User):
        browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))
        browser.element('.table').all('td').even.should(
            have.texts(
                f'{user.first_name} {user.last_name}',
                {user.email},
                {user.gender.value},
                {user.mobile_num},
                {user.date_of_birth},
                {user.subjects},
                {user.hobbies.value},
                {user.photo},
                {user.current_address},
                f'{user.state} {user.city}'
            )
        )
