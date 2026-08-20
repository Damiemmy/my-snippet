5. One important performance point

Remember your selector:

Material.objects.select_related(
    "course",
    "uploaded_by",
)

and:

.order_by("-created_at")

Pagination doesn't magically make a badly designed query fast.

Our query is currently reasonably structured:

Filter
 ↓
Order
 ↓
Database pagination
 ↓
select_related
 ↓
Serializer

Later, with a genuinely large dataset, we can examine:

database indexes
PostgreSQL query plans
full-text search
cursor pagination

But not yet.


6. Don't add database indexes everywhere

You might now think:

"Should we add indexes to title, description, course, created_at, etc.?"

Not automatically.

Indexes have costs:

Faster reads
       +
Slower writes
       +
More storage
       +
More database maintenance

We add indexes because we have a query pattern that benefits from them.

That's engineering rather than guessing.

7. Our current Material API

We're getting a nice structure:

POST   /materials/create/
GET    /materials/
GET    /materials/?course=1
GET    /materials/?search=lecture
GET    /materials/?page=2
GET    /materials/?page=2&page_size=50


GET    /materials/<id>/
GET    /materials/<id>/download/

That's already a respectable MVP API.