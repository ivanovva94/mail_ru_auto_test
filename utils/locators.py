from selenium.webdriver.common.by import By


class LoginPageLocators:
    MAIL_ENTER_BUTTON = (By.XPATH, "//button[@class='ph-login svelte-1ke9xx5']")
    LOGIN_FIELD = (By.XPATH, "//input[@name='username']")
    LOGIN_ENTER_BUTTON = (By.XPATH, "//button[@data-test-id='next-button']")
    PASSWORD_FIELD = (By.NAME, "password")
    PASSWORD_ENTER_BUTTON = (By.XPATH, "//button[@data-test-id='submit-button']")
    ICON_USER_ACCOUNT = (By.XPATH, "//div[@class='ph-project ph-project__account svelte-1osmzf1']")
    IFRAME = (By.XPATH, "//iframe[@class='ag-popup__frame__layout__iframe']")
    EXIT_BUTTON = (By.XPATH, "//div[@data-testid='whiteline-account-exit']")


class MailBoxLocators:
    WRITE_MESSAGE_BUTTON = (By.XPATH, "//a[@title='Написать письмо']")
    MESSAGE_FORM = (By.XPATH, "//div[@class='focus-zone focus-zone_fluid']")
    TO_WHOM_FIELD = (By.XPATH, "(//input[@class='container--H9L5q size_s--3_M-_'])[1]")
    SUBJECT_FIELD = (By.XPATH, "(//input[@class='container--H9L5q size_s--3_M-_'])[2]")
    MESSAGE_BODY = (By.XPATH, "//div[@role='textbox']")
    MESSAGE_SAVE_BUTTON = (By.XPATH, "//button[@data-test-id='save']")
    MESSAGE_SEND_BUTTON = (By.XPATH, "//button[@data-test-id='send']")
    MESSAGE_SAVE_NOTIFICATION = (By.XPATH, "//span[@class='notify__message__text']")
    CLOSE_WRITE_MESSAGE_BUTTON = (By.XPATH, "//button[@title='Закрыть']")
    DRAFTS_BUTTON = (By.XPATH, "//a[@data-folder-link-id='500001']")
    LAST_SAVED_DRAFT = (By.XPATH, "(//a[contains(@href, '/drafts/')])[2]")
    TO_WHOM_MAIL_CHECK_DRAFT = (By.XPATH, "//span[@class='text--1tHKB']")
    MESSAGE_BODY_CHECK_DRAFT = (By.XPATH, "//div[@role='textbox']/div/div/div/div/div")
    MESSAGE_SEND_NOTIFICATION = (By.XPATH, "//a[@class='layer__link']")
    CLOSE_SEND_NOTIFICATION_BUTTON = (By.XPATH, "//div[@class='layer__controls']/span")
    SENT_BUTTON = (By.XPATH, "//a[@data-folder-link-id='500000']")
    LAST_SEND_MESSAGE = (By.XPATH, "(//a[contains(@href, '/sent/')])[2]")
    TO_WHOM_MAIL_CHECK_SENT = (By.XPATH, "(//span[@class='letter-contact'])[2]")
    SUBJECT_CHECK_SENT = (By.XPATH, "//h2[@class='thread-subject']")
    MESSAGE_BODY_CHECK_SENT = (By.XPATH, "//div[@class='letter-body__body-content']/div/div/div/div/div/div/div/div")
