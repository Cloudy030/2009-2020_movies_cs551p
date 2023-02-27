from behave import given, when, then

@given(u'I navigate to the movie pages')
def nav(context):
    """ 
    Navigate to the movie page
    """
    context.browser.get('http://localhost:5000/index')

@when(u'I click on the movie name in movie full list')
def click(context):
    """ 
    Find the desired link
    """
    context.browser.find_element_by_partial_link_text('2').click()

@then(u'I should see the details of that movie')
def details(context):
    """ 
    if successful, then we should be directed to the movie details page
    """
    # use print(context.browser.page_source) to aid debugging
    print(context.browser.page_source)
    assert context.browser.current_url == 'http://localhost:5000/movie_detail/Inglourious Basterds'
    assert '01595 Amanda Loaf' in context.browser.page_source