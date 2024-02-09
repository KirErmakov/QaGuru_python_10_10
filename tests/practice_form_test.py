from demoqa_tests.model.pages.registration_page import *


def test_fill_form_automation_flow():
    registration_page = RegistrationPage()
    registration_page.open()
    # WHEN
    (
        registration_page
        .fill_first_name('Kuraj')
        .fill_last_name('Bombei')
        .fill_email('kjb@gmail.com')
        .select_gender('Male')
        .fill_mobile_number('9876543210')
        .fill_date_of_birth('31 December 1991')
        .fill_subject('Computer Science')
        .select_hobby('Sports')
        .upload_picture('Rajesh.jpg')
        .fill_current_address('Somewhere in India')
        .select_state('NCR')
        .select_city('Delhi')
        .submit()
    )

    # THEN
    registration_page.should_register_user_with('Kuraj Bombei',
                                                'kjb@gmail.com',
                                                'Male',
                                                '9876543210',
                                                '31 December,1991',
                                                'Computer Science',
                                                'Sports',
                                                'Rajesh.jpg',
                                                'Somewhere in India',
                                                'NCR Delhi'
                                                )
