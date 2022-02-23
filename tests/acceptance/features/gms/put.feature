Feature: Grading management fully EDIT access

    Superuser can fully update every resource for all programs
    Instructor user can fully update every resource of the programs they are assigned to

    Scenario: requesting to auth login
        Given no initial logon
        When request GET to /auth/login/
        Then server will respond with 405

    Scenario: superuser requesting to fully update a cnaRotations resource
        Given logged on as superuser
        When request PUT to /api/gms/cnaRotations
        Then database will fully update the cna rotation record

    Scenario: superuser requesting to fully update a cnaStudents resource
        Given logged on as superuser
        When request PUT to /api/gms/cnaStudents
        Then database will fully update the cna student record

    Scenario: superuser requesting to fully update a cnaTheoryRecords resource
        Given logged on as superuser
        When request PUT to /api/gms/cnaTheoryRecords
        Then database will fully update the cna theory record

    Scenario: superuser requesting to fully update a cnaClinicalRecords resource
        Given logged on as superuser
        When request PUT to /api/gms/cnaClinicalRecords
        Then database will fully update the cna clinical record

    Scenario: superuser requesting to fully update a hhaRotations resource
        Given logged on as superuser
        When request PUT to /api/gms/hhaRotations
        Then database will fully update the hha rotation record

    Scenario: superuser requesting to fully update a hhaStudents resource
        Given logged on as superuser
        When request PUT to /api/gms/hhaStudents
        Then database will fully update the hha student record

    Scenario: superuser requesting to fully update a hhaTheoryRecords resource
        Given logged on as superuser
        When request PUT to /api/gms/hhaTheoryRecords
        Then database will fully update the hha theory record

    Scenario: superuser requesting to fully update a hhaClinicalRecords resource
        Given logged on as superuser
        When request PUT to /api/gms/hhaClinicalRecords
        Then database will fully update the hha clinical record





    Scenario: admin instructor user requesting to fully update a cnaRotations resource
        Given logged on as admin instructor user
        When request PUT to /api/gms/cnaRotations
        Then database will fully update the cna rotation record

    Scenario: admin instructor user requesting to fully update a cnaStudents resource
        Given logged on as admin instructor user
        When request PUT to /api/gms/cnaStudents
        Then database will fully update the cna student record

    Scenario: admin instructor user requesting to fully update a cnaTheoryRecords resource
        Given logged on as admin instructor user
        When request PUT to /api/gms/cnaTheoryRecords
        Then database will fully update the cna theory record

    Scenario: admin instructor user requesting to fully update a cnaClinicalRecords resource
        Given logged on as admin instructor user
        When request PUT to /api/gms/cnaClinicalRecords
        Then database will fully update the cna clinical record

    Scenario: admin instructor user requesting to fully update a hhaRotations resource
        Given logged on as admin instructor user
        When request PUT to /api/gms/hhaRotations
        Then database will fully update the hha rotation record

    Scenario: admin instructor user requesting to fully update a hhaStudents resource
        Given logged on as admin instructor user
        When request PUT to /api/gms/hhaStudents
        Then database will fully update the hha student record

    Scenario: admin instructor user requesting to fully update a hhaTheoryRecords resource
        Given logged on as admin instructor user
        When request PUT to /api/gms/hhaTheoryRecords
        Then database will fully update the hha theory record

    Scenario: admin instructor user requesting to fully update a hhaClinicalRecords resource
        Given logged on as admin instructor user
        When request PUT to /api/gms/hhaClinicalRecords
        Then database will fully update the hha clinical record






    Scenario: staff cna instructor user requesting to fully update a cnaRotations resource
        Given logged on as staff cna instructor user
        When request PUT to /api/gms/cnaRotations
        Then database will fully update the cna rotation record

    Scenario: staff cna instructor user requesting to fully update a cnaStudents resource
        Given logged on as staff cna instructor user
        When request PUT to /api/gms/cnaStudents
        Then database will fully update the cna student record

    Scenario: staff cna instructor user requesting to fully update a cnaTheoryRecords resource
        Given logged on as staff cna instructor user
        When request PUT to /api/gms/cnaTheoryRecords
        Then database will fully update the cna theory record

    Scenario: staff cna instructor user requesting to fully update a cnaClinicalRecords resource
        Given logged on as staff cna instructor user
        When request PUT to /api/gms/cnaClinicalRecords
        Then database will fully update the cna clinical record

    Scenario: staff hha instructor user requesting to fully update a hhaRotations resource
        Given logged on as staff hha instructor user
        When request PUT to /api/gms/hhaRotations
        Then database will fully update the hha rotation record

    Scenario: staff hha instructor user requesting to fully update a hhaStudents resource
        Given logged on as staff hha instructor user
        When request PUT to /api/gms/hhaStudents
        Then database will fully update the hha student record

    Scenario: staff hha instructor user requesting to fully update a hhaTheoryRecords resource
        Given logged on as staff hha instructor user
        When request PUT to /api/gms/hhaTheoryRecords
        Then database will fully update the hha theory record

    Scenario: staff hha instructor user requesting to fully update a hhaClinicalRecords resource
        Given logged on as staff hha instructor user
        When request PUT to /api/gms/hhaClinicalRecords
        Then database will fully update the hha clinical record




    Scenario: staff hha instructor user requesting to fully update cnaRotations resource
        Given logged on as staff hha instructor user
        When request PUT to /api/gms/cnaRotations
        Then will be permission denied

    Scenario: staff hha instructor user requesting to fully update cnaStudents resource
        Given logged on as staff hha instructor user
        When request PUT to /api/gms/cnaStudents
        Then will be permission denied

    Scenario: staff hha instructor user requesting to fully update cnaTheoryRecords resource
        Given logged on as staff hha instructor user
        When request PUT to /api/gms/cnaTheoryRecords
        Then will be permission denied

    Scenario: staff hha instructor user requesting to fully update cnaClinicalRecord resource
        Given logged on as staff hha instructor user
        When request PUT to /api/gms/cnaClinicalRecords
        Then will be permission denied

    Scenario: staff cna instructor user requesting to fully update hhaRotations resource
        Given logged on as staff cna instructor user
        When request PUT to /api/gms/hhaRotations
        Then will be permission denied

    Scenario: staff cna instructor user requesting to fully update hhaStudents resource
        Given logged on as staff cna instructor user
        When request PUT to /api/gms/hhaStudents
        Then will be permission denied

    Scenario: staff cna instructor user requesting to fully update hhaTheoryRecords resource
        Given logged on as staff cna instructor user
        When request PUT to /api/gms/hhaTheoryRecords
        Then will be permission denied

    Scenario: staff cna instructor user requesting to fully update hhaClinicalRecord resource
        Given logged on as staff cna instructor user
        When request PUT to /api/gms/hhaClinicalRecords
        Then will be permission denied






    Scenario: cna instructor user requesting to fully update cnaRotations resource
        Given logged on as cna instructor user
        When request PUT to /api/gms/cnaRotations
        Then database will fully update the cna rotation record

    Scenario: cna instructor user requesting to fully update cnaStudents resource
        Given logged on as cna instructor user
        When request PUT to /api/gms/cnaStudents
        Then database will fully update the cna student record

    Scenario: cna instructor user requesting to fully update cnaTheoryRecords resource
        Given logged on as cna instructor user
        When request PUT to /api/gms/cnaTheoryRecords
        Then database will fully update the cna theory record

    Scenario: cna instructor user requesting to fully update cnaClinicalRecord resource
        Given logged on as cna instructor user
        When request PUT to /api/gms/cnaClinicalRecords
        Then database will fully update the cna clinical record

    Scenario: hha instructor user requesting to fully update hhaRotations resource
        Given logged on as hha instructor user
        When request PUT to /api/gms/hhaRotations
        Then database will fully update the hha rotation record

    Scenario: hha instructor user requesting to fully update hhaStudents resource
        Given logged on as hha instructor user
        When request PUT to /api/gms/hhaStudents
        Then database will fully update the hha student record

    Scenario: hha instructor user requesting to fully update hhaTheoryRecords resource
        Given logged on as hha instructor user
        When request PUT to /api/gms/hhaTheoryRecords
        Then database will fully update the hha theory record

    Scenario: hha instructor user requesting to fully update hhaClinicalRecord resource
        Given logged on as hha instructor user
        When request PUT to /api/gms/hhaClinicalRecords
        Then database will fully update the hha clinical record







    Scenario: hha instructor user requesting to fully update cnaRotations resource
        Given logged on as hha instructor user
        When request PUT to /api/gms/cnaRotations
        Then will be permission denied

    Scenario: hha instructor user requesting to fully update cnaStudents resource
        Given logged on as hha instructor user
        When request PUT to /api/gms/cnaStudents
        Then will be permission denied

    Scenario: hha instructor user requesting to fully update cnaTheoryRecords resource
        Given logged on as hha instructor user
        When request PUT to /api/gms/cnaTheoryRecords
        Then will be permission denied

    Scenario: hha instructor user requesting to fully update cnaClinicalRecord resource
        Given logged on as hha instructor user
        When request PUT to /api/gms/cnaClinicalRecords
        Then will be permission denied

    Scenario: cna instructor user requesting to fully update hhaRotations resource
        Given logged on as cna instructor user
        When request PUT to /api/gms/hhaRotations
        Then will be permission denied

    Scenario: cna instructor user requesting to fully update hhaStudents resource
        Given logged on as cna instructor user
        When request PUT to /api/gms/hhaStudents
        Then will be permission denied

    Scenario: cna instructor user requesting to fully update hhaTheoryRecords resource
        Given logged on as cna instructor user
        When request PUT to /api/gms/hhaTheoryRecords
        Then will be permission denied

    Scenario: cna instructor user requesting to fully update hhaClinicalRecord resource
        Given logged on as cna instructor user
        When request PUT to /api/gms/hhaClinicalRecords
        Then will be permission denied







    Scenario: second cna instructor user requesting to fully update cnaRotations resources
        Given logged on as second cna instructor user
        When request PUT to /api/gms/cnaRotations
        Then server will respond with 404

    
    Scenario: second cna instructor user requesting to fully update cnaStudents resources
        Given logged on as second cna instructor user
        When request PUT to /api/gms/cnaStudents
        Then server will respond with 404

    
    Scenario: second cna instructor user requesting to fully update cnaTheoryRecords resources
        Given logged on as second cna instructor user
        When request PUT to /api/gms/cnaTheoryRecords
        Then server will respond with 404

    
    Scenario: second cna instructor user requesting to fully update cnaClinicalRecords resources
        Given logged on as second cna instructor user
        When request PUT to /api/gms/cnaClinicalRecords
        Then server will respond with 404

    
    Scenario: second hha instructor user requesting to fully update hhaRotations resources
        Given logged on as second hha instructor user
        When request PUT to /api/gms/hhaRotationS
        Then server will respond with 404

    
    Scenario: second hha instructor user requesting to fully update hhaStudents resources
        Given logged on as second hha instructor user
        When request PUT to /api/gms/hhaStudents
        Then server will respond with 404

    
    Scenario: second hha instructor user requesting to fully update hhaTheoryRecords resources
        Given logged on as second hha instructor user
        When request PUT to /api/gms/hhaTheoryRecords
        Then server will respond with 404

    
    Scenario: second hha instructor user requesting to fully update hhaClinicalRecords resources
        Given logged on as second hha instructor user
        When request PUT to /api/gms/hhaClinicalRecords
        Then server will respond with 404















    
    Scenario: superuser requesting to fully update ST2 cnaRotations resources
        Given logged on as superuser
        When request PUT to ST2 /api/gms/cnaRotations
        Then database will fully update the ST2 cna rotation record

    
    Scenario: superuser requesting to fully update ST2 cnaStudents resources
        Given logged on as superuser
        When request PUT to ST2 /api/gms/cnaStudents
        Then database will fully update the ST2 cna student record

    
    Scenario: superuser requesting to fully update ST2 cnaTheoryRecords resources
        Given logged on as superuser
        When request PUT to ST2 /api/gms/cnaTheoryRecords
        Then database will fully update the ST2 cna theory record

    
    Scenario: superuser requesting to fully update ST2 cnaClinicalRecords resources
        Given logged on as superuser
        When request PUT to ST2 /api/gms/cnaClinicalRecords
        Then database will fully update the ST2 cna clinical record

    
    Scenario: superuser requesting to fully update ST2 hhaRotations resources
        Given logged on as superuser
        When request PUT to ST2 /api/gms/hhaRotations
        Then database will fully update the ST2 hha rotation record


    
    Scenario: superuser requesting to fully update ST2 hhaStudents resources
        Given logged on as superuser
        When request PUT to ST2 /api/gms/hhaStudents
        Then database will fully update the ST2 hha student record
    

    
    Scenario: superuser requesting to fully update ST2 hhaTheoryRecords resources
        Given logged on as superuser
        When request PUT to ST2 /api/gms/hhaTheoryRecords
        Then database will fully update the ST2 hha theory record

    
    Scenario: superuser requesting to fully update ST2 hhaClinicalRecords resources
        Given logged on as superuser
        When request PUT to ST2 /api/gms/hhaClinicalRecords
        Then database will fully update the ST2 hha clinical record





    
    Scenario: admin instructor user requesting to fully update ST2 cnaRotations resources
        Given logged on as admin instructor user
        When request PUT to ST2 /api/gms/cnaRotations
        Then server will respond with 404

    
    Scenario: admin instructor user requesting to fully update ST2 cnaStudents resources
        Given logged on as admin instructor user
        When request PUT to ST2 /api/gms/cnaStudents
        Then server will respond with 404

    
    Scenario: admin instructor user requesting to fully update ST2 cnaTheoryRecords resources
        Given logged on as admin instructor user
        When request PUT to ST2 /api/gms/cnaTheoryRecords
        Then server will respond with 404

    
    Scenario: admin instructor user requesting to fully update ST2 cnaClinicalRecords resources
        Given logged on as admin instructor user
        When request PUT to ST2 /api/gms/cnaClinicalRecords
        Then server will respond with 404

    
    Scenario: admin instructor user requesting to fully update ST2 hhaRotations resources
        Given logged on as admin instructor user
        When request PUT to ST2 /api/gms/hhaRotations
        Then server will respond with 404

    
    Scenario: admin instructor user requesting to fully update ST2 hhaStudents resources
        Given logged on as admin instructor user
        When request PUT to ST2 /api/gms/hhaStudents
        Then server will respond with 404

    
    Scenario: admin instructor user requesting to fully update ST2 hhaTheoryRecords resources
        Given logged on as admin instructor user
        When request PUT to ST2 /api/gms/hhaTheoryRecords
        Then server will respond with 404

    
    Scenario: admin instructor user requesting to fully update ST2 hhaClinicalRecords resources
        Given logged on as admin instructor user
        When request PUT to ST2 /api/gms/hhaClinicalRecords
        Then server will respond with 404



    
    Scenario: staff cna instructor user requesting to fully update ST2 cnaRotations resources
        Given logged on as staff cna instructor user
        When request PUT to ST2 /api/gms/cnaRotations
        Then server will respond with 404

    
    Scenario: staff cna instructor user requesting to fully update ST2 cnaStudents resources
        Given logged on as staff cna instructor user
        When request PUT to ST2 /api/gms/cnaStudents
        Then server will respond with 404

    
    Scenario: staff cna instructor user requesting to fully update ST2 cnaTheoryRecords resources
        Given logged on as staff cna instructor user
        When request PUT to ST2 /api/gms/cnaTheoryRecords
        Then server will respond with 404

    
    Scenario: staff cna instructor user requesting to fully update ST2 cnaClinicalRecords resources
        Given logged on as staff cna instructor user
        When request PUT to ST2 /api/gms/cnaClinicalRecords
        Then server will respond with 404

    
    Scenario: staff hha instructor user requesting to fully update ST2 hhaRotations resources
        Given logged on as staff hha instructor user
        When request PUT to ST2 /api/gms/hhaRotations
        Then server will respond with 404

    
    Scenario: staff hha instructor user requesting to fully update ST2 hhaStudents resources
        Given logged on as staff hha instructor user
        When request PUT to ST2 /api/gms/hhaStudents
        Then server will respond with 404

    
    Scenario: staff hha instructor user requesting to fully update ST2 hhaTheoryRecords resources
        Given logged on as staff hha instructor user
        When request PUT to ST2 /api/gms/hhaTheoryRecords
        Then server will respond with 404

    
    Scenario: staff hha instructor user requesting to fully update ST2 hhaClinicalRecords resources
        Given logged on as staff hha instructor user
        When request PUT to ST2 /api/gms/hhaClinicalRecords
        Then server will respond with 404




    
    Scenario: cna instructor user requesting to fully update ST2 cnaRotations resources
        Given logged on as cna instructor user
        When request PUT to ST2 /api/gms/cnaRotations
        Then server will respond with 404

    
    Scenario: cna instructor user requesting to fully update ST2 cnaStudents resources
        Given logged on as cna instructor user
        When request PUT to ST2 /api/gms/cnaStudents
        Then server will respond with 404

    
    Scenario: cna instructor user requesting to fully update ST2 cnaTheoryRecords resources
        Given logged on as cna instructor user
        When request PUT to ST2 /api/gms/cnaTheoryRecords
        Then server will respond with 404

    
    Scenario: cna instructor user requesting to fully update ST2 cnaClinicalRecords resources
        Given logged on as cna instructor user
        When request PUT to ST2 /api/gms/cnaClinicalRecords
        Then server will respond with 404

    
    Scenario: hha instructor user requesting to fully update ST2 hhaRotations resources
        Given logged on as hha instructor user
        When request PUT to ST2 /api/gms/hhaRotations
        Then server will respond with 404

    
    Scenario: hha instructor user requesting to fully update ST2 hhaStudents resources
        Given logged on as hha instructor user
        When request PUT to ST2 /api/gms/hhaStudents
        Then server will respond with 404

    
    Scenario: hha instructor user requesting to fully update ST2 hhaTheoryRecords resources
        Given logged on as hha instructor user
        When request PUT to ST2 /api/gms/hhaTheoryRecords
        Then server will respond with 404

    
    Scenario: hha instructor user requesting to fully update ST2 hhaClinicalRecords resources
        Given logged on as hha instructor user
        When request PUT to ST2 /api/gms/hhaClinicalRecords
        Then server will respond with 404
