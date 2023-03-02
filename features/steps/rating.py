from behave import given, when, then

@given(u'I navigate to rating page')
def nav(context):
    """ 
    Navigate to the genre page
    """
    context.browser.get('http://localhost:5000/genre')

@when(u'I click on the rating category in rating list')
def click(context):
    """ 
    Find the desired link
    """
    context.browser.find_element_by_partial_link_text('G').click()

@then(u'I should see the rating details and movies with that rating')
def details(context):
    """ 
    if successful, then we should be directed to the rating movie page
    """
    # use print(context.browser.page_source) to aid debugging
    print(context.browser.page_source)
    assert context.browser.current_url == 'http://localhost:5000/rating_movie/G'
    # assert '01595 Amanda Loaf' in context.browser.page_source