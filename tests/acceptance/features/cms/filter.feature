Feature: Client Management filter

    All recruit user can filter all gms model objects that they have access to based on attributes via GET parameters

    Scenario: superuser requesting to filter cms/clients resource by first_name
        Given logged on as superuser
        When request GET to /api/cms/clients with filters by first_name
        Then the specific clients data will be returned as JSON response

    Scenario: superuser requesting to filter cms/clients resource by last_name
        Given logged on as superuser
        When request GET to /api/cms/clients with filters by last_name
        Then the specific clients data will be returned as JSON response

    Scenario: superuser requesting to filter cms/clients resource by phone_number
        Given logged on as superuser
        When request GET to /api/cms/clients with filters by phone_number
        Then the specific clients data will be returned as JSON response

    Scenario: superuser requesting to filter cms/clients resource by email
        Given logged on as superuser
        When request GET to /api/cms/clients with filters by email
        Then the specific clients data will be returned as JSON response

    Scenario: superuser requesting to filter cms/clients resource by city
        Given logged on as superuser
        When request GET to /api/cms/clients with filters by city
        Then the specific clients data will be returned as JSON response

    Scenario: superuser requesting to filter cms/clients resource by success
        Given logged on as superuser
        When request GET to /api/cms/clients with filters by success
        Then the specific clients data will be returned as JSON response

    Scenario: superuser requesting to filter cms/clients resource by initial_contact
        Given logged on as superuser
        When request GET to /api/cms/clients with filters by initial_contact
        Then the specific clients data will be returned as JSON response

    Scenario: superuser requesting to filter cms/notes resource by date
        Given logged on as superuser
        When request GET to /api/cms/notes with filters by date
        Then the specific notes data will be returned as JSON response

    Scenario: superuser requesting to filter cms/notes resource by content
        Given logged on as superuser
        When request GET to /api/cms/notes with filters by content
        Then the specific notes data will be returned as JSON response





    Scenario: admin recruit user requesting to filter cms/clients resource by first_name
        Given logged on as admin recruit user
        When request GET to /api/cms/clients with filters by first_name
        Then the specific clients data will be returned as JSON response

    Scenario: admin recruit user requesting to filter cms/clients resource by last_name
        Given logged on as admin recruit user
        When request GET to /api/cms/clients with filters by last_name
        Then the specific clients data will be returned as JSON response

    Scenario: admin recruit user requesting to filter cms/clients resource by phone_number
        Given logged on as admin recruit user
        When request GET to /api/cms/clients with filters by phone_number
        Then the specific clients data will be returned as JSON response

    Scenario: admin recruit user requesting to filter cms/clients resource by email
        Given logged on as admin recruit user
        When request GET to /api/cms/clients with filters by email
        Then the specific clients data will be returned as JSON response

    Scenario: admin recruit user requesting to filter cms/clients resource by city
        Given logged on as admin recruit user
        When request GET to /api/cms/clients with filters by city
        Then the specific clients data will be returned as JSON response

    Scenario: admin recruit user requesting to filter cms/clients resource by success
        Given logged on as admin recruit user
        When request GET to /api/cms/clients with filters by success
        Then the specific clients data will be returned as JSON response

    Scenario: admin recruit user requesting to filter cms/clients resource by initial_contact
        Given logged on as admin recruit user
        When request GET to /api/cms/clients with filters by initial_contact
        Then the specific clients data will be returned as JSON response

    Scenario: admin recruit user requesting to filter cms/notes resource by date
        Given logged on as admin recruit user
        When request GET to /api/cms/notes with filters by date
        Then the specific notes data will be returned as JSON response

    Scenario: admin recruit user requesting to filter cms/notes resource by content
        Given logged on as admin recruit user
        When request GET to /api/cms/notes with filters by content
        Then the specific notes data will be returned as JSON response






    Scenario: staff recruit user requesting to filter cms/clients resource by first_name
        Given logged on as staff recruit user
        When request GET to /api/cms/clients with filters by first_name
        Then the specific clients data will be returned as JSON response

    Scenario: staff recruit user requesting to filter cms/clients resource by last_name
        Given logged on as staff recruit user
        When request GET to /api/cms/clients with filters by last_name
        Then the specific clients data will be returned as JSON response

    Scenario: staff recruit user requesting to filter cms/clients resource by phone_number
        Given logged on as staff recruit user
        When request GET to /api/cms/clients with filters by phone_number
        Then the specific clients data will be returned as JSON response

    Scenario: staff recruit user requesting to filter cms/clients resource by email
        Given logged on as staff recruit user
        When request GET to /api/cms/clients with filters by email
        Then the specific clients data will be returned as JSON response

    Scenario: staff recruit user requesting to filter cms/clients resource by city
        Given logged on as staff recruit user
        When request GET to /api/cms/clients with filters by city
        Then the specific clients data will be returned as JSON response

    Scenario: staff recruit user requesting to filter cms/clients resource by success
        Given logged on as staff recruit user
        When request GET to /api/cms/clients with filters by success
        Then the specific clients data will be returned as JSON response

    Scenario: staff recruit user requesting to filter cms/clients resource by initial_contact
        Given logged on as staff recruit user
        When request GET to /api/cms/clients with filters by initial_contact
        Then the specific clients data will be returned as JSON response

    Scenario: staff recruit user requesting to filter cms/notes resource by date
        Given logged on as staff recruit user
        When request GET to /api/cms/notes with filters by date
        Then the specific notes data will be returned as JSON response

    Scenario: staff recruit user requesting to filter cms/notes resource by content
        Given logged on as staff recruit user
        When request GET to /api/cms/notes with filters by content
        Then the specific notes data will be returned as JSON response






    Scenario: regular recruit user requesting to filter cms/clients resource by first_name
        Given logged on as regular recruit user
        When request GET to /api/cms/clients with filters by first_name
        Then the specific clients data will be returned as JSON response

    Scenario: regular recruit user requesting to filter cms/clients resource by last_name
        Given logged on as regular recruit user
        When request GET to /api/cms/clients with filters by last_name
        Then the specific clients data will be returned as JSON response

    Scenario: regular recruit user requesting to filter cms/clients resource by phone_number
        Given logged on as regular recruit user
        When request GET to /api/cms/clients with filters by phone_number
        Then the specific clients data will be returned as JSON response

    Scenario: regular recruit user requesting to filter cms/clients resource by email
        Given logged on as regular recruit user
        When request GET to /api/cms/clients with filters by email
        Then the specific clients data will be returned as JSON response

    Scenario: regular recruit user requesting to filter cms/clients resource by city
        Given logged on as regular recruit user
        When request GET to /api/cms/clients with filters by city
        Then the specific clients data will be returned as JSON response

    Scenario: regular recruit user requesting to filter cms/clients resource by success
        Given logged on as regular recruit user
        When request GET to /api/cms/clients with filters by success
        Then the specific clients data will be returned as JSON response

    Scenario: regular recruit user requesting to filter cms/clients resource by initial_contact
        Given logged on as regular recruit user
        When request GET to /api/cms/clients with filters by initial_contact
        Then the specific clients data will be returned as JSON response

    Scenario: regular recruit user requesting to filter cms/notes resource by date
        Given logged on as regular recruit user
        When request GET to /api/cms/notes with filters by date
        Then the specific notes data will be returned as JSON response

    Scenario: regular recruit user requesting to filter cms/notes resource by content
        Given logged on as regular recruit user
        When request GET to /api/cms/notes with filters by content
        Then the specific notes data will be returned as JSON response















    Scenario: superuser requesting to filter second cms/clients resource by first_name
        Given logged on as superuser
        When request GET to second /api/cms/clients with filters by first_name
        Then the specific second clients data will be returned as JSON response

    Scenario: superuser requesting to filter second cms/clients resource by last_name
        Given logged on as superuser
        When request GET to second /api/cms/clients with filters by last_name
        Then the specific second clients data will be returned as JSON response

    Scenario: superuser requesting to filter second cms/clients resource by phone_number
        Given logged on as superuser
        When request GET to second /api/cms/clients with filters by phone_number
        Then the specific second clients data will be returned as JSON response

    Scenario: superuser requesting to filter second cms/clients resource by email
        Given logged on as superuser
        When request GET to second /api/cms/clients with filters by email
        Then the specific second clients data will be returned as JSON response

    Scenario: superuser requesting to filter second cms/clients resource by city
        Given logged on as superuser
        When request GET to second /api/cms/clients with filters by city
        Then the specific second clients data will be returned as JSON response

    Scenario: superuser requesting to filter second cms/clients resource by success
        Given logged on as superuser
        When request GET to second /api/cms/clients with filters by success
        Then the specific second clients data will be returned as JSON response

    Scenario: superuser requesting to filter second cms/clients resource by initial_contact
        Given logged on as superuser
        When request GET to second /api/cms/clients with filters by initial_contact
        Then the specific second clients data will be returned as JSON response

    Scenario: superuser requesting to filter cms/notes resource by date
        Given logged on as superuser
        When request GET to second /api/cms/notes with filters by date
        Then the specific second notes data will be returned as JSON response

    Scenario: superuser requesting to filter cms/notes resource by content
        Given logged on as superuser
        When request GET to second /api/cms/notes with filters by content
        Then the specific second notes data will be returned as JSON response





    Scenario: admin recruit user requesting to filter second cms/clients resource by first_name
        Given logged on as admin recruit user
        When request GET to second /api/cms/clients with filters by first_name
        Then the specific second clients data will be returned as JSON response

    Scenario: admin recruit user requesting to filter second cms/clients resource by last_name
        Given logged on as admin recruit user
        When request GET to second /api/cms/clients with filters by last_name
        Then the specific second clients data will be returned as JSON response

    Scenario: admin recruit user requesting to filter second cms/clients resource by phone_number
        Given logged on as admin recruit user
        When request GET to second /api/cms/clients with filters by phone_number
        Then the specific second clients data will be returned as JSON response

    Scenario: admin recruit user requesting to filter second cms/clients resource by email
        Given logged on as admin recruit user
        When request GET to second /api/cms/clients with filters by email
        Then the specific second clients data will be returned as JSON response

    Scenario: admin recruit user requesting to filter second cms/clients resource by city
        Given logged on as admin recruit user
        When request GET to second /api/cms/clients with filters by city
        Then the specific second clients data will be returned as JSON response

    Scenario: admin recruit user requesting to filter second cms/clients resource by success
        Given logged on as admin recruit user
        When request GET to second /api/cms/clients with filters by success
        Then the specific second clients data will be returned as JSON response

    Scenario: admin recruit user requesting to filter second cms/clients resource by initial_contact
        Given logged on as admin recruit user
        When request GET to second /api/cms/clients with filters by initial_contact
        Then the specific second clients data will be returned as JSON response

    Scenario: admin recruit user requesting to filter cms/notes resource by date
        Given logged on as admin recruit user
        When request GET to second /api/cms/notes with filters by date
        Then the specific second notes data will be returned as JSON response

    Scenario: admin recruit user requesting to filter cms/notes resource by content
        Given logged on as admin recruit user
        When request GET to second /api/cms/notes with filters by content
        Then the specific second notes data will be returned as JSON response






    Scenario: staff recruit user requesting to filter second cms/clients resource by first_name
        Given logged on as staff recruit user
        When request GET to second /api/cms/clients with filters by first_name
        Then no data will be returned as JSON response

    Scenario: staff recruit user requesting to filter second cms/clients resource by last_name
        Given logged on as staff recruit user
        When request GET to second /api/cms/clients with filters by last_name
        Then no data will be returned as JSON response

    Scenario: staff recruit user requesting to filter second cms/clients resource by phone_number
        Given logged on as staff recruit user
        When request GET to second /api/cms/clients with filters by phone_number
        Then no data will be returned as JSON response

    Scenario: staff recruit user requesting to filter second cms/clients resource by email
        Given logged on as staff recruit user
        When request GET to second /api/cms/clients with filters by email
        Then no data will be returned as JSON response

    Scenario: staff recruit user requesting to filter second cms/clients resource by city
        Given logged on as staff recruit user
        When request GET to second /api/cms/clients with filters by city
        Then no data will be returned as JSON response

    Scenario: staff recruit user requesting to filter second cms/clients resource by success
        Given logged on as staff recruit user
        When request GET to second /api/cms/clients with filters by success
        Then no data will be returned as JSON response

    Scenario: staff recruit user requesting to filter second cms/clients resource by initial_contact
        Given logged on as staff recruit user
        When request GET to second /api/cms/clients with filters by initial_contact
        Then no data will be returned as JSON response

    Scenario: staff recruit user requesting to filter cms/notes resource by date
        Given logged on as staff recruit user
        When request GET to second /api/cms/notes with filters by date
        Then no data will be returned as JSON response

    Scenario: staff recruit user requesting to filter cms/notes resource by content
        Given logged on as staff recruit user
        When request GET to second /api/cms/notes with filters by content
        Then no data will be returned as JSON response






    Scenario: regular recruit user requesting to filter second cms/clients resource by first_name
        Given logged on as regular recruit user
        When request GET to second /api/cms/clients with filters by first_name
        Then no data will be returned as JSON response

    Scenario: regular recruit user requesting to filter second cms/clients resource by last_name
        Given logged on as regular recruit user
        When request GET to second /api/cms/clients with filters by last_name
        Then no data will be returned as JSON response

    Scenario: regular recruit user requesting to filter second cms/clients resource by phone_number
        Given logged on as regular recruit user
        When request GET to second /api/cms/clients with filters by phone_number
        Then no data will be returned as JSON response

    Scenario: regular recruit user requesting to filter second cms/clients resource by email
        Given logged on as regular recruit user
        When request GET to second /api/cms/clients with filters by email
        Then no data will be returned as JSON response

    Scenario: regular recruit user requesting to filter second cms/clients resource by city
        Given logged on as regular recruit user
        When request GET to second /api/cms/clients with filters by city
        Then no data will be returned as JSON response

    Scenario: regular recruit user requesting to filter second cms/clients resource by success
        Given logged on as regular recruit user
        When request GET to second /api/cms/clients with filters by success
        Then no data will be returned as JSON response

    Scenario: regular recruit user requesting to filter second cms/clients resource by initial_contact
        Given logged on as regular recruit user
        When request GET to second /api/cms/clients with filters by initial_contact
        Then no data will be returned as JSON response

    Scenario: regular recruit user requesting to filter cms/notes resource by date
        Given logged on as regular recruit user
        When request GET to second /api/cms/notes with filters by date
        Then no data will be returned as JSON response

    Scenario: regular recruit user requesting to filter cms/notes resource by content
        Given logged on as regular recruit user
        When request GET to second /api/cms/notes with filters by content
        Then no data will be returned as JSON response














    Scenario: superuser requesting to filter ST2 cms/clients resource by first_name
        Given logged on as superuser
        When request GET to ST2 /api/cms/clients with filters by first_name
        Then the specific ST2 clients data will be returned as JSON response

    Scenario: superuser requesting to filter ST2 cms/clients resource by last_name
        Given logged on as superuser
        When request GET to ST2 /api/cms/clients with filters by last_name
        Then the specific ST2 clients data will be returned as JSON response

    Scenario: superuser requesting to filter ST2 cms/clients resource by phone_number
        Given logged on as superuser
        When request GET to ST2 /api/cms/clients with filters by phone_number
        Then the specific ST2 clients data will be returned as JSON response

    Scenario: superuser requesting to filter ST2 cms/clients resource by email
        Given logged on as superuser
        When request GET to ST2 /api/cms/clients with filters by email
        Then the specific ST2 clients data will be returned as JSON response

    Scenario: superuser requesting to filter ST2 cms/clients resource by city
        Given logged on as superuser
        When request GET to ST2 /api/cms/clients with filters by city
        Then the specific ST2 clients data will be returned as JSON response

    Scenario: superuser requesting to filter ST2 cms/clients resource by success
        Given logged on as superuser
        When request GET to ST2 /api/cms/clients with filters by success
        Then the specific ST2 clients data will be returned as JSON response

    Scenario: superuser requesting to filter ST2 cms/clients resource by initial_contact
        Given logged on as superuser
        When request GET to ST2 /api/cms/clients with filters by initial_contact
        Then the specific ST2 clients data will be returned as JSON response

    Scenario: superuser requesting to filter cms/notes resource by date
        Given logged on as superuser
        When request GET to ST2 /api/cms/notes with filters by date
        Then the specific ST2 notes data will be returned as JSON response

    Scenario: superuser requesting to filter cms/notes resource by content
        Given logged on as superuser
        When request GET to ST2 /api/cms/notes with filters by content
        Then the specific ST2 notes data will be returned as JSON response





    Scenario: admin recruit user requesting to filter ST2 cms/clients resource by first_name
        Given logged on as admin recruit user
        When request GET to ST2 /api/cms/clients with filters by first_name
        Then no data will be returned as JSON response

    Scenario: admin recruit user requesting to filter ST2 cms/clients resource by last_name
        Given logged on as admin recruit user
        When request GET to ST2 /api/cms/clients with filters by last_name
        Then no data will be returned as JSON response

    Scenario: admin recruit user requesting to filter ST2 cms/clients resource by phone_number
        Given logged on as admin recruit user
        When request GET to ST2 /api/cms/clients with filters by phone_number
        Then no data will be returned as JSON response

    Scenario: admin recruit user requesting to filter ST2 cms/clients resource by email
        Given logged on as admin recruit user
        When request GET to ST2 /api/cms/clients with filters by email
        Then no data will be returned as JSON response

    Scenario: admin recruit user requesting to filter ST2 cms/clients resource by city
        Given logged on as admin recruit user
        When request GET to ST2 /api/cms/clients with filters by city
        Then no data will be returned as JSON response

    Scenario: admin recruit user requesting to filter ST2 cms/clients resource by success
        Given logged on as admin recruit user
        When request GET to ST2 /api/cms/clients with filters by success
        Then no data will be returned as JSON response

    Scenario: admin recruit user requesting to filter ST2 cms/clients resource by initial_contact
        Given logged on as admin recruit user
        When request GET to ST2 /api/cms/clients with filters by initial_contact
        Then no data will be returned as JSON response

    Scenario: admin recruit user requesting to filter cms/notes resource by date
        Given logged on as admin recruit user
        When request GET to ST2 /api/cms/notes with filters by date
        Then no data will be returned as JSON response

    Scenario: admin recruit user requesting to filter cms/notes resource by content
        Given logged on as admin recruit user
        When request GET to ST2 /api/cms/notes with filters by content
        Then no data will be returned as JSON response






    Scenario: staff recruit user requesting to filter ST2 cms/clients resource by first_name
        Given logged on as staff recruit user
        When request GET to ST2 /api/cms/clients with filters by first_name
        Then no data will be returned as JSON response

    Scenario: staff recruit user requesting to filter ST2 cms/clients resource by last_name
        Given logged on as staff recruit user
        When request GET to ST2 /api/cms/clients with filters by last_name
        Then no data will be returned as JSON response

    Scenario: staff recruit user requesting to filter ST2 cms/clients resource by phone_number
        Given logged on as staff recruit user
        When request GET to ST2 /api/cms/clients with filters by phone_number
        Then no data will be returned as JSON response

    Scenario: staff recruit user requesting to filter ST2 cms/clients resource by email
        Given logged on as staff recruit user
        When request GET to ST2 /api/cms/clients with filters by email
        Then no data will be returned as JSON response

    Scenario: staff recruit user requesting to filter ST2 cms/clients resource by city
        Given logged on as staff recruit user
        When request GET to ST2 /api/cms/clients with filters by city
        Then no data will be returned as JSON response

    Scenario: staff recruit user requesting to filter ST2 cms/clients resource by success
        Given logged on as staff recruit user
        When request GET to ST2 /api/cms/clients with filters by success
        Then no data will be returned as JSON response

    Scenario: staff recruit user requesting to filter ST2 cms/clients resource by initial_contact
        Given logged on as staff recruit user
        When request GET to ST2 /api/cms/clients with filters by initial_contact
        Then no data will be returned as JSON response

    Scenario: staff recruit user requesting to filter cms/notes resource by date
        Given logged on as staff recruit user
        When request GET to ST2 /api/cms/notes with filters by date
        Then no data will be returned as JSON response

    Scenario: staff recruit user requesting to filter cms/notes resource by content
        Given logged on as staff recruit user
        When request GET to ST2 /api/cms/notes with filters by content
        Then no data will be returned as JSON response






    Scenario: regular recruit user requesting to filter ST2 cms/clients resource by first_name
        Given logged on as regular recruit user
        When request GET to ST2 /api/cms/clients with filters by first_name
        Then no data will be returned as JSON response

    Scenario: regular recruit user requesting to filter ST2 cms/clients resource by last_name
        Given logged on as regular recruit user
        When request GET to ST2 /api/cms/clients with filters by last_name
        Then no data will be returned as JSON response

    Scenario: regular recruit user requesting to filter ST2 cms/clients resource by phone_number
        Given logged on as regular recruit user
        When request GET to ST2 /api/cms/clients with filters by phone_number
        Then no data will be returned as JSON response

    Scenario: regular recruit user requesting to filter ST2 cms/clients resource by email
        Given logged on as regular recruit user
        When request GET to ST2 /api/cms/clients with filters by email
        Then no data will be returned as JSON response

    Scenario: regular recruit user requesting to filter ST2 cms/clients resource by city
        Given logged on as regular recruit user
        When request GET to ST2 /api/cms/clients with filters by city
        Then no data will be returned as JSON response

    Scenario: regular recruit user requesting to filter ST2 cms/clients resource by success
        Given logged on as regular recruit user
        When request GET to ST2 /api/cms/clients with filters by success
        Then no data will be returned as JSON response

    Scenario: regular recruit user requesting to filter ST2 cms/clients resource by initial_contact
        Given logged on as regular recruit user
        When request GET to ST2 /api/cms/clients with filters by initial_contact
        Then no data will be returned as JSON response

    Scenario: regular recruit user requesting to filter cms/notes resource by date
        Given logged on as regular recruit user
        When request GET to ST2 /api/cms/notes with filters by date
        Then no data will be returned as JSON response

    Scenario: regular recruit user requesting to filter cms/notes resource by content
        Given logged on as regular recruit user
        When request GET to ST2 /api/cms/notes with filters by content
        Then no data will be returned as JSON response