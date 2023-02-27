Feature: Movie
""" 
Confirm that we can browse the movie related pages on our site
"""

Scenario: success for visiting movie and movie details pages
    Given I navigate to movie pages
    When I click on the movie name in movie full list
    Then I should see the details of that movie
