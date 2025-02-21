from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        """Navigate to a specified URL."""
        self.page.goto(url)

    def get_element(self, locator: str):
        """Return an element by its locator (CSS or XPath)."""
        return self.page.locator(locator)

    def click_element(self, locator: str):
        """Click an element."""
        self.get_element(locator).click()

    def fill_input(self, locator: str, value: str):
        """Fill input with a value."""
        self.get_element(locator).fill(value)

    def get_text(self, locator: str) -> str:
        """Get text content of an element."""
        return self.get_element(locator).text_content()

    def is_element_visible(self, locator: str) -> bool:
        """Check if an element is visible."""
        return self.get_element(locator).is_visible()

    def wait_for_element(self, locator: str, timeout: int = 5000):
        """Wait for an element to appear."""
        self.page.wait_for_selector(locator, timeout=timeout)

    def take_screenshot(self, path: str):
        """Take a screenshot and save to the specified path."""
        self.page.screenshot(path=path)
