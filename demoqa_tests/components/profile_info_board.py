from selene import browser, have
from demoqa_tests.data.users import SimpleUser


class ProfileInfoBoard:
    def should_have_user_info(self, user: SimpleUser):
        browser.element('.border').all('p').should(have.exact_texts(
                f'Name:{user.full_name}',
                f'Email:{user.email}',
                f'Current Address :{user.current_address}',
                f'Permananet Address :{user.permanent_address}',
            )
        )
