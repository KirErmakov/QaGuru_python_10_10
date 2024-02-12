from demoqa_tests.components.left_panel import LeftPanel
from demoqa_tests.components.profile_info_board import ProfileInfoBoard
from demoqa_tests.model.pages.simple_user_registration_page import SimpleUserRegistrationPage


class ApplicationManager:
    def __init__(self):
        self.simple_user_registration_form = SimpleUserRegistrationPage()
        self.left_panel = LeftPanel()
        self.profile_info_board = ProfileInfoBoard()


app = ApplicationManager()
