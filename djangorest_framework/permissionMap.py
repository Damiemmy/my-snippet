#Pro Tip (what top devs do)
#If your ViewSet grows, use a permission map:

permission_map = {
    'become_host': [IsAuthenticated],
}

def get_permissions(self):
    return [perm() for perm in self.permission_map.get(self.action, [])]

#This scales beautifully in large APIs.


ROADMAP FOR MASTERY ChatGPT(Action Vs HTTP Method):
If you want next level 🔥
I can show you how to:
    -restrict users from sending multiple requests at DB level (not just logic)
    -automatically trigger approval workflows (signals / services)
    -connect this with your frontend RBAC system

Just tell me.