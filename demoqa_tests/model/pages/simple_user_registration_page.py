from selene import browser, command, have, be
from selene.support.shared.jquery_style import s
from demoqa_tests.data.users import SimpleUser


class SimpleUserRegistrationPage:
    def __init__(self):
        self.full_name = s('#userName')
        self.email = s('#userEmail')
        self.current_address = s('#currentAddress')
        self.permanent_address = s('#permanentAddress')
        self.submit_button = s('#submit')

    @staticmethod
    def open():
        browser.open('/text-box')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).should(
            have.size_greater_than_or_equal(3))
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    def fill_full_name(self, user: SimpleUser):
        self.full_name.should(be.blank).type(user.full_name)
        return self

    def fill_email(self, user: SimpleUser):
        self.email.should(be.blank).type(user.email)
        return self

    def fill_current_address(self, user: SimpleUser):
        self.current_address.should(be.blank).type(user.current_address)
        return self

    def fill_permanent_address(self, user: SimpleUser):
        self.permanent_address.should(be.blank).type(user.permanent_address)
        return self

    def submit(self):
        self.submit_button.click()

    def simple_user_registration(self, user: SimpleUser):
        self.fill_full_name(user) \
            .fill_email(user) \
            .fill_current_address(user) \
            .fill_permanent_address(user) \
            .submit()
