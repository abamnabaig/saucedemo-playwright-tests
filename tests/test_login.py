from playwright.sync_api import Page, expect

URL = "https://www.saucedemo.com"


def test_valid_login(page: Page):
    # Arrange
    page.goto(URL)

    # Act
    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()

    # Assert
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator('[data-test="title"]')).to_have_text("Products")


def test_login_wrong_password(page: Page):
    page.goto(URL)
    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("wrong123")
    page.locator('[data-test="login-button"]').click()

    expect(page.locator('[data-test="error"]')).to_contain_text("do not match")