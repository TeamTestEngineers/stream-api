import json
from urllib import response


def hello(event, context):
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
    }

    return {"statusCode": 200, "body": json.dumps(body)}

def scampy(event,context):
    body={
        "message":"this is scampy method",
        "info":"scampy",
        "input":event,
    }

    response={
            "statusCode":200,
            "body":json.dumps(body)
        }

    return response
