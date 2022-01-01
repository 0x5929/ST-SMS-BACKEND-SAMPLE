Feature: Grading Management filter

All user can filter all gms model objects that they have access to based on attributes via GET parameters


# only super users can see records from other school
# all other type of user will fail to GET but users above and below can!
# cna/hhainstructoruser2 will be of ST2, they can also see ST2, but no STI
# instructoruser will have both CNA and HHA will be able to see both all CNA and HHA records in the same school