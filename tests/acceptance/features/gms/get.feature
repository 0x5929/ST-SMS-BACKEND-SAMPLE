Feature: Grading Management READ access

    Instructor users have read access to gms resources belonging to their program assigned


    ## NOTE: please add in scenarios where we cannot read the resource, such as cna instructor or hha staff instructor etc..
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
        When request GET to /api/gms/cnaClinicalRecords
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




    Scenario: admin instructor user requesting to read cnaRotations resources
        Given logged on as admin instructor user
        When request GET to /api/gms/cnaRotations
        Then will receive JSON response of data

    Scenario: admin instructor user requesting to read cnaStudents resources
        Given logged on as admin instructor user
        When request GET to /api/gms/cnaStudents
        Then will receive JSON response of data

    Scenario: admin instructor user requesting to read cnaTheoryRecords resources
        Given logged on as admin instructor user
        When request GET to /api/gms/cnaTheoryRecords
        Then will receive JSON response of data

    Scenario: admin instructor user requesting to read cnaClinicalRecords resources
        Given logged on as admin instructor user
        When request GET to /api/gms/cnaClinicalRecords
        Then will receive JSON response of data

    Scenario: admin instructor user requesting to read hhaRotations resources
        Given logged on as admin instructor user
        When request GET to /api/gms/hhaRotations
        Then will receive JSON response of data

    Scenario: admin instructor user requesting to read hhaStudents resources
        Given logged on as admin instructor user
        When request GET to /api/gms/hhaStudents
        Then will receive JSON response of data

    Scenario: admin instructor user requesting to read hhaTheoryRecords resources
        Given logged on as admin instructor user
        When request GET to /api/gms/hhaTheoryRecords
        Then will receive JSON response of data

    Scenario: admin instructor user requesting to read hhaClinicalRecords resources
        Given logged on as admin instructor user
        When request GET to /api/gms/hhaClinicalRecords
        Then will receive JSON response of data




    Scenario: staff cna instructor user requesting to read cnaRotations resources
        Given logged on as staff cna instructor user
        When request GET to /api/gms/cnaRotations
        Then will receive JSON response of data

    Scenario: staff cna instructor user requesting to read cnaStudents resources
        Given logged on as staff cna instructor user
        When request GET to /api/gms/cnaStudents
        Then will receive JSON response of data

    Scenario: staff cna instructor user requesting to read cnaTheoryRecords resources
        Given logged on as staff cna instructor user
        When request GET to /api/gms/cnaTheoryRecords
        Then will receive JSON response of data

    Scenario: staff cna instructor user requesting to read cnaClinicalRecords resources
        Given logged on as staff cna instructor user
        When request GET to /api/gms/cnaClinicalRecords
        Then will receive JSON response of data

    Scenario: staff hha instructor user requesting to read hhaRotations resources
        Given logged on as staff hha instructor user
        When request GET to /api/gms/hhaRotations
        Then will receive JSON response of data

    Scenario: staff hha instructor user requesting to read hhaStudents resources
        Given logged on as staff hha instructor user
        When request GET to /api/gms/hhaStudents
        Then will receive JSON response of data

    Scenario: staff hha instructor user requesting to read hhaTheoryRecords resources
        Given logged on as staff hha instructor user
        When request GET to /api/gms/hhaTheoryRecords
        Then will receive JSON response of data

    Scenario: staff hha instructor user requesting to read hhaClinicalRecords resources
        Given logged on as staff hha instructor user
        When request GET to /api/gms/hhaClinicalRecords
        Then will receive JSON response of data





    Scenario: staff hha instructor user requesting to read cnaRotations resources
        Given logged on as staff hha instructor user
        When request GET to /api/gms/cnaRotations
        Then will be permission denied

    Scenario: staff hha instructor user requesting to read cnaStudents resources
        Given logged on as staff hha instructor user
        When request GET to /api/gms/cnaStudents
        Then will be permission denied

    Scenario: staff hha instructor user requesting to read cnaTheoryRecords resources
        Given logged on as staff hha instructor user
        When request GET to /api/gms/cnaTheoryRecords
        Then will be permission denied

    Scenario: staff hha instructor user requesting to read cnaClinicalRecords resources
        Given logged on as staff hha instructor user
        When request GET to /api/gms/cnaClinicalRecords
        Then will be permission denied

    Scenario: staff cna instructor user requesting to read hhaRotations resources
        Given logged on as staff cna instructor user
        When request GET to /api/gms/hhaRotations
        Then will be permission denied

    Scenario: staff cna instructor user requesting to read hhaStudents resources
        Given logged on as staff cna instructor user
        When request GET to /api/gms/hhaStudents
        Then will be permission denied

    Scenario: staff cna instructor user requesting to read hhaTheoryRecords resources
        Given logged on as staff cna instructor user
        When request GET to /api/gms/hhaTheoryRecords
        Then will be permission denied

    Scenario: staff cna instructor user requesting to read hhaClinicalRecords resources
        Given logged on as staff cna instructor user
        When request GET to /api/gms/hhaClinicalRecords
        Then will be permission denied






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
        When request GET to /api/gms/cnaClinicalRecords
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





    Scenario: hha instructor user requesting to read cnaRotations resources
        Given logged on as hha instructor user
        When request GET to /api/gms/cnaRotations
        Then will be permission denied

    Scenario: hha instructor user requesting to read cnaStudents resources
        Given logged on as hha instructor user
        When request GET to /api/gms/cnaStudents
        Then will be permission denied

    Scenario: hha instructor user requesting to read cnaTheoryRecords resources
        Given logged on as hha instructor user
        When request GET to /api/gms/cnaTheoryRecords
        Then will be permission denied

    Scenario: hha instructor user requesting to read cnaClinicalRecords resources
        Given logged on as hha instructor user
        When request GET to /api/gms/cnaClinicalRecords
        Then will be permission denied

    Scenario: cna instructor user requesting to read hhaRotations resources
        Given logged on as cna instructor user
        When request GET to /api/gms/hhaRotations
        Then will be permission denied

    Scenario: cna instructor user requesting to read hhaStudents resources
        Given logged on as cna instructor user
        When request GET to /api/gms/hhaStudents
        Then will be permission denied

    Scenario: cna instructor user requesting to read hhaTheoryRecords resources
        Given logged on as cna instructor user
        When request GET to /api/gms/hhaTheoryRecords
        Then will be permission denied

    Scenario: cna instructor user requesting to read hhaClinicalRecords resources
        Given logged on as cna instructor user
        When request GET to /api/gms/hhaClinicalRecords
        Then will be permission denied
















