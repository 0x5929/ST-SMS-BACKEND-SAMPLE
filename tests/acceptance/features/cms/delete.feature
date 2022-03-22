Feature: Client Management DELETE access
    
    Regular recruit users have delete access cms resource assignned to them by email. 
    Admin recruit users have delete access to all cms resource within that school.
    Superusers have delete access to all cms resources.


    # diff users deleting the same client/notes resource that is assigned to regular user
    Scenario: superuser requesting to delete cms/clients resource
        Given logged on as superuser
        When request DELETE to /api/cms/clients/client_uuid
        Then database will delete the client record

    Scenario: superuser requesting to delete cms/notes resource
        Given logged on as superuser
        When request DELETE to /api/cms/notes/note_uuid
        Then database will delete the note record

    Scenario: admin recruit user requesting to delete cms/clients resource
        Given logged on as admin recruit user
        When request DELETE to /api/cms/clients/client_uuid
        Then database will delete the client record

    Scenario: admin recruit user requesting to delete cms/notes resource
        Given logged on as admin recruit user
        When request DELETE to /api/cms/notes/note_uuid
        Then database will delete the note record

    Scenario: staff recruit user requesting to delete cms/clients resource
        Given logged on as staff recruit user
        When request DELETE to /api/cms/clients/client_uuid
        Then database will delete the client record

    Scenario: staff recruit user requesting to delete cms/notes resource
        Given logged on as staff recruit user
        When request DELETE to /api/cms/notes/note_uuid
        Then database will delete the note record

    Scenario: regular recruit user requesting to delete cms/clients resource
        Given logged on as regular recruit user
        When request DELETE to /api/cms/clients/client_uuid
        Then database will delete the client record

    Scenario: regular recruit user requesting to delete cms/notes resource
        Given logged on as regular recruit user
        When request DELETE to /api/cms/notes/note_uuid
        Then database will delete the note record


    # # diff users deleting the same client/notes resource that is not assigned to our regular user, should only fail with reg users
    Scenario: superuser requesting to delete second cms/clients resource
        Given logged on as superuser
        When request DELETE to second /api/cms/clients/client_uuid
        Then database will delete the second client record

    Scenario: superuser requesting to delete second cms/notes resource
        Given logged on as superuser
        When request DELETE to second /api/cms/notes/note_uuid
        Then database will delete the second note record

    Scenario: admin recruit user requesting to delete second cms/clients resource
        Given logged on as admin recruit user
        When request DELETE to second /api/cms/clients/client_uuid
        Then database will delete the second client record

    Scenario: admin recruit user requesting to delete second cms/notes resource
        Given logged on as admin recruit user
        When request DELETE to second /api/cms/notes/note_uuid
        Then database will delete the second note record

    Scenario: staff recruit user requesting to delete second cms/clients resource
        Given logged on as staff recruit user
        When request DELETE to second /api/cms/clients/client_uuid
        Then server will respond with 404

    Scenario: staff recruit user requesting to delete second cms/notes resource
        Given logged on as staff recruit user
        When request DELETE to second /api/cms/notes/note_uuid
        Then server will respond with 404

    Scenario: regular recruit user requesting to delete second cms/clients resource
        Given logged on as regular recruit user
        When request DELETE to second /api/cms/clients/client_uuid
        Then server will respond with 404

    Scenario: regular recruit user requesting to delete second cms/notes resource
        Given logged on as regular recruit user
        When request DELETE to second /api/cms/notes/note_uuid
        Then server will respond with 404


    # # diff users deleting the same client/notes resource that is from ST2, should only be success with superuser
    Scenario: superuser requesting to delete ST2 cms/clients resource
        Given logged on as superuser
        When request DELETE to ST2 /api/cms/clients
        Then database will delete the ST2 client record

    Scenario: superuser requesting to delete ST2 cms/notes resource
        Given logged on as superuser
        When request DELETE to ST2 /api/cms/notes
        Then database will delete the ST2 note record

    Scenario: admin recruit user requesting to delete ST2 cms/clients resource
        Given logged on as admin recruit user
        When request DELETE to ST2 /api/cms/clients
        Then server will respond with 404

    Scenario: admin recruit user requesting to delete ST2 cms/notes resource
        Given logged on as admin recruit user
        When request DELETE to ST2 /api/cms/notes
        Then server will respond with 404

    Scenario: staff recruit user requesting to delete ST2 cms/clients resource
        Given logged on as staff recruit user
        When request DELETE to ST2 /api/cms/clients
        Then server will respond with 404

    Scenario: staff recruit user requesting to delete ST2 cms/notes resource
        Given logged on as staff recruit user
        When request DELETE to ST2 /api/cms/notes
        Then server will respond with 404

    Scenario: regular recruit user requesting to delete ST2 cms/clients resource
        Given logged on as regular recruit user
        When request DELETE to ST2 /api/cms/clients
        Then server will respond with 404

    Scenario: regular recruit user requesting to delete ST2 cms/notes resource
        Given logged on as regular recruit user
        When request DELETE to ST2 /api/cms/notes
        Then server will respond with 404


