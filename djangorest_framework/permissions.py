from rest_framework.permissions import BasePermission, SAFE_METHODS

class isOwnerPermission(BasePermission):
    def has_object_permission(self,request,view,obj):
        # Allow GET, HEAD, OPTIONS (read-only)
        if request.method in SAFE_METHODS:
            return True
        # Allow only owner to edit/delete
        return obj.user==request.user

'''    
Pro Tip (Production mindset)
    This line: 
        return obj.user == request.user
    assumes: 
        obj.user exist in model.py
    If your model uses something else like:
        owner = models.ForeignKey(User, ...)
    Then you must update it:
        obj.owner==request.user

'''


'''⚠️ STEP 3: What if you WANT public products?

Maybe your app is like an e-commerce store:

Everyone can view products
Only owners can edit/delete

Then do this instead:'''

def get_queryset(self):
    if self.request.user.is_authenticated:
        return Product.objects.all()  # everyone can see all
    return Product.objects.all()  # or filter public=True if you add that field


'''
👉 In that case:

Visibility = open
Control = restricted by permission class
'''

'''
🚀 STEP 4: The REAL production pattern (Best Practice)

Most serious apps use both filtering + ownership field

Example:
'''

def get_queryset(self):
    queryset = Product.objects.all()

    category = self.request.query_params.get('category')
    if category:
        queryset = queryset.filter(category=category)

    # Restrict to user
    if self.request.user.is_authenticated:
        queryset = queryset.filter(user=self.request.user)
    else:
        queryset = Product.objects.none()

    return queryset

'''
🧠 Big Picture (VERY IMPORTANT)

Think like this:

get_queryset() → controls WHAT data is visible
permissions → controls WHO can modify data

👉 If you miss one, your app is vulnerable.

'''




'''
💥 Real-world mistake you just avoided

Without this:'''

Product.objects.all()
'''
A user could:

See ALL products
Guess IDs
Try hitting endpoints manually (Postman, curl)

Even if they can't edit, data leakage is already a problem
'''




👉 Admin users seeing everything
👉 Role-based permissions (like staff vs normal users)
👉 Field-level protection (e.g., price cannot be changed)