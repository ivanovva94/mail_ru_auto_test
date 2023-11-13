from utils.test_data import TestData


class TestMailDrafts:

    def test_login_user(self, browser, login_page):
        login_page.open_url()
        login_page.click_enter_button()
        login_page.enter_email(TestData.USERNAME)
        login_page.enter_password(TestData.PASSWORD)
        login_page.click_login_button()
        login_page.check_authorized_user(TestData.USERNAME)

    def test_write_message_form(self, browser, mailbox_page):
        mailbox_page.click_write_message()
        mailbox_page.check_message_form()

    def test_save_message_in_drafts(self, browser, mailbox_page):
        mailbox_page.enter_message_data(TestData.RECIPIENT, TestData.SUBJECT, TestData.MESSAGE_BODY)
        mailbox_page.click_save_message()
        mailbox_page.check_save_message()
        mailbox_page.close_message_form()

    def test_check_data_draft(self, browser, mailbox_page):
        mailbox_page.open_drafts()
        mailbox_page.open_last_saved_draft()
        mailbox_page.check_data_draft(TestData.RECIPIENT, TestData.SUBJECT, TestData.MESSAGE_BODY)
        mailbox_page.close_message_form()

    def test_logout_user(self, browser, login_page):
        login_page.exit_from_account()
        login_page.check_exit()


class TestMailSend:

    def test_login_user(self, browser, login_page):
        login_page.open_url()
        login_page.click_enter_button()
        login_page.enter_email(TestData.USERNAME)
        login_page.enter_password(TestData.PASSWORD)
        login_page.click_login_button()
        login_page.check_authorized_user(TestData.USERNAME)

    def test_write_message_form(self, browser, mailbox_page):
        mailbox_page.click_write_message()
        mailbox_page.check_message_form()

    def test_send_message(self, browser, mailbox_page):
        mailbox_page.enter_message_data(TestData.RECIPIENT, TestData.SUBJECT, TestData.MESSAGE_BODY)
        mailbox_page.click_send_message()
        mailbox_page.check_send_message()
        mailbox_page.click_close_message_send_notification()

    def test_check_data_sent_message(self, browser, mailbox_page):
        mailbox_page.open_sent()
        mailbox_page.open_last_send_message()
        mailbox_page.check_data_send_message(TestData.RECIPIENT, TestData.SUBJECT, TestData.MESSAGE_BODY)

    def test_logout_user(self, browser, login_page):
        login_page.exit_from_account()
        login_page.check_exit()
