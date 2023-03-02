from behave import given, when, then

@given(u'I navigate to genre movie page')
def nav(context):
    """ 
    Navigate to the genre movie page
    """
    context.browser.get('https://sierraviolin-learncombine-5000.codio-box.uk/genre_movie/Family')

@when(u'I click on the movie name in genre list')
def click(context):
    """ 
    Find the desired link
    """
    context.browser.find_element_by_partial_link_text('Beauty and the Beast').click()

@then(u'I should see the details of that movie')
def details(context):
    """ 
    if successful, then we should be directed to the movie details page
    """
    # use print(context.browser.page_source) to aid debugging
    print(context.browser.page_source)
    assert context.browser.current_url == 'https://sierraviolin-learncombine-5000.codio-box.uk/movie_detail/Beauty%20and%20the%20Beast'
    assert 'Beauty and the Beast |      PG |      Family |      2017 |      March 17, 2017 (United States) |      7.1 |      283000.0 |      Bill Condon |      Emma Watson |      Stephen Chbosky |      United States |      160000000.0 |      1264434525.0 |      Mandeville Films |      129.0' in context.browser.page_source