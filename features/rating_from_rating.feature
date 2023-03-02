Feature: Rating from rating
""" 
Confirm that we can browse the rating movie page on our site
"""

Scenario: success for visiting rating movie page
    Given I navigate to rating page
    When I click on the rating in rating list
    Then I should see the rating details and movies with that rating