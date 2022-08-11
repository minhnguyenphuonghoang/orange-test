Feature: Vacancies search
    
    Background: Open Login page
        Given I am on the login page
        When I login successfully
        Then I navigate to Vacancies page

    Scenario: Search and Verify a vacancy
        When I search for vacancy "Senior QA Lead"
        Then I should see the vacancy
        
