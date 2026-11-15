
from playwright.sync_api import Page, expect


def test_add_one_item(logged_in_page: Page):
    logged_in_page.locator(
        '[data-test="add-to-cart-sauce-labs-backpack"]'
    ).click()

    expect(
        logged_in_page.locator('[data-test="shopping-cart-badge"]')
    ).to_have_text("1")


def test_add_two_items(logged_in_page: Page):
    logged_in_page.locator(
        '[data-test="add-to-cart-sauce-labs-backpack"]'
    ).click()

    logged_in_page.locator(
        '[data-test="add-to-cart-sauce-labs-bike-light"]'
    ).click()

    expect(
        logged_in_page.locator('[data-test="shopping-cart-badge"]')
    ).to_have_text("2")


def test_remove_item(logged_in_page: Page):
    logged_in_page.locator(
        '[data-test="add-to-cart-sauce-labs-backpack"]'
    ).click()

    logged_in_page.locator(
        '[data-test="remove-sauce-labs-backpack"]'
    ).click()

    expect(
        logged_in_page.locator('[data-test="shopping-cart-badge"]')
    ).to_have_count(0)
