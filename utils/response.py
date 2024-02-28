from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

def errorResponse(msg,statusCode):
    response = Response({
        "success" : False,
        "message" : msg,
    },status=statusCode)
    # response.accepted_renderer = JSONRenderer()
    # response.accepted_media_type = "application/json"
    # response.renderer_context = {}
    # response.render()
    return response

def successResponse(data,msg,statusCode):
    response = Response({
        "success" : True,
        "message" : msg,
        "data" : data
    },status=statusCode)
    return response