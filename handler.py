import json
import lunchpy.recommend as recommend


def hello(event, context):
    return recommend.lambda_handler(event, context)