# StudentHub Functional Requirements
The StudentHub is an interactive online multi-user community for students to use student-built academic, social, and 
recreational tools.
 
## General requirements
### User Data and Privacy
All users will have a “profile” with private and public data fields they can fill out at 
their discretion – such as name, email address, and other sensitive data. A user can request 
copies of all data stored on the system associated with them. A user's private data 
will be hidden from non-staff members by default – such as name, email address, and so 
on. However, a user can opt-in to share this data with other users. <BR>

User data not considered sensitive include usernames, nicknames, and other data to be 
determined.
### Passwords
A user shall be able to manually reset their password with a new password that meets 
complexity requirements.
 
## Current Apps
### Trivia: 
A simple trivia game with variable levels of difficulty and categories. Trivia questions include both approved trivia 
submissions and stock trivia questions sourced from OpenTriviaDB under a Creative Common 2.0 license.
- Current Features: Selectable difficulty levels and categories
- Desired Features: trivia question submission – subject to approval.
### Flashcard: 
An app to support learning by presenting digital flashcards for the purpose of study and course concept retentions.
- Current features: Generate and present flashcard deck filtered by subject, course, and module. Additionally, 
  flashcard decks can have varying lengths.
- Desired features:
  - User submitted Flashcards (subject to approval)
  - Admin panel to streamline flashcard approval
  - A “flip” flashcard function to allow more dynamic user interaction
  - Statistical tracking to identify user-specific learning opportunities and “smartly” 
    generate flashcard decks to close knowledge gaps faster

## Future apps:
### Class Scheduler: 
Generate a balanced multi-semester schedule based on anticipated course offerings, course difficulty, desired 
difficulty, course pre-requisites, and other restrictions. <br>
Requirements:
- A staff admin shall be able to add new majors, course, and course requirements.
- A user shall be able to specify preferred schedule requirements and save those requirements for later use in schedule requests.
- A user shall be able to select their major of choice and store it as part of their profile. (this is considered private information)
- A user shall be able to self-report courses taken and performance in that course.
- A user shall be able to request a generated for a semester, multiple semesters, or the number of semesters required to complete their degree.
- A user shall be able to specify instructor preferences in schedule constraints.
- A user shall be able to save generated schedules for review later.

### StudentChat: 
A multi-room encrypted chat service with public and private rooms as well as direct messaging capabilities.

### Battleship: 
A hosted 2 players game with a dedicated host, client ui, and leaderboards.



