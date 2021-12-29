Feature: Grading Management READ access

    Instructor users have read access to gms resources belonging to their program assigned

    Scenario: superuser requesting to read cnaRotations resources
        Given logged on as superuser
        When request GET to /api/gms/cnaRotations
        Then will receive JSON response of data

    Scenario: superuser requesting to read cnaStudents resources
        Given logged on as superuser
        When request GET to /api/gms/cnaStudents
        Then will receive JSON response of data

    Scenario: superuser requesting to read cnaTheoryRecords resources
        Given logged on as superuser
        When request GET to /api/gms/cnaTheoryRecords
        Then will receive JSON response of data

    Scenario: superuser requesting to read cnaClinicalRecords resources
        Given logged on as superuser
        When request GET to /api/gms/cnaClinicalRecord
        Then will receive JSON response of data

    Scenario: superuser requesting to read hhaRotations resources
        Given logged on as superuser
        When request GET to /api/gms/hhaRotations
        Then will receive JSON response of data

    Scenario: superuser requesting to read hhaStudents resources
        Given logged on as superuser
        When request GET to /api/gms/hhaStudents
        Then will receive JSON response of data

    Scenario: superuser requesting to read hhaTheoryRecords resources
        Given logged on as superuser
        When request GET to /api/gms/hhaTheoryRecords
        Then will receive JSON response of data

    Scenario: superuser requesting to read hhaClinicalRecords resources
        Given logged on as superuser
        When request GET to /api/gms/hhaClinicalRecords
        Then will receive JSON response of data

    Scenario: cna instructor user requesting to read cnaRotations resources
        Given logged on as cna instructor user
        When request GET to /api/gms/cnaRotations
        Then will receive JSON response of data

    Scenario: cna instructor user requesting to read cnaStudents resources
        Given logged on as cna instructor user
        When request GET to /api/gms/cnaStudents
        Then will receive JSON response of data

    Scenario: cna instructor user requesting to read cnaTheoryRecords resources
        Given logged on as cna instructor user
        When request GET to /api/gms/cnaTheoryRecords
        Then will receive JSON response of data

    Scenario: cna instructor user requesting to read cnaClinicalRecords resources
        Given logged on as cna instructor user
        When request GET to /api/gms/cnaClinicalRecord
        Then will receive JSON response of data

    Scenario: hha instructor user requesting to read hhaRotations resources
        Given logged on as hha instructor user
        When request GET to /api/gms/hhaRotations
        Then will receive JSON response of data

    Scenario: hha instructor user requesting to read hhaStudents resources
        Given logged on as hha instructor user
        When request GET to /api/gms/hhaStudents
        Then will receive JSON response of data

    Scenario: hha instructor user requesting to read hhaTheoryRecords resources
        Given logged on as hha instructor user
        When request GET to /api/gms/hhaTheoryRecords
        Then will receive JSON response of data

    Scenario: hha instructor user requesting to read hhaClinicalRecords resources
        Given logged on as hha instructor user
        When request GET to /api/gms/hhaClinicalRecords
        Then will receive JSON response of data