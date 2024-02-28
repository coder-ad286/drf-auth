from user.models import User
from .response import errorResponse
import jwt

def isAuthenticated(req):
    token = req.COOKIES.get("token")
    if token is None:return None
    try:
        payload = jwt.decode(token, "secret_key", algorithms=["HS256"])
    except:
        return None
    user = User.objects.filter(id=payload["id"]).first()
    if user is None : return None
    req.user = user
    return req
        
def isAdmin(user):
    if user.is_admin : 
        return True 
    else : 
        return False