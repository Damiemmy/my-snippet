class User(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=True,
        blank=True,
        null=True,
    )

    email = models.EmailField(unique=True)

    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["username"]

    objects = UserManager()



    #Questions why i used inherited Users
1.)
    Why redefine username?:Because the inherited one is required.We are replacing it with one that is optional.

2.)
    Why null=True?: The database can store:NULL,instead of forcing an empty string.

3.)
    Why keep unique=True? Because if someone chooses a username like:damisa, no one else should be allowed to use it.

4.)

    Why REQUIRED_FIELDS?REQUIRED_FIELDS tells Django what additional fields are needed when creating a superuser with:python manage.py createsuperuser

    If you keep:
    REQUIRED_FIELDS = ["username"]

    the command will prompt for a username.
    If you truly want username to be optional—even for superusers—you can set:

    REQUIRED_FIELDS = []