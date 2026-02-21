python manage.py import_truckstops --file=data/truckstops.csv
python manage.py import_truckstops --file=data/truckstops.csv


note:“I structured the data to normalize TruckStops and racks. In admin, each TruckStop shows its multiple racks inline, making it easy to manage and query fuel prices efficiently.”

🎯 What Impresses More Than Swagger or Jazzmin
On Day 1, this impresses more:
Proper model indexing
Clean services folder
Management command for CSV import
Well-structured serializers
Clear README structure
Architecture > UI polish.


🏗️ Ideal Build Timeline
✅ Day 1

Django setup

DRF installed

TruckStop model

Import command

Basic APIView skeleton

✅ Day 2

Routing API integration

Polyline decoding

Distance calculation

Fuel segmentation logic

✅ Day 3

Optimization logic

Cheapest stop selection

Cost simulation

Caching

✅ Final Polish (Last 1–2 hours)

Add drf-spectacular (Swagger UI)

Clean README

Record Loom

Optional: Jazzmin if you want



http://127.0.0.1:8000/api/truckstops/
http://127.0.0.1:8000/api/truckstops/?search=Houston
http://127.0.0.1:8000/api/truckstops/?ordering=-retail_price