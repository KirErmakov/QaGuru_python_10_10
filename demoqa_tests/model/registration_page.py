from selene import browser, command, have, be
from selene.support.shared.jquery_style import s
from selenium.webdriver import Keys
from demoqa_tests import resource


class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).should(
            have.size_greater_than_or_equal(3)
        ).perform(command.js.remove)

    def fill_first_name(self, value):
        s('#firstName').should(be.blank).type(value)
        return self

    def fill_last_name(self, value):
        s('#lastName').should(be.blank).type(value)
        return self

    def fill_date_of_birth(self, value):
        s('#dateOfBirthInput').send_keys(Keys.CONTROL, 'a').type('31 December 1991').press_enter()
        return self

    def fill_email(self, value):
        s('#userEmail').should(be.blank).type(value)
        return self

    def select_gender(self, value):
        browser.all('[for^=gender-radio]').element_by(have.exact_text(value)).click()
        return self

    def fill_mobile_number(self, value):
        s('#userNumber').type(value)
        return self

    def fill_subject(self, value):
        s('#subjectsInput').type(value).press_enter()
        return self

    def select_hobby(self, value):
        browser.all('[for^=hobbies-checkbox]').element_by(have.exact_text(value)).click()
        return self

    def upload_picture(self, value):
        s('#uploadPicture').set_value(resource.path(value))
        return self

    def fill_current_address(self, data):
        s('#currentAddress').should(be.blank).perform((command.js.set_value(data)))
        return self

    def select_state(self, value):
        s('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(value)).click()
        return self

    def select_city(self, value):
        s('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(value)).click()
        return self

    def submit(self):
        s('#submit').perform(command.js.click)

    def should_register_user_with(self, full_name, email, gender, number, date_of_birth, subjects, hobbies, photo,
                                  current_address, state_city):
        browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))
        browser.element('.table').all('td').even.should(
            have.texts(
                full_name,
                email,
                gender,
                number,
                date_of_birth,
                subjects,
                hobbies,
                photo,
                current_address,
                state_city
            )
        )
