from behave import given, when, then
from selenium import webdriver

@given('I am on the Google search page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.google.com/")

@when('I search for "{query}"')
def step_impl(context, query):
    search_box = context.driver.find_element_by_name('q')
    search_box.send_keys(query)
    search_box.submit()

@then('I see the search results page')
def step_impl(context):
    assert "Google Search Results" in context.driver.title

    context.driver.quit()
