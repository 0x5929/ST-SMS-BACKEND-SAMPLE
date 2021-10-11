Feature: Student Management System
  when regular user logs onto sms system
  only is_office can have permissions on sms
  will have READ access to all sms endpoints
  will have POST/PUT/PATCH access to sms students endpoints
  can filter student query by student parameters
  and everything is done only to user's own school

  when staff user logs onto sms system
  only is_office can have permissions on sms
  will have READ access to all sms endpoints
  will have POST/PUT/PATCH/DELETE access to sms students, rotations endpoints
  can filter student query by student parameters
  and everything is done only to user's own school

  when admin user logs onto sms system
  only is_office can have permissions on sms
  will have READ access to all sms endpoints
  will have POST/PUT/PATCH/DELETE access to sms students, rotations, programs endpoints
  can filter student query by student parameters
  and everything is done only to user's own school

  when super user logs onto sms system
  will have GET/POST/PUT/PATCH/DELETE access to all sms endpoints
  can filter student query by student parameters
  and can do everything regardless of the school

  Scenario: logs onto sms system as a regular user
      Given logged on regular user is a office user
       When requesting GET to all sms end points
       Then each endpoing will return JSON responses

  Scenario: logs onto sms system as a regular user
      Given logged on regular user is a office user
       When requesting POST/PUT/PATCH to sms students endpoint
       Then database will conduct the same operation using the JSON request body

  Scenario: logs onto sms system as a regular user
      Given logged on regular user is a office user
       When requesting POST/PUT/PATCH to other sms endpoints 
       Then will receive permission denied 403

  Scenario: logs onto sms system as a regular user
      Given logged on regular user is a office user
       When requesting DELETE to all sms endpoints
       Then will receive permission denied 403