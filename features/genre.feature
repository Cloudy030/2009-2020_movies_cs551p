Feature: Genre
""" 
Confirm that we can browse the genre related pages on our site
"""

Scenario: success for visiting genre page
    Given I navigate to the genre pages
    When I click on the link to customer details
    Then I should see the order for that customer

