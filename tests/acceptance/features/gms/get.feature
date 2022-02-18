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






    
    Scenario: second cna instructor user requesting to read cnaRotations resources
        Given logged on as second cna instructor user
        When request GET to /api/gms/cnaRotations/cnaRotation_uuid
        Then server will respond with 404

    
    Scenario: second cna instructor user requesting to read cnaStudents resources
        Given logged on as second cna instructor user
        When request GET to /api/gms/cnaStudents/cnaStudent_uuid
        Then server will respond with 404

    
    Scenario: second cna instructor user requesting to read cnaTheoryRecords resources
        Given logged on as second cna instructor user
        When request GET to /api/gms/cnaTheoryRecords/cnaTheoryRecord_uuid
        Then server will respond with 404

    
    Scenario: second cna instructor user requesting to read cnaClinicalRecords resources
        Given logged on as second cna instructor user
        When request GET to /api/gms/cnaClinicalRecords/cnaClinicalRecord_uuid
        Then server will respond with 404

    
    Scenario: second hha instructor user requesting to read hhaRotations resources
        Given logged on as second hha instructor user
        When request GET to /api/gms/hhaRotations/hhaRotation_uuid
        Then server will respond with 404

    
    Scenario: second hha instructor user requesting to read hhaStudents resources
        Given logged on as second hha instructor user
        When request GET to /api/gms/hhaStudents/hhaStudent_uuid
        Then server will respond with 404

    
    Scenario: second hha instructor user requesting to read hhaTheoryRecords resources
        Given logged on as second hha instructor user
        When request GET to /api/gms/hhaTheoryRecords/hhaTheoryRecord_uuid
        Then server will respond with 404

    
    Scenario: second hha instructor user requesting to read hhaClinicalRecords resources
        Given logged on as second hha instructor user
        When request GET to /api/gms/hhaClinicalRecords/hhaClinicalRecord_uuid
        Then server will respond with 404
















    @current
    Scenario: superuser requesting to read ST2 cnaRotations resources
        Given logged on as superuser
        When request GET to ST2 /api/gms/cnaRotations/cnaRotation_uuid
        Then will receive JSON response of data

    @current
    Scenario: superuser requesting to read ST2 cnaStudents resources
        Given logged on as superuser
        When request GET to ST2 /api/gms/cnaStudents/cnaStudent_uuid
        Then will receive JSON response of data

    @current
    Scenario: superuser requesting to read ST2 cnaTheoryRecords resources
        Given logged on as superuser
        When request GET to ST2 /api/gms/cnaTheoryRecords/cnaTheoryRecord_uuid
        Then will receive JSON response of data

    @current
    Scenario: superuser requesting to read ST2 cnaClinicalRecords resources
        Given logged on as superuser
        When request GET to ST2 /api/gms/cnaClinicalRecords/cnaClinicalRecord_uuid
        Then will receive JSON response of data

    @current
    Scenario: superuser requesting to read ST2 hhaRotations resources
        Given logged on as superuser
        When request GET to ST2 /api/gms/hhaRotations/hhaRotation_uuid
        Then will receive JSON response of data

    @current
    Scenario: superuser requesting to read ST2 hhaStudents resources
        Given logged on as superuser
        When request GET to ST2 /api/gms/hhaStudents/hhaStudent_uuid
        Then will receive JSON response of data
    
    @current
    Scenario: superuser requesting to read ST2 hhaTheoryRecords resources
        Given logged on as superuser
        When request GET to ST2 /api/gms/hhaTheoryRecords/hhaTheoryRecord_uuid
        Then will receive JSON response of data

    @current
    Scenario: superuser requesting to read ST2 hhaClinicalRecords resources
        Given logged on as superuser
        When request GET to ST2 /api/gms/hhaClinicalRecords/hhaClinicalRecord_uuid
        Then will receive JSON response of data





    @current
    Scenario: admin instructor user requesting to read ST2 cnaRotations resources
        Given logged on as admin instructor user
        When request GET to ST2 /api/gms/cnaRotations/cnaRotation_uuid
        Then server will respond with 404

    @current
    Scenario: admin instructor user requesting to read ST2 cnaStudents resources
        Given logged on as admin instructor user
        When request GET to ST2 /api/gms/cnaStudents/cnaStudent_uuid
        Then server will respond with 404

    @current
    Scenario: admin instructor user requesting to read ST2 cnaTheoryRecords resources
        Given logged on as admin instructor user
        When request GET to ST2 /api/gms/cnaTheoryRecords/cnaTheoryRecord_uuid
        Then server will respond with 404

    @current
    Scenario: admin instructor user requesting to read ST2 cnaClinicalRecords resources
        Given logged on as admin instructor user
        When request GET to ST2 /api/gms/cnaClinicalRecords/cnaClinicalRecord_uuid
        Then server will respond with 404

    @current
    Scenario: admin instructor user requesting to read ST2 hhaRotations resources
        Given logged on as admin instructor user
        When request GET to ST2 /api/gms/hhaRotations/hhaRotation_uuid
        Then server will respond with 404

    @current
    Scenario: admin instructor user requesting to read ST2 hhaStudents resources
        Given logged on as admin instructor user
        When request GET to ST2 /api/gms/hhaStudents/hhaStudent_uuid
        Then server will respond with 404

    @current
    Scenario: admin instructor user requesting to read ST2 hhaTheoryRecords resources
        Given logged on as admin instructor user
        When request GET to ST2 /api/gms/hhaTheoryRecords/hhaTheoryRecord_uuid
        Then server will respond with 404

    @current
    Scenario: admin instructor user requesting to read ST2 hhaClinicalRecords resources
        Given logged on as admin instructor user
        When request GET to ST2 /api/gms/hhaClinicalRecords/hhaClinicalRecord_uuid
        Then server will respond with 404



    @current
    Scenario: staff cna instructor user requesting to read ST2 cnaRotations resources
        Given logged on as staff cna instructor user
        When request GET to ST2 /api/gms/cnaRotations/cnaRotation_uuid
        Then server will respond with 404

    @current
    Scenario: staff cna instructor user requesting to read ST2 cnaStudents resources
        Given logged on as staff cna instructor user
        When request GET to ST2 /api/gms/cnaStudents/cnaStudent_uuid
        Then server will respond with 404

    @current
    Scenario: staff cna instructor user requesting to read ST2 cnaTheoryRecords resources
        Given logged on as staff cna instructor user
        When request GET to ST2 /api/gms/cnaTheoryRecords/cnaTheoryRecord_uuid
        Then server will respond with 404

    @current
    Scenario: staff cna instructor user requesting to read ST2 cnaClinicalRecords resources
        Given logged on as staff cna instructor user
        When request GET to ST2 /api/gms/cnaClinicalRecords/cnaClinicalRecord_uuid
        Then server will respond with 404

    @current
    Scenario: staff hha instructor user requesting to read ST2 hhaRotations resources
        Given logged on as staff hha instructor user
        When request GET to ST2 /api/gms/hhaRotations/hhaRotation_uuid
        Then server will respond with 404

    @current
    Scenario: staff hha instructor user requesting to read ST2 hhaStudents resources
        Given logged on as staff hha instructor user
        When request GET to ST2 /api/gms/hhaStudents/hhaStudent_uuid
        Then server will respond with 404

    @current
    Scenario: staff hha instructor user requesting to read ST2 hhaTheoryRecords resources
        Given logged on as staff hha instructor user
        When request GET to ST2 /api/gms/hhaTheoryRecords/hhaTheoryRecord_uuid
        Then server will respond with 404

    @current
    Scenario: staff hha instructor user requesting to read ST2 hhaClinicalRecords resources
        Given logged on as staff hha instructor user
        When request GET to ST2 /api/gms/hhaClinicalRecords/hhaClinicalRecord_uuid
        Then server will respond with 404




    @current
    Scenario: cna instructor user requesting to read ST2 cnaRotations resources
        Given logged on as cna instructor user
        When request GET to ST2 /api/gms/cnaRotations/cnaRotation_uuid
        Then server will respond with 404

    @current
    Scenario: cna instructor user requesting to read ST2 cnaStudents resources
        Given logged on as cna instructor user
        When request GET to ST2 /api/gms/cnaStudents/cnaStudent_uuid
        Then server will respond with 404

    @current
    Scenario: cna instructor user requesting to read ST2 cnaTheoryRecords resources
        Given logged on as cna instructor user
        When request GET to ST2 /api/gms/cnaTheoryRecords/cnaTheoryRecord_uuid
        Then server will respond with 404

    @current
    Scenario: cna instructor user requesting to read ST2 cnaClinicalRecords resources
        Given logged on as cna instructor user
        When request GET to ST2 /api/gms/cnaClinicalRecords/cnaClinicalRecord_uuid
        Then server will respond with 404

    @current
    Scenario: hha instructor user requesting to read ST2 hhaRotations resources
        Given logged on as hha instructor user
        When request GET to ST2 /api/gms/hhaRotations/hhaRotation_uuid
        Then server will respond with 404

    @current
    Scenario: hha instructor user requesting to read ST2 hhaStudents resources
        Given logged on as hha instructor user
        When request GET to ST2 /api/gms/hhaStudents/hhaStudent_uuid
        Then server will respond with 404

    @current
    Scenario: hha instructor user requesting to read ST2 hhaTheoryRecords resources
        Given logged on as hha instructor user
        When request GET to ST2 /api/gms/hhaTheoryRecords/hhaTheoryRecord_uuid
        Then server will respond with 404

    @current
    Scenario: hha instructor user requesting to read ST2 hhaClinicalRecords resources
        Given logged on as hha instructor user
        When request GET to ST2 /api/gms/hhaClinicalRecords/hhaClinicalRecord_uuid
        Then server will respond with 404
