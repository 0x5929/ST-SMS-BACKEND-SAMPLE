Feature: Student Management Google Sheet Datadump

    Only superusers have any access to googlesheet datadump feature


    Scenario: superuser requesting to GET without parameters
        Given logged on as superuser
        When request GET to /api/sms/google_sheet_datadump/
        Then server response status is bad request 400


    Scenario: superuser requesting to GET with parameters
        Given logged on as superuser
        When request GET to /api/sms/google_sheet_datadump/?ssid=<>&sid=<>&school_name=<>
        Then will receive student data in json datadump
        And server response status is OK 200

    Scenario: superuser requesting to POST
        Given logged on as superuser
        When request POST to /api/sms/google_sheet_datadump/
        Then server will respond with 405

    Scenario: superuser requesting to PUT
        Given logged on as superuser
        When request PUT to /api/sms/google_sheet_datadump/
        Then server will respond with 405

    Scenario: superuser requesting to PATCH
        Given logged on as superuser
        When request PATCH to /api/sms/google_sheet_datadump/
        Then server will respond with 405


    Scenario: superuser requesting to DELETE
        Given logged on as superuser
        When request DELETE to /api/sms/google_sheet_datadump/
        Then server will respond with 405


    Scenario: admin user requesting to GET with parameters
        Given logged on as admin office user
        When request GET to /api/sms/google_sheet_datadump/?ssid=<>&sid=<>&school_name=<>
        Then will receive superuser only message
        And server response status is forbidden 403


    Scenario: staff user requesting to GET with parameters
        Given logged on as staff office user
        When request GET to /api/sms/google_sheet_datadump/?ssid=<>&sid=<>&school_name=<>
        Then will receive superuser only message
        And server response status is forbidden 403


    Scenario: regular user requesting to GET with parameters
        Given logged on as regular office user
        When request GET to /api/sms/google_sheet_datadump/?ssid=<>&sid=<>&school_name=<>
        Then will receive superuser only message
        And server response status is forbidden 403