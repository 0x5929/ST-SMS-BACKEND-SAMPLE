Feature: Client Management PARTIALLY UPDATE access
    
    Regular recruit users have partially update access cms resource assignned to them by email. 
    Admin recruit users have partially update access to all cms resource within that school.
    Superusers have partially update access to all cms resources.


    # diff users partially updating the same client/notes resource that is assigned to regular user
    Scenario: superuser requesting to partially update cms/clients resource
        Given logged on as superuser
        When request PATCH to /api/cms/clients/client_uuid
        Then database will partially update the client record

    Scenario: superuser requesting to partially update cms/notes resource
        Given logged on as superuser
        When request PATCH to /api/cms/notes/note_uuid
        Then database will partially update the note record

    Scenario: admin recruit user requesting to partially update cms/clients resource
        Given logged on as admin recruit user
        When request PATCH to /api/cms/clients/client_uuid
        Then database will partially update the client record

    Scenario: admin recruit user requesting to partially update cms/notes resource
        Given logged on as admin recruit user
        When request PATCH to /api/cms/notes/note_uuid
        Then database will partially update the note record

    Scenario: staff recruit user requesting to partially update cms/clients resource
        Given logged on as staff recruit user
        When request PATCH to /api/cms/clients/client_uuid
        Then database will partially update the client record

    Scenario: staff recruit user requesting to partially update cms/notes resource
        Given logged on as staff recruit user
        When request PATCH to /api/cms/notes/note_uuid
        Then database will partially update the note record

    Scenario: regular recruit user requesting to partially update cms/clients resource
        Given logged on as regular recruit user
        When request PATCH to /api/cms/clients/client_uuid
        Then database will partially update the client record

    Scenario: regular recruit user requesting to partially update cms/notes resource
        Given logged on as regular recruit user
        When request PATCH to /api/cms/notes/note_uuid
        Then database will partially update the note record


    # # diff users partially updating the same client/notes resource that is not assigned to our regular user, should only fail with reg users
    Scenario: superuser requesting to partially update second cms/clients resource
        Given logged on as superuser
        When request PATCH to second /api/cms/clients/client_uuid
        Then database will partially update the second client record

    Scenario: superuser requesting to partially update second cms/notes resource
        Given logged on as superuser
        When request PATCH to second /api/cms/notes/note_uuid
        Then database will partially update the second note record

    Scenario: admin recruit user requesting to partially update second cms/clients resource
        Given logged on as admin recruit user
        When request PATCH to second /api/cms/clients/client_uuid
        Then database will partially update the second client record

    Scenario: admin recruit user requesting to partially update second cms/notes resource
        Given logged on as admin recruit user
        When request PATCH to second /api/cms/notes/note_uuid
        Then database will partially update the second note record

    Scenario: staff recruit user requesting to partially update second cms/clients resource
        Given logged on as staff recruit user
        When request PATCH to second /api/cms/clients/client_uuid
        Then server will respond with 404

    Scenario: staff recruit user requesting to partially update second cms/notes resource
        Given logged on as staff recruit user
        When request PATCH to second /api/cms/notes/note_uuid
        Then server will respond with 404

    Scenario: regular recruit user requesting to partially update second cms/clients resource
        Given logged on as regular recruit user
        When request PATCH to second /api/cms/clients/client_uuid
        Then server will respond with 404

    Scenario: regular recruit user requesting to partially update second cms/notes resource
        Given logged on as regular recruit user
        When request PATCH to second /api/cms/notes/note_uuid
        Then server will respond with 404


    # # diff users creating the same client/notes resource that is from ST2, should only be success with superuser
    Scenario: superuser requesting to partially update ST2 cms/clients resource
        Given logged on as superuser
        When request PATCH to ST2 /api/cms/clients
        Then database will partially update the ST2 client record

    Scenario: superuser requesting to partially update ST2 cms/notes resource
        Given logged on as superuser
        When request PATCH to ST2 /api/cms/notes
        Then database will partially update the ST2 note record

    Scenario: admin recruit user requesting to partially update ST2 cms/clients resource
        Given logged on as admin recruit user
        When request PATCH to ST2 /api/cms/clients
        Then server will respond with 404

    Scenario: admin recruit user requesting to partially update ST2 cms/notes resource
        Given logged on as admin recruit user
        When request PATCH to ST2 /api/cms/notes
        Then server will respond with 404

    Scenario: staff recruit user requesting to partially update ST2 cms/clients resource
        Given logged on as staff recruit user
        When request PATCH to ST2 /api/cms/clients
        Then server will respond with 404

    Scenario: staff recruit user requesting to partially update ST2 cms/notes resource
        Given logged on as staff recruit user
        When request PATCH to ST2 /api/cms/notes
        Then server will respond with 404

    Scenario: regular recruit user requesting to partially update ST2 cms/clients resource
        Given logged on as regular recruit user
        When request PATCH to ST2 /api/cms/clients
        Then server will respond with 404

    Scenario: regular recruit user requesting to partially update ST2 cms/notes resource
        Given logged on as regular recruit user
        When request PATCH to ST2 /api/cms/notes
        Then server will respond with 404



    Scenario: superuser requesting to partially update cms/clients resource with bad email
        Given logged on as superuser
        When request PATCH to /api/cms/clients with email to a non-existant user
        Then bad request since the email added does not belong to an active user

    Scenario: admin recruit user requesting to partially update cms/clients resource bad email
        Given logged on as admin recruit user
        When request PATCH to /api/cms/clients with email to a non-existant user
        Then bad request since the email added does not belong to an active user

    Scenario: staff recruit user requesting to partially update cms/clients resource bad email
        Given logged on as staff recruit user
        When request PATCH to /api/cms/clients with email to a non-existant user
        Then bad request since the email added does not belong to an active user

    Scenario: regular recruit user requesting to partially update cms/clients resource bad email
        Given logged on as regular recruit user
        When request PATCH to /api/cms/clients with email to a non-existant user
        Then bad request since the email added does not belong to an active user
