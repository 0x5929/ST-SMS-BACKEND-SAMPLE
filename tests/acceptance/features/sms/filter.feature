Feature: Student Management filter

    All office users can filter student model objects based on student attributes via GET parameters

    Scenario: superuser requesting to filter sms/students resource by school
        Given logged on as superuser
        When request GET to /api/sms/students with filters by school name
        Then the specific students data will be returned as JSON response


    Scenario: superuser requesting to filter sms/students resource by program
        Given logged on as superuser
        When request GET to /api/sms/students with filters by program name
        Then the specific students data will be returned as JSON response


    Scenario: superuser requesting to filter sms/students resource by rotation
        Given logged on as superuser
        When request GET to /api/sms/students with filters by rotation number
        Then the specific students data will be returned as JSON response


    Scenario: superuser requesting to filter sms/students resource by student first name
        Given logged on as superuser
        When request GET to /api/sms/students with filters by student first name
        Then the specific students data will be returned as JSON response


    Scenario: superuser requesting to filter sms/students resource by student last name
        Given logged on as superuser
        When request GET to /api/sms/students with filters by student last name
        Then the specific students data will be returned as JSON response


    Scenario: superuser requesting to filter sms/students resource by student email
        Given logged on as superuser
        When request GET to /api/sms/students with filters by student email
        Then the specific students data will be returned as JSON response

    Scenario: superuser requesting to filter sms/students resource by student phone
        Given logged on as superuser
        When request GET to /api/sms/students with filters by student phone number
        Then the specific students data will be returned as JSON response


    Scenario: superuser requesting to filter sms/students resource by student ID
        Given logged on as superuser
        When request GET to /api/sms/students with filters by student ID
        Then the specific students data will be returned as JSON response


    Scenario: superuser requesting to filter sms/students resource by student program start date
        Given logged on as superuser
        When request GET to /api/sms/students with filters by student program start date
        Then the specific students data will be returned as JSON response


    Scenario: superuser requesting to filter sms/students resource by student program end date
        Given logged on as superuser
        When request GET to /api/sms/students with filters by student program end date
        Then the specific students data will be returned as JSON response


    Scenario: superuser requesting to filter sms/students resource by student payment completions
        Given logged on as superuser
        When request GET to /api/sms/students with filters by student payment completions
        Then the specific students data will be returned as JSON response



    Scenario: superuser requesting to filter sms/students resource by student program completions
        Given logged on as superuser
        When request GET to /api/sms/students with filters by student program completions
        Then the specific students data will be returned as JSON response



    Scenario: superuser requesting to filter sms/students resource by student employment status
        Given logged on as superuser
        When request GET to /api/sms/students with filters by student employment status
        Then the specific students data will be returned as JSON response

    Scenario: admin office user requesting to filter sms/students resource by school
        Given logged on as admin office user
        When request GET to /api/sms/students with filters by school name
        Then the specific students data will be returned as JSON response


    Scenario: admin office user requesting to filter sms/students resource by program
        Given logged on as admin office user
        When request GET to /api/sms/students with filters by program name
        Then the specific students data will be returned as JSON response


    Scenario: admin office user requesting to filter sms/students resource by rotation
        Given logged on as admin office user
        When request GET to /api/sms/students with filters by rotation number
        Then the specific students data will be returned as JSON response


    Scenario: admin office user requesting to filter sms/students resource by student first name
        Given logged on as admin office user
        When request GET to /api/sms/students with filters by student first name
        Then the specific students data will be returned as JSON response


    Scenario: admin office user requesting to filter sms/students resource by student last name
        Given logged on as admin office user
        When request GET to /api/sms/students with filters by student last name
        Then the specific students data will be returned as JSON response


    Scenario: admin office user requesting to filter sms/students resource by student email
        Given logged on as admin office user
        When request GET to /api/sms/students with filters by student email
        Then the specific students data will be returned as JSON response


    Scenario: admin office user requesting to filter sms/students resource by student phone
        Given logged on as admin office user
        When request GET to /api/sms/students with filters by student phone number
        Then the specific students data will be returned as JSON response


    Scenario: admin office user requesting to filter sms/students resource by student ID
        Given logged on as admin office user
        When request GET to /api/sms/students with filters by student ID
        Then the specific students data will be returned as JSON response


    Scenario: admin office user requesting to filter sms/students resource by student program start date
        Given logged on as admin office user
        When request GET to /api/sms/students with filters by student program start date
        Then the specific students data will be returned as JSON response


    Scenario: admin office user requesting to filter sms/students resource by student program end date
        Given logged on as admin office user
        When request GET to /api/sms/students with filters by student program end date
        Then the specific students data will be returned as JSON response


    Scenario: admin office user requesting to filter sms/students resource by student payment completions
        Given logged on as admin office user
        When request GET to /api/sms/students with filters by student payment completions
        Then the specific students data will be returned as JSON response


    Scenario: admin office user requesting to filter sms/students resource by student program completions
        Given logged on as admin office user
        When request GET to /api/sms/students with filters by student program completions
        Then the specific students data will be returned as JSON response

    Scenario: admin office user requesting to filter sms/students resource by student employment status
        Given logged on as admin office user
        When request GET to /api/sms/students with filters by student employment status
        Then the specific students data will be returned as JSON response

    Scenario: staff office user requesting to filter sms/students resource by school
        Given logged on as staff office user
        When request GET to /api/sms/students with filters by school name
        Then the specific students data will be returned as JSON response


    Scenario: staff office user requesting to filter sms/students resource by program
        Given logged on as staff office user
        When request GET to /api/sms/students with filters by program name
        Then the specific students data will be returned as JSON response


    Scenario: staff office user requesting to filter sms/students resource by rotation
        Given logged on as staff office user
        When request GET to /api/sms/students with filters by rotation number
        Then the specific students data will be returned as JSON response


    Scenario: staff office user requesting to filter sms/students resource by student first name
        Given logged on as staff office user
        When request GET to /api/sms/students with filters by student first name
        Then the specific students data will be returned as JSON response


    Scenario: staff office user requesting to filter sms/students resource by student last name
        Given logged on as staff office user
        When request GET to /api/sms/students with filters by student last name
        Then the specific students data will be returned as JSON response


    Scenario: staff office user requesting to filter sms/students resource by student email
        Given logged on as staff office user
        When request GET to /api/sms/students with filters by student email
        Then the specific students data will be returned as JSON response


    Scenario: staff office user requesting to filter sms/students resource by student phone
        Given logged on as staff office user
        When request GET to /api/sms/students with filters by student phone number
        Then the specific students data will be returned as JSON response


    Scenario: staff office user requesting to filter sms/students resource by student ID
        Given logged on as staff office user
        When request GET to /api/sms/students with filters by student ID
        Then the specific students data will be returned as JSON response


    Scenario: staff office user requesting to filter sms/students resource by student program start date
        Given logged on as staff office user
        When request GET to /api/sms/students with filters by student program start date
        Then the specific students data will be returned as JSON response


    Scenario: staff office user requesting to filter sms/students resource by student program end date
        Given logged on as staff office user
        When request GET to /api/sms/students with filters by student program end date
        Then the specific students data will be returned as JSON response


    Scenario: staff office user requesting to filter sms/students resource by student payment completions
        Given logged on as staff office user
        When request GET to /api/sms/students with filters by student payment completions
        Then the specific students data will be returned as JSON response



    Scenario: staff office user requesting to filter sms/students resource by student program completions
        Given logged on as staff office user
        When request GET to /api/sms/students with filters by student program completions
        Then the specific students data will be returned as JSON response



    Scenario: staff office user requesting to filter sms/students resource by student employment status
        Given logged on as staff office user
        When request GET to /api/sms/students with filters by student employment status
        Then the specific students data will be returned as JSON response

    Scenario: regular office user requesting to filter sms/students resource by school
        Given logged on as regular office user
        When request GET to /api/sms/students with filters by school name
        Then the specific students data will be returned as JSON response


    Scenario: regular office user requesting to filter sms/students resource by program
        Given logged on as regular office user
        When request GET to /api/sms/students with filters by program name
        Then the specific students data will be returned as JSON response


    Scenario: regular office user requesting to filter sms/students resource by rotation
        Given logged on as regular office user
        When request GET to /api/sms/students with filters by rotation number
        Then the specific students data will be returned as JSON response


    Scenario: regular office user requesting to filter sms/students resource by student first name
        Given logged on as regular office user
        When request GET to /api/sms/students with filters by student first name
        Then the specific students data will be returned as JSON response


    Scenario: regular office user requesting to filter sms/students resource by student last name
        Given logged on as regular office user
        When request GET to /api/sms/students with filters by student last name
        Then the specific students data will be returned as JSON response


    Scenario: regular office user requesting to filter sms/students resource by student email
        Given logged on as regular office user
        When request GET to /api/sms/students with filters by student email
        Then the specific students data will be returned as JSON response


    Scenario: regular office user requesting to filter sms/students resource by student phone
        Given logged on as regular office user
        When request GET to /api/sms/students with filters by student phone number
        Then the specific students data will be returned as JSON response


    Scenario: regular office user requesting to filter sms/students resource by student ID
        Given logged on as regular office user
        When request GET to /api/sms/students with filters by student ID
        Then the specific students data will be returned as JSON response


    Scenario: regular office user requesting to filter sms/students resource by student program start date
        Given logged on as regular office user
        When request GET to /api/sms/students with filters by student program start date
        Then the specific students data will be returned as JSON response


    Scenario: regular office user requesting to filter sms/students resource by student program end date
        Given logged on as regular office user
        When request GET to /api/sms/students with filters by student program end date
        Then the specific students data will be returned as JSON response


    Scenario: regular office user requesting to filter sms/students resource by student payment completions
        Given logged on as regular office user
        When request GET to /api/sms/students with filters by student payment completions
        Then the specific students data will be returned as JSON response



    Scenario: regular office user requesting to filter sms/students resource by student program completions
        Given logged on as regular office user
        When request GET to /api/sms/students with filters by student program completions
        Then the specific students data will be returned as JSON response



    Scenario: regular office user requesting to filter sms/students resource by student employment status
        Given logged on as regular office user
        When request GET to /api/sms/students with filters by student employment status
        Then the specific students data will be returned as JSON response




















    Scenario: superuser requesting to filter sms/students resource by ST2 school
        Given logged on as superuser
        When request GET to /api/sms/students with filters by ST2 school name
        Then the specific ST2 students data will be returned as JSON response


    Scenario: superuser requesting to filter sms/students resource by ST2 program
        Given logged on as superuser
        When request GET to /api/sms/students with filters by ST2 program name
        Then the specific ST2 students data will be returned as JSON response


    Scenario: superuser requesting to filter sms/students resource by ST2 rotation
        Given logged on as superuser
        When request GET to /api/sms/students with filters by ST2 rotation number
        Then the specific ST2 students data will be returned as JSON response


    Scenario: superuser requesting to filter sms/students resource by ST2 student first name
        Given logged on as superuser
        When request GET to /api/sms/students with filters by ST2 student first name
        Then the specific ST2 students data will be returned as JSON response


    Scenario: superuser requesting to filter sms/students resource by ST2 student last name
        Given logged on as superuser
        When request GET to /api/sms/students with filters by ST2 student last name
        Then the specific ST2 students data will be returned as JSON response


    Scenario: superuser requesting to filter sms/students resource by ST2 student email
        Given logged on as superuser
        When request GET to /api/sms/students with filters by ST2 student email
        Then the specific ST2 students data will be returned as JSON response

    Scenario: superuser requesting to filter sms/students resource by ST2 student phone
        Given logged on as superuser
        When request GET to /api/sms/students with filters by ST2 student phone number
        Then the specific ST2 students data will be returned as JSON response


    Scenario: superuser requesting to filter sms/students resource by ST2 student ID
        Given logged on as superuser
        When request GET to /api/sms/students with filters by ST2 student ID
        Then the specific ST2 students data will be returned as JSON response


    Scenario: superuser requesting to filter sms/students resource by ST2 student program start date
        Given logged on as superuser
        When request GET to /api/sms/students with filters by ST2 student program start date
        Then the specific ST2 students data will be returned as JSON response


    Scenario: superuser requesting to filter sms/students resource by ST2 student program end date
        Given logged on as superuser
        When request GET to /api/sms/students with filters by ST2 student program end date
        Then the specific ST2 students data will be returned as JSON response


    Scenario: superuser requesting to filter sms/students resource by ST2 student payment completions
        Given logged on as superuser
        When request GET to /api/sms/students with filters by ST2 student payment completions
        Then the specific ST2 students data will be returned as JSON response



    Scenario: superuser requesting to filter sms/students resource by ST2 student program completions
        Given logged on as superuser
        When request GET to /api/sms/students with filters by ST2 student program completions
        Then the specific ST2 students data will be returned as JSON response



    Scenario: superuser requesting to filter sms/students resource by ST2 student employment status
        Given logged on as superuser
        When request GET to /api/sms/students with filters by ST2 student employment status
        Then the specific ST2 students data will be returned as JSON response


    Scenario: admin office user requesting to filter sms/students resource by ST2 school
        Given logged on as admin office user
        When request GET to /api/sms/students with filters by ST2 school name
        Then no data will be returned as JSON response


    Scenario: admin office user requesting to filter sms/students resource by ST2 program
        Given logged on as admin office user
        When request GET to /api/sms/students with filters by ST2 program name
        Then no desired ST2 students data filtered by rotation or program will be returned as JSON response


    Scenario: admin office user requesting to filter sms/students resource by ST2 rotation
        Given logged on as admin office user
        When request GET to /api/sms/students with filters by ST2 rotation number
        Then no desired ST2 students data filtered by rotation or program will be returned as JSON response

    Scenario: admin office user requesting to filter sms/students resource by ST2 student first name
        Given logged on as admin office user
        When request GET to /api/sms/students with filters by ST2 student first name
        Then no data will be returned as JSON response


    Scenario: admin office user requesting to filter sms/students resource by ST2 student last name
        Given logged on as admin office user
        When request GET to /api/sms/students with filters by ST2 student last name
        Then no data will be returned as JSON response


    Scenario: admin office user requesting to filter sms/students resource by ST2 student email
        Given logged on as admin office user
        When request GET to /api/sms/students with filters by ST2 student email
        Then no data will be returned as JSON response


    Scenario: admin office user requesting to filter sms/students resource by ST2 student phone
        Given logged on as admin office user
        When request GET to /api/sms/students with filters by ST2 student phone number
        Then no data will be returned as JSON response


    Scenario: admin office user requesting to filter sms/students resource by ST2 student ID
        Given logged on as admin office user
        When request GET to /api/sms/students with filters by ST2 student ID
        Then no data will be returned as JSON response


    Scenario: admin office user requesting to filter sms/students resource by ST2 student program start date
        Given logged on as admin office user
        When request GET to /api/sms/students with filters by ST2 student program start date
        Then no data will be returned as JSON response


    Scenario: admin office user requesting to filter sms/students resource by ST2 student program end date
        Given logged on as admin office user
        When request GET to /api/sms/students with filters by ST2 student program end date
        Then no data will be returned as JSON response


    Scenario: admin office user requesting to filter sms/students resource by ST2 student payment completions
        Given logged on as admin office user
        When request GET to /api/sms/students with filters by ST2 student payment completions
        Then no data will be returned as JSON response


    Scenario: admin office user requesting to filter sms/students resource by ST2 student program completions
        Given logged on as admin office user
        When request GET to /api/sms/students with filters by ST2 student program completions
        Then no data will be returned as JSON response

    Scenario: admin office user requesting to filter sms/students resource by ST2 student employment status
        Given logged on as admin office user
        When request GET to /api/sms/students with filters by ST2 student employment status
        Then no data will be returned as JSON response

    Scenario: staff office user requesting to filter sms/students resource by ST2 school
        Given logged on as staff office user
        When request GET to /api/sms/students with filters by ST2 school name
        Then no data will be returned as JSON response


    Scenario: staff office user requesting to filter sms/students resource by ST2 program
        Given logged on as staff office user
        When request GET to /api/sms/students with filters by ST2 program name
        Then no desired ST2 students data filtered by rotation or program will be returned as JSON response


    Scenario: staff office user requesting to filter sms/students resource by ST2 rotation
        Given logged on as staff office user
        When request GET to /api/sms/students with filters by ST2 rotation number
        Then no desired ST2 students data filtered by rotation or program will be returned as JSON response


    Scenario: staff office user requesting to filter sms/students resource by ST2 student first name
        Given logged on as staff office user
        When request GET to /api/sms/students with filters by ST2 student first name
        Then no data will be returned as JSON response


    Scenario: staff office user requesting to filter sms/students resource by ST2 student last name
        Given logged on as staff office user
        When request GET to /api/sms/students with filters by ST2 student last name
        Then no data will be returned as JSON response


    Scenario: staff office user requesting to filter sms/students resource by ST2 student email
        Given logged on as staff office user
        When request GET to /api/sms/students with filters by ST2 student email
        Then no data will be returned as JSON response


    Scenario: staff office user requesting to filter sms/students resource by ST2 student phone
        Given logged on as staff office user
        When request GET to /api/sms/students with filters by ST2 student phone number
        Then no data will be returned as JSON response


    Scenario: staff office user requesting to filter sms/students resource by ST2 student ID
        Given logged on as staff office user
        When request GET to /api/sms/students with filters by ST2 student ID
        Then no data will be returned as JSON response


    Scenario: staff office user requesting to filter sms/students resource by ST2 student program start date
        Given logged on as staff office user
        When request GET to /api/sms/students with filters by ST2 student program start date
        Then no data will be returned as JSON response


    Scenario: staff office user requesting to filter sms/students resource by ST2 student program end date
        Given logged on as staff office user
        When request GET to /api/sms/students with filters by ST2 student program end date
        Then no data will be returned as JSON response


    Scenario: staff office user requesting to filter sms/students resource by ST2 student payment completions
        Given logged on as staff office user
        When request GET to /api/sms/students with filters by ST2 student payment completions
        Then no data will be returned as JSON response



    Scenario: staff office user requesting to filter sms/students resource by ST2 student program completions
        Given logged on as staff office user
        When request GET to /api/sms/students with filters by ST2 student program completions
        Then no data will be returned as JSON response



    Scenario: staff office user requesting to filter sms/students resource by ST2 student employment status
        Given logged on as staff office user
        When request GET to /api/sms/students with filters by ST2 student employment status
        Then no data will be returned as JSON response

    Scenario: regular office user requesting to filter sms/students resource by ST2 school
        Given logged on as regular office user
        When request GET to /api/sms/students with filters by ST2 school name
        Then no data will be returned as JSON response


    Scenario: regular office user requesting to filter sms/students resource by ST2 program
        Given logged on as regular office user
        When request GET to /api/sms/students with filters by ST2 program name
        Then no desired ST2 students data filtered by rotation or program will be returned as JSON response


    Scenario: regular office user requesting to filter sms/students resource by ST2 rotation
        Given logged on as regular office user
        When request GET to /api/sms/students with filters by ST2 rotation number
        Then no desired ST2 students data filtered by rotation or program will be returned as JSON response


    Scenario: regular office user requesting to filter sms/students resource by ST2 student first name
        Given logged on as regular office user
        When request GET to /api/sms/students with filters by ST2 student first name
        Then no data will be returned as JSON response


    Scenario: regular office user requesting to filter sms/students resource by ST2 student last name
        Given logged on as regular office user
        When request GET to /api/sms/students with filters by ST2 student last name
        Then no data will be returned as JSON response


    Scenario: regular office user requesting to filter sms/students resource by ST2 student email
        Given logged on as regular office user
        When request GET to /api/sms/students with filters by ST2 student email
        Then no data will be returned as JSON response


    Scenario: regular office user requesting to filter sms/students resource by ST2 student phone
        Given logged on as regular office user
        When request GET to /api/sms/students with filters by ST2 student phone number
        Then no data will be returned as JSON response


    Scenario: regular office user requesting to filter sms/students resource by ST2 student ID
        Given logged on as regular office user
        When request GET to /api/sms/students with filters by ST2 student ID
        Then no data will be returned as JSON response


    Scenario: regular office user requesting to filter sms/students resource by ST2 student program start date
        Given logged on as regular office user
        When request GET to /api/sms/students with filters by ST2 student program start date
        Then no data will be returned as JSON response


    Scenario: regular office user requesting to filter sms/students resource by ST2 student program end date
        Given logged on as regular office user
        When request GET to /api/sms/students with filters by ST2 student program end date
        Then no data will be returned as JSON response


    Scenario: regular office user requesting to filter sms/students resource by ST2 student payment completions
        Given logged on as regular office user
        When request GET to /api/sms/students with filters by ST2 student payment completions
        Then no data will be returned as JSON response



    Scenario: regular office user requesting to filter sms/students resource by ST2 student program completions
        Given logged on as regular office user
        When request GET to /api/sms/students with filters by ST2 student program completions
        Then no data will be returned as JSON response



    Scenario: regular office user requesting to filter sms/students resource by ST2 student employment status
        Given logged on as regular office user
        When request GET to /api/sms/students with filters by ST2 student employment status
        Then no data will be returned as JSON response








    @current
    Scenario: superuser requesting to filter sms/rotations resource by program name
        Given logged on as superuser
        When request GET to /api/sms/rotations with filters by program name
        Then the specific rotation data will be returned as JSON response

    @current
    Scenario: admin office user requesting to filter sms/rotations resource by program name
        Given logged on as admin office user
        When request GET to /api/sms/rotations with filters by program name
        Then the specific rotation data will be returned as JSON response

    @current
    Scenario: staff office user requesting to filter sms/rotations resource by program name
        Given logged on as staff office user
        When request GET to /api/sms/rotations with filters by program name
        Then the specific rotation data will be returned as JSON response

    @current
    Scenario: regular office user requesting to filter sms/rotations resource by program name
        Given logged on as regular office user
        When request GET to /api/sms/rotations with filters by program name
        Then the specific rotation data will be returned as JSON response





    @current
    Scenario: superuser requesting to filter sms/rotations resource by school name
        Given logged on as superuser
        When request GET to /api/sms/rotations with filters by school name
        Then the specific rotation data will be returned as JSON response

    @current
    Scenario: admin office user requesting to filter sms/rotations resource by school name
        Given logged on as admin office user
        When request GET to /api/sms/rotations with filters by school name
        Then the specific rotation data will be returned as JSON response

    @current
    Scenario: staff office user requesting to filter sms/rotations resource by school name
        Given logged on as staff office user
        When request GET to /api/sms/rotations with filters by school name
        Then the specific rotation data will be returned as JSON response

    @current
    Scenario: regular office user requesting to filter sms/rotations resource by school name
        Given logged on as regular office user
        When request GET to /api/sms/rotations with filters by school name
        Then the specific rotation data will be returned as JSON response















    @current
    Scenario: superuser requesting to filter sms/rotations resource by rotation number
        Given logged on as superuser
        When request GET to /api/sms/rotations with filters by rotation number
        Then the specific rotation data will be returned as JSON response

    @current
    Scenario: admin office user requesting to filter sms/rotations resource by rotation number
        Given logged on as admin office user
        When request GET to /api/sms/rotations with filters by rotation number
        Then the specific rotation data will be returned as JSON response

    @current
    Scenario: staff office user requesting to filter sms/rotations resource by rotation number
        Given logged on as staff office user
        When request GET to /api/sms/rotations with filters by rotation number
        Then the specific rotation data will be returned as JSON response

    @current
    Scenario: regular office user requesting to filter sms/rotations resource by rotation number
        Given logged on as regular office user
        When request GET to /api/sms/rotations with filters by rotation number
        Then the specific rotation data will be returned as JSON response












    @current
    Scenario: superuser requesting to filter sms/programs resource by school name
        Given logged on as superuser
        When request GET to /api/sms/programs with filters by school name
        Then the specific program data will be returned as JSON response

    @current
    Scenario: admin office user requesting to filter sms/programs resource by school name
        Given logged on as admin office user
        When request GET to /api/sms/programs with filters by school name
        Then the specific program data will be returned as JSON response

    @current
    Scenario: staff office user requesting to filter sms/programs resource by school name
        Given logged on as staff office user
        When request GET to /api/sms/programs with filters by school name
        Then the specific program data will be returned as JSON response

    @current
    Scenario: regular office user requesting to filter sms/programs resource by school name
        Given logged on as regular office user
        When request GET to /api/sms/programs with filters by school name
        Then the specific program data will be returned as JSON response

