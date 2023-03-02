from behave import given, when, then

@given(u'I navigate to genre page')
def nav(context):
    """ 
    Navigate to the genre page
    """
    context.browser.get('http://localhost:5000/genre')

@when(u'I click on the genre category in genre list')
def click(context):
    """ 
    Find the desired link
    """
    context.browser.find_element_by_partial_link_text('Animation').click()

@then(u'I should see the genre details and movies in that genre')
def details(context):
    """ 
    if successful, then we should be directed to the genre movie page
    """
    # use print(context.browser.page_source) to aid debugging
    print(context.browser.page_source)
    assert context.browser.current_url == 'http://localhost:5000/genre_movie/Animation'
    # assert '01595 Amanda Loaf' in context.browser.page_source