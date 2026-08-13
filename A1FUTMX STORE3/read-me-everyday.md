1.)Application validation is useful, but critical invariants should ultimately be enforced by the database.

2.)python manage.py showmigrations academics: after creating models
3.)Selectors read data. Services perform business workflows.
HTTP Request
     ↓
    View
     ↓
 Serializer
     ↓
 Selector
     ↓
 Database

 4.)Optimize based on the data the query actually needs, not because an optimization exists.

 5.) rule("Only authorized Course Reps, Lecturers, Vendors, and Admins can upload)