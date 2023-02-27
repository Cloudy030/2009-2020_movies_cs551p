from behave import given, when, then

@given(u'I navigate to movie details page')
def nav(context):
    """ 
    Navigate to all movies page
    """
    context.browser.get('http://localhost:5000/indexdexmo')

@when(u'I click on movie name in movie full list')
def click(context):
    """ 
    Find the desired link
    """
    context.browser.find_element(By.PARTIAL_LINK_TEXT, "Inglourious Basterds").click()
    # element = driver.find_element(By.PARTIAL_LINK_TEXT, "element_partial_link_text")
    # https://stackoverflow.com/questions/69875125/find-element-by-commands-are-deprecated-in-selenium
    # explain this part in the reflective journey as challenge

@then(u'I should see details of that movie')
def details(context):
    """ 
    if successful, then we should be directed to movie details page
    """
    # use print(context.browser.page_source) to aid debugging
    print(context.browser.page_source)
    assert context.browser.current_url == 'http://localhost:5000/movie_detail/Inglourious Basterds'
    assert '01595 Amanda Loaf' in context.browser.page_source