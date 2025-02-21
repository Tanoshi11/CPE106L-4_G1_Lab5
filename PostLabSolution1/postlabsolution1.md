Table Participant {
    ParticipantID int [pk]  // Primary Key
    LastName varchar
    FirstName varchar
    Address varchar
    City varchar
    State varchar
    PostalCode varchar
    PhoneNumber varchar
    DateOfBirth date
}

Table AdventureClass {
    ClassID int [pk]  // Primary Key
    ClassDescription varchar
    MaxParticipants int
    ClassFee decimal
}

Table ClassSchedule {
    ClassScheduleID int [pk]  // Primary Key
    ClassID int [ref: > AdventureClass.ClassID]  // Foreign Key
    ClassDate date
}

Table Enrollment {
    ParticipantID int [ref: > Participant.ParticipantID]  // Foreign Key
    ClassScheduleID int [ref: > ClassSchedule.ClassScheduleID]  // Foreign Key
}
