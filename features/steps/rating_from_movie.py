from behave import given, when, then

@given(u'I navigate to movie page')
def nav(context):
    """ 
    Navigate to the movie page
    """
    context.browser.get('https://sierraviolin-learncombine-5000.codio-box.uk/')

@when(u'I click on the rating in movie list')
def click(context):
    """ 
    Find the desired link
    """
    context.browser.find_element_by_partial_link_text('TV-14').click()

@then(u'I should see the rating details and movies with that rating')
def details(context):
    """ 
    if successful, then we should be directed to the rating movie page
    """
    # use print(context.browser.page_source) to aid debugging
    print(context.browser.page_source)
    assert context.browser.current_url == 'https://sierraviolin-learncombine-5000.codio-box.uk/rating_movie/TV-14'
    assert 'Furie | ->    TV-14 | Action | 2019 | 6.3    ' in context.browser.page_source