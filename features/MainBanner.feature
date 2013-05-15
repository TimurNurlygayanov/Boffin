Feature: User Web Interface (Main Banner)


    Scenario: Check banner page 1 on main page
        Given browser with new page "test.mirantis.com"
         When I click on button "BannerPage1"
         Then page should contain button "BannerButton"


    Scenario: Check banner page 2 on main page
        Given browser with new page "test.mirantis.com"
         When I click on button "BannerPage2"
         Then page should contain button "BannerButton"


    Scenario: Check banner page 3 on main page
        Given browser with new page "test.mirantis.com"
         When I click on button "BannerPage3"
         Then page should contain button "BannerButton"


    Scenario: Check banner page 4 on main page
        Given browser with new page "test.mirantis.com"
         When I click on button "BannerPage4"
         Then page should contain button "BannerButton"


    Scenario: Check banner next button on main page
        Given browser with new page "test.mirantis.com"
         When I click on button "NextBannerPage"
         Then page should contain button "BannerButton"


    Scenario: Check banner previous button on main page
        Given browser with new page "test.mirantis.com"
         When I click on button "PreviousBannerPage"
         Then page should contain button "BannerButton"