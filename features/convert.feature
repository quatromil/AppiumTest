Feature: Convert Units in the App.


    @dimensions
    Scenario: As an active user I want to Convert Longitude
      Given I start the App
      When I press keys for the value
      Then I see result

    @dimensions
    Scenario: As an active user I want to Convert Area
      Given I start the App
      When I open the Menu
      And I go to Area option
      And I press keys for the value
      Then I see result

    @dimensions
    Scenario: As an active user I want to Convert Volume
      Given I start the App
      When I open the Menu
      And I go to Volume option
      And I press keys for the value
      Then I see result

    @velocities
    Scenario: As an active user I want to Convert Velocity
      Given I start the App
      When I open the Menu
      And I perform Dropdown
      And I go to Velocity option
      And I press keys for the value
      Then I see result

    @velocities
    Scenario: As an active user I want to Convert Aceleration
      Given I start the App
      When I open the Menu
      And I perform Dropdown
      And I go to Aceleration option
      And I press keys for the value
      Then I see result

    @velocities
    Scenario: As an active user I want to Convert Angular Velocity
      Given I start the App
      When I open the Menu
      And I perform Dropdown
      And I go to Angular Velocity option
      And I press keys for the value
      Then I see result

    @velocities
    Scenario: As an active user I want to Convert Fluid Velocity
      Given I start the App
      When I open the Menu
      And I perform Dropdown
      And I go to Fluid Velocity option
      And I press keys for the value
      Then I see result