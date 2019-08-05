# Trivia Game
Simple trivia game that quizzes a user, evaluates the answers, and saves 
user-specific results to a leaderboard. The app tracks userid, score %,
 time elapsed, and difficulty.

## Populate Trivia questions
The app has a populate script. In commandline, from the django project root 
(~/studenthub/)virtual environment, type: <br>
`python manage.py populate_trivia`

## Adjust Score Weights
Scores as weighted based on difficulty. Initially, all difficulties carry the same 
weight with a 1 scalar value. Modify this as appropriate for the Difficulty model in 
the relevant section of the django admin panel at: <br>
http://127.0.0.1:8000/admin/

#License
The question data provided in trivia app is available under the Creative Commons 
Attribution-ShareAlike 4.0 International License. Data was sourced from 
https://opentdb.com/api_config.php

https://creativecommons.org/licenses/by-sa/4.0/