Feature: Client Management READ access
    
    Regular recruit users have read access cms resource assignned to them by email. 
    Admin recruit users have read access to all cms resource within that school.
    Superusers have read access to all cms resources.


    # diff users reading the same client/notes resource that is already assigned to regular user
    Scenario: superuser requesting to read cms/clients resource
        Given logged on as superuser
        When request GET to /api/cms/clients/client_uuid
        Then will receive JSON response of data

    Scenario: superuser requesting to read cms/notes resource
        Given logged on as superuser
        When request GET to /api/cms/notes/note_uuid
        Then will receive JSON response of data

    Scenario: admin recruit user requesting to read cms/clients resource
        Given logged on as admin recruit user
        When request GET to /api/cms/clients/client_uuid
        Then will receive JSON response of data

    Scenario: admin recruit user requesting to read cms/notes resource
        Given logged on as admin recruit user
        When request GET to /api/cms/notes/note_uuid
        Then will receive JSON response of data

    Scenario: staff recruit user requesting to read cms/clients resource
        Given logged on as staff recruit user
        When request GET to /api/cms/clients/client_uuid
        Then will receive JSON response of data

    Scenario: staff recruit user requesting to read cms/notes resource
        Given logged on as staff recruit user
        When request GET to /api/cms/notes/note_uuid
        Then will receive JSON response of data

    Scenario: regular recruit user requesting to read cms/clients resource
        Given logged on as regular recruit user
        When request GET to /api/cms/clients/client_uuid
        Then will receive JSON response of data

    Scenario: regular recruit user requesting to read cms/notes resource
        Given logged on as regular recruit user
        When request GET to /api/cms/notes/note_uuid
        Then will receive JSON response of data


    # # diff users reading the same client/notes resource that is not assigned to our regular user, should only fail with reg users
    Scenario: superuser requesting to read second cms/clients resource
        Given logged on as superuser
        When request GET to second /api/cms/clients/client_uuid
        Then will receive JSON response of data

    Scenario: superuser requesting to read second cms/notes resource
        Given logged on as superuser
        When request GET to second /api/cms/notes/note_uuid
        Then will receive JSON response of data

    Scenario: admin recruit user requesting to read second cms/clients resource
        Given logged on as admin recruit user
        When request GET to second /api/cms/clients/client_uuid
        Then will receive JSON response of data

    Scenario: admin recruit user requesting to read second cms/notes resource
        Given logged on as admin recruit user
        When request GET to second /api/cms/notes/note_uuid
        Then will receive JSON response of data

    Scenario: staff recruit user requesting to read second cms/clients resource
        Given logged on as staff recruit user
        When request GET to second /api/cms/clients/client_uuid
        Then server will respond with 404

    Scenario: staff recruit user requesting to read second cms/notes resource
        Given logged on as staff recruit user
        When request GET to second /api/cms/notes/note_uuid
        Then server will respond with 404

    Scenario: regular recruit user requesting to read second cms/clients resource
        Given logged on as regular recruit user
        When request GET to second /api/cms/clients/client_uuid
        Then server will respond with 404

    Scenario: regular recruit user requesting to read second cms/notes resource
        Given logged on as regular recruit user
        When request GET to second /api/cms/notes/note_uuid
        Then server will respond with 404


    # # diff users reading the same client/notes resource that is from ST2, should only be success with superuser
    Scenario: superuser requesting to read ST2 cms/clients resource
        Given logged on as superuser
        When request GET to ST2 /api/cms/clients/client_uuid
        Then will receive JSON response of data

    Scenario: superuser requesting to read ST2 cms/notes resource
        Given logged on as superuser
        When request GET to ST2 /api/cms/notes/note_uuid
        Then will receive JSON response of data

    Scenario: admin recruit user requesting to read ST2 cms/clients resource
        Given logged on as admin recruit user
        When request GET to ST2 /api/cms/clients/client_uuid
        Then server will respond with 404

    Scenario: admin recruit user requesting to read ST2 cms/notes resource
        Given logged on as admin recruit user
        When request GET to ST2 /api/cms/notes/note_uuid
        Then server will respond with 404

    Scenario: staff recruit user requesting to read ST2 cms/clients resource
        Given logged on as staff recruit user
        When request GET to ST2 /api/cms/clients/client_uuid
        Then server will respond with 404

    Scenario: staff recruit user requesting to read ST2 cms/notes resource
        Given logged on as staff recruit user
        When request GET to ST2 /api/cms/notes/note_uuid
        Then server will respond with 404

    Scenario: regular recruit user requesting to read ST2 cms/clients resource
        Given logged on as regular recruit user
        When request GET to ST2 /api/cms/clients/client_uuid
        Then server will respond with 404

    Scenario: regular recruit user requesting to read ST2 cms/notes resource
        Given logged on as regular recruit user
        When request GET to ST2 /api/cms/notes/note_uuid
        Then server will respond with 404