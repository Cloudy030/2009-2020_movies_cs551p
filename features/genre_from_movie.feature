Feature: Genre from movie
""" 
Confirm that we can browse the genre movie page on our site
"""

Scenario: success for visiting genre movie page
    Given I navigate to movie page
    When I click on the genre in movie list
    Then I should see the genre details and movies in that genre