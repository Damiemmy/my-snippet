The 5-hour execution

I'd structure the session roughly like this:

Hour 1 — Foundation

Django project
PostgreSQL
domain apps
custom User
roles
authentication
base configuration
environment variables

Hour 2 — Users + Marketplace

profiles
categories
services
provider services
portfolio
provider discovery/search

Hour 3 — Request + Quote

service requests
quote system
permissions
selectors
services
validation
quote lifecycle

Hour 4 — Booking + Reviews + Notifications

quote acceptance
atomic booking creation
booking state transitions
completion
reviews
notifications

Hour 5 — Professionalization

critical tests
constraints
edge cases
permissions audit
API documentation
admin
security/configuration review
full end-to-end test
One thing I would NOT do

I wouldn't spend those 5 hours trying to build:

payments
real-time chat
WebSockets
Celery/Redis
AI matching
recommendation engine
email/SMS infrastructure
advanced provider verification
analytics
complicated event architecture

Those are post-MVP systems.