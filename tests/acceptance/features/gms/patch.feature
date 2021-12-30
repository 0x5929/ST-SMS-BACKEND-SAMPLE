Feature: Grading management partially EDIT access

    Superuser can partially update every resource for all programs
    Instructor user can partially update every resource of the programs they are assigned to

    Scenario: superuser requesting to partially update a cnaRotations resource
        Given logged on as superuser
        When request PATCH to /api/gms/cnaRotations
        Then database will partially update the cna rotation record

    Scenario: superuser requesting to partially update a cnaStudents resource
        Given logged on as superuser
        When request PATCH to /api/gms/cnaStudents
        Then database will partially update the cna student record

    Scenario: superuser requesting to partially update a cnaTheoryRecords resource
        Given logged on as superuser
        When request PATCH to /api/gms/cnaTheoryRecords
        Then database will partially update the cna theory record

    Scenario: superuser requesting to partially update a cnaClinicalRecords resource
        Given logged on as superuser
        When request PATCH to /api/gms/cnaClinicalRecords
        Then database will partially update the cna clinical record

    Scenario: superuser requesting to partially update a hhaRotations resource
        Given logged on as superuser
        When request PATCH to /api/gms/hhaRotations
        Then database will partially update the hha rotation record

    Scenario: superuser requesting to partially update a hhaStudents resource
        Given logged on as superuser
        When request PATCH to /api/gms/hhaStudents
        Then database will partially update the hha student record

    Scenario: superuser requesting to partially update a hhaTheoryRecords resource
        Given logged on as superuser
        When request PATCH to /api/gms/hhaTheoryRecords
        Then database will partially update the hha theory record

    Scenario: superuser requesting to partially update a hhaClinicalRecords resource
        Given logged on as superuser
        When request PATCH to /api/gms/hhaClinicalRecords
        Then database will partially update the hha clinical record






    Scenario: admin instructor user requesting to partially update a cnaRotations resource
        Given logged on as admin instructor user
        When request PATCH to /api/gms/cnaRotations
        Then database will partially update the cna rotation record

    Scenario: admin instructor user requesting to partially update a cnaStudents resource
        Given logged on as admin instructor user
        When request PATCH to /api/gms/cnaStudents
        Then database will partially update the cna student record

    Scenario: admin instructor user requesting to partially update a cnaTheoryRecords resource
        Given logged on as admin instructor user
        When request PATCH to /api/gms/cnaTheoryRecords
        Then database will partially update the cna theory record

    Scenario: admin instructor user requesting to partially update a cnaClinicalRecords resource
        Given logged on as admin instructor user
        When request PATCH to /api/gms/cnaClinicalRecords
        Then database will partially update the cna clinical record

    Scenario: admin instructor user requesting to partially update a hhaRotations resource
        Given logged on as admin instructor user
        When request PATCH to /api/gms/hhaRotations
        Then database will partially update the hha rotation record

    Scenario: admin instructor user requesting to partially update a hhaStudents resource
        Given logged on as admin instructor user
        When request PATCH to /api/gms/hhaStudents
        Then database will partially update the hha student record

    Scenario: admin instructor user requesting to partially update a hhaTheoryRecords resource
        Given logged on as admin instructor user
        When request PATCH to /api/gms/hhaTheoryRecords
        Then database will partially update the hha theory record

    Scenario: admin instructor user requesting to partially update a hhaClinicalRecords resource
        Given logged on as admin instructor user
        When request PATCH to /api/gms/hhaClinicalRecords
        Then database will partially update the hha clinical record



    Scenario: staff cna instructor user requesting to partially update cnaRotations resource
        Given logged on as staff cna instructor user
        When request PATCH to /api/gms/cnaRotations
        Then database will partially update the cna rotation record

    Scenario: staff cna instructor user requesting to partially update cnaStudents resource
        Given logged on as staff cna instructor user
        When request PATCH to /api/gms/cnaStudents
        Then database will partially update the cna student record

    Scenario: staff cna instructor user requesting to partially update cnaTheoryRecords resource
        Given logged on as staff cna instructor user
        When request PATCH to /api/gms/cnaTheoryRecords
        Then database will partially update the cna theory record

    Scenario: staff cna instructor user requesting to partially update cnaClinicalRecord resource
        Given logged on as staff cna instructor user
        When request PATCH to /api/gms/cnaClinicalRecords
        Then database will partially update the cna clinical record

    Scenario: staff hha instructor user requesting to partially update hhaRotations resource
        Given logged on as staff hha instructor user
        When request PATCH to /api/gms/hhaRotations
        Then database will partially update the hha rotation record

    Scenario: staff hha instructor user requesting to partially update hhaStudents resource
        Given logged on as staff hha instructor user
        When request PATCH to /api/gms/hhaStudents
        Then database will partially update the hha student record

    Scenario: staff hha instructor user requesting to partially update hhaTheoryRecords resource
        Given logged on as staff hha instructor user
        When request PATCH to /api/gms/hhaTheoryRecords
        Then database will partially update the hha theory record

    Scenario: staff hha instructor user requesting to partially update hhaClinicalRecord resource
        Given logged on as staff hha instructor user
        When request PATCH to /api/gms/hhaClinicalRecords
        Then database will partially update the hha clinical record








    Scenario: staff hha instructor user requesting to partially update cnaRotations resource
        Given logged on as staff hha instructor user
        When request PATCH to /api/gms/cnaRotations
        Then will be permission denied

    Scenario: staff hha instructor user requesting to partially update cnaStudents resource
        Given logged on as staff hha instructor user
        When request PATCH to /api/gms/cnaStudents
        Then will be permission denied

    Scenario: staff hha instructor user requesting to partially update cnaTheoryRecords resource
        Given logged on as staff hha instructor user
        When request PATCH to /api/gms/cnaTheoryRecords
        Then will be permission denied

    Scenario: staff hha instructor user requesting to partially update cnaClinicalRecord resource
        Given logged on as staff hha instructor user
        When request PATCH to /api/gms/cnaClinicalRecords
        Then will be permission denied

    Scenario: staff cna instructor user requesting to partially update hhaRotations resource
        Given logged on as staff cna instructor user
        When request PATCH to /api/gms/hhaRotations
        Then will be permission denied

    Scenario: staff cna instructor user requesting to partially update hhaStudents resource
        Given logged on as staff cna instructor user
        When request PATCH to /api/gms/hhaStudents
        Then will be permission denied

    Scenario: staff cna instructor user requesting to partially update hhaTheoryRecords resource
        Given logged on as staff cna instructor user
        When request PATCH to /api/gms/hhaTheoryRecords
        Then will be permission denied

    Scenario: staff cna instructor user requesting to partially update hhaClinicalRecord resource
        Given logged on as staff cna instructor user
        When request PATCH to /api/gms/hhaClinicalRecords
        Then will be permission denied






    Scenario: cna instructor user requesting to partially update cnaRotations resource
        Given logged on as cna instructor user
        When request PATCH to /api/gms/cnaRotations
        Then database will partially update the cna rotation record

    Scenario: cna instructor user requesting to partially update cnaStudents resource
        Given logged on as cna instructor user
        When request PATCH to /api/gms/cnaStudents
        Then database will partially update the cna student record

    Scenario: cna instructor user requesting to partially update cnaTheoryRecords resource
        Given logged on as cna instructor user
        When request PATCH to /api/gms/cnaTheoryRecords
        Then database will partially update the cna theory record

    Scenario: cna instructor user requesting to partially update cnaClinicalRecord resource
        Given logged on as cna instructor user
        When request PATCH to /api/gms/cnaClinicalRecords
        Then database will partially update the cna clinical record

    Scenario: hha instructor user requesting to partially update hhaRotations resource
        Given logged on as hha instructor user
        When request PATCH to /api/gms/hhaRotations
        Then database will partially update the hha rotation record

    Scenario: hha instructor user requesting to partially update hhaStudents resource
        Given logged on as hha instructor user
        When request PATCH to /api/gms/hhaStudents
        Then database will partially update the hha student record

    Scenario: hha instructor user requesting to partially update hhaTheoryRecords resource
        Given logged on as hha instructor user
        When request PATCH to /api/gms/hhaTheoryRecords
        Then database will partially update the hha theory record

    Scenario: hha instructor user requesting to partially update hhaClinicalRecord resource
        Given logged on as hha instructor user
        When request PATCH to /api/gms/hhaClinicalRecords
        Then database will partially update the hha clinical record







    Scenario: hha instructor user requesting to partially update cnaRotations resource
        Given logged on as hha instructor user
        When request PATCH to /api/gms/cnaRotations
        Then will be permission denied

    Scenario: hha instructor user requesting to partially update cnaStudents resource
        Given logged on as hha instructor user
        When request PATCH to /api/gms/cnaStudents
        Then will be permission denied

    Scenario: hha instructor user requesting to partially update cnaTheoryRecords resource
        Given logged on as hha instructor user
        When request PATCH to /api/gms/cnaTheoryRecords
        Then will be permission denied

    Scenario: hha instructor user requesting to partially update cnaClinicalRecord resource
        Given logged on as hha instructor user
        When request PATCH to /api/gms/cnaClinicalRecords
        Then will be permission denied

    Scenario: cna instructor user requesting to partially update hhaRotations resource
        Given logged on as cna instructor user
        When request PATCH to /api/gms/hhaRotations
        Then will be permission denied

    Scenario: cna instructor user requesting to partially update hhaStudents resource
        Given logged on as cna instructor user
        When request PATCH to /api/gms/hhaStudents
        Then will be permission denied

    Scenario: cna instructor user requesting to partially update hhaTheoryRecords resource
        Given logged on as cna instructor user
        When request PATCH to /api/gms/hhaTheoryRecords
        Then will be permission denied

    Scenario: cna instructor user requesting to partially update hhaClinicalRecord resource
        Given logged on as cna instructor user
        When request PATCH to /api/gms/hhaClinicalRecords
        Then will be permission denied