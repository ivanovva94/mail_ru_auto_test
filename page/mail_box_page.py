from page.base_page import BasePage
from utils.locators import *


class MailBoxPage(BasePage):
    def __init__(self, browser):
        self.locator = MailBoxLocators
        super().__init__(browser)

    def click_write_message(self):
        self.find_element(*self.locator.WRITE_MESSAGE_BUTTON).click()

    def check_message_form(self):
        self.wait_element(*self.locator.MESSAGE_FORM)
        assert self.is_element_present(*self.locator.MESSAGE_FORM), "Форма для создания письма не найдена"

    def enter_message_data(self, to_whom, subject, text):
        self.find_element(*self.locator.TO_WHOM_FIELD).send_keys(to_whom)
        self.find_element(*self.locator.SUBJECT_FIELD).send_keys(subject)
        self.find_element(*self.locator.MESSAGE_BODY).send_keys(text)

    def click_save_message(self):
        self.find_element(*self.locator.MESSAGE_SAVE_BUTTON).click()

    def check_save_message(self):
        self.wait_element(*self.locator.MESSAGE_SAVE_NOTIFICATION)
        assert self.is_element_present(*self.locator.MESSAGE_SAVE_NOTIFICATION), "Не появилось уведомление" \
                                                                                 " о сохранении письма в черновик"

    def click_send_message(self):
        self.find_element(*self.locator.MESSAGE_SEND_BUTTON).click()

    def check_send_message(self):
        check_text = self.wait_element(*self.locator.MESSAGE_SEND_NOTIFICATION).text
        assert check_text == "Письмо отправлено", "Не появилось уведомление об отправке письма"

    def close_message_form(self):
        self.find_element(*self.locator.CLOSE_WRITE_MESSAGE_BUTTON).click()

    def open_drafts(self):
        self.wait_element(*self.locator.DRAFTS_BUTTON).click()

    def open_last_saved_draft(self):
        self.wait_element(*self.locator.LAST_SAVED_DRAFT).click()
        self.wait_element(*self.locator.MESSAGE_FORM)

    def check_data_draft(self, to_whom, subject, text):
        mail_data = self.find_element(*self.locator.TO_WHOM_MAIL_CHECK_DRAFT).text
        subject_data = self.find_element(*self.locator.SUBJECT_FIELD).get_attribute("value")
        text_data = self.find_element(*self.locator.MESSAGE_BODY_CHECK_DRAFT).text

        assert mail_data == to_whom, "Получатель в черновике не совпадает с заполненным в шаге 3"
        assert subject_data == subject, "Тема в черновике не совпадает с заполненным в шаге 3"
        assert text_data == text, "Тело письма в черновике не совпадает с заполненным в шаге 3"

    def click_close_message_send_notification(self):
        self.wait_element(*self.locator.MESSAGE_SEND_NOTIFICATION).click()

    def open_sent(self):
        self.wait_element(*self.locator.SENT_BUTTON).click()

    def open_last_send_message(self):
        self.wait_element(*self.locator.LAST_SEND_MESSAGE).click()

    def check_data_send_message(self, to_whom, subject, text):
        mail_data = self.wait_element(*self.locator.TO_WHOM_MAIL_CHECK_SENT).get_attribute("title")
        subject_data = self.find_element(*self.locator.SUBJECT_CHECK_SENT).text
        text_data = self.find_element(*self.locator.MESSAGE_BODY_CHECK_SENT).text

        assert to_whom == mail_data, "Получатель в отправленном письме не совпадает с заполненным в шаге 3"
        assert subject in subject_data, "Тема в отправленном письме не совпадает с заполненным в шаге 3"
        assert text == text_data, "Текст в отправленном письме не совпадает с заполненным в шаге 3"
