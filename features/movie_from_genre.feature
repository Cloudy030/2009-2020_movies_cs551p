Feature: Movie from genre
""" 
Confirm that we can browse the movie details page on our site
"""

Scenario: success for visiting movie details page
    Given I navigate to genre movie page
    When I click on the movie name in genre list
    Then I should see the details of that movie