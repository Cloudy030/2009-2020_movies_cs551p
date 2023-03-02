Feature: Genre
""" 
Confirm that we can browse the genre related pages on our site
"""

Scenario: success for visiting genre pages
    Given I navigate to genre page
    When I click on the genre category in genre list
    Then I should see the genre details and movies in that genre

Scenario: success for visiting genre pages
    Given I navigate to movie page
    When I click on the genre in movie list
    Then I should see the genre details and movies in that genre

Scenario: success for visiting genre pages
    Given I navigate to rating page
    When I click on the genre category in rating movie list
    Then I should see the genre details and movies in that genre