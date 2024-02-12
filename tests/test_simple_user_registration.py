from demoqa_tests.application import app
from demoqa_tests.data import users


def test_simple_user_registration():
    app.left_panel.open_simple_registration_form()

    app.simple_user_registration_form.simple_user_registration(users.person)

    app.profile_info_board.should_have_user_info(users.person)
