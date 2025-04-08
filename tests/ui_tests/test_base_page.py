from pages.base_page import BasePage


class TestBasic:

    def test_base_page(self, page):
        base_page = BasePage(page)
        base_page.navigate('https://demoqa.com/')
        forms_locator = base_page.get_element('//*[@class="category-cards"]//*[@class="card mt-4 top-card"][2]')
        base_page.get_element('//*[@class="category-cards"]//*[@class="card mt-4 top-card"][2]').click()
        base_page.click_element(forms_locator)


