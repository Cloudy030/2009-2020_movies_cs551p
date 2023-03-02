Feature: Movie from movie
""" 
Confirm that we can browse the movie details page on our site
"""

Scenario: success for visiting movie details page
    Given I navigate to movie page
    When I click on the movie name in movie full list
    Then I should see the details of that movie