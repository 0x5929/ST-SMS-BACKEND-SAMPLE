Feature: Client Management recruit users only
    
    admin, staff, regular users must be labled as an recruit worker to access cms resources
    superuser not tested in this feature, can access all, but is tested in respective get/post/put/patch/del features


    Scenario: admin user requesting to read /api/cms/clients resources
        Given logged on as admin user with is_recruit set to false
        When request GET to /api/cms/clients/client_uuid
        Then will be permission denied

    Scenario: admin user requesting to read /api/cms/notes resources
        Given logged on as admin user with is_recruit set to false
        When request GET to /api/cms/notes/note_uuid
        Then will be permission denied

    Scenario: admin user requesting to create /api/cms/clients resource
        Given logged on as admin user with is_recruit set to false
        When request POST to /api/cms/clients
        Then will be permission denied

    Scenario: admin user requesting to create /api/cms/notes resource
        Given logged on as admin user with is_recruit set to false
        When request POST to /api/cms/notes
        Then will be permission denied

    Scenario: admin user requesting to partially update a /api/cms/clients resource
        Given logged on as admin user with is_recruit set to false
        When request PATCH to /api/cms/clients/client_uuid
        Then will be permission denied

    Scenario: admin user requesting to partially update a /api/cms/notes resource
        Given logged on as admin user with is_recruit set to false
        When request PATCH to /api/cms/notes/note_uuid
        Then will be permission denied

    Scenario: admin user requesting to fully update a /api/cms/clients resource
        Given logged on as admin user with is_recruit set to false
        When request PUT to /api/cms/clients/client_uuid
        Then will be permission denied

    Scenario: admin user requesting to fully update a /api/cms/notes resource
        Given logged on as admin user with is_recruit set to false
        When request PUT to /api/cms/notes/note_uuid
        Then will be permission denied

    Scenario: admin user requesting to delete a /api/cms/clients resource
        Given logged on as admin user with is_recruit set to false
        When request DELETE to /api/cms/clients/client_uuid
        Then will be permission denied

    Scenario: admin user requesting to delete a /api/cms/notes resource
        Given logged on as admin user with is_recruit set to false
        When request DELETE to /api/cms/notes/note_uuid
        Then will be permission denied




    Scenario: staff user requesting to read /api/cms/clients resources
        Given logged on as staff user with is_recruit set to false
        When request GET to /api/cms/clients/client_uuid
        Then will be permission denied

    Scenario: staff user requesting to read /api/cms/notes resources
        Given logged on as staff user with is_recruit set to false
        When request GET to /api/cms/notes/note_uuid
        Then will be permission denied

    Scenario: staff user requesting to create /api/cms/clients resource
        Given logged on as staff user with is_recruit set to false
        When request POST to /api/cms/clients
        Then will be permission denied

    Scenario: staff user requesting to create /api/cms/notes resource
        Given logged on as staff user with is_recruit set to false
        When request POST to /api/cms/notes
        Then will be permission denied

    Scenario: staff user requesting to partially update a /api/cms/clients resource
        Given logged on as staff user with is_recruit set to false
        When request PATCH to /api/cms/clients/client_uuid
        Then will be permission denied

    Scenario: staff user requesting to partially update a /api/cms/notes resource
        Given logged on as staff user with is_recruit set to false
        When request PATCH to /api/cms/notes/note_uuid
        Then will be permission denied

    Scenario: staff user requesting to fully update a /api/cms/clients resource
        Given logged on as staff user with is_recruit set to false
        When request PUT to /api/cms/clients/client_uuid
        Then will be permission denied

    Scenario: staff user requesting to fully update a /api/cms/notes resource
        Given logged on as staff user with is_recruit set to false
        When request PUT to /api/cms/notes/note_uuid
        Then will be permission denied

    Scenario: staff user requesting to delete a /api/cms/clients resource
        Given logged on as staff user with is_recruit set to false
        When request DELETE to /api/cms/clients/client_uuid
        Then will be permission denied

    Scenario: staff user requesting to delete a /api/cms/notes resource
        Given logged on as staff user with is_recruit set to false
        When request DELETE to /api/cms/notes/note_uuid
        Then will be permission denied






    Scenario: regular user requesting to read /api/cms/clients resources
        Given logged on as regular user with is_recruit set to false
        When request GET to /api/cms/clients/client_uuid
        Then will be permission denied

    Scenario: regular user requesting to read /api/cms/notes resources
        Given logged on as regular user with is_recruit set to false
        When request GET to /api/cms/notes/note_uuid
        Then will be permission denied

    Scenario: regular user requesting to create /api/cms/clients resource
        Given logged on as regular user with is_recruit set to false
        When request POST to /api/cms/clients
        Then will be permission denied

    Scenario: regular user requesting to create /api/cms/notes resource
        Given logged on as regular user with is_recruit set to false
        When request POST to /api/cms/notes
        Then will be permission denied

    Scenario: regular user requesting to partially update a /api/cms/clients resource
        Given logged on as regular user with is_recruit set to false
        When request PATCH to /api/cms/clients/client_uuid
        Then will be permission denied

    Scenario: regular user requesting to partially update a /api/cms/notes resource
        Given logged on as regular user with is_recruit set to false
        When request PATCH to /api/cms/notes/note_uuid
        Then will be permission denied

    Scenario: regular user requesting to fully update a /api/cms/clients resource
        Given logged on as regular user with is_recruit set to false
        When request PUT to /api/cms/clients/client_uuid
        Then will be permission denied

    Scenario: regular user requesting to fully update a /api/cms/notes resource
        Given logged on as regular user with is_recruit set to false
        When request PUT to /api/cms/notes/note_uuid
        Then will be permission denied

    Scenario: regular user requesting to delete a /api/cms/clients resource
        Given logged on as regular user with is_recruit set to false
        When request DELETE to /api/cms/clients/client_uuid
        Then will be permission denied

    Scenario: regular user requesting to delete a /api/cms/notes resource
        Given logged on as regular user with is_recruit set to false
        When request DELETE to /api/cms/notes/note_uuid
        Then will be permission denied