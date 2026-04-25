1
(from rest_framework.permissions import BasePermission, SAFE_METHODS

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



MY ROADMAP:
    👉 Admin users seeing everything
    👉 Role-based permissions (like staff vs normal users)
    👉 Field-level protection (e.g., price cannot be changed)
    👉 Add host approval system (like real Airbnb)
    👉 Add email verification before becoming host
    👉 Or integrate this directly into your current project step-by-step

Just tell me 👍

In real-world apps:
Authentication = Who are you?
Permissions = What can you do?

Skip them… and your app becomes chaos.

Let’s fix that with Django 🔐

Imagine a banking app without authentication & permission classes…

Your money = my money
My money = your money

Basically… OUR money 😭

That’s why backend security matters.

No authentication. No permissions.

Congrats… you just built a public wallet 💀

This is why Django auth & permission classes matter.


Imagine a banking app with no authentication or permissions…
Your money becomes my money 😳
And mine becomes yours.

That’s why authentication & permission classes in Django are NOT optional.


'''

⚠️ SECURITY RULES (DO NOT BREAK THESE):

❌ Never allow frontend to set role directly
❌ Never trust UI hiding buttons
✅ Always enforce roles in backend
✅ Always combine permissions + queryset

🧠 FINAL MENTAL MODEL:

Registration → always user
Upgrade → controlled API (host)
Admin → only via backend/admin pane

'''

CLEAR EXPLANATION OF RBAC SYSTEM:
'''
👤 User---------🔒 Limited access
🏠 Host---------🔑 Owns their stuff
🛡️ Admin--------🧠 Controls the entire system



And this line:

    if request.user.is_authenticated and request.user.role == 'admin':
    return True

is what gives admin that power

🧒 REAL-LIFE ANALOGY:
Without admin check:
    Only the owner of a house can open the door
With admin check:
    Security manager has a master key
    → can open ANY house

🔁 FLOW OF EXECUTION (VERY IMPORTANT)
Let’s simulate what happens when a request comes in:
    Scenario: Someone tries to DELETE a product
        Step 1: Permission class runs:
            def has_object_permission(self, request, view, obj):
        Step 2: Admin check runs FIRST:
            if request.user.is_authenticated and request.user.role == 'admin':
                return True
        🔥 If TRUE:
            👉 It stops here
            👉 It does NOT check anything else
        🔥 If FALSE:
            👉 Then it continues: return obj.user == request.user

⚠️ ORDER MATTERS (VERY IMPORTANT):
    RIGHT ORDER
        '''
        if request.user.is_authenticated and request.user.role == 'admin':
            return True

        return obj.user == request.user

        '''
    WRONG ORDER
        '''
        if request.user.is_authenticated and request.user.role == 'admin':
            return True

        return obj.user == request.user
        '''


YOU JUST MASTERED SOMETHING IMPORTANT

This line is used in:

SaaS dashboards
Banking systems
Marketplaces
Admin panels

⚡ ONE-LINE SUMMARY: This line gives admin the ability to bypass all ownership restrictions and control any resource in the system.OR 
👉 Authority override rule

🔥 WHEN SHOULD YOU USE THIS?
    Use this when:
    - You want admins to bypass restrictions
    - You want system-level control
    - You want debugging power

🔐 WHY WE ADD is_authenticated
🧒 Why?
    if request.user.is_authenticated and request.user.role == 'admin':
    return True
    
    Because:
    👉 If user is NOT logged in → no role
    👉 Prevents crashes

⚠️ WHEN THIS CAN BE DANGEROUS
If misused:
❌ Mistake 1: No authentication check
    if request.user.role == 'admin':

❌ Mistake 2: Giving wrong users admin role:
    👉 They gain FULL CONTROL
    👉 Security risk
❌ Mistake 3: Overusing it:
    👉 Everything becomes bypassable
    👉 System loses structure
'''




PROMPT:
'''
draw a visual diagram of your permission flow
'''

