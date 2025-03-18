class TestUi:

    def test_first(self, class_setup):
        driver = class_setup
        driver.get(r'https://www.google.com/')
        title = driver.title
        assert title == 'Google'

    def test_second(self, class_setup):
        driver = class_setup
        driver.get(r'https://selectorshub.com/xpath-practice-page/')
        title = driver.title
        assert title == 'Xpath Practice Page | Shadow dom, nested shadow dom, iframe, nested iframe and more complex automation scenarios.'
