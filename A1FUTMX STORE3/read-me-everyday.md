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