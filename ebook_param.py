import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains


ebooks = (
        'data-ethics-preference-management',
        'cdp-vs-crm',
        'ai-product-recommendation-engines',
        'cookbook-of-marketing-automation-in-ecommerce',
        'definitive-guide-to-email-deliverability',
        'complete-guide-to-ma-in-ecommerce',
        'online_consumer_trends',
        'how_marketing_automation_is_transformed_by_ai_and_data_science',
        'ebook_live_chat',
        '10_success_stories_ebook'
        )


class Ebook(unittest.TestCase):

    def setUp(self):

        self.options = Options()
        self.options.add_argument("--disable-notifications")
        self.options.add_argument("start-maximized")

        self.browser = webdriver.Chrome(chrome_options=self.options)

    def tearDown(self):
        self.browser.close()


def test_generator(ebook_name):
    def testEbookDownload(self):

        self.browser.get("https://www.salesmanago.com/")

        self.browser.find_element_by_link_text('resources').click()
        self.browser.find_element_by_link_text('Ebooks').click()

        self.browser.find_element_by_xpath("//a[contains(@href,'{}')]".format(ebook_name)).click()

        window_before = self.browser.window_handles[0]
        window_form = self.browser.window_handles[1]
        self.browser.switch_to.window(window_form)
        action = ActionChains(self.browser)

        self.browser.find_element_by_name("name").click()
        self.browser.find_element_by_name("name").send_keys("Ann")
        time.sleep(3)

        email = self.browser.find_element_by_id("email")
        action.move_to_element(email).click().perform()
        email.send_keys("ann@gla.com")

        self.browser.find_element_by_name("company").click()
        self.browser.find_element_by_name("company").send_keys("GLA")

        url = self.browser.find_element_by_name("url")
        action.move_to_element(url).click().perform()
        url.send_keys("gla.com")

        phone_number = self.browser.find_element_by_id("phoneNumber")
        action.move_to_element(phone_number).click().perform()
        phone_number.send_keys("723434885")

        submit_button = self.browser.find_element_by_xpath("//button[@type='submit']")
        submit_button.submit()
        # self.assertTrue(self.browser.find_element_by_xpath("//body[contains('Submitted')]"))

    return testEbookDownload


if __name__ == '__main__':
    tested_ebook = ebooks[6]
    test_name = 'test {}'.format(tested_ebook)
    test = test_generator(tested_ebook)
    setattr(Ebook, test_name, test)
    unittest.main()
