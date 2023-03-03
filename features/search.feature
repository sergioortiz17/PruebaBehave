Feature: Google Search
  Scenario: Search for "Python"
    Given I am on the Google search page
    When I search for "Python"
    Then I see the search results page
