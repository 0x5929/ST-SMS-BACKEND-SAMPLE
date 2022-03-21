Feature: Client Management CREATE access
    
    Regular recruit users have create access cms resource assignned to them by email. 
    Admin recruit users have create access to all cms resource within that school.
    Superusers have create access to all cms resources.


    # diff users creating the same client/notes resource that is assigned to regular user
    Scenario: superuser requesting to create cms/clients resource
        Given logged on as superuser
        When request POST to /api/cms/clients
        Then database will create the client record

    Scenario: superuser requesting to create cms/notes resource
        Given logged on as superuser
        When request POST to /api/cms/notes
        Then database will create the note record

    Scenario: admin recruit user requesting to create cms/clients resource
        Given logged on as admin recruit user
        When request POST to /api/cms/clients
        Then database will create the client record

    Scenario: admin recruit user requesting to create cms/notes resource
        Given logged on as admin recruit user
        When request POST to /api/cms/notes
        Then database will create the note record

    Scenario: staff recruit user requesting to create cms/clients resource
        Given logged on as staff recruit user
        When request POST to /api/cms/clients
        Then database will create the client record

    Scenario: staff recruit user requesting to create cms/notes resource
        Given logged on as staff recruit user
        When request POST to /api/cms/notes
        Then database will create the note record

    Scenario: regular recruit user requesting to create cms/clients resource
        Given logged on as regular recruit user
        When request POST to /api/cms/clients
        Then database will create the client record

    Scenario: regular recruit user requesting to create cms/notes resource
        Given logged on as regular recruit user
        When request POST to /api/cms/notes
        Then database will create the note record


#     # # diff users reading the same client/notes resource that is not assigned to our regular user, should only fail with reg users
#     Scenario: superuser requesting to read second cms/clients resource
#         Given logged on as superuser
#         When request GET to second /api/cms/clients
#         Then will receive JSON response of data

#     Scenario: superuser requesting to read second cms/notes resource
#         Given logged on as superuser
#         When request GET to second /api/cms/notes
#         Then will receive JSON response of data

#     Scenario: admin recruit user requesting to read second cms/clients resource
#         Given logged on as admin recruit user
#         When request GET to second /api/cms/clients
#         Then will receive JSON response of data

#     Scenario: admin recruit user requesting to read second cms/notes resource
#         Given logged on as admin recruit user
#         When request GET to second /api/cms/notes
#         Then will receive JSON response of data

#     Scenario: staff recruit user requesting to read second cms/clients resource
#         Given logged on as staff recruit user
#         When request GET to second /api/cms/clients
#         Then server will respond with 404

#     Scenario: staff recruit user requesting to read second cms/notes resource
#         Given logged on as staff recruit user
#         When request GET to second /api/cms/notes
#         Then server will respond with 404

#     Scenario: regular recruit user requesting to read second cms/clients resource
#         Given logged on as regular recruit user
#         When request GET to second /api/cms/clients
#         Then server will respond with 404

#     Scenario: regular recruit user requesting to read second cms/notes resource
#         Given logged on as regular recruit user
#         When request GET to second /api/cms/notes
#         Then server will respond with 404


    # # diff users creating the same client/notes resource that is from ST2, should only be success with superuser
    Scenario: superuser requesting to create ST2 cms/clients resource
        Given logged on as superuser
        When request POST to ST2 /api/cms/clients
        Then database will create the ST2 client record

    Scenario: superuser requesting to create ST2 cms/notes resource
        Given logged on as superuser
        When request POST to ST2 /api/cms/notes
        Then database will create the ST2 note record

    Scenario: admin recruit user requesting to create ST2 cms/clients resource
        Given logged on as admin recruit user
        When request POST to ST2 /api/cms/clients
        Then bad request error since we cannot add another school's resource

    Scenario: admin recruit user requesting to create ST2 cms/notes resource
        Given logged on as admin recruit user
        When request POST to ST2 /api/cms/notes
        Then bad request error since we cannot add another school's resource

    Scenario: staff recruit user requesting to create ST2 cms/clients resource
        Given logged on as staff recruit user
        When request POST to ST2 /api/cms/clients
        Then bad request error since we cannot add another school's resource

    Scenario: staff recruit user requesting to create ST2 cms/notes resource
        Given logged on as staff recruit user
        When request POST to ST2 /api/cms/notes
        Then bad request error since we cannot add another school's resource

    Scenario: regular recruit user requesting to create ST2 cms/clients resource
        Given logged on as regular recruit user
        When request POST to ST2 /api/cms/clients
        Then bad request error since we cannot add another school's resource

    Scenario: regular recruit user requesting to create ST2 cms/notes resource
        Given logged on as regular recruit user
        When request POST to ST2 /api/cms/notes
        Then bad request error since we cannot add another school's resource



    Scenario: superuser requesting to create cms/clients resource with bad email
        Given logged on as superuser
        When request POST to /api/cms/clients with email to a non-existant user
        Then bad request since the email added does not belong to an active user

    Scenario: admin recruit user requesting to create cms/clients resource bad email
        Given logged on as admin recruit user
        When request POST to /api/cms/clients with email to a non-existant user
        Then bad request since the email added does not belong to an active user

    Scenario: staff recruit user requesting to create cms/clients resource bad email
        Given logged on as staff recruit user
        When request POST to /api/cms/clients with email to a non-existant user
        Then bad request since the email added does not belong to an active user

    Scenario: regular recruit user requesting to create cms/clients resource bad email
        Given logged on as regular recruit user
        When request POST to /api/cms/clients with email to a non-existant user
        Then bad request since the email added does not belong to an active user
