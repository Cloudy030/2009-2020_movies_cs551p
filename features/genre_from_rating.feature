Feature: Genre from rating
""" 
Confirm that we can browse the genre movie page on our site
"""

Scenario: success for visiting genre movie page
    Given I navigate to rating movie page
    When I click on the genre in rating movie list
    Then I should see the genre details and movies in that genre