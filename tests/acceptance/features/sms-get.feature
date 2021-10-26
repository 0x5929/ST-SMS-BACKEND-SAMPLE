
Feature: Student Management READ access
    
    all users have read access to all sms resources


    Scenario: superuser requesting to read schools resource
        Given logged on as superuser
        When request GET to /api/sms/schools
        Then will receive JSON response of data

    Scenario: superuser requesting to read programs resource
        Given logged on as superuser
        When request GET to /api/sms/programs
        Then will receive JSON response of data

    Scenario: superuser requesting to read rotations resource
        Given logged on as superuser
        When request GET to /api/sms/rotations
        Then will receive JSON response of data

    Scenario: superuser requesting to read students resource
        Given logged on as superuser
        When request GET to /api/sms/students
        Then will receive JSON response of data

    Scenario: admin office user requesting to read schools resource
        Given logged on as admin office user
        When request GET to /api/sms/schools
        Then will receive JSON response of data

    Scenario: admin office user requesting to read programs resource
        Given logged on as admin office user
        When request GET to /api/sms/programs
        Then will receive JSON response of data

    Scenario: admin office user requesting to read rotations resource
        Given logged on as admin office user
        When request GET to /api/sms/rotations
        Then will receive JSON response of data

    Scenario: admin office user requesting to read students resource
        Given logged on as admin office user
        When request GET to /api/sms/students
        Then will receive JSON response of data
 
   Scenario: staff office user requesting to read schools resource
        Given logged on as staff office user
        When request GET to /api/sms/schools
        Then will receive JSON response of data


    Scenario: staff office user requesting to read programs resource
        Given logged on as staff office user
        When request GET to /api/sms/programs
        Then will receive JSON response of data
        And server response status is OK 200


    Scenario: staff office user requesting to read rotations resource
        Given logged on as staff office user
        When request GET to /api/sms/rotations
        Then will receive JSON response of data


    Scenario: staff office user requesting to read students resource
        Given logged on as staff office user
        When request GET to /api/sms/students
        Then will receive JSON response of data

    Scenario: regular office user requesting to read schools resource
        Given logged on as regular office user
        When request GET to /api/sms/schools
        Then will receive JSON response of data


    Scenario: regular office user requesting to read programs resource
        Given logged on as regular office user
        When request GET to /api/sms/programs
        Then will receive JSON response of data


    Scenario: regular office user requesting to read rotations resource
        Given logged on as regular office user
        When request GET to /api/sms/rotations
        Then will receive JSON response of data


    Scenario: regular office user requesting to read students resource
        Given logged on as regular office user
        When request GET to /api/sms/students
        Then will receive JSON response of data