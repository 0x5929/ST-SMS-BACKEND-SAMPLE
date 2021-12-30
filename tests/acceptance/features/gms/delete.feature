Feature: Grading management DELETE access

    Superuser can delete every resource for all programs
    Instructor user can delete every resource of the programs they are assigned to


    Scenario: requesting to auth login
        Given no initial logon
        When request GET to /auth/login/
        Then server will respond with 405

    Scenario: superuser requesting to delete a cnaRotations resource
        Given logged on as superuser
        When request DELETE to /api/gms/cnaRotations
        Then database will delete the cna rotation record

    Scenario: superuser requesting to delete a cnaStudents resource
        Given logged on as superuser
        When request DELETE to /api/gms/cnaStudents
        Then database will delete the cna student record

    Scenario: superuser requesting to delete a cnaTheoryRecords resource
        Given logged on as superuser
        When request DELETE to /api/gms/cnaTheoryRecords
        Then database will delete the cna theory record

    Scenario: superuser requesting to delete a cnaClinicalRecords resource
        Given logged on as superuser
        When request DELETE to /api/gms/cnaClinicalRecords
        Then database will delete the cna clinical record

    Scenario: superuser requesting to delete a hhaRotations resource
        Given logged on as superuser
        When request DELETE to /api/gms/hhaRotations
        Then database will delete the hha rotation record

    Scenario: superuser requesting to delete a hhaStudents resource
        Given logged on as superuser
        When request DELETE to /api/gms/hhaStudents
        Then database will delete the hha student record

    Scenario: superuser requesting to delete a hhaTheoryRecords resource
        Given logged on as superuser
        When request DELETE to /api/gms/hhaTheoryRecords
        Then database will delete the hha theory record

    Scenario: superuser requesting to delete a hhaClinicalRecords resource
        Given logged on as superuser
        When request DELETE to /api/gms/hhaClinicalRecords
        Then database will delete the hha clinical record




    Scenario: admin instructor user requesting to delete a cnaRotations resource
        Given logged on as admin instructor user
        When request DELETE to /api/gms/cnaRotations
        Then database will delete the cna rotation record

    Scenario: admin instructor user requesting to delete a cnaStudents resource
        Given logged on as admin instructor user
        When request DELETE to /api/gms/cnaStudents
        Then database will delete the cna student record

    Scenario: admin instructor user requesting to delete a cnaTheoryRecords resource
        Given logged on as admin instructor user
        When request DELETE to /api/gms/cnaTheoryRecords
        Then database will delete the cna theory record

    Scenario: admin instructor user requesting to delete a cnaClinicalRecords resource
        Given logged on as admin instructor user
        When request DELETE to /api/gms/cnaClinicalRecords
        Then database will delete the cna clinical record

    Scenario: admin instructor user requesting to delete a hhaRotations resource
        Given logged on as admin instructor user
        When request DELETE to /api/gms/hhaRotations
        Then database will delete the hha rotation record

    Scenario: admin instructor user requesting to delete a hhaStudents resource
        Given logged on as admin instructor user
        When request DELETE to /api/gms/hhaStudents
        Then database will delete the hha student record

    Scenario: admin instructor user requesting to delete a hhaTheoryRecords resource
        Given logged on as admin instructor user
        When request DELETE to /api/gms/hhaTheoryRecords
        Then database will delete the hha theory record

    Scenario: admin instructor user requesting to delete a hhaClinicalRecords resource
        Given logged on as admin instructor user
        When request DELETE to /api/gms/hhaClinicalRecords
        Then database will delete the hha clinical record





    Scenario: staff cna instructor user requesting to delete a cnaRotations resource
        Given logged on as staff cna instructor user
        When request DELETE to /api/gms/cnaRotations
        Then database will delete the cna rotation record

    Scenario: staff cna instructor user requesting to delete a cnaStudents resource
        Given logged on as staff cna instructor user
        When request DELETE to /api/gms/cnaStudents
        Then database will delete the cna student record

    Scenario: staff cna instructor user requesting to delete a cnaTheoryRecords resource
        Given logged on as staff cna instructor user
        When request DELETE to /api/gms/cnaTheoryRecords
        Then database will delete the cna theory record

    Scenario: staff cna instructor user requesting to delete a cnaClinicalRecords resource
        Given logged on as staff cna instructor user
        When request DELETE to /api/gms/cnaClinicalRecords
        Then database will delete the cna clinical record

    Scenario: staff hha instructor user requesting to delete a hhaRotations resource
        Given logged on as staff hha instructor user
        When request DELETE to /api/gms/hhaRotations
        Then database will delete the hha rotation record

    Scenario: staff hha instructor user requesting to delete a hhaStudents resource
        Given logged on as staff hha instructor user
        When request DELETE to /api/gms/hhaStudents
        Then database will delete the hha student record

    Scenario: staff hha instructor user requesting to delete a hhaTheoryRecords resource
        Given logged on as staff hha instructor user
        When request DELETE to /api/gms/hhaTheoryRecords
        Then database will delete the hha theory record

    Scenario: staff hha instructor user requesting to delete a hhaClinicalRecords resource
        Given logged on as staff hha instructor user
        When request DELETE to /api/gms/hhaClinicalRecords
        Then database will delete the hha clinical record





    Scenario: staff hha instructor user requesting to delete a cnaRotations resource
        Given logged on as staff hha instructor user
        When request DELETE to /api/gms/cnaRotations
        Then will be permission denied

    Scenario: staff hha instructor user requesting to delete a cnaStudents resource
        Given logged on as staff hha instructor user
        When request DELETE to /api/gms/cnaStudents
        Then will be permission denied

    Scenario: staff hha instructor user requesting to delete a cnaTheoryRecords resource
        Given logged on as staff hha instructor user
        When request DELETE to /api/gms/cnaTheoryRecords
        Then will be permission denied

    Scenario: staff hha instructor user requesting to delete a cnaClinicalRecords resource
        Given logged on as staff hha instructor user
        When request DELETE to /api/gms/cnaClinicalRecords
        Then will be permission denied

    Scenario: staff cna instructor user requesting to delete a hhaRotations resource
        Given logged on as staff cna instructor user
        When request DELETE to /api/gms/hhaRotations
        Then will be permission denied

    Scenario: staff cna instructor user requesting to delete a hhaStudents resource
        Given logged on as staff cna instructor user
        When request DELETE to /api/gms/hhaStudents
        Then will be permission denied

    Scenario: staff cna instructor user requesting to delete a hhaTheoryRecords resource
        Given logged on as staff cna instructor user
        When request DELETE to /api/gms/hhaTheoryRecords
        Then will be permission denied

    Scenario: staff cna instructor user requesting to delete a hhaClinicalRecords resource
        Given logged on as staff cna instructor user
        When request DELETE to /api/gms/hhaClinicalRecords
        Then will be permission denied






    Scenario: cna instructor user requesting to delete cnaRotations resource
        Given logged on as cna instructor user
        When request DELETE to /api/gms/cnaRotations
        Then database will delete the cna rotation record

    Scenario: cna instructor user requesting to delete cnaStudents resource
        Given logged on as cna instructor user
        When request DELETE to /api/gms/cnaStudents
        Then database will delete the cna student record

    Scenario: cna instructor user requesting to delete cnaTheoryRecords resource
        Given logged on as cna instructor user
        When request DELETE to /api/gms/cnaTheoryRecords
        Then database will delete the cna theory record

    Scenario: cna instructor user requesting to delete cnaClinicalRecord resource
        Given logged on as cna instructor user
        When request DELETE to /api/gms/cnaClinicalRecords
        Then database will delete the cna clinical record

    Scenario: hha instructor user requesting to delete hhaRotations resource
        Given logged on as hha instructor user
        When request DELETE to /api/gms/hhaRotations
        Then database will delete the hha rotation record

    Scenario: hha instructor user requesting to delete hhaStudents resource
        Given logged on as hha instructor user
        When request DELETE to /api/gms/hhaStudents
        Then database will delete the hha student record

    Scenario: hha instructor user requesting to delete hhaTheoryRecords resource
        Given logged on as hha instructor user
        When request DELETE to /api/gms/hhaTheoryRecords
        Then database will delete the hha theory record

    Scenario: hha instructor user requesting to delete hhaClinicalRecord resource
        Given logged on as hha instructor user
        When request DELETE to /api/gms/hhaClinicalRecords
        Then database will delete the hha clinical record







    Scenario: hha instructor user requesting to delete cnaRotations resource
        Given logged on as hha instructor user
        When request DELETE to /api/gms/cnaRotations
        Then will be permission denied

    Scenario: hha instructor user requesting to delete cnaStudents resource
        Given logged on as hha instructor user
        When request DELETE to /api/gms/cnaStudents
        Then will be permission denied

    Scenario: hha instructor user requesting to delete cnaTheoryRecords resource
        Given logged on as hha instructor user
        When request DELETE to /api/gms/cnaTheoryRecords
        Then will be permission denied

    Scenario: hha instructor user requesting to delete cnaClinicalRecord resource
        Given logged on as hha instructor user
        When request DELETE to /api/gms/cnaClinicalRecords
        Then will be permission denied

    Scenario: cna instructor user requesting to delete hhaRotations resource
        Given logged on as cna instructor user
        When request DELETE to /api/gms/hhaRotations
        Then will be permission denied

    Scenario: cna instructor user requesting to delete hhaStudents resource
        Given logged on as cna instructor user
        When request DELETE to /api/gms/hhaStudents
        Then will be permission denied

    Scenario: cna instructor user requesting to delete hhaTheoryRecords resource
        Given logged on as cna instructor user
        When request DELETE to /api/gms/hhaTheoryRecords
        Then will be permission denied

    Scenario: cna instructor user requesting to delete hhaClinicalRecord resource
        Given logged on as cna instructor user
        When request DELETE to /api/gms/hhaClinicalRecords
        Then will be permission denied
