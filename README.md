# Plant Shop Database
### This is my portfolio project for Nucamp's SQL with Python.
Throughout this project, I utilized several tools including: postgres, docker, pgAdmin, django, insomnia, and many more.


| Property | Description |
| :--- | :----: |
| URL | http://127.0.0.1:8000/api/plants/ |
| Method | GET |
| Success | Http status 200 |
| Failure | Http status 400/500 |

| Property | Description |
| :--- | :----: |
| URL | http://127.0.0.1:8000/api/plants/ |
| Method | POST |
| Success | Http status 200 |
| Failure | Http status 400/500 |
| Content/Media-Type | application/json |

| Property | Description |
| :--- | :----: |
| URL | http://localhost:5000/plants/<int:pk> |
| Method | DELETE |
| Success | Http status 200 |
| Failure | Http status 400/500 |



Within the project, I implemented POST, GET, and DELETE. I have a POST statement to create a new plant in the database, GET a plant by ID or index all existing plants, and DELETE a plant altogether.
In future states, I could implement many more features like creating a user, changing the email for the customer, updating existing plant information,etc.
