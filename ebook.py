import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


ebooks = {
    "Data Ethics & Customer Preference Management":
        "data-ethics-preference-management",
    "The Ultimate marketer's guide to Customer Data Platforms":
        "cdp-vs-crm",
    "AI Product Recommendation Engines":
        "ai-product-recommendation-engines",
    "Cookbook of marketing automation in eCommerce":
        "cookbook-of-marketing-automation-in-ecommerce",
    "Kamasutra of eMail Marketing Deliverability":
        "definitive-guide-to-email-deliverability",
    "The Complete Guide to Marketing Automationin Ecommerce":
        "complete-guide-to-ma-in-ecommerce",
    "Online Consumer Trends 2020":
        "online_consumer_trends",
    "How Marketing Automation is transformed by AI and Data Science":
        "how_marketing_automation_is_transformed_by_ai_and_data_science",
    "How Live Chat is redefined by AI, Machine Learning, Deep Learning and Bots":
        "ebook_live_chat",
    "10 success stories of Europe's biggest brands implementing marketing automation":
        "10_success_stories_ebook"
}


class Ebook(unittest.TestCase):

    def setUp(self):

        self.options = Options()
        self.options.add_argument("--disable-notifications")
        self.options.add_argument("start-maximized")

        self.browser = webdriver.Chrome(options=self.options)

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
        self.browser.find_element_by_name("name").send_keys("Ela")

        email = self.browser.find_element_by_id("email")
        action.move_to_element(email).click().perform()
        email.send_keys("ela@salesmanago.com")

        self.browser.find_element_by_name("company").click()
        self.browser.find_element_by_name("company").send_keys("Sales Manago")

        url = self.browser.find_element_by_name("url")
        action.move_to_element(url).click().perform()
        url.send_keys("https://www.salesmanago.com/")

        phone_number = self.browser.find_element_by_id("phoneNumber")
        action.move_to_element(phone_number).click().perform()
        phone_number.send_keys("123456789")

        self.assertTrue(self.browser.find_element_by_xpath("//div[@class='thanks-message']"))

        submit_button = self.browser.find_element_by_xpath("//*[@id='uspForm']/div[2]/div/button")
        self.browser.execute_script("arguments[0].click();", submit_button)

        self.assertTrue(self.browser.find_element_by_xpath("//div[@class='thanks-message']"))

        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "HERE")))
        self.browser.find_element_by_link_text("HERE").click()
        time.sleep(5)

    return testEbookDownload


if __name__ == '__main__':
    tested_ebook = ebooks["Online Consumer Trends 2020"]
    test_name = 'test {}'.format(tested_ebook)
    test = test_generator(tested_ebook)
    setattr(Ebook, test_name, test)
    unittest.main()

