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


        




    
    Scenario: second cna instructor user requesting to partially update cnaRotations resources
        Given logged on as second cna instructor user
        When request PATCH to /api/gms/cnaRotations
        Then server will respond with 404

    
    Scenario: second cna instructor user requesting to partially update cnaStudents resources
        Given logged on as second cna instructor user
        When request PATCH to /api/gms/cnaStudents
        Then server will respond with 404

    
    Scenario: second cna instructor user requesting to partially update cnaTheoryRecords resources
        Given logged on as second cna instructor user
        When request PATCH to /api/gms/cnaTheoryRecords
        Then server will respond with 404

    
    Scenario: second cna instructor user requesting to partially update cnaClinicalRecords resources
        Given logged on as second cna instructor user
        When request PATCH to /api/gms/cnaClinicalRecords
        Then server will respond with 404

    
    Scenario: second hha instructor user requesting to partially update hhaRotations resources
        Given logged on as second hha instructor user
        When request PATCH to /api/gms/hhaRotationS
        Then server will respond with 404

    
    Scenario: second hha instructor user requesting to partially update hhaStudents resources
        Given logged on as second hha instructor user
        When request PATCH to /api/gms/hhaStudents
        Then server will respond with 404

    
    Scenario: second hha instructor user requesting to partially update hhaTheoryRecords resources
        Given logged on as second hha instructor user
        When request PATCH to /api/gms/hhaTheoryRecords
        Then server will respond with 404

    
    Scenario: second hha instructor user requesting to partially update hhaClinicalRecords resources
        Given logged on as second hha instructor user
        When request PATCH to /api/gms/hhaClinicalRecords
        Then server will respond with 404










    
    Scenario: superuser requesting to partially update ST2 cnaRotations resources
        Given logged on as superuser
        When request PATCH to ST2 /api/gms/cnaRotations/cnaRotation_uuid
        Then database will partially update the ST2 cna rotation record

    
    Scenario: superuser requesting to partially update ST2 cnaStudents resources
        Given logged on as superuser
        When request PATCH to ST2 /api/gms/cnaStudents/cnaStudent_uuid
        Then database will partially update the ST2 cna student record

    
    Scenario: superuser requesting to partially update ST2 cnaTheoryRecords resources
        Given logged on as superuser
        When request PATCH to ST2 /api/gms/cnaTheoryRecords/cnaTheoryRecord_uuid
        Then database will partially update the ST2 cna theory record

    
    Scenario: superuser requesting to partially update ST2 cnaClinicalRecords resources
        Given logged on as superuser
        When request PATCH to ST2 /api/gms/cnaClinicalRecords/cnaClinicalRecord_uuid
        Then database will partially update the ST2 cna clinical record

    
    Scenario: superuser requesting to partially update ST2 hhaRotations resources
        Given logged on as superuser
        When request PATCH to ST2 /api/gms/hhaRotations/hhaRotation_uuid
        Then database will partially update the ST2 hha rotation record

    
    Scenario: superuser requesting to partially update ST2 hhaStudents resources
        Given logged on as superuser
        When request PATCH to ST2 /api/gms/hhaStudents/hhaStudent_uuid
        Then database will partially update the ST2 hha student record
    

    
    Scenario: superuser requesting to partially update ST2 hhaTheoryRecords resources
        Given logged on as superuser
        When request PATCH to ST2 /api/gms/hhaTheoryRecords/hhaTheoryRecord_uuid
        Then database will partially update the ST2 hha theory record

    
    Scenario: superuser requesting to partially update ST2 hhaClinicalRecords resources
        Given logged on as superuser
        When request PATCH to ST2 /api/gms/hhaClinicalRecords/hhaClinicalRecord_uuid
        Then database will partially update the ST2 hha clinical record





    
    Scenario: admin instructor user requesting to partially update ST2 cnaRotations resources
        Given logged on as admin instructor user
        When request PATCH to ST2 /api/gms/cnaRotations/cnaRotation_uuid
        Then server will respond with 404

    
    Scenario: admin instructor user requesting to partially update ST2 cnaStudents resources
        Given logged on as admin instructor user
        When request PATCH to ST2 /api/gms/cnaStudents/cnaStudent_uuid
        Then server will respond with 404

    
    Scenario: admin instructor user requesting to partially update ST2 cnaTheoryRecords resources
        Given logged on as admin instructor user
        When request PATCH to ST2 /api/gms/cnaTheoryRecords/cnaTheoryRecord_uuid
        Then server will respond with 404

    
    Scenario: admin instructor user requesting to partially update ST2 cnaClinicalRecords resources
        Given logged on as admin instructor user
        When request PATCH to ST2 /api/gms/cnaClinicalRecords/cnaClinicalRecord_uuid
        Then server will respond with 404

    
    Scenario: admin instructor user requesting to partially update ST2 hhaRotations resources
        Given logged on as admin instructor user
        When request PATCH to ST2 /api/gms/hhaRotations/hhaRotation_uuid
        Then server will respond with 404

    
    Scenario: admin instructor user requesting to partially update ST2 hhaStudents resources
        Given logged on as admin instructor user
        When request PATCH to ST2 /api/gms/hhaStudents/hhaStudent_uuid
        Then server will respond with 404

    
    Scenario: admin instructor user requesting to partially update ST2 hhaTheoryRecords resources
        Given logged on as admin instructor user
        When request PATCH to ST2 /api/gms/hhaTheoryRecords/hhaTheoryRecord_uuid
        Then server will respond with 404

    
    Scenario: admin instructor user requesting to partially update ST2 hhaClinicalRecords resources
        Given logged on as admin instructor user
        When request PATCH to ST2 /api/gms/hhaClinicalRecords/hhaClinicalRecord_uuid
        Then server will respond with 404



    
    Scenario: staff cna instructor user requesting to partially update ST2 cnaRotations resources
        Given logged on as staff cna instructor user
        When request PATCH to ST2 /api/gms/cnaRotations/cnaRotation_uuid
        Then server will respond with 404

    
    Scenario: staff cna instructor user requesting to partially update ST2 cnaStudents resources
        Given logged on as staff cna instructor user
        When request PATCH to ST2 /api/gms/cnaStudents/cnaStudent_uuid
        Then server will respond with 404

    
    Scenario: staff cna instructor user requesting to partially update ST2 cnaTheoryRecords resources
        Given logged on as staff cna instructor user
        When request PATCH to ST2 /api/gms/cnaTheoryRecords/cnaTheoryRecord_uuid
        Then server will respond with 404

    
    Scenario: staff cna instructor user requesting to partially update ST2 cnaClinicalRecords resources
        Given logged on as staff cna instructor user
        When request PATCH to ST2 /api/gms/cnaClinicalRecords/cnaClinicalRecord_uuid
        Then server will respond with 404

    
    Scenario: staff hha instructor user requesting to partially update ST2 hhaRotations resources
        Given logged on as staff hha instructor user
        When request PATCH to ST2 /api/gms/hhaRotations/hhaRotation_uuid
        Then server will respond with 404

    
    Scenario: staff hha instructor user requesting to partially update ST2 hhaStudents resources
        Given logged on as staff hha instructor user
        When request PATCH to ST2 /api/gms/hhaStudents/hhaStudent_uuid
        Then server will respond with 404

    
    Scenario: staff hha instructor user requesting to partially update ST2 hhaTheoryRecords resources
        Given logged on as staff hha instructor user
        When request PATCH to ST2 /api/gms/hhaTheoryRecords/hhaTheoryRecord_uuid
        Then server will respond with 404

    
    Scenario: staff hha instructor user requesting to partially update ST2 hhaClinicalRecords resources
        Given logged on as staff hha instructor user
        When request PATCH to ST2 /api/gms/hhaClinicalRecords/hhaClinicalRecord_uuid
        Then server will respond with 404




    
    Scenario: cna instructor user requesting to partially update ST2 cnaRotations resources
        Given logged on as cna instructor user
        When request PATCH to ST2 /api/gms/cnaRotations/cnaRotation_uuid
        Then server will respond with 404

    
    Scenario: cna instructor user requesting to partially update ST2 cnaStudents resources
        Given logged on as cna instructor user
        When request PATCH to ST2 /api/gms/cnaStudents/cnaStudent_uuid
        Then server will respond with 404

    
    Scenario: cna instructor user requesting to partially update ST2 cnaTheoryRecords resources
        Given logged on as cna instructor user
        When request PATCH to ST2 /api/gms/cnaTheoryRecords/cnaTheoryRecord_uuid
        Then server will respond with 404

    
    Scenario: cna instructor user requesting to partially update ST2 cnaClinicalRecords resources
        Given logged on as cna instructor user
        When request PATCH to ST2 /api/gms/cnaClinicalRecords/cnaClinicalRecord_uuid
        Then server will respond with 404

    
    Scenario: hha instructor user requesting to partially update ST2 hhaRotations resources
        Given logged on as hha instructor user
        When request PATCH to ST2 /api/gms/hhaRotations/hhaRotation_uuid
        Then server will respond with 404

    
    Scenario: hha instructor user requesting to partially update ST2 hhaStudents resources
        Given logged on as hha instructor user
        When request PATCH to ST2 /api/gms/hhaStudents/hhaStudent_uuid
        Then server will respond with 404

    
    Scenario: hha instructor user requesting to partially update ST2 hhaTheoryRecords resources
        Given logged on as hha instructor user
        When request PATCH to ST2 /api/gms/hhaTheoryRecords/hhaTheoryRecord_uuid
        Then server will respond with 404

    
    Scenario: hha instructor user requesting to partially update ST2 hhaClinicalRecords resources
        Given logged on as hha instructor user
        When request PATCH to ST2 /api/gms/hhaClinicalRecords/hhaClinicalRecord_uuid
        Then server will respond with 404





    @current
    Scenario: superuser requesting to partially update cnaRotations resources with bad email
        Given logged on as superuser
        When request PATCH to /api/gms/cnaRotations with bad email
        Then bad request since the email added does not belong to an active user

    @current
    Scenario: superuser requesting to partially update hhaRotations resources with bad email
        Given logged on as superuser
        When request PATCH to /api/gms/hhaRotations with bad email
        Then bad request since the email added does not belong to an active user
    
    @current
    Scenario: admin instructor user requesting to partially update cnaRotations resources with bad email
        Given logged on as admin instructor user
        When request PATCH to /api/gms/cnaRotations with bad email
        Then bad request since the email added does not belong to an active user

    @current
    Scenario: admin instructor user requesting to partially update hhaRotations resources with bad email
        Given logged on as admin instructor user
        When request PATCH to /api/gms/hhaRotations with bad email
        Then bad request since the email added does not belong to an active user

    @current
    Scenario: staff cna instructor user requesting to partially update cnaRotations resources with bad email
        Given logged on as staff cna instructor user
        When request PATCH to /api/gms/cnaRotations with bad email
        Then bad request since the email added does not belong to an active user

    @current
    Scenario: staff hha instructor user requesting to partially update hhaRotations resources with bad email
        Given logged on as staff hha instructor user
        When request PATCH to /api/gms/hhaRotations with bad email
        Then bad request since the email added does not belong to an active user

    @current
    Scenario: cna instructor user requesting to partially update cnaRotations resources with bad email
        Given logged on as cna instructor user
        When request PATCH to /api/gms/cnaRotations with bad email
        Then bad request since the email added does not belong to an active user

    @current
    Scenario: hha instructor user requesting to partially update hhaRotations resources with bad email
        Given logged on as hha instructor user
        When request PATCH to /api/gms/hhaRotations with bad email
        Then bad request since the email added does not belong to an active user