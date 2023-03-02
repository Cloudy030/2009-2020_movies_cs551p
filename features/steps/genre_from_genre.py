from behave import given, when, then

@given(u'I navigate to genre page')
def nav(context):
    """ 
    Navigate to the genre page
    """
    context.browser.get('https://sierraviolin-learncombine-5000.codio-box.uk/genre')

@when(u'I click on the genre in genre list')
def click(context):
    """ 
    Find the desired link
    """
    context.browser.find_element_by_partial_link_text('Family').click()

@then(u'I should see the genre details and movies in that genre')
def details(context):
    """ 
    if successful, then we should be directed to the genre movie page
    """
    # use print(context.browser.page_source) to aid debugging
    print(context.browser.page_source)
    assert context.browser.current_url == 'https://sierraviolin-learncombine-5000.codio-box.uk/genre_movie/Family'
    assert 'Beauty and the Beast | ->    PG | Family | 2017 | 7.1 Round of Your Life | ->     | Family | 2019 | 4.6' in context.browser.page_source