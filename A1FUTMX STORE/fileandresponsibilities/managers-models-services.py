1.)managers.py:
Our Manager's Responsibility
A custom manager should answer questions like:
    How is a normal user created?
    How is a superuser created?
    What fields are required?
    What validation should happen?

Notice something.
This isn't business logic.
It's object creation logic.

That's why it belongs in the manager.

secondly:
    When creating a user,
    what should it validate?
    What should it normalize?
    How should it hash the password?
    How should it create a superuser?
    That's your job.
    That's why we write a custom manager.


major role of managers.py file:
    - create_user()
    - create_superuser()
2.)models.py.
    - models.py answers:What is a User? while
    - managers.py answers:How do we create Users?

3.)services/.
contains:
    - register()
    - login()
    - send_email()
    - verify()
    - approve()


| File           | Responsibility                                                     |
| -------------- | ------------------------------------------------------------------ |
| `models.py`    | Defines what a `User` is                                           |
| `managers.py`  | Defines how `User` objects are created                             |
| `services.py`  | Defines business workflows (registration, verification, approvals) |
| `selectors.py` | Defines reusable read/query logic                                  |
| `views.py`     | Handles HTTP requests and responses                                |

This separation is one of the reasons large Django codebases remain maintainable.

2.)selectors.py:Defines reusable read/query logic
Find user by email

Find verified users

Find active users

Find lecturers