Step 8 — Protect the existing production data
Before running the migration, preserve existing courses and materials as approved. Otherwise, your current catalogue could disappear from public view immediately after deployment.
Generate the migration:

#python manage.py makemigrations academics


Open the generated migration and add this data-migration function:

def preserve_existing_content(apps, schema_editor):
    Course = apps.get_model("academics", "Course")
    Material = apps.get_model("academics", "Material")

    Course.objects.all().update(status="approved")
    Material.objects.all().update(status="approved")



Then add this operation after the new status fields have been added in the migration's operations list:

'''
migrations.RunPython(
    preserve_existing_content,
    migrations.RunPython.noop,
),
'''

Keep the models' default status as pending. This way, existing records remain approved, while all newly created courses and materials start pending.
Review the generated migration, then run:

#python manage.py migrate
#python manage.py check


Don't apply this migration to production until it has been tested against a copy of the production database.