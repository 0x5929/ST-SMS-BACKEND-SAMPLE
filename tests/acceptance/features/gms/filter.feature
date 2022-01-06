Feature: Grading Management filter

    All user can filter all gms model objects that they have access to based on attributes via GET parameters

    @init
    Scenario: requesting to auth login
        Given no initial logon
        When request GET to /auth/login/
        Then server will respond with 405
    # only super users can see records from other school
    # all other type of user will fail to GET but users above and below can!
    # cna/hhainstructoruser2 will be of ST2, they can also see ST2, but no STI
    # instructoruser will have both CNA and HHA will be able to see both all CNA and HHA records in the same school
    Scenario: superuser requesting to filter gms/cnaRotations resource by STI start_date
        Given logged on as superuser
        When request GET to /api/gms/cnaRotations with filters by STI start_date
        Then the specific STI cnaRotations data will be returned as JSON response


    Scenario: superuser requesting to filter gms/cnaRotations resource by STI end_date
        Given logged on as superuser
        When request GET to /api/gms/cnaRotations with filters by STI end_date
        Then the specific STI cnaRotations data will be returned as JSON response


    Scenario: superuser requesting to filter gms/cnaRotations resource by STI rotation_num
        Given logged on as superuser
        When request GET to /api/gms/cnaRotations with filters by STI rotation_num
        Then the specific STI cnaRotations data will be returned as JSON response

    Scenario: superuser requesting to filter second instructor gms/cnaRotations resource by STI start_date
        Given logged on as superuser
        When request GET to second instructor /api/gms/cnaRotations with filters by STI start_date
        Then the specific STI second cnaRotations data will be returned as JSON response

    Scenario: superuser requesting to filter second instructor gms/cnaRotations resource by STI end_date
        Given logged on as superuser
        When request GET to second instructor /api/gms/cnaRotations with filters by STI end_date
        Then the specific STI second cnaRotations data will be returned as JSON response

    Scenario: superuser requesting to filter second instructor gms/cnaRotations resource by STI rotation_num
        Given logged on as superuser
        When request GET to second instructor /api/gms/cnaRotations with filters by STI rotation_num
        Then the specific STI second cnaRotations data will be returned as JSON response

    Scenario: superuser requesting to filter gms/hhaRotations resource by STI start_date
        Given logged on as superuser
        When request GET to /api/gms/hhaRotations with filters by STI start_date
        Then the specific STI hhaRotations data will be returned as JSON response


    Scenario: superuser requesting to filter gms/hhaRotations resource by STI end_date
        Given logged on as superuser
        When request GET to /api/gms/hhaRotations with filters by STI end_date
        Then the specific STI hhaRotations data will be returned as JSON response


    Scenario: superuser requesting to filter gms/hhaRotations resource by STI rotation_num
        Given logged on as superuser
        When request GET to /api/gms/hhaRotations with filters by STI rotation_num
        Then the specific STI hhaRotations data will be returned as JSON response

    Scenario: superuser requesting to filter second instructor gms/hhaRotations resource by STI start_date
        Given logged on as superuser
        When request GET to second instructor /api/gms/hhaRotations with filters by STI start_date
        Then the specific STI second hhaRotations data will be returned as JSON response

    Scenario: superuser requesting to filter second instructor gms/hhaRotations resource by STI end_date
        Given logged on as superuser
        When request GET to second instructor /api/gms/hhaRotations with filters by STI end_date
        Then the specific STI second hhaRotations data will be returned as JSON response

    Scenario: superuser requesting to filter second instructor gms/hhaRotations resource by STI rotation_num
        Given logged on as superuser
        When request GET to second instructor /api/gms/hhaRotations with filters by STI rotation_num
        Then the specific STI second hhaRotations data will be returned as JSON response




    Scenario: superuser requesting to filter gms/cnaRotations resource by ST2 start_date
        Given logged on as superuser
        When request GET to /api/gms/cnaRotations with filters by ST2 start_date
        Then the specific ST2 cnaRotations data will be returned as JSON response


    Scenario: superuser requesting to filter gms/cnaRotations resource by ST2 end_date
        Given logged on as superuser
        When request GET to /api/gms/cnaRotations with filters by ST2 end_date
        Then the specific ST2 cnaRotations data will be returned as JSON response


    Scenario: superuser requesting to filter gms/cnaRotations resource by ST2 rotation_num
        Given logged on as superuser
        When request GET to /api/gms/cnaRotations with filters by ST2 rotation_num
        Then the specific ST2 cnaRotations data will be returned as JSON response


    Scenario: superuser requesting to filter gms/hhaRotations resource by ST2 start_date
        Given logged on as superuser
        When request GET to /api/gms/hhaRotations with filters by ST2 start_date
        Then the specific ST2 hhaRotations data will be returned as JSON response


    Scenario: superuser requesting to filter gms/hhaRotations resource by ST2 end_date
        Given logged on as superuser
        When request GET to /api/gms/hhaRotations with filters by ST2 end_date
        Then the specific ST2 hhaRotations data will be returned as JSON response


    Scenario: superuser requesting to filter gms/hhaRotations resource by ST2 rotation_num
        Given logged on as superuser
        When request GET to /api/gms/hhaRotations with filters by ST2 rotation_num
        Then the specific ST2 hhaRotations data will be returned as JSON response
    # remember also a scenario where filter for data for another school? should not appear unless your superuser




    Scenario: admin instructor user requesting to filter gms/cnaRotations resource by STI start_date
        Given logged on as admin instructor user
        When request GET to /api/gms/cnaRotations with filters by STI start_date
        Then the specific STI cnaRotations data will be returned as JSON response


    Scenario: admin instructor user requesting to filter gms/cnaRotations resource by STI end_date
        Given logged on as admin instructor user
        When request GET to /api/gms/cnaRotations with filters by STI end_date
        Then the specific STI cnaRotations data will be returned as JSON response


    Scenario: admin instructor user requesting to filter gms/cnaRotations resource by STI rotation_num
        Given logged on as admin instructor user
        When request GET to /api/gms/cnaRotations with filters by STI rotation_num
        Then the specific STI cnaRotations data will be returned as JSON response

    Scenario: admin instructor user requesting to filter second instructor gms/cnaRotations resource by STI start_date
        Given logged on as admin instructor user
        When request GET to second instructor /api/gms/cnaRotations with filters by STI start_date
        Then the specific STI second cnaRotations data will be returned as JSON response

    Scenario: admin instructor user requesting to filter second instructor gms/cnaRotations resource by STI end_date
        Given logged on as admin instructor user
        When request GET to second instructor /api/gms/cnaRotations with filters by STI end_date
        Then the specific STI second cnaRotations data will be returned as JSON response

    Scenario: admin instructor user requesting to filter second instructor gms/cnaRotations resource by STI rotation_num
        Given logged on as admin instructor user
        When request GET to second instructor /api/gms/cnaRotations with filters by STI rotation_num
        Then the specific STI second cnaRotations data will be returned as JSON response

    Scenario: admin instructor user requesting to filter gms/hhaRotations resource by STI start_date
        Given logged on as admin instructor user
        When request GET to /api/gms/hhaRotations with filters by STI start_date
        Then the specific STI hhaRotations data will be returned as JSON response


    Scenario: admin instructor user requesting to filter gms/hhaRotations resource by STI end_date
        Given logged on as admin instructor user
        When request GET to /api/gms/hhaRotations with filters by STI end_date
        Then the specific STI hhaRotations data will be returned as JSON response


    Scenario: admin instructor user requesting to filter gms/hhaRotations resource by STI rotation_num
        Given logged on as admin instructor user
        When request GET to /api/gms/hhaRotations with filters by STI rotation_num
        Then the specific STI hhaRotations data will be returned as JSON response

    Scenario: admin instructor user requesting to filter second instructor gms/hhaRotations resource by STI start_date
        Given logged on as admin instructor user
        When request GET to second instructor /api/gms/hhaRotations with filters by STI start_date
        Then the specific STI second hhaRotations data will be returned as JSON response

    Scenario: admin instructor user requesting to filter second instructor gms/hhaRotations resource by STI end_date
        Given logged on as admin instructor user
        When request GET to second instructor /api/gms/hhaRotations with filters by STI end_date
        Then the specific STI second hhaRotations data will be returned as JSON response

    Scenario: admin instructor user requesting to filter second instructor gms/hhaRotations resource by STI rotation_num
        Given logged on as admin instructor user
        When request GET to second instructor /api/gms/hhaRotations with filters by STI rotation_num
        Then the specific STI second hhaRotations data will be returned as JSON response


    Scenario: STI admin instructor user requesting to filter gms/cnaRotations resource by ST2 start_date
        Given logged on as admin instructor user
        When request GET to /api/gms/cnaRotations with filters by ST2 start_date
        Then no data will be returned as JSON response


    Scenario: STI admin instructor user requesting to filter gms/cnaRotations resource by ST2 end_date
        Given logged on as admin instructor user
        When request GET to /api/gms/cnaRotations with filters by ST2 end_date
        Then no data will be returned as JSON response


    Scenario: STI admin instructor user requesting to filter gms/cnaRotations resource by ST2 rotation_num
        Given logged on as admin instructor user
        When request GET to /api/gms/cnaRotations with filters by ST2 rotation_num
        Then no data will be returned as JSON response


    Scenario: STI admin instructor user requesting to filter gms/hhaRotations resource by ST2 start_date
        Given logged on as admin instructor user
        When request GET to /api/gms/hhaRotations with filters by ST2 start_date
        Then no data will be returned as JSON response


    Scenario: STI admin instructor user requesting to filter gms/hhaRotations resource by ST2 end_date
        Given logged on as admin instructor user
        When request GET to /api/gms/hhaRotations with filters by ST2 end_date
        Then no data will be returned as JSON response


    Scenario: STI admin instructor user requesting to filter gms/hhaRotations resource by ST2 rotation_num
        Given logged on as admin instructor user
        When request GET to /api/gms/hhaRotations with filters by ST2 rotation_num
        Then no data will be returned as JSON response




    Scenario: staff cna instructor user requesting to filter gms/cnaRotations resource by STI start_date
        Given logged on as staff cna instructor user
        When request GET to /api/gms/cnaRotations with filters by STI start_date
        Then the specific STI cnaRotations data will be returned as JSON response


    Scenario: staff cna instructor user requesting to filter gms/cnaRotations resource by STI end_date
        Given logged on as staff cna instructor user
        When request GET to /api/gms/cnaRotations with filters by STI end_date
        Then the specific STI cnaRotations data will be returned as JSON response


    Scenario: staff cna instructor user requesting to filter gms/cnaRotations resource by STI rotation_num
        Given logged on as staff cna instructor user
        When request GET to /api/gms/cnaRotations with filters by STI rotation_num
        Then the specific STI cnaRotations data will be returned as JSON response

    Scenario: staff cna instructor user requesting to filter second instructor gms/cnaRotations resource by STI start_date
        Given logged on as staff cna instructor user
        When request GET to second instructor /api/gms/cnaRotations with filters by STI start_date
        Then the specific STI second cnaRotations data will be returned as JSON response

    Scenario: staff cna instructor user requesting to filter second instructor gms/cnaRotations resource by STI end_date
        Given logged on as staff cna instructor user
        When request GET to second instructor /api/gms/cnaRotations with filters by STI end_date
        Then the specific STI second cnaRotations data will be returned as JSON response

    Scenario: staff cna instructor user requesting to filter second instructor gms/cnaRotations resource by STI rotation_num
        Given logged on as staff cna instructor user
        When request GET to second instructor /api/gms/cnaRotations with filters by STI rotation_num
        Then the specific STI second cnaRotations data will be returned as JSON response

    Scenario: staff cna instructor user requesting to filter gms/hhaRotations resource by STI start_date
        Given logged on as staff cna instructor user
        When request GET to /api/gms/hhaRotations with filters by STI start_date
        Then will be permission denied


    Scenario: staff cna instructor user requesting to filter gms/hhaRotations resource by STI end_date
        Given logged on as staff cna instructor user
        When request GET to /api/gms/hhaRotations with filters by STI end_date
        Then will be permission denied


    Scenario: staff cna instructor user requesting to filter gms/hhaRotations resource by STI rotation_num
        Given logged on as staff cna instructor user
        When request GET to /api/gms/hhaRotations with filters by STI rotation_num
        Then will be permission denied

    Scenario: staff cna instructor user requesting to filter second instructor gms/hhaRotations resource by STI start_date
        Given logged on as staff cna instructor user
        When request GET to second instructor /api/gms/hhaRotations with filters by STI start_date
        Then will be permission denied

    Scenario: staff cna instructor user requesting to filter second instructor gms/hhaRotations resource by STI end_date
        Given logged on as staff cna instructor user
        When request GET to second instructor /api/gms/hhaRotations with filters by STI end_date
        Then will be permission denied

    Scenario: staff cna instructor user requesting to filter second instructor gms/hhaRotations resource by STI rotation_num
        Given logged on as staff cna instructor user
        When request GET to second instructor /api/gms/hhaRotations with filters by STI rotation_num
        Then will be permission denied



    Scenario: STI staff cna instructor user requesting to filter gms/cnaRotations resource by ST2 start_date
        Given logged on as staff cna instructor user
        When request GET to /api/gms/cnaRotations with filters by ST2 start_date
        Then no data will be returned as JSON response


    Scenario: STI staff cna instructor user requesting to filter gms/cnaRotations resource by ST2 end_date
        Given logged on as staff cna instructor user
        When request GET to /api/gms/cnaRotations with filters by ST2 end_date
        Then no data will be returned as JSON response


    Scenario: STI staff cna instructor user requesting to filter gms/cnaRotations resource by ST2 rotation_num
        Given logged on as staff cna instructor user
        When request GET to /api/gms/cnaRotations with filters by ST2 rotation_num
        Then no data will be returned as JSON response


    Scenario: STI staff cna instructor user requesting to filter gms/hhaRotations resource by ST2 start_date
        Given logged on as staff cna instructor user
        When request GET to /api/gms/hhaRotations with filters by ST2 start_date
        Then will be permission denied


    Scenario: STI staff cna instructor user requesting to filter gms/hhaRotations resource by ST2 end_date
        Given logged on as staff cna instructor user
        When request GET to /api/gms/hhaRotations with filters by ST2 end_date
        Then will be permission denied


    Scenario: STI staff cna instructor user requesting to filter gms/hhaRotations resource by ST2 rotation_num
        Given logged on as staff cna instructor user
        When request GET to /api/gms/hhaRotations with filters by ST2 rotation_num
        Then will be permission denied













    Scenario: staff hha instructor user requesting to filter gms/cnaRotations resource by STI start_date
        Given logged on as staff hha instructor user
        When request GET to /api/gms/cnaRotations with filters by STI start_date
        Then will be permission denied


    Scenario: staff hha instructor user requesting to filter gms/cnaRotations resource by STI end_date
        Given logged on as staff hha instructor user
        When request GET to /api/gms/cnaRotations with filters by STI end_date
        Then will be permission denied


    Scenario: staff hha instructor user requesting to filter gms/cnaRotations resource by STI rotation_num
        Given logged on as staff hha instructor user
        When request GET to /api/gms/cnaRotations with filters by STI rotation_num
        Then will be permission denied

    Scenario: staff hha instructor user requesting to filter second instructor gms/cnaRotations resource by STI start_date
        Given logged on as staff hha instructor user
        When request GET to second instructor /api/gms/cnaRotations with filters by STI start_date
        Then will be permission denied

    Scenario: staff hha instructor user requesting to filter second instructor gms/cnaRotations resource by STI end_date
        Given logged on as staff hha instructor user
        When request GET to second instructor /api/gms/cnaRotations with filters by STI end_date
        Then will be permission denied

    Scenario: staff hha instructor user requesting to filter second instructor gms/cnaRotations resource by STI rotation_num
        Given logged on as staff hha instructor user
        When request GET to second instructor /api/gms/cnaRotations with filters by STI rotation_num
        Then will be permission denied

    Scenario: staff hha instructor user requesting to filter gms/hhaRotations resource by STI start_date
        Given logged on as staff hha instructor user
        When request GET to /api/gms/hhaRotations with filters by STI start_date
        Then the specific STI hhaRotations data will be returned as JSON response


    Scenario: staff hha instructor user requesting to filter gms/hhaRotations resource by STI end_date
        Given logged on as staff hha instructor user
        When request GET to /api/gms/hhaRotations with filters by STI end_date
        Then the specific STI hhaRotations data will be returned as JSON response


    Scenario: staff hha instructor user requesting to filter gms/hhaRotations resource by STI rotation_num
        Given logged on as staff hha instructor user
        When request GET to /api/gms/hhaRotations with filters by STI rotation_num
        Then the specific STI hhaRotations data will be returned as JSON response

    Scenario: staff hha instructor user requesting to filter second instructor gms/hhaRotations resource by STI start_date
        Given logged on as staff hha instructor user
        When request GET to second instructor /api/gms/hhaRotations with filters by STI start_date
        Then the specific STI second hhaRotations data will be returned as JSON response

    Scenario: staff hha instructor user requesting to filter second instructor gms/hhaRotations resource by STI end_date
        Given logged on as staff hha instructor user
        When request GET to second instructor /api/gms/hhaRotations with filters by STI end_date
        Then the specific STI second hhaRotations data will be returned as JSON response

    Scenario: staff hha instructor user requesting to filter second instructor gms/hhaRotations resource by STI rotation_num
        Given logged on as staff hha instructor user
        When request GET to second instructor /api/gms/hhaRotations with filters by STI rotation_num
        Then the specific STI second hhaRotations data will be returned as JSON response



    Scenario: STI staff hha instructor user requesting to filter gms/cnaRotations resource by ST2 start_date
        Given logged on as staff hha instructor user
        When request GET to /api/gms/cnaRotations with filters by ST2 start_date
        Then will be permission denied


    Scenario: STI staff hha instructor user requesting to filter gms/cnaRotations resource by ST2 end_date
        Given logged on as staff hha instructor user
        When request GET to /api/gms/cnaRotations with filters by ST2 end_date
        Then will be permission denied


    Scenario: STI staff hha instructor user requesting to filter gms/cnaRotations resource by ST2 rotation_num
        Given logged on as staff hha instructor user
        When request GET to /api/gms/cnaRotations with filters by ST2 rotation_num
        Then will be permission denied


    Scenario: STI staff hha instructor user requesting to filter gms/hhaRotations resource by ST2 start_date
        Given logged on as staff hha instructor user
        When request GET to /api/gms/hhaRotations with filters by ST2 start_date
        Then no data will be returned as JSON response


    Scenario: STI staff hha instructor user requesting to filter gms/hhaRotations resource by ST2 end_date
        Given logged on as staff hha instructor user
        When request GET to /api/gms/hhaRotations with filters by ST2 end_date
        Then no data will be returned as JSON response


    Scenario: STI staff hha instructor user requesting to filter gms/hhaRotations resource by ST2 rotation_num
        Given logged on as staff hha instructor user
        When request GET to /api/gms/hhaRotations with filters by ST2 rotation_num
        Then no data will be returned as JSON response












    Scenario: cna instructor user requesting to filter gms/cnaRotations resource by STI start_date
        Given logged on as cna instructor user
        When request GET to /api/gms/cnaRotations with filters by STI start_date
        Then the specific STI cnaRotations data will be returned as JSON response


    Scenario: cna instructor user requesting to filter gms/cnaRotations resource by STI end_date
        Given logged on as cna instructor user
        When request GET to /api/gms/cnaRotations with filters by STI end_date
        Then the specific STI cnaRotations data will be returned as JSON response


    Scenario: cna instructor user requesting to filter gms/cnaRotations resource by STI rotation_num
        Given logged on as cna instructor user
        When request GET to /api/gms/cnaRotations with filters by STI rotation_num
        Then the specific STI cnaRotations data will be returned as JSON response

    Scenario: cna instructor user requesting to filter second instructor gms/cnaRotations resource by STI start_date
        Given logged on as cna instructor user
        When request GET to second instructor /api/gms/cnaRotations with filters by STI start_date
        Then no data will be returned as JSON response

    Scenario: cna instructor user requesting to filter second instructor gms/cnaRotations resource by STI end_date
        Given logged on as cna instructor user
        When request GET to second instructor /api/gms/cnaRotations with filters by STI end_date
        Then no data will be returned as JSON response

    Scenario: cna instructor user requesting to filter second instructor gms/cnaRotations resource by STI rotation_num
        Given logged on as cna instructor user
        When request GET to second instructor /api/gms/cnaRotations with filters by STI rotation_num
        Then no data will be returned as JSON response

    Scenario: cna instructor user requesting to filter gms/hhaRotations resource by STI start_date
        Given logged on as cna instructor user
        When request GET to /api/gms/hhaRotations with filters by STI start_date
        Then will be permission denied


    Scenario: cna instructor user requesting to filter gms/hhaRotations resource by STI end_date
        Given logged on as cna instructor user
        When request GET to /api/gms/hhaRotations with filters by STI end_date
        Then will be permission denied


    Scenario: cna instructor user requesting to filter gms/hhaRotations resource by STI rotation_num
        Given logged on as cna instructor user
        When request GET to /api/gms/hhaRotations with filters by STI rotation_num
        Then will be permission denied

    Scenario: cna instructor user requesting to filter second instructor gms/hhaRotations resource by STI start_date
        Given logged on as cna instructor user
        When request GET to second instructor /api/gms/hhaRotations with filters by STI start_date
        Then will be permission denied

    Scenario: cna instructor user requesting to filter second instructor gms/hhaRotations resource by STI end_date
        Given logged on as cna instructor user
        When request GET to second instructor /api/gms/hhaRotations with filters by STI end_date
        Then will be permission denied

    Scenario: cna instructor user requesting to filter second instructor gms/hhaRotations resource by STI rotation_num
        Given logged on as cna instructor user
        When request GET to second instructor /api/gms/hhaRotations with filters by STI rotation_num
        Then will be permission denied



    Scenario: STI cna instructor user requesting to filter gms/cnaRotations resource by ST2 start_date
        Given logged on as cna instructor user
        When request GET to /api/gms/cnaRotations with filters by ST2 start_date
        Then no data will be returned as JSON response


    Scenario: STI cna instructor user requesting to filter gms/cnaRotations resource by ST2 end_date
        Given logged on as cna instructor user
        When request GET to /api/gms/cnaRotations with filters by ST2 end_date
        Then no data will be returned as JSON response


    Scenario: STI cna instructor user requesting to filter gms/cnaRotations resource by ST2 rotation_num
        Given logged on as cna instructor user
        When request GET to /api/gms/cnaRotations with filters by ST2 rotation_num
        Then no data will be returned as JSON response


    Scenario: STI cna instructor user requesting to filter gms/hhaRotations resource by ST2 start_date
        Given logged on as cna instructor user
        When request GET to /api/gms/hhaRotations with filters by ST2 start_date
        Then will be permission denied


    Scenario: STI cna instructor user requesting to filter gms/hhaRotations resource by ST2 end_date
        Given logged on as cna instructor user
        When request GET to /api/gms/hhaRotations with filters by ST2 end_date
        Then will be permission denied


    Scenario: STI cna instructor user requesting to filter gms/hhaRotations resource by ST2 rotation_num
        Given logged on as cna instructor user
        When request GET to /api/gms/hhaRotations with filters by ST2 rotation_num
        Then will be permission denied










    Scenario: hha instructor user requesting to filter gms/cnaRotations resource by STI start_date
        Given logged on as hha instructor user
        When request GET to /api/gms/cnaRotations with filters by STI start_date
        Then will be permission denied


    Scenario: hha instructor user requesting to filter gms/cnaRotations resource by STI end_date
        Given logged on as hha instructor user
        When request GET to /api/gms/cnaRotations with filters by STI end_date
        Then will be permission denied


    Scenario: hha instructor user requesting to filter gms/cnaRotations resource by STI rotation_num
        Given logged on as hha instructor user
        When request GET to /api/gms/cnaRotations with filters by STI rotation_num
        Then will be permission denied

    Scenario: hha instructor user requesting to filter second instructor gms/cnaRotations resource by STI start_date
        Given logged on as hha instructor user
        When request GET to second instructor /api/gms/cnaRotations with filters by STI start_date
        Then will be permission denied

    Scenario: hha instructor user requesting to filter second instructor gms/cnaRotations resource by STI end_date
        Given logged on as hha instructor user
        When request GET to second instructor /api/gms/cnaRotations with filters by STI end_date
        Then will be permission denied

    Scenario: hha instructor user requesting to filter second instructor gms/cnaRotations resource by STI rotation_num
        Given logged on as hha instructor user
        When request GET to second instructor /api/gms/cnaRotations with filters by STI rotation_num
        Then will be permission denied

    Scenario: hha instructor user requesting to filter gms/hhaRotations resource by STI start_date
        Given logged on as hha instructor user
        When request GET to /api/gms/hhaRotations with filters by STI start_date
        Then the specific STI hhaRotations data will be returned as JSON response


    Scenario: hha instructor user requesting to filter gms/hhaRotations resource by STI end_date
        Given logged on as hha instructor user
        When request GET to /api/gms/hhaRotations with filters by STI end_date
        Then the specific STI hhaRotations data will be returned as JSON response


    Scenario: hha instructor user requesting to filter gms/hhaRotations resource by STI rotation_num
        Given logged on as hha instructor user
        When request GET to /api/gms/hhaRotations with filters by STI rotation_num
        Then the specific STI hhaRotations data will be returned as JSON response

    Scenario: hha instructor user requesting to filter second instructor gms/hhaRotations resource by STI start_date
        Given logged on as hha instructor user
        When request GET to second instructor /api/gms/hhaRotations with filters by STI start_date
        Then the specific STI hhaRotations data will be returned as JSON response

    Scenario: hha instructor user requesting to filter second instructor gms/hhaRotations resource by STI end_date
        Given logged on as hha instructor user
        When request GET to second instructor /api/gms/hhaRotations with filters by STI end_date
        Then the specific STI hhaRotations data will be returned as JSON response

    Scenario: hha instructor user requesting to filter second instructor gms/hhaRotations resource by STI rotation_num
        Given logged on as hha instructor user
        When request GET to second instructor /api/gms/hhaRotations with filters by STI rotation_num
        Then the specific STI hhaRotations data will be returned as JSON response



    Scenario: STI hha instructor user requesting to filter gms/cnaRotations resource by ST2 start_date
        Given logged on as hha instructor user
        When request GET to /api/gms/cnaRotations with filters by ST2 start_date
        Then will be permission denied


    Scenario: STI hha instructor user requesting to filter gms/cnaRotations resource by ST2 end_date
        Given logged on as hha instructor user
        When request GET to /api/gms/cnaRotations with filters by ST2 end_date
        Then will be permission denied


    Scenario: STI hha instructor user requesting to filter gms/cnaRotations resource by ST2 rotation_num
        Given logged on as hha instructor user
        When request GET to /api/gms/cnaRotations with filters by ST2 rotation_num
        Then will be permission denied


    Scenario: STI hha instructor user requesting to filter gms/hhaRotations resource by ST2 start_date
        Given logged on as hha instructor user
        When request GET to /api/gms/hhaRotations with filters by ST2 start_date
        Then no data will be returned as JSON response


    Scenario: STI hha instructor user requesting to filter gms/hhaRotations resource by ST2 end_date
        Given logged on as hha instructor user
        When request GET to /api/gms/hhaRotations with filters by ST2 end_date
        Then no data will be returned as JSON response


    Scenario: STI hha instructor user requesting to filter gms/hhaRotations resource by ST2 rotation_num
        Given logged on as hha instructor user
        When request GET to /api/gms/hhaRotations with filters by ST2 rotation_num
        Then no data will be returned as JSON response












    ## NOTE: replace Rotations below with Students; Done

    Scenario: superuser requesting to filter gms/cnaStudents resource by STI first_name
        Given logged on as superuser
        When request GET to /api/gms/cnaStudents with filters by STI first_name
        Then the specific STI cnaStudents data will be returned as JSON response


    Scenario: superuser requesting to filter gms/cnaStudents resource by STI last_name
        Given logged on as superuser
        When request GET to /api/gms/cnaStudents with filters by STI last_name
        Then the specific STI cnaStudents data will be returned as JSON response


    Scenario: superuser requesting to filter gms/cnaStudents resource by STI makeup_student
        Given logged on as superuser
        When request GET to /api/gms/cnaStudents with filters by STI makeup_student
        Then the specific STI cnaStudents data will be returned as JSON response




    Scenario: superuser requesting to filter second instructor gms/cnaStudents resource by STI first_name
        Given logged on as superuser
        When request GET to second instructor /api/gms/cnaStudents with filters by STI first_name
        Then the specific STI second cnaStudents data will be returned as JSON response

    Scenario: superuser requesting to filter second instructor gms/cnaStudents resource by STI last_name
        Given logged on as superuser
        When request GET to second instructor /api/gms/cnaStudents with filters by STI last_name
        Then the specific STI second cnaStudents data will be returned as JSON response

    Scenario: superuser requesting to filter second instructor gms/cnaStudents resource by STI makeup_student
        Given logged on as superuser
        When request GET to second instructor /api/gms/cnaStudents with filters by STI makeup_student
        Then the specific STI second cnaStudents data will be returned as JSON response



    Scenario: superuser requesting to filter gms/hhaStudents resource by STI first_name
        Given logged on as superuser
        When request GET to /api/gms/hhaStudents with filters by STI first_name
        Then the specific STI hhaStudents data will be returned as JSON response


    Scenario: superuser requesting to filter gms/hhaStudents resource by STI last_name
        Given logged on as superuser
        When request GET to /api/gms/hhaStudents with filters by STI last_name
        Then the specific STI hhaStudents data will be returned as JSON response


    Scenario: superuser requesting to filter gms/hhaStudents resource by STI makeup_student
        Given logged on as superuser
        When request GET to /api/gms/hhaStudents with filters by STI makeup_student
        Then the specific STI hhaStudents data will be returned as JSON response




    Scenario: superuser requesting to filter second instructor gms/hhaStudents resource by STI first_name
        Given logged on as superuser
        When request GET to second instructor /api/gms/hhaStudents with filters by STI first_name
        Then the specific STI second hhaStudents data will be returned as JSON response

    Scenario: superuser requesting to filter second instructor gms/hhaStudents resource by STI last_name
        Given logged on as superuser
        When request GET to second instructor /api/gms/hhaStudents with filters by STI last_name
        Then the specific STI second hhaStudents data will be returned as JSON response

    Scenario: superuser requesting to filter second instructor gms/hhaStudents resource by STI makeup_student
        Given logged on as superuser
        When request GET to second instructor /api/gms/hhaStudents with filters by STI makeup_student
        Then the specific STI second hhaStudents data will be returned as JSON response







    Scenario: superuser requesting to filter gms/cnaStudents resource by ST2 first_name
        Given logged on as superuser
        When request GET to /api/gms/cnaStudents with filters by ST2 first_name
        Then the specific ST2 cnaStudents data will be returned as JSON response


    Scenario: superuser requesting to filter gms/cnaStudents resource by ST2 last_name
        Given logged on as superuser
        When request GET to /api/gms/cnaStudents with filters by ST2 last_name
        Then the specific ST2 cnaStudents data will be returned as JSON response


    Scenario: superuser requesting to filter gms/cnaStudents resource by ST2 makeup_student
        Given logged on as superuser
        When request GET to /api/gms/cnaStudents with filters by ST2 makeup_student
        Then the specific ST2 cnaStudents data will be returned as JSON response


    Scenario: superuser requesting to filter gms/hhaStudents resource by ST2 first_name
        Given logged on as superuser
        When request GET to /api/gms/hhaStudents with filters by ST2 first_name
        Then the specific ST2 hhaStudents data will be returned as JSON response


    Scenario: superuser requesting to filter gms/hhaStudents resource by ST2 last_name
        Given logged on as superuser
        When request GET to /api/gms/hhaStudents with filters by ST2 last_name
        Then the specific ST2 hhaStudents data will be returned as JSON response


    Scenario: superuser requesting to filter gms/hhaStudents resource by ST2 makeup_student
        Given logged on as superuser
        When request GET to /api/gms/hhaStudents with filters by ST2 makeup_student
        Then the specific ST2 hhaStudents data will be returned as JSON response
    # remember also a scenario where filter for data for another school? should not appear unless your superuser




    Scenario: admin instructor user requesting to filter gms/cnaStudents resource by STI first_name
        Given logged on as admin instructor user
        When request GET to /api/gms/cnaStudents with filters by STI first_name
        Then the specific STI cnaStudents data will be returned as JSON response


    Scenario: admin instructor user requesting to filter gms/cnaStudents resource by STI last_name
        Given logged on as admin instructor user
        When request GET to /api/gms/cnaStudents with filters by STI last_name
        Then the specific STI cnaStudents data will be returned as JSON response


    Scenario: admin instructor user requesting to filter gms/cnaStudents resource by STI makeup_student
        Given logged on as admin instructor user
        When request GET to /api/gms/cnaStudents with filters by STI makeup_student
        Then the specific STI cnaStudents data will be returned as JSON response




    Scenario: admin instructor user requesting to filter second instructor gms/cnaStudents resource by STI first_name
        Given logged on as admin instructor user
        When request GET to second instructor /api/gms/cnaStudents with filters by STI first_name
        Then the specific STI second cnaStudents data will be returned as JSON response

    Scenario: admin instructor user requesting to filter second instructor gms/cnaStudents resource by STI last_name
        Given logged on as admin instructor user
        When request GET to second instructor /api/gms/cnaStudents with filters by STI last_name
        Then the specific STI second cnaStudents data will be returned as JSON response

    Scenario: admin instructor user requesting to filter second instructor gms/cnaStudents resource by STI makeup_student
        Given logged on as admin instructor user
        When request GET to second instructor /api/gms/cnaStudents with filters by STI makeup_student
        Then the specific STI second cnaStudents data will be returned as JSON response





    Scenario: admin instructor user requesting to filter gms/hhaStudents resource by STI first_name
        Given logged on as admin instructor user
        When request GET to /api/gms/hhaStudents with filters by STI first_name
        Then the specific STI hhaStudents data will be returned as JSON response


    Scenario: admin instructor user requesting to filter gms/hhaStudents resource by STI last_name
        Given logged on as admin instructor user
        When request GET to /api/gms/hhaStudents with filters by STI last_name
        Then the specific STI hhaStudents data will be returned as JSON response


    Scenario: admin instructor user requesting to filter gms/hhaStudents resource by STI makeup_student
        Given logged on as admin instructor user
        When request GET to /api/gms/hhaStudents with filters by STI makeup_student
        Then the specific STI hhaStudents data will be returned as JSON response




    Scenario: admin instructor user requesting to filter second instructor gms/hhaRotations resource by STI start_date
        Given logged on as admin instructor user
        When request GET to second instructor /api/gms/hhaRotations with filters by STI start_date
        Then the specific STI second hhaRotations data will be returned as JSON response

    Scenario: admin instructor user requesting to filter second instructor gms/hhaRotations resource by STI end_date
        Given logged on as admin instructor user
        When request GET to second instructor /api/gms/hhaRotations with filters by STI end_date
        Then the specific STI second hhaRotations data will be returned as JSON response

    Scenario: admin instructor user requesting to filter second instructor gms/hhaRotations resource by STI rotation_num
        Given logged on as admin instructor user
        When request GET to second instructor /api/gms/hhaRotations with filters by STI rotation_num
        Then the specific STI second hhaRotations data will be returned as JSON response





    Scenario: STI admin instructor user requesting to filter gms/cnaStudents resource by ST2 first_name
        Given logged on as admin instructor user
        When request GET to /api/gms/cnaStudents with filters by ST2 first_name
        Then no data will be returned as JSON response


    Scenario: STI admin instructor user requesting to filter gms/cnaStudents resource by ST2 last_name
        Given logged on as admin instructor user
        When request GET to /api/gms/cnaStudents with filters by ST2 last_name
        Then no data will be returned as JSON response


    Scenario: STI admin instructor user requesting to filter gms/cnaStudents resource by ST2 makeup_student
        Given logged on as admin instructor user
        When request GET to /api/gms/cnaStudents with filters by ST2 makeup_student
        Then no data will be returned as JSON response


    Scenario: STI admin instructor user requesting to filter gms/hhaStudents resource by ST2 first_name
        Given logged on as admin instructor user
        When request GET to /api/gms/hhaStudents with filters by ST2 first_name
        Then no data will be returned as JSON response


    Scenario: STI admin instructor user requesting to filter gms/hhaStudents resource by ST2 last_name
        Given logged on as admin instructor user
        When request GET to /api/gms/hhaStudents with filters by ST2 last_name
        Then no data will be returned as JSON response


    Scenario: STI admin instructor user requesting to filter gms/hhaStudents resource by ST2 makeup_student
        Given logged on as admin instructor user
        When request GET to /api/gms/hhaStudents with filters by ST2 makeup_student
        Then no data will be returned as JSON response






    Scenario: staff cna instructor user requesting to filter gms/cnaStudents resource by STI first_name
        Given logged on as staff cna instructor user
        When request GET to /api/gms/cnaStudents with filters by STI first_name
        Then the specific STI cnaStudents data will be returned as JSON response


    Scenario: staff cna instructor user requesting to filter gms/cnaStudents resource by STI last_name
        Given logged on as staff cna instructor user
        When request GET to /api/gms/cnaStudents with filters by STI last_name
        Then the specific STI cnaStudents data will be returned as JSON response


    Scenario: staff cna instructor user requesting to filter gms/cnaStudents resource by STI makeup_student
        Given logged on as staff cna instructor user
        When request GET to /api/gms/cnaStudents with filters by STI makeup_student
        Then the specific STI cnaStudents data will be returned as JSON response

    Scenario: staff cna instructor user requesting to filter second instructor gms/cnaStudents resource by STI first_name
        Given logged on as staff cna instructor user
        When request GET to second instructor /api/gms/cnaStudents with filters by STI first_name
        Then the specific STI second cnaStudents data will be returned as JSON response

    Scenario: staff cna instructor user requesting to filter second instructor gms/cnaStudents resource by STI last_name
        Given logged on as staff cna instructor user
        When request GET to second instructor /api/gms/cnaStudents with filters by STI last_name
        Then the specific STI second cnaStudents data will be returned as JSON response

    Scenario: staff cna instructor user requesting to filter second instructor gms/cnaStudents resource by STI makeup_student
        Given logged on as staff cna instructor user
        When request GET to second instructor /api/gms/cnaStudents with filters by STI makeup_student
        Then the specific STI second cnaStudents data will be returned as JSON response

    Scenario: staff cna instructor user requesting to filter gms/hhaStudents resource by STI first_name
        Given logged on as staff cna instructor user
        When request GET to /api/gms/hhaStudents with filters by STI first_name
        Then will be permission denied


    Scenario: staff cna instructor user requesting to filter gms/hhaStudents resource by STI last_name
        Given logged on as staff cna instructor user
        When request GET to /api/gms/hhaStudents with filters by STI last_name
        Then will be permission denied


    Scenario: staff cna instructor user requesting to filter gms/hhaStudents resource by STI makeup_student
        Given logged on as staff cna instructor user
        When request GET to /api/gms/hhaStudents with filters by STI makeup_student
        Then will be permission denied

    Scenario: staff cna instructor user requesting to filter second instructor gms/hhaStudents resource by STI first_name
        Given logged on as staff cna instructor user
        When request GET to second instructor /api/gms/hhaStudents with filters by STI first_name
        Then will be permission denied

    Scenario: staff cna instructor user requesting to filter second instructor gms/hhaStudents resource by STI last_name
        Given logged on as staff cna instructor user
        When request GET to second instructor /api/gms/hhaStudents with filters by STI last_name
        Then will be permission denied

    Scenario: staff cna instructor user requesting to filter second instructor gms/hhaStudents resource by STI makeup_student
        Given logged on as staff cna instructor user
        When request GET to second instructor /api/gms/hhaStudents with filters by STI makeup_student
        Then will be permission denied



    Scenario: STI staff cna instructor user requesting to filter gms/cnaStudents resource by ST2 first_name
        Given logged on as staff cna instructor user
        When request GET to /api/gms/cnaStudents with filters by ST2 first_name
        Then no data will be returned as JSON response


    Scenario: STI staff cna instructor user requesting to filter gms/cnaStudents resource by ST2 last_name
        Given logged on as staff cna instructor user
        When request GET to /api/gms/cnaStudents with filters by ST2 last_name
        Then no data will be returned as JSON response


    Scenario: STI staff cna instructor user requesting to filter gms/cnaStudents resource by ST2 makeup_student
        Given logged on as staff cna instructor user
        When request GET to /api/gms/cnaStudents with filters by ST2 makeup_student
        Then no data will be returned as JSON response


    Scenario: STI staff cna instructor user requesting to filter gms/hhaStudents resource by ST2 first_name
        Given logged on as staff cna instructor user
        When request GET to /api/gms/hhaStudents with filters by ST2 first_name
        Then will be permission denied


    Scenario: STI staff cna instructor user requesting to filter gms/hhaStudents resource by ST2 last_name
        Given logged on as staff cna instructor user
        When request GET to /api/gms/hhaStudents with filters by ST2 last_name
        Then will be permission denied


    Scenario: STI staff cna instructor user requesting to filter gms/hhaStudents resource by ST2 makeup_student
        Given logged on as staff cna instructor user
        When request GET to /api/gms/hhaStudents with filters by ST2 makeup_student
        Then will be permission denied













    Scenario: staff hha instructor user requesting to filter gms/cnaStudents resource by STI first_name
        Given logged on as staff hha instructor user
        When request GET to /api/gms/cnaStudents with filters by STI first_name
        Then will be permission denied


    Scenario: staff hha instructor user requesting to filter gms/cnaStudents resource by STI last_name
        Given logged on as staff hha instructor user
        When request GET to /api/gms/cnaStudents with filters by STI last_name
        Then will be permission denied


    Scenario: staff hha instructor user requesting to filter gms/cnaStudents resource by STI makeup_student
        Given logged on as staff hha instructor user
        When request GET to /api/gms/cnaStudents with filters by STI makeup_student
        Then will be permission denied

    Scenario: staff hha instructor user requesting to filter second instructor gms/cnaStudents resource by STI first_name
        Given logged on as staff hha instructor user
        When request GET to second instructor /api/gms/cnaStudents with filters by STI first_name
        Then will be permission denied

    Scenario: staff hha instructor user requesting to filter second instructor gms/cnaStudents resource by STI last_name
        Given logged on as staff hha instructor user
        When request GET to second instructor /api/gms/cnaStudents with filters by STI last_name
        Then will be permission denied

    Scenario: staff hha instructor user requesting to filter second instructor gms/cnaStudents resource by STI makeup_student
        Given logged on as staff hha instructor user
        When request GET to second instructor /api/gms/cnaStudents with filters by STI makeup_student
        Then will be permission denied

    Scenario: staff hha instructor user requesting to filter gms/hhaStudents resource by STI first_name
        Given logged on as staff hha instructor user
        When request GET to /api/gms/hhaStudents with filters by STI first_name
        Then the specific STI hhaStudents data will be returned as JSON response


    Scenario: staff hha instructor user requesting to filter gms/hhaStudents resource by STI last_name
        Given logged on as staff hha instructor user
        When request GET to /api/gms/hhaStudents with filters by STI last_name
        Then the specific STI hhaStudents data will be returned as JSON response


    Scenario: staff hha instructor user requesting to filter gms/hhaStudents resource by STI makeup_student
        Given logged on as staff hha instructor user
        When request GET to /api/gms/hhaStudents with filters by STI makeup_student
        Then the specific STI hhaStudents data will be returned as JSON response

    Scenario: staff hha instructor user requesting to filter second instructor gms/hhaStudents resource by STI first_name
        Given logged on as staff hha instructor user
        When request GET to second instructor /api/gms/hhaStudents with filters by STI first_name
        Then the specific STI second hhaStudents data will be returned as JSON response

    Scenario: staff hha instructor user requesting to filter second instructor gms/hhaStudents resource by STI last_name
        Given logged on as staff hha instructor user
        When request GET to second instructor /api/gms/hhaStudents with filters by STI last_name
        Then the specific STI second hhaStudents data will be returned as JSON response

    Scenario: staff hha instructor user requesting to filter second instructor gms/hhaStudents resource by STI makeup_student
        Given logged on as staff hha instructor user
        When request GET to second instructor /api/gms/hhaStudents with filters by STI makeup_student
        Then the specific STI second hhaStudents data will be returned as JSON response



    Scenario: STI staff hha instructor user requesting to filter gms/cnaStudents resource by ST2 first_name
        Given logged on as staff hha instructor user
        When request GET to /api/gms/cnaStudents with filters by ST2 first_name
        Then will be permission denied


    Scenario: STI staff hha instructor user requesting to filter gms/cnaStudents resource by ST2 last_name
        Given logged on as staff hha instructor user
        When request GET to /api/gms/cnaStudents with filters by ST2 last_name
        Then will be permission denied


    Scenario: STI staff hha instructor user requesting to filter gms/cnaStudents resource by ST2 makeup_student
        Given logged on as staff hha instructor user
        When request GET to /api/gms/cnaStudents with filters by ST2 makeup_student
        Then will be permission denied


    Scenario: STI staff hha instructor user requesting to filter gms/hhaStudents resource by ST2 first_name
        Given logged on as staff hha instructor user
        When request GET to /api/gms/hhaStudents with filters by ST2 first_name
        Then no data will be returned as JSON response


    Scenario: STI staff hha instructor user requesting to filter gms/hhaStudents resource by ST2 last_name
        Given logged on as staff hha instructor user
        When request GET to /api/gms/hhaStudents with filters by ST2 last_name
        Then no data will be returned as JSON response


    Scenario: STI staff hha instructor user requesting to filter gms/hhaStudents resource by ST2 makeup_student
        Given logged on as staff hha instructor user
        When request GET to /api/gms/hhaStudents with filters by ST2 makeup_student
        Then no data will be returned as JSON response












    Scenario: cna instructor user requesting to filter gms/cnaStudents resource by STI first_name
        Given logged on as cna instructor user
        When request GET to /api/gms/cnaStudents with filters by STI first_name
        Then the specific STI cnaStudents data will be returned as JSON response


    Scenario: cna instructor user requesting to filter gms/cnaStudents resource by STI last_name
        Given logged on as cna instructor user
        When request GET to /api/gms/cnaStudents with filters by STI last_name
        Then the specific STI cnaStudents data will be returned as JSON response


    Scenario: cna instructor user requesting to filter gms/cnaStudents resource by STI makeup_student
        Given logged on as cna instructor user
        When request GET to /api/gms/cnaStudents with filters by STI makeup_student
        Then the specific STI cnaStudents data will be returned as JSON response

    Scenario: cna instructor user requesting to filter second instructor gms/cnaStudents resource by STI first_name
        Given logged on as cna instructor user
        When request GET to second instructor /api/gms/cnaStudents with filters by STI first_name
        Then no data will be returned as JSON response

    Scenario: cna instructor user requesting to filter second instructor gms/cnaStudents resource by STI last_name
        Given logged on as cna instructor user
        When request GET to second instructor /api/gms/cnaStudents with filters by STI last_name
        Then no data will be returned as JSON response

    Scenario: cna instructor user requesting to filter second instructor gms/cnaStudents resource by STI makeup_student
        Given logged on as cna instructor user
        When request GET to second instructor /api/gms/cnaStudents with filters by STI makeup_student
        Then no desired ST2 cnaStudents data will be returned as JSON response

    Scenario: cna instructor user requesting to filter gms/hhaStudents resource by STI first_name
        Given logged on as cna instructor user
        When request GET to /api/gms/hhaStudents with filters by STI first_name
        Then will be permission denied


    Scenario: cna instructor user requesting to filter gms/hhaStudents resource by STI last_name
        Given logged on as cna instructor user
        When request GET to /api/gms/hhaStudents with filters by STI last_name
        Then will be permission denied


    Scenario: cna instructor user requesting to filter gms/hhaStudents resource by STI makeup_student
        Given logged on as cna instructor user
        When request GET to /api/gms/hhaStudents with filters by STI makeup_student
        Then will be permission denied

    Scenario: cna instructor user requesting to filter second instructor gms/hhaStudents resource by STI first_name
        Given logged on as cna instructor user
        When request GET to second instructor /api/gms/hhaStudents with filters by STI first_name
        Then will be permission denied

    Scenario: cna instructor user requesting to filter second instructor gms/hhaStudents resource by STI last_name
        Given logged on as cna instructor user
        When request GET to second instructor /api/gms/hhaStudents with filters by STI last_name
        Then will be permission denied

    Scenario: cna instructor user requesting to filter second instructor gms/hhaStudents resource by STI makeup_student
        Given logged on as cna instructor user
        When request GET to second instructor /api/gms/hhaStudents with filters by STI makeup_student
        Then will be permission denied



    Scenario: STI cna instructor user requesting to filter gms/cnaStudents resource by ST2 first_name
        Given logged on as cna instructor user
        When request GET to /api/gms/cnaStudents with filters by ST2 first_name
        Then no data will be returned as JSON response


    Scenario: STI cna instructor user requesting to filter gms/cnaStudents resource by ST2 last_name
        Given logged on as cna instructor user
        When request GET to /api/gms/cnaStudents with filters by ST2 last_name
        Then no data will be returned as JSON response


    Scenario: STI cna instructor user requesting to filter gms/cnaStudents resource by ST2 makeup_student
        Given logged on as cna instructor user
        When request GET to /api/gms/cnaStudents with filters by ST2 makeup_student
        Then no data will be returned as JSON response


    Scenario: STI cna instructor user requesting to filter gms/hhaStudents resource by ST2 first_name
        Given logged on as cna instructor user
        When request GET to /api/gms/hhaStudents with filters by ST2 first_name
        Then will be permission denied


    Scenario: STI cna instructor user requesting to filter gms/hhaStudents resource by ST2 last_name
        Given logged on as cna instructor user
        When request GET to /api/gms/hhaStudents with filters by ST2 last_name
        Then will be permission denied


    Scenario: STI cna instructor user requesting to filter gms/hhaStudents resource by ST2 makeup_student
        Given logged on as cna instructor user
        When request GET to /api/gms/hhaStudents with filters by ST2 makeup_student
        Then will be permission denied










    Scenario: hha instructor user requesting to filter gms/cnaStudents resource by STI first_name
        Given logged on as hha instructor user
        When request GET to /api/gms/cnaStudents with filters by STI first_name
        Then will be permission denied


    Scenario: hha instructor user requesting to filter gms/cnaStudents resource by STI last_name
        Given logged on as hha instructor user
        When request GET to /api/gms/cnaStudents with filters by STI last_name
        Then will be permission denied


    Scenario: hha instructor user requesting to filter gms/cnaStudents resource by STI makeup_student
        Given logged on as hha instructor user
        When request GET to /api/gms/cnaStudents with filters by STI makeup_student
        Then will be permission denied

    Scenario: hha instructor user requesting to filter second instructor gms/cnaStudents resource by STI first_name
        Given logged on as hha instructor user
        When request GET to second instructor /api/gms/cnaStudents with filters by STI first_name
        Then will be permission denied

    Scenario: hha instructor user requesting to filter second instructor gms/cnaStudents resource by STI last_name
        Given logged on as hha instructor user
        When request GET to second instructor /api/gms/cnaStudents with filters by STI last_name
        Then will be permission denied

    Scenario: hha instructor user requesting to filter second instructor gms/cnaStudents resource by STI makeup_student
        Given logged on as hha instructor user
        When request GET to second instructor /api/gms/cnaStudents with filters by STI makeup_student
        Then will be permission denied

    Scenario: hha instructor user requesting to filter gms/hhaStudents resource by STI first_name
        Given logged on as hha instructor user
        When request GET to /api/gms/hhaStudents with filters by STI first_name
        Then the specific STI hhaStudents data will be returned as JSON response


    Scenario: hha instructor user requesting to filter gms/hhaStudents resource by STI last_name
        Given logged on as hha instructor user
        When request GET to /api/gms/hhaStudents with filters by STI last_name
        Then the specific STI hhaStudents data will be returned as JSON response


    Scenario: hha instructor user requesting to filter gms/hhaStudents resource by STI makeup_student
        Given logged on as hha instructor user
        When request GET to /api/gms/hhaStudents with filters by STI makeup_student
        Then the specific STI hhaStudents data will be returned as JSON response

    Scenario: hha instructor user requesting to filter second instructor gms/hhaStudents resource by STI first_name
        Given logged on as hha instructor user
        When request GET to second instructor /api/gms/hhaStudents with filters by STI first_name
        Then the specific STI hhaStudents data will be returned as JSON response

    Scenario: hha instructor user requesting to filter second instructor gms/hhaStudents resource by STI last_name
        Given logged on as hha instructor user
        When request GET to second instructor /api/gms/hhaStudents with filters by STI last_name
        Then the specific STI hhaStudents data will be returned as JSON response

    Scenario: hha instructor user requesting to filter second instructor gms/hhaStudents resource by STI makeup_student
        Given logged on as hha instructor user
        When request GET to second instructor /api/gms/hhaStudents with filters by STI makeup_student
        Then the specific STI hhaStudents data will be returned as JSON response



    Scenario: STI hha instructor user requesting to filter gms/cnaStudents resource by ST2 first_name
        Given logged on as hha instructor user
        When request GET to /api/gms/cnaStudents with filters by ST2 first_name
        Then will be permission denied


    Scenario: STI hha instructor user requesting to filter gms/cnaStudents resource by ST2 last_name
        Given logged on as hha instructor user
        When request GET to /api/gms/cnaStudents with filters by ST2 last_name
        Then will be permission denied


    Scenario: STI hha instructor user requesting to filter gms/cnaStudents resource by ST2 makeup_student
        Given logged on as hha instructor user
        When request GET to /api/gms/cnaStudents with filters by ST2 makeup_student
        Then will be permission denied


    Scenario: STI hha instructor user requesting to filter gms/hhaStudents resource by ST2 first_name
        Given logged on as hha instructor user
        When request GET to /api/gms/hhaStudents with filters by ST2 first_name
        Then no data will be returned as JSON response


    Scenario: STI hha instructor user requesting to filter gms/hhaStudents resource by ST2 last_name
        Given logged on as hha instructor user
        When request GET to /api/gms/hhaStudents with filters by ST2 last_name
        Then no data will be returned as JSON response


    Scenario: STI hha instructor user requesting to filter gms/hhaStudents resource by ST2 makeup_student
        Given logged on as hha instructor user
        When request GET to /api/gms/hhaStudents with filters by ST2 makeup_student
        Then no data will be returned as JSON response

























    # BELOW ARE FOR CNA/HHATHEORYRECORD
    Scenario: superuser requesting to filter gms/cnaTheoryRecords resource by STI date
        Given logged on as superuser
        When request GET to /api/gms/cnaTheoryRecords with filters by STI date
        Then the specific STI cnaTheoryRecords data will be returned as JSON response


    Scenario: superuser requesting to filter gms/cnaTheoryRecords resource by STI completed
        Given logged on as superuser
        When request GET to /api/gms/cnaTheoryRecords with filters by STI completed
        Then the specific STI cnaTheoryRecords data will be returned as JSON response


    Scenario: superuser requesting to filter gms/cnaTheoryRecords resource by STI topic
        Given logged on as superuser
        When request GET to /api/gms/cnaTheoryRecords with filters by STI topic
        Then the specific STI cnaTheoryRecords data will be returned as JSON response




    Scenario: superuser requesting to filter second instructor gms/cnaTheoryRecords resource by STI date
        Given logged on as superuser
        When request GET to second instructor /api/gms/cnaTheoryRecords with filters by STI date
        Then the specific STI second cnaTheoryRecords data will be returned as JSON response

    Scenario: superuser requesting to filter second instructor gms/cnaTheoryRecords resource by STI completed
        Given logged on as superuser
        When request GET to second instructor /api/gms/cnaTheoryRecords with filters by STI completed
        Then the specific STI second cnaTheoryRecords data will be returned as JSON response

    Scenario: superuser requesting to filter second instructor gms/cnaTheoryRecords resource by STI topic
        Given logged on as superuser
        When request GET to second instructor /api/gms/cnaTheoryRecords with filters by STI topic
        Then the specific STI second cnaTheoryRecords data will be returned as JSON response



    Scenario: superuser requesting to filter gms/hhaTheoryRecords resource by STI date
        Given logged on as superuser
        When request GET to /api/gms/hhaTheoryRecords with filters by STI date
        Then the specific STI hhaTheoryRecords data will be returned as JSON response


    Scenario: superuser requesting to filter gms/hhaTheoryRecords resource by STI completed
        Given logged on as superuser
        When request GET to /api/gms/hhaTheoryRecords with filters by STI completed
        Then the specific STI hhaTheoryRecords data will be returned as JSON response


    Scenario: superuser requesting to filter gms/hhaTheoryRecords resource by STI topic
        Given logged on as superuser
        When request GET to /api/gms/hhaTheoryRecords with filters by STI topic
        Then the specific STI hhaTheoryRecords data will be returned as JSON response




    Scenario: superuser requesting to filter second instructor gms/hhaTheoryRecords resource by STI date
        Given logged on as superuser
        When request GET to second instructor /api/gms/hhaTheoryRecords with filters by STI date
        Then the specific STI second hhaTheoryRecords data will be returned as JSON response

    Scenario: superuser requesting to filter second instructor gms/hhaTheoryRecords resource by STI completed
        Given logged on as superuser
        When request GET to second instructor /api/gms/hhaTheoryRecords with filters by STI completed
        Then the specific STI second hhaTheoryRecords data will be returned as JSON response

    Scenario: superuser requesting to filter second instructor gms/hhaTheoryRecords resource by STI topic
        Given logged on as superuser
        When request GET to second instructor /api/gms/hhaTheoryRecords with filters by STI topic
        Then the specific STI second hhaTheoryRecords data will be returned as JSON response







    Scenario: superuser requesting to filter gms/cnaTheoryRecords resource by ST2 date
        Given logged on as superuser
        When request GET to /api/gms/cnaTheoryRecords with filters by ST2 date
        Then the specific ST2 cnaTheoryRecords data will be returned as JSON response


    Scenario: superuser requesting to filter gms/cnaTheoryRecords resource by ST2 completed
        Given logged on as superuser
        When request GET to /api/gms/cnaTheoryRecords with filters by ST2 completed
        Then the specific ST2 cnaTheoryRecords data will be returned as JSON response


    Scenario: superuser requesting to filter gms/cnaTheoryRecords resource by ST2 topic
        Given logged on as superuser
        When request GET to /api/gms/cnaTheoryRecords with filters by ST2 topic
        Then the specific ST2 cnaTheoryRecords data will be returned as JSON response


    Scenario: superuser requesting to filter gms/hhaTheoryRecords resource by ST2 date
        Given logged on as superuser
        When request GET to /api/gms/hhaTheoryRecords with filters by ST2 date
        Then the specific ST2 hhaTheoryRecords data will be returned as JSON response


    Scenario: superuser requesting to filter gms/hhaTheoryRecords resource by ST2 completed
        Given logged on as superuser
        When request GET to /api/gms/hhaTheoryRecords with filters by ST2 completed
        Then the specific ST2 hhaTheoryRecords data will be returned as JSON response


    Scenario: superuser requesting to filter gms/hhaTheoryRecords resource by ST2 topic
        Given logged on as superuser
        When request GET to /api/gms/hhaTheoryRecords with filters by ST2 topic
        Then the specific ST2 hhaTheoryRecords data will be returned as JSON response
    # remember also a scenario where filter for data for another school? should not appear unless your superuser




    Scenario: admin instructor user requesting to filter gms/cnaTheoryRecords resource by STI date
        Given logged on as admin instructor user
        When request GET to /api/gms/cnaTheoryRecords with filters by STI date
        Then the specific STI cnaTheoryRecords data will be returned as JSON response


    Scenario: admin instructor user requesting to filter gms/cnaTheoryRecords resource by STI completed
        Given logged on as admin instructor user
        When request GET to /api/gms/cnaTheoryRecords with filters by STI completed
        Then the specific STI cnaTheoryRecords data will be returned as JSON response


    Scenario: admin instructor user requesting to filter gms/cnaTheoryRecords resource by STI topic
        Given logged on as admin instructor user
        When request GET to /api/gms/cnaTheoryRecords with filters by STI topic
        Then the specific STI cnaTheoryRecords data will be returned as JSON response




    Scenario: admin instructor user requesting to filter second instructor gms/cnaTheoryRecords resource by STI date
        Given logged on as admin instructor user
        When request GET to second instructor /api/gms/cnaTheoryRecords with filters by STI date
        Then the specific STI second cnaTheoryRecords data will be returned as JSON response

    Scenario: admin instructor user requesting to filter second instructor gms/cnaTheoryRecords resource by STI completed
        Given logged on as admin instructor user
        When request GET to second instructor /api/gms/cnaTheoryRecords with filters by STI completed
        Then the specific STI second cnaTheoryRecords data will be returned as JSON response

    Scenario: admin instructor user requesting to filter second instructor gms/cnaTheoryRecords resource by STI topic
        Given logged on as admin instructor user
        When request GET to second instructor /api/gms/cnaTheoryRecords with filters by STI topic
        Then the specific STI second cnaTheoryRecords data will be returned as JSON response





    Scenario: admin instructor user requesting to filter gms/hhaTheoryRecords resource by STI date
        Given logged on as admin instructor user
        When request GET to /api/gms/hhaTheoryRecords with filters by STI date
        Then the specific STI hhaTheoryRecords data will be returned as JSON response


    Scenario: admin instructor user requesting to filter gms/hhaTheoryRecords resource by STI completed
        Given logged on as admin instructor user
        When request GET to /api/gms/hhaTheoryRecords with filters by STI completed
        Then the specific STI hhaTheoryRecords data will be returned as JSON response


    Scenario: admin instructor user requesting to filter gms/hhaTheoryRecords resource by STI topic
        Given logged on as admin instructor user
        When request GET to /api/gms/hhaTheoryRecords with filters by STI topic
        Then the specific STI hhaTheoryRecords data will be returned as JSON response




    Scenario: admin instructor user requesting to filter second instructor gms/hhaRotations resource by STI start_date
        Given logged on as admin instructor user
        When request GET to second instructor /api/gms/hhaRotations with filters by STI start_date
        Then the specific STI second hhaRotations data will be returned as JSON response

    Scenario: admin instructor user requesting to filter second instructor gms/hhaRotations resource by STI end_date
        Given logged on as admin instructor user
        When request GET to second instructor /api/gms/hhaRotations with filters by STI end_date
        Then the specific STI second hhaRotations data will be returned as JSON response

    Scenario: admin instructor user requesting to filter second instructor gms/hhaRotations resource by STI rotation_num
        Given logged on as admin instructor user
        When request GET to second instructor /api/gms/hhaRotations with filters by STI rotation_num
        Then the specific STI second hhaRotations data will be returned as JSON response





    Scenario: STI admin instructor user requesting to filter gms/cnaTheoryRecords resource by ST2 date
        Given logged on as admin instructor user
        When request GET to /api/gms/cnaTheoryRecords with filters by ST2 date
        Then no data will be returned as JSON response


    Scenario: STI admin instructor user requesting to filter gms/cnaTheoryRecords resource by ST2 completed
        Given logged on as admin instructor user
        When request GET to /api/gms/cnaTheoryRecords with filters by ST2 completed
        Then no data will be returned as JSON response


    Scenario: STI admin instructor user requesting to filter gms/cnaTheoryRecords resource by ST2 topic
        Given logged on as admin instructor user
        When request GET to /api/gms/cnaTheoryRecords with filters by ST2 topic
        Then no data will be returned as JSON response


    Scenario: STI admin instructor user requesting to filter gms/hhaTheoryRecords resource by ST2 date
        Given logged on as admin instructor user
        When request GET to /api/gms/hhaTheoryRecords with filters by ST2 date
        Then no data will be returned as JSON response


    Scenario: STI admin instructor user requesting to filter gms/hhaTheoryRecords resource by ST2 completed
        Given logged on as admin instructor user
        When request GET to /api/gms/hhaTheoryRecords with filters by ST2 completed
        Then no data will be returned as JSON response


    Scenario: STI admin instructor user requesting to filter gms/hhaTheoryRecords resource by ST2 topic
        Given logged on as admin instructor user
        When request GET to /api/gms/hhaTheoryRecords with filters by ST2 topic
        Then no data will be returned as JSON response











    Scenario: staff cna instructor user requesting to filter gms/cnaTheoryRecords resource by STI date
        Given logged on as staff cna instructor user
        When request GET to /api/gms/cnaTheoryRecords with filters by STI date
        Then the specific STI cnaTheoryRecords data will be returned as JSON response


    Scenario: staff cna instructor user requesting to filter gms/cnaTheoryRecords resource by STI completed
        Given logged on as staff cna instructor user
        When request GET to /api/gms/cnaTheoryRecords with filters by STI completed
        Then the specific STI cnaTheoryRecords data will be returned as JSON response


    Scenario: staff cna instructor user requesting to filter gms/cnaTheoryRecords resource by STI topic
        Given logged on as staff cna instructor user
        When request GET to /api/gms/cnaTheoryRecords with filters by STI topic
        Then the specific STI cnaTheoryRecords data will be returned as JSON response

    Scenario: staff cna instructor user requesting to filter second instructor gms/cnaTheoryRecords resource by STI date
        Given logged on as staff cna instructor user
        When request GET to second instructor /api/gms/cnaTheoryRecords with filters by STI date
        Then the specific STI second cnaTheoryRecords data will be returned as JSON response

    Scenario: staff cna instructor user requesting to filter second instructor gms/cnaTheoryRecords resource by STI completed
        Given logged on as staff cna instructor user
        When request GET to second instructor /api/gms/cnaTheoryRecords with filters by STI completed
        Then the specific STI second cnaTheoryRecords data will be returned as JSON response

    Scenario: staff cna instructor user requesting to filter second instructor gms/cnaTheoryRecords resource by STI topic
        Given logged on as staff cna instructor user
        When request GET to second instructor /api/gms/cnaTheoryRecords with filters by STI topic
        Then the specific STI second cnaTheoryRecords data will be returned as JSON response

    Scenario: staff cna instructor user requesting to filter gms/hhaTheoryRecords resource by STI date
        Given logged on as staff cna instructor user
        When request GET to /api/gms/hhaTheoryRecords with filters by STI date
        Then will be permission denied


    Scenario: staff cna instructor user requesting to filter gms/hhaTheoryRecords resource by STI completed
        Given logged on as staff cna instructor user
        When request GET to /api/gms/hhaTheoryRecords with filters by STI completed
        Then will be permission denied


    Scenario: staff cna instructor user requesting to filter gms/hhaTheoryRecords resource by STI topic
        Given logged on as staff cna instructor user
        When request GET to /api/gms/hhaTheoryRecords with filters by STI topic
        Then will be permission denied

    Scenario: staff cna instructor user requesting to filter second instructor gms/hhaTheoryRecords resource by STI date
        Given logged on as staff cna instructor user
        When request GET to second instructor /api/gms/hhaTheoryRecords with filters by STI date
        Then will be permission denied

    Scenario: staff cna instructor user requesting to filter second instructor gms/hhaTheoryRecords resource by STI completed
        Given logged on as staff cna instructor user
        When request GET to second instructor /api/gms/hhaTheoryRecords with filters by STI completed
        Then will be permission denied

    Scenario: staff cna instructor user requesting to filter second instructor gms/hhaTheoryRecords resource by STI topic
        Given logged on as staff cna instructor user
        When request GET to second instructor /api/gms/hhaTheoryRecords with filters by STI topic
        Then will be permission denied



    Scenario: STI staff cna instructor user requesting to filter gms/cnaTheoryRecords resource by ST2 date
        Given logged on as staff cna instructor user
        When request GET to /api/gms/cnaTheoryRecords with filters by ST2 date
        Then no data will be returned as JSON response


    Scenario: STI staff cna instructor user requesting to filter gms/cnaTheoryRecords resource by ST2 completed
        Given logged on as staff cna instructor user
        When request GET to /api/gms/cnaTheoryRecords with filters by ST2 completed
        Then no data will be returned as JSON response


    Scenario: STI staff cna instructor user requesting to filter gms/cnaTheoryRecords resource by ST2 topic
        Given logged on as staff cna instructor user
        When request GET to /api/gms/cnaTheoryRecords with filters by ST2 topic
        Then no data will be returned as JSON response


    Scenario: STI staff cna instructor user requesting to filter gms/hhaTheoryRecords resource by ST2 date
        Given logged on as staff cna instructor user
        When request GET to /api/gms/hhaTheoryRecords with filters by ST2 date
        Then will be permission denied


    Scenario: STI staff cna instructor user requesting to filter gms/hhaTheoryRecords resource by ST2 completed
        Given logged on as staff cna instructor user
        When request GET to /api/gms/hhaTheoryRecords with filters by ST2 completed
        Then will be permission denied


    Scenario: STI staff cna instructor user requesting to filter gms/hhaTheoryRecords resource by ST2 topic
        Given logged on as staff cna instructor user
        When request GET to /api/gms/hhaTheoryRecords with filters by ST2 topic
        Then will be permission denied













    Scenario: staff hha instructor user requesting to filter gms/cnaTheoryRecords resource by STI date
        Given logged on as staff hha instructor user
        When request GET to /api/gms/cnaTheoryRecords with filters by STI date
        Then will be permission denied


    Scenario: staff hha instructor user requesting to filter gms/cnaTheoryRecords resource by STI completed
        Given logged on as staff hha instructor user
        When request GET to /api/gms/cnaTheoryRecords with filters by STI completed
        Then will be permission denied


    Scenario: staff hha instructor user requesting to filter gms/cnaTheoryRecords resource by STI topic
        Given logged on as staff hha instructor user
        When request GET to /api/gms/cnaTheoryRecords with filters by STI topic
        Then will be permission denied

    Scenario: staff hha instructor user requesting to filter second instructor gms/cnaTheoryRecords resource by STI date
        Given logged on as staff hha instructor user
        When request GET to second instructor /api/gms/cnaTheoryRecords with filters by STI date
        Then will be permission denied

    Scenario: staff hha instructor user requesting to filter second instructor gms/cnaTheoryRecords resource by STI completed
        Given logged on as staff hha instructor user
        When request GET to second instructor /api/gms/cnaTheoryRecords with filters by STI completed
        Then will be permission denied

    Scenario: staff hha instructor user requesting to filter second instructor gms/cnaTheoryRecords resource by STI topic
        Given logged on as staff hha instructor user
        When request GET to second instructor /api/gms/cnaTheoryRecords with filters by STI topic
        Then will be permission denied

    Scenario: staff hha instructor user requesting to filter gms/hhaTheoryRecords resource by STI date
        Given logged on as staff hha instructor user
        When request GET to /api/gms/hhaTheoryRecords with filters by STI date
        Then the specific STI hhaTheoryRecords data will be returned as JSON response


    Scenario: staff hha instructor user requesting to filter gms/hhaTheoryRecords resource by STI completed
        Given logged on as staff hha instructor user
        When request GET to /api/gms/hhaTheoryRecords with filters by STI completed
        Then the specific STI hhaTheoryRecords data will be returned as JSON response


    Scenario: staff hha instructor user requesting to filter gms/hhaTheoryRecords resource by STI topic
        Given logged on as staff hha instructor user
        When request GET to /api/gms/hhaTheoryRecords with filters by STI topic
        Then the specific STI hhaTheoryRecords data will be returned as JSON response

    Scenario: staff hha instructor user requesting to filter second instructor gms/hhaTheoryRecords resource by STI date
        Given logged on as staff hha instructor user
        When request GET to second instructor /api/gms/hhaTheoryRecords with filters by STI date
        Then the specific STI second hhaTheoryRecords data will be returned as JSON response

    Scenario: staff hha instructor user requesting to filter second instructor gms/hhaTheoryRecords resource by STI completed
        Given logged on as staff hha instructor user
        When request GET to second instructor /api/gms/hhaTheoryRecords with filters by STI completed
        Then the specific STI second hhaTheoryRecords data will be returned as JSON response

    Scenario: staff hha instructor user requesting to filter second instructor gms/hhaTheoryRecords resource by STI topic
        Given logged on as staff hha instructor user
        When request GET to second instructor /api/gms/hhaTheoryRecords with filters by STI topic
        Then the specific STI second hhaTheoryRecords data will be returned as JSON response



    Scenario: STI staff hha instructor user requesting to filter gms/cnaTheoryRecords resource by ST2 date
        Given logged on as staff hha instructor user
        When request GET to /api/gms/cnaTheoryRecords with filters by ST2 date
        Then will be permission denied


    Scenario: STI staff hha instructor user requesting to filter gms/cnaTheoryRecords resource by ST2 completed
        Given logged on as staff hha instructor user
        When request GET to /api/gms/cnaTheoryRecords with filters by ST2 completed
        Then will be permission denied


    Scenario: STI staff hha instructor user requesting to filter gms/cnaTheoryRecords resource by ST2 topic
        Given logged on as staff hha instructor user
        When request GET to /api/gms/cnaTheoryRecords with filters by ST2 topic
        Then will be permission denied


    Scenario: STI staff hha instructor user requesting to filter gms/hhaTheoryRecords resource by ST2 date
        Given logged on as staff hha instructor user
        When request GET to /api/gms/hhaTheoryRecords with filters by ST2 date
        Then no data will be returned as JSON response


    Scenario: STI staff hha instructor user requesting to filter gms/hhaTheoryRecords resource by ST2 completed
        Given logged on as staff hha instructor user
        When request GET to /api/gms/hhaTheoryRecords with filters by ST2 completed
        Then no data will be returned as JSON response


    Scenario: STI staff hha instructor user requesting to filter gms/hhaTheoryRecords resource by ST2 topic
        Given logged on as staff hha instructor user
        When request GET to /api/gms/hhaTheoryRecords with filters by ST2 topic
        Then no data will be returned as JSON response












    Scenario: cna instructor user requesting to filter gms/cnaTheoryRecords resource by STI date
        Given logged on as cna instructor user
        When request GET to /api/gms/cnaTheoryRecords with filters by STI date
        Then the specific STI cnaTheoryRecords data will be returned as JSON response


    Scenario: cna instructor user requesting to filter gms/cnaTheoryRecords resource by STI completed
        Given logged on as cna instructor user
        When request GET to /api/gms/cnaTheoryRecords with filters by STI completed
        Then the specific STI cnaTheoryRecords data will be returned as JSON response


    Scenario: cna instructor user requesting to filter gms/cnaTheoryRecords resource by STI topic
        Given logged on as cna instructor user
        When request GET to /api/gms/cnaTheoryRecords with filters by STI topic
        Then the specific STI cnaTheoryRecords data will be returned as JSON response

    Scenario: cna instructor user requesting to filter second instructor gms/cnaTheoryRecords resource by STI date
        Given logged on as cna instructor user
        When request GET to second instructor /api/gms/cnaTheoryRecords with filters by STI date
        Then no data will be returned as JSON response

    Scenario: cna instructor user requesting to filter second instructor gms/cnaTheoryRecords resource by STI completed
        Given logged on as cna instructor user
        When request GET to second instructor /api/gms/cnaTheoryRecords with filters by STI completed
        Then no desired second instructor cnaTheoryRecords data filterd by completed will be returned as JSON response

    Scenario: cna instructor user requesting to filter second instructor gms/cnaTheoryRecords resource by STI topic
        Given logged on as cna instructor user
        When request GET to second instructor /api/gms/cnaTheoryRecords with filters by STI topic
        Then no data will be returned as JSON response

    Scenario: cna instructor user requesting to filter gms/hhaTheoryRecords resource by STI date
        Given logged on as cna instructor user
        When request GET to /api/gms/hhaTheoryRecords with filters by STI date
        Then will be permission denied


    Scenario: cna instructor user requesting to filter gms/hhaTheoryRecords resource by STI completed
        Given logged on as cna instructor user
        When request GET to /api/gms/hhaTheoryRecords with filters by STI completed
        Then will be permission denied


    Scenario: cna instructor user requesting to filter gms/hhaTheoryRecords resource by STI topic
        Given logged on as cna instructor user
        When request GET to /api/gms/hhaTheoryRecords with filters by STI topic
        Then will be permission denied

    Scenario: cna instructor user requesting to filter second instructor gms/hhaTheoryRecords resource by STI date
        Given logged on as cna instructor user
        When request GET to second instructor /api/gms/hhaTheoryRecords with filters by STI date
        Then will be permission denied

    Scenario: cna instructor user requesting to filter second instructor gms/hhaTheoryRecords resource by STI completed
        Given logged on as cna instructor user
        When request GET to second instructor /api/gms/hhaTheoryRecords with filters by STI completed
        Then will be permission denied

    Scenario: cna instructor user requesting to filter second instructor gms/hhaTheoryRecords resource by STI topic
        Given logged on as cna instructor user
        When request GET to second instructor /api/gms/hhaTheoryRecords with filters by STI topic
        Then will be permission denied



    Scenario: STI cna instructor user requesting to filter gms/cnaTheoryRecords resource by ST2 date
        Given logged on as cna instructor user
        When request GET to /api/gms/cnaTheoryRecords with filters by ST2 date
        Then no data will be returned as JSON response


    Scenario: STI cna instructor user requesting to filter gms/cnaTheoryRecords resource by ST2 completed
        Given logged on as cna instructor user
        When request GET to /api/gms/cnaTheoryRecords with filters by ST2 completed
        Then no data will be returned as JSON response


    Scenario: STI cna instructor user requesting to filter gms/cnaTheoryRecords resource by ST2 topic
        Given logged on as cna instructor user
        When request GET to /api/gms/cnaTheoryRecords with filters by ST2 topic
        Then no data will be returned as JSON response


    Scenario: STI cna instructor user requesting to filter gms/hhaTheoryRecords resource by ST2 date
        Given logged on as cna instructor user
        When request GET to /api/gms/hhaTheoryRecords with filters by ST2 date
        Then will be permission denied


    Scenario: STI cna instructor user requesting to filter gms/hhaTheoryRecords resource by ST2 completed
        Given logged on as cna instructor user
        When request GET to /api/gms/hhaTheoryRecords with filters by ST2 completed
        Then will be permission denied


    Scenario: STI cna instructor user requesting to filter gms/hhaTheoryRecords resource by ST2 topic
        Given logged on as cna instructor user
        When request GET to /api/gms/hhaTheoryRecords with filters by ST2 topic
        Then will be permission denied










    Scenario: hha instructor user requesting to filter gms/cnaTheoryRecords resource by STI date
        Given logged on as hha instructor user
        When request GET to /api/gms/cnaTheoryRecords with filters by STI date
        Then will be permission denied


    Scenario: hha instructor user requesting to filter gms/cnaTheoryRecords resource by STI completed
        Given logged on as hha instructor user
        When request GET to /api/gms/cnaTheoryRecords with filters by STI completed
        Then will be permission denied


    Scenario: hha instructor user requesting to filter gms/cnaTheoryRecords resource by STI topic
        Given logged on as hha instructor user
        When request GET to /api/gms/cnaTheoryRecords with filters by STI topic
        Then will be permission denied

    Scenario: hha instructor user requesting to filter second instructor gms/cnaTheoryRecords resource by STI date
        Given logged on as hha instructor user
        When request GET to second instructor /api/gms/cnaTheoryRecords with filters by STI date
        Then will be permission denied

    Scenario: hha instructor user requesting to filter second instructor gms/cnaTheoryRecords resource by STI completed
        Given logged on as hha instructor user
        When request GET to second instructor /api/gms/cnaTheoryRecords with filters by STI completed
        Then will be permission denied

    Scenario: hha instructor user requesting to filter second instructor gms/cnaTheoryRecords resource by STI topic
        Given logged on as hha instructor user
        When request GET to second instructor /api/gms/cnaTheoryRecords with filters by STI topic
        Then will be permission denied

    Scenario: hha instructor user requesting to filter gms/hhaTheoryRecords resource by STI date
        Given logged on as hha instructor user
        When request GET to /api/gms/hhaTheoryRecords with filters by STI date
        Then the specific STI hhaTheoryRecords data will be returned as JSON response


    Scenario: hha instructor user requesting to filter gms/hhaTheoryRecords resource by STI completed
        Given logged on as hha instructor user
        When request GET to /api/gms/hhaTheoryRecords with filters by STI completed
        Then the specific STI hhaTheoryRecords data will be returned as JSON response


    Scenario: hha instructor user requesting to filter gms/hhaTheoryRecords resource by STI topic
        Given logged on as hha instructor user
        When request GET to /api/gms/hhaTheoryRecords with filters by STI topic
        Then the specific STI hhaTheoryRecords data will be returned as JSON response

    Scenario: hha instructor user requesting to filter second instructor gms/hhaTheoryRecords resource by STI date
        Given logged on as hha instructor user
        When request GET to second instructor /api/gms/hhaTheoryRecords with filters by STI date
        Then the specific STI hhaTheoryRecords data will be returned as JSON response

    Scenario: hha instructor user requesting to filter second instructor gms/hhaTheoryRecords resource by STI completed
        Given logged on as hha instructor user
        When request GET to second instructor /api/gms/hhaTheoryRecords with filters by STI completed
        Then the specific STI hhaTheoryRecords data will be returned as JSON response

    Scenario: hha instructor user requesting to filter second instructor gms/hhaTheoryRecords resource by STI topic
        Given logged on as hha instructor user
        When request GET to second instructor /api/gms/hhaTheoryRecords with filters by STI topic
        Then the specific STI hhaTheoryRecords data will be returned as JSON response



    Scenario: STI hha instructor user requesting to filter gms/cnaTheoryRecords resource by ST2 date
        Given logged on as hha instructor user
        When request GET to /api/gms/cnaTheoryRecords with filters by ST2 date
        Then will be permission denied


    Scenario: STI hha instructor user requesting to filter gms/cnaTheoryRecords resource by ST2 completed
        Given logged on as hha instructor user
        When request GET to /api/gms/cnaTheoryRecords with filters by ST2 completed
        Then will be permission denied


    Scenario: STI hha instructor user requesting to filter gms/cnaTheoryRecords resource by ST2 topic
        Given logged on as hha instructor user
        When request GET to /api/gms/cnaTheoryRecords with filters by ST2 topic
        Then will be permission denied


    Scenario: STI hha instructor user requesting to filter gms/hhaTheoryRecords resource by ST2 date
        Given logged on as hha instructor user
        When request GET to /api/gms/hhaTheoryRecords with filters by ST2 date
        Then no data will be returned as JSON response


    Scenario: STI hha instructor user requesting to filter gms/hhaTheoryRecords resource by ST2 completed
        Given logged on as hha instructor user
        When request GET to /api/gms/hhaTheoryRecords with filters by ST2 completed
        Then no data will be returned as JSON response


    Scenario: STI hha instructor user requesting to filter gms/hhaTheoryRecords resource by ST2 topic
        Given logged on as hha instructor user
        When request GET to /api/gms/hhaTheoryRecords with filters by ST2 topic
        Then no data will be returned as JSON response










    # below are for cna/hhaClinicalRecords
    Scenario: superuser requesting to filter gms/cnaClinicalRecords resource by STI date
        Given logged on as superuser
        When request GET to /api/gms/cnaClinicalRecords with filters by STI date
        Then the specific STI cnaClinicalRecords data will be returned as JSON response


    Scenario: superuser requesting to filter gms/cnaClinicalRecords resource by STI completed
        Given logged on as superuser
        When request GET to /api/gms/cnaClinicalRecords with filters by STI completed
        Then the specific STI cnaClinicalRecords data will be returned as JSON response


    Scenario: superuser requesting to filter gms/cnaClinicalRecords resource by STI topic
        Given logged on as superuser
        When request GET to /api/gms/cnaClinicalRecords with filters by STI topic
        Then the specific STI cnaClinicalRecords data will be returned as JSON response




    Scenario: superuser requesting to filter second instructor gms/cnaClinicalRecords resource by STI date
        Given logged on as superuser
        When request GET to second instructor /api/gms/cnaClinicalRecords with filters by STI date
        Then the specific STI second cnaClinicalRecords data will be returned as JSON response

    Scenario: superuser requesting to filter second instructor gms/cnaClinicalRecords resource by STI completed
        Given logged on as superuser
        When request GET to second instructor /api/gms/cnaClinicalRecords with filters by STI completed
        Then the specific STI second cnaClinicalRecords data will be returned as JSON response

    Scenario: superuser requesting to filter second instructor gms/cnaClinicalRecords resource by STI topic
        Given logged on as superuser
        When request GET to second instructor /api/gms/cnaClinicalRecords with filters by STI topic
        Then the specific STI second cnaClinicalRecords data will be returned as JSON response



    Scenario: superuser requesting to filter gms/hhaClinicalRecords resource by STI date
        Given logged on as superuser
        When request GET to /api/gms/hhaClinicalRecords with filters by STI date
        Then the specific STI hhaClinicalRecords data will be returned as JSON response


    Scenario: superuser requesting to filter gms/hhaClinicalRecords resource by STI completed
        Given logged on as superuser
        When request GET to /api/gms/hhaClinicalRecords with filters by STI completed
        Then the specific STI hhaClinicalRecords data will be returned as JSON response


    Scenario: superuser requesting to filter gms/hhaClinicalRecords resource by STI topic
        Given logged on as superuser
        When request GET to /api/gms/hhaClinicalRecords with filters by STI topic
        Then the specific STI hhaClinicalRecords data will be returned as JSON response




    Scenario: superuser requesting to filter second instructor gms/hhaClinicalRecords resource by STI date
        Given logged on as superuser
        When request GET to second instructor /api/gms/hhaClinicalRecords with filters by STI date
        Then the specific STI second hhaClinicalRecords data will be returned as JSON response


    Scenario: superuser requesting to filter second instructor gms/hhaClinicalRecords resource by STI completed
        Given logged on as superuser
        When request GET to second instructor /api/gms/hhaClinicalRecords with filters by STI completed
        Then the specific STI second hhaClinicalRecords data will be returned as JSON response


    Scenario: superuser requesting to filter second instructor gms/hhaClinicalRecords resource by STI topic
        Given logged on as superuser
        When request GET to second instructor /api/gms/hhaClinicalRecords with filters by STI topic
        Then the specific STI second hhaClinicalRecords data will be returned as JSON response







    Scenario: superuser requesting to filter gms/cnaClinicalRecords resource by ST2 date
        Given logged on as superuser
        When request GET to /api/gms/cnaClinicalRecords with filters by ST2 date
        Then the specific ST2 cnaClinicalRecords data will be returned as JSON response


    Scenario: superuser requesting to filter gms/cnaClinicalRecords resource by ST2 completed
        Given logged on as superuser
        When request GET to /api/gms/cnaClinicalRecords with filters by ST2 completed
        Then the specific ST2 cnaClinicalRecords data will be returned as JSON response


    Scenario: superuser requesting to filter gms/cnaClinicalRecords resource by ST2 topic
        Given logged on as superuser
        When request GET to /api/gms/cnaClinicalRecords with filters by ST2 topic
        Then the specific ST2 cnaClinicalRecords data will be returned as JSON response


    Scenario: superuser requesting to filter gms/hhaClinicalRecords resource by ST2 date
        Given logged on as superuser
        When request GET to /api/gms/hhaClinicalRecords with filters by ST2 date
        Then the specific ST2 hhaClinicalRecords data will be returned as JSON response


    Scenario: superuser requesting to filter gms/hhaClinicalRecords resource by ST2 completed
        Given logged on as superuser
        When request GET to /api/gms/hhaClinicalRecords with filters by ST2 completed
        Then the specific ST2 hhaClinicalRecords data will be returned as JSON response



    Scenario: superuser requesting to filter gms/hhaClinicalRecords resource by ST2 topic
        Given logged on as superuser
        When request GET to /api/gms/hhaClinicalRecords with filters by ST2 topic
        Then the specific ST2 hhaClinicalRecords data will be returned as JSON response
    # remember also a scenario where filter for data for another school? should not appear unless your superuser




    Scenario: admin instructor user requesting to filter gms/cnaClinicalRecords resource by STI date
        Given logged on as admin instructor user
        When request GET to /api/gms/cnaClinicalRecords with filters by STI date
        Then the specific STI cnaClinicalRecords data will be returned as JSON response


    Scenario: admin instructor user requesting to filter gms/cnaClinicalRecords resource by STI completed
        Given logged on as admin instructor user
        When request GET to /api/gms/cnaClinicalRecords with filters by STI completed
        Then the specific STI cnaClinicalRecords data will be returned as JSON response


    Scenario: admin instructor user requesting to filter gms/cnaClinicalRecords resource by STI topic
        Given logged on as admin instructor user
        When request GET to /api/gms/cnaClinicalRecords with filters by STI topic
        Then the specific STI cnaClinicalRecords data will be returned as JSON response




    Scenario: admin instructor user requesting to filter second instructor gms/cnaClinicalRecords resource by STI date
        Given logged on as admin instructor user
        When request GET to second instructor /api/gms/cnaClinicalRecords with filters by STI date
        Then the specific STI second cnaClinicalRecords data will be returned as JSON response

    Scenario: admin instructor user requesting to filter second instructor gms/cnaClinicalRecords resource by STI completed
        Given logged on as admin instructor user
        When request GET to second instructor /api/gms/cnaClinicalRecords with filters by STI completed
        Then the specific STI second cnaClinicalRecords data will be returned as JSON response

    Scenario: admin instructor user requesting to filter second instructor gms/cnaClinicalRecords resource by STI topic
        Given logged on as admin instructor user
        When request GET to second instructor /api/gms/cnaClinicalRecords with filters by STI topic
        Then the specific STI second cnaClinicalRecords data will be returned as JSON response





    Scenario: admin instructor user requesting to filter gms/hhaClinicalRecords resource by STI date
        Given logged on as admin instructor user
        When request GET to /api/gms/hhaClinicalRecords with filters by STI date
        Then the specific STI hhaClinicalRecords data will be returned as JSON response


    Scenario: admin instructor user requesting to filter gms/hhaClinicalRecords resource by STI completed
        Given logged on as admin instructor user
        When request GET to /api/gms/hhaClinicalRecords with filters by STI completed
        Then the specific STI hhaClinicalRecords data will be returned as JSON response


    Scenario: admin instructor user requesting to filter gms/hhaClinicalRecords resource by STI topic
        Given logged on as admin instructor user
        When request GET to /api/gms/hhaClinicalRecords with filters by STI topic
        Then the specific STI hhaClinicalRecords data will be returned as JSON response




    Scenario: admin instructor user requesting to filter second instructor gms/hhaRotations resource by STI start_date
        Given logged on as admin instructor user
        When request GET to second instructor /api/gms/hhaRotations with filters by STI start_date
        Then the specific STI second hhaRotations data will be returned as JSON response

    Scenario: admin instructor user requesting to filter second instructor gms/hhaRotations resource by STI end_date
        Given logged on as admin instructor user
        When request GET to second instructor /api/gms/hhaRotations with filters by STI end_date
        Then the specific STI second hhaRotations data will be returned as JSON response

    Scenario: admin instructor user requesting to filter second instructor gms/hhaRotations resource by STI rotation_num
        Given logged on as admin instructor user
        When request GET to second instructor /api/gms/hhaRotations with filters by STI rotation_num
        Then the specific STI second hhaRotations data will be returned as JSON response





    Scenario: STI admin instructor user requesting to filter gms/cnaClinicalRecords resource by ST2 date
        Given logged on as admin instructor user
        When request GET to /api/gms/cnaClinicalRecords with filters by ST2 date
        Then no data will be returned as JSON response


    Scenario: STI admin instructor user requesting to filter gms/cnaClinicalRecords resource by ST2 completed
        Given logged on as admin instructor user
        When request GET to /api/gms/cnaClinicalRecords with filters by ST2 completed
        Then no data will be returned as JSON response


    Scenario: STI admin instructor user requesting to filter gms/cnaClinicalRecords resource by ST2 topic
        Given logged on as admin instructor user
        When request GET to /api/gms/cnaClinicalRecords with filters by ST2 topic
        Then no data will be returned as JSON response


    Scenario: STI admin instructor user requesting to filter gms/hhaClinicalRecords resource by ST2 date
        Given logged on as admin instructor user
        When request GET to /api/gms/hhaClinicalRecords with filters by ST2 date
        Then no data will be returned as JSON response


    Scenario: STI admin instructor user requesting to filter gms/hhaClinicalRecords resource by ST2 completed
        Given logged on as admin instructor user
        When request GET to /api/gms/hhaClinicalRecords with filters by ST2 completed
        Then no data will be returned as JSON response


    Scenario: STI admin instructor user requesting to filter gms/hhaClinicalRecords resource by ST2 topic
        Given logged on as admin instructor user
        When request GET to /api/gms/hhaClinicalRecords with filters by ST2 topic
        Then no desired ST2 hhaClinicalRecords data filtered by topic will be returned as JSON response







    Scenario: staff cna instructor user requesting to filter gms/cnaClinicalRecords resource by STI date
        Given logged on as staff cna instructor user
        When request GET to /api/gms/cnaClinicalRecords with filters by STI date
        Then the specific STI cnaClinicalRecords data will be returned as JSON response


    Scenario: staff cna instructor user requesting to filter gms/cnaClinicalRecords resource by STI completed
        Given logged on as staff cna instructor user
        When request GET to /api/gms/cnaClinicalRecords with filters by STI completed
        Then the specific STI cnaClinicalRecords data will be returned as JSON response


    Scenario: staff cna instructor user requesting to filter gms/cnaClinicalRecords resource by STI topic
        Given logged on as staff cna instructor user
        When request GET to /api/gms/cnaClinicalRecords with filters by STI topic
        Then the specific STI cnaClinicalRecords data will be returned as JSON response

    Scenario: staff cna instructor user requesting to filter second instructor gms/cnaClinicalRecords resource by STI date
        Given logged on as staff cna instructor user
        When request GET to second instructor /api/gms/cnaClinicalRecords with filters by STI date
        Then the specific STI second cnaClinicalRecords data will be returned as JSON response

    Scenario: staff cna instructor user requesting to filter second instructor gms/cnaClinicalRecords resource by STI completed
        Given logged on as staff cna instructor user
        When request GET to second instructor /api/gms/cnaClinicalRecords with filters by STI completed
        Then the specific STI second cnaClinicalRecords data will be returned as JSON response

    Scenario: staff cna instructor user requesting to filter second instructor gms/cnaClinicalRecords resource by STI topic
        Given logged on as staff cna instructor user
        When request GET to second instructor /api/gms/cnaClinicalRecords with filters by STI topic
        Then the specific STI second cnaClinicalRecords data will be returned as JSON response

    Scenario: staff cna instructor user requesting to filter gms/hhaClinicalRecords resource by STI date
        Given logged on as staff cna instructor user
        When request GET to /api/gms/hhaClinicalRecords with filters by STI date
        Then will be permission denied


    Scenario: staff cna instructor user requesting to filter gms/hhaClinicalRecords resource by STI completed
        Given logged on as staff cna instructor user
        When request GET to /api/gms/hhaClinicalRecords with filters by STI completed
        Then will be permission denied


    Scenario: staff cna instructor user requesting to filter gms/hhaClinicalRecords resource by STI topic
        Given logged on as staff cna instructor user
        When request GET to /api/gms/hhaClinicalRecords with filters by STI topic
        Then will be permission denied

    Scenario: staff cna instructor user requesting to filter second instructor gms/hhaClinicalRecords resource by STI date
        Given logged on as staff cna instructor user
        When request GET to second instructor /api/gms/hhaClinicalRecords with filters by STI date
        Then will be permission denied

    Scenario: staff cna instructor user requesting to filter second instructor gms/hhaClinicalRecords resource by STI completed
        Given logged on as staff cna instructor user
        When request GET to second instructor /api/gms/hhaClinicalRecords with filters by STI completed
        Then will be permission denied

    Scenario: staff cna instructor user requesting to filter second instructor gms/hhaClinicalRecords resource by STI topic
        Given logged on as staff cna instructor user
        When request GET to second instructor /api/gms/hhaClinicalRecords with filters by STI topic
        Then will be permission denied



    Scenario: STI staff cna instructor user requesting to filter gms/cnaClinicalRecords resource by ST2 date
        Given logged on as staff cna instructor user
        When request GET to /api/gms/cnaClinicalRecords with filters by ST2 date
        Then no data will be returned as JSON response


    Scenario: STI staff cna instructor user requesting to filter gms/cnaClinicalRecords resource by ST2 completed
        Given logged on as staff cna instructor user
        When request GET to /api/gms/cnaClinicalRecords with filters by ST2 completed
        Then no data will be returned as JSON response


    Scenario: STI staff cna instructor user requesting to filter gms/cnaClinicalRecords resource by ST2 topic
        Given logged on as staff cna instructor user
        When request GET to /api/gms/cnaClinicalRecords with filters by ST2 topic
        Then no data will be returned as JSON response


    Scenario: STI staff cna instructor user requesting to filter gms/hhaClinicalRecords resource by ST2 date
        Given logged on as staff cna instructor user
        When request GET to /api/gms/hhaClinicalRecords with filters by ST2 date
        Then will be permission denied


    Scenario: STI staff cna instructor user requesting to filter gms/hhaClinicalRecords resource by ST2 completed
        Given logged on as staff cna instructor user
        When request GET to /api/gms/hhaClinicalRecords with filters by ST2 completed
        Then will be permission denied


    Scenario: STI staff cna instructor user requesting to filter gms/hhaClinicalRecords resource by ST2 topic
        Given logged on as staff cna instructor user
        When request GET to /api/gms/hhaClinicalRecords with filters by ST2 topic
        Then will be permission denied













    Scenario: staff hha instructor user requesting to filter gms/cnaClinicalRecords resource by STI date
        Given logged on as staff hha instructor user
        When request GET to /api/gms/cnaClinicalRecords with filters by STI date
        Then will be permission denied


    Scenario: staff hha instructor user requesting to filter gms/cnaClinicalRecords resource by STI completed
        Given logged on as staff hha instructor user
        When request GET to /api/gms/cnaClinicalRecords with filters by STI completed
        Then will be permission denied


    Scenario: staff hha instructor user requesting to filter gms/cnaClinicalRecords resource by STI topic
        Given logged on as staff hha instructor user
        When request GET to /api/gms/cnaClinicalRecords with filters by STI topic
        Then will be permission denied

    Scenario: staff hha instructor user requesting to filter second instructor gms/cnaClinicalRecords resource by STI date
        Given logged on as staff hha instructor user
        When request GET to second instructor /api/gms/cnaClinicalRecords with filters by STI date
        Then will be permission denied

    Scenario: staff hha instructor user requesting to filter second instructor gms/cnaClinicalRecords resource by STI completed
        Given logged on as staff hha instructor user
        When request GET to second instructor /api/gms/cnaClinicalRecords with filters by STI completed
        Then will be permission denied

    Scenario: staff hha instructor user requesting to filter second instructor gms/cnaClinicalRecords resource by STI topic
        Given logged on as staff hha instructor user
        When request GET to second instructor /api/gms/cnaClinicalRecords with filters by STI topic
        Then will be permission denied

    Scenario: staff hha instructor user requesting to filter gms/hhaClinicalRecords resource by STI date
        Given logged on as staff hha instructor user
        When request GET to /api/gms/hhaClinicalRecords with filters by STI date
        Then the specific STI hhaClinicalRecords data will be returned as JSON response

    Scenario: staff hha instructor user requesting to filter gms/hhaClinicalRecords resource by STI completed
        Given logged on as staff hha instructor user
        When request GET to /api/gms/hhaClinicalRecords with filters by STI completed
        Then the specific STI hhaClinicalRecords data will be returned as JSON response


    Scenario: staff hha instructor user requesting to filter gms/hhaClinicalRecords resource by STI topic
        Given logged on as staff hha instructor user
        When request GET to /api/gms/hhaClinicalRecords with filters by STI topic
        Then the specific STI hhaClinicalRecords data will be returned as JSON response

    @current
    Scenario: staff hha instructor user requesting to filter second instructor gms/hhaClinicalRecords resource by STI date
        Given logged on as staff hha instructor user
        When request GET to second instructor /api/gms/hhaClinicalRecords with filters by STI date
        Then the specific STI second hhaClinicalRecords data will be returned as JSON response


    Scenario: staff hha instructor user requesting to filter second instructor gms/hhaClinicalRecords resource by STI completed
        Given logged on as staff hha instructor user
        When request GET to second instructor /api/gms/hhaClinicalRecords with filters by STI completed
        Then the specific STI hhaClinicalRecords data will be returned as JSON response

    @current
    Scenario: staff hha instructor user requesting to filter second instructor gms/hhaClinicalRecords resource by STI topic
        Given logged on as staff hha instructor user
        When request GET to second instructor /api/gms/hhaClinicalRecords with filters by STI topic
        Then the specific STI second hhaClinicalRecords data will be returned as JSON response



    Scenario: STI staff hha instructor user requesting to filter gms/cnaClinicalRecords resource by ST2 date
        Given logged on as staff hha instructor user
        When request GET to /api/gms/cnaClinicalRecords with filters by ST2 date
        Then will be permission denied


    Scenario: STI staff hha instructor user requesting to filter gms/cnaClinicalRecords resource by ST2 completed
        Given logged on as staff hha instructor user
        When request GET to /api/gms/cnaClinicalRecords with filters by ST2 completed
        Then will be permission denied


    Scenario: STI staff hha instructor user requesting to filter gms/cnaClinicalRecords resource by ST2 topic
        Given logged on as staff hha instructor user
        When request GET to /api/gms/cnaClinicalRecords with filters by ST2 topic
        Then will be permission denied


    Scenario: STI staff hha instructor user requesting to filter gms/hhaClinicalRecords resource by ST2 date
        Given logged on as staff hha instructor user
        When request GET to /api/gms/hhaClinicalRecords with filters by ST2 date
        Then no data will be returned as JSON response


    Scenario: STI staff hha instructor user requesting to filter gms/hhaClinicalRecords resource by ST2 completed
        Given logged on as staff hha instructor user
        When request GET to /api/gms/hhaClinicalRecords with filters by ST2 completed
        Then no data will be returned as JSON response


    Scenario: STI staff hha instructor user requesting to filter gms/hhaClinicalRecords resource by ST2 topic
        Given logged on as staff hha instructor user
        When request GET to /api/gms/hhaClinicalRecords with filters by ST2 topic
        Then no desired ST2 hhaClinicalRecords data filtered by topic will be returned as JSON response












    Scenario: cna instructor user requesting to filter gms/cnaClinicalRecords resource by STI date
        Given logged on as cna instructor user
        When request GET to /api/gms/cnaClinicalRecords with filters by STI date
        Then the specific STI cnaClinicalRecords data will be returned as JSON response


    Scenario: cna instructor user requesting to filter gms/cnaClinicalRecords resource by STI completed
        Given logged on as cna instructor user
        When request GET to /api/gms/cnaClinicalRecords with filters by STI completed
        Then the specific STI cnaClinicalRecords data will be returned as JSON response


    Scenario: cna instructor user requesting to filter gms/cnaClinicalRecords resource by STI topic
        Given logged on as cna instructor user
        When request GET to /api/gms/cnaClinicalRecords with filters by STI topic
        Then the specific STI cnaClinicalRecords data will be returned as JSON response

    Scenario: cna instructor user requesting to filter second instructor gms/cnaClinicalRecords resource by STI date
        Given logged on as cna instructor user
        When request GET to second instructor /api/gms/cnaClinicalRecords with filters by STI date
        Then no data will be returned as JSON response

    Scenario: cna instructor user requesting to filter second instructor gms/cnaClinicalRecords resource by STI completed
        Given logged on as cna instructor user
        When request GET to second instructor /api/gms/cnaClinicalRecords with filters by STI completed
        Then no desired second instructor cnaClinicalRecords data will be returned as JSON response

    Scenario: cna instructor user requesting to filter second instructor gms/cnaClinicalRecords resource by STI topic
        Given logged on as cna instructor user
        When request GET to second instructor /api/gms/cnaClinicalRecords with filters by STI topic
        Then no data will be returned as JSON response

    Scenario: cna instructor user requesting to filter gms/hhaClinicalRecords resource by STI date
        Given logged on as cna instructor user
        When request GET to /api/gms/hhaClinicalRecords with filters by STI date
        Then will be permission denied


    Scenario: cna instructor user requesting to filter gms/hhaClinicalRecords resource by STI completed
        Given logged on as cna instructor user
        When request GET to /api/gms/hhaClinicalRecords with filters by STI completed
        Then will be permission denied


    Scenario: cna instructor user requesting to filter gms/hhaClinicalRecords resource by STI topic
        Given logged on as cna instructor user
        When request GET to /api/gms/hhaClinicalRecords with filters by STI topic
        Then will be permission denied

    Scenario: cna instructor user requesting to filter second instructor gms/hhaClinicalRecords resource by STI date
        Given logged on as cna instructor user
        When request GET to second instructor /api/gms/hhaClinicalRecords with filters by STI date
        Then will be permission denied

    Scenario: cna instructor user requesting to filter second instructor gms/hhaClinicalRecords resource by STI completed
        Given logged on as cna instructor user
        When request GET to second instructor /api/gms/hhaClinicalRecords with filters by STI completed
        Then will be permission denied

    Scenario: cna instructor user requesting to filter second instructor gms/hhaClinicalRecords resource by STI topic
        Given logged on as cna instructor user
        When request GET to second instructor /api/gms/hhaClinicalRecords with filters by STI topic
        Then will be permission denied



    Scenario: STI cna instructor user requesting to filter gms/cnaClinicalRecords resource by ST2 date
        Given logged on as cna instructor user
        When request GET to /api/gms/cnaClinicalRecords with filters by ST2 date
        Then no data will be returned as JSON response


    Scenario: STI cna instructor user requesting to filter gms/cnaClinicalRecords resource by ST2 completed
        Given logged on as cna instructor user
        When request GET to /api/gms/cnaClinicalRecords with filters by ST2 completed
        Then no data will be returned as JSON response


    Scenario: STI cna instructor user requesting to filter gms/cnaClinicalRecords resource by ST2 topic
        Given logged on as cna instructor user
        When request GET to /api/gms/cnaClinicalRecords with filters by ST2 topic
        Then no data will be returned as JSON response


    Scenario: STI cna instructor user requesting to filter gms/hhaClinicalRecords resource by ST2 date
        Given logged on as cna instructor user
        When request GET to /api/gms/hhaClinicalRecords with filters by ST2 date
        Then will be permission denied


    Scenario: STI cna instructor user requesting to filter gms/hhaClinicalRecords resource by ST2 completed
        Given logged on as cna instructor user
        When request GET to /api/gms/hhaClinicalRecords with filters by ST2 completed
        Then will be permission denied


    Scenario: STI cna instructor user requesting to filter gms/hhaClinicalRecords resource by ST2 topic
        Given logged on as cna instructor user
        When request GET to /api/gms/hhaClinicalRecords with filters by ST2 topic
        Then will be permission denied










    Scenario: hha instructor user requesting to filter gms/cnaClinicalRecords resource by STI date
        Given logged on as hha instructor user
        When request GET to /api/gms/cnaClinicalRecords with filters by STI date
        Then will be permission denied


    Scenario: hha instructor user requesting to filter gms/cnaClinicalRecords resource by STI completed
        Given logged on as hha instructor user
        When request GET to /api/gms/cnaClinicalRecords with filters by STI completed
        Then will be permission denied


    Scenario: hha instructor user requesting to filter gms/cnaClinicalRecords resource by STI topic
        Given logged on as hha instructor user
        When request GET to /api/gms/cnaClinicalRecords with filters by STI topic
        Then will be permission denied

    Scenario: hha instructor user requesting to filter second instructor gms/cnaClinicalRecords resource by STI date
        Given logged on as hha instructor user
        When request GET to second instructor /api/gms/cnaClinicalRecords with filters by STI date
        Then will be permission denied

    Scenario: hha instructor user requesting to filter second instructor gms/cnaClinicalRecords resource by STI completed
        Given logged on as hha instructor user
        When request GET to second instructor /api/gms/cnaClinicalRecords with filters by STI completed
        Then will be permission denied

    Scenario: hha instructor user requesting to filter second instructor gms/cnaClinicalRecords resource by STI topic
        Given logged on as hha instructor user
        When request GET to second instructor /api/gms/cnaClinicalRecords with filters by STI topic
        Then will be permission denied

    Scenario: hha instructor user requesting to filter gms/hhaClinicalRecords resource by STI date
        Given logged on as hha instructor user
        When request GET to /api/gms/hhaClinicalRecords with filters by STI date
        Then the specific STI hhaClinicalRecords data will be returned as JSON response

    Scenario: hha instructor user requesting to filter gms/hhaClinicalRecords resource by STI completed
        Given logged on as hha instructor user
        When request GET to /api/gms/hhaClinicalRecords with filters by STI completed
        Then the specific STI hhaClinicalRecords data will be returned as JSON response


    Scenario: hha instructor user requesting to filter gms/hhaClinicalRecords resource by STI topic
        Given logged on as hha instructor user
        When request GET to /api/gms/hhaClinicalRecords with filters by STI topic
        Then the specific STI hhaClinicalRecords data will be returned as JSON response

    Scenario: hha instructor user requesting to filter second instructor gms/hhaClinicalRecords resource by STI date
        Given logged on as hha instructor user
        When request GET to second instructor /api/gms/hhaClinicalRecords with filters by STI date
        Then the specific STI hhaClinicalRecords data will be returned as JSON response


    Scenario: hha instructor user requesting to filter second instructor gms/hhaClinicalRecords resource by STI completed
        Given logged on as hha instructor user
        When request GET to second instructor /api/gms/hhaClinicalRecords with filters by STI completed
        Then the specific STI hhaClinicalRecords data will be returned as JSON response

    Scenario: hha instructor user requesting to filter second instructor gms/hhaClinicalRecords resource by STI topic
        Given logged on as hha instructor user
        When request GET to second instructor /api/gms/hhaClinicalRecords with filters by STI topic
        Then the specific STI hhaClinicalRecords data will be returned as JSON response



    Scenario: STI hha instructor user requesting to filter gms/cnaClinicalRecords resource by ST2 date
        Given logged on as hha instructor user
        When request GET to /api/gms/cnaClinicalRecords with filters by ST2 date
        Then will be permission denied


    Scenario: STI hha instructor user requesting to filter gms/cnaClinicalRecords resource by ST2 completed
        Given logged on as hha instructor user
        When request GET to /api/gms/cnaClinicalRecords with filters by ST2 completed
        Then will be permission denied


    Scenario: STI hha instructor user requesting to filter gms/cnaClinicalRecords resource by ST2 topic
        Given logged on as hha instructor user
        When request GET to /api/gms/cnaClinicalRecords with filters by ST2 topic
        Then will be permission denied


    Scenario: STI hha instructor user requesting to filter gms/hhaClinicalRecords resource by ST2 date
        Given logged on as hha instructor user
        When request GET to /api/gms/hhaClinicalRecords with filters by ST2 date
        Then no data will be returned as JSON response


    Scenario: STI hha instructor user requesting to filter gms/hhaClinicalRecords resource by ST2 completed
        Given logged on as hha instructor user
        When request GET to /api/gms/hhaClinicalRecords with filters by ST2 completed
        Then no data will be returned as JSON response


    Scenario: STI hha instructor user requesting to filter gms/hhaClinicalRecords resource by ST2 topic
        Given logged on as hha instructor user
        When request GET to /api/gms/hhaClinicalRecords with filters by ST2 topic
        Then no data will be returned as JSON response
