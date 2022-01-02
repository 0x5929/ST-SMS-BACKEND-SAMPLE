Feature: Grading Management filter

    All user can filter all gms model objects that they have access to based on attributes via GET parameters

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