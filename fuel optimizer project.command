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


Django>=4.2,<5.0
djangorestframework>=3.14
djangorestframework-simplejwt>=5.3
drf-spectacular>=0.27
requests>=2.31
python-dotenv>=1.0
psycopg2-binary>=2.9
django-cors-headers>=4.3
django-filter>=23.5
gunicorn>=21.2
whitenoise>=6.6

http://127.0.0.1:8000/api/truckstops/
http://127.0.0.1:8000/api/truckstops/?search=Houston
http://127.0.0.1:8000/api/truckstops/?ordering=-retail_price



#This command is used for test in Linux or windows system and django server must be running before initiallizing the command :
curl "http://127.0.0.1:8000/api/route?start=-74.0060,40.7128&finish=-118.2437,34.0522"



3️⃣ Using Postman / Insomnia (Recommended)

Tools like Postman or Insomnia are much better for testing APIs.

You can:

Set the method to GET.

Paste the URL.

Send the request and see nicely formatted JSON.