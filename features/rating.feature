Feature: Rating
""" 
Confirm that we can browse the rating related pages on our site
"""

Scenario: success for visiting rating pages
    Given I navigate to rating page
    When I click on the rating category in rating list
    Then I should see the rating details and movies with that rating

Scenario: success for visiting rating pages
    Given I navigate to movies page
    When I click on the rating category in movie list
    Then I should see the rating details and movies with that rating

Scenario: success for visiting rating pages
    Given I navigate to genre page
    When I click on the rating category in genre movie list
    Then I should see the rating details and movies with that rating