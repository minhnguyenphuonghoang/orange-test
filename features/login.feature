Feature: Tests for login page
    
    Background: Open Login page
        Given I am on the login page

    Scenario Outline: Log in successfully
        When I log in with username <username> and password <password>
        Then I should be logged in
        Examples:
        | username | password |
        | Admin    | admin123 |
            
