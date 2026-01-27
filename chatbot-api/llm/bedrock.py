import boto3
import json
bedrock = boto3.client("bedrock-runtime", region_name= "us-east-1")
def bedrock_embed(text:str):
    response = bedrock.invoke_model(
        modelId = "amazon.titan-embed-text-v1",
        body = json.dumps({"inputText":text}),
        accept = "application/json",
        contentType = "application/json"
    )
    body = json.loads(response["body"].read())
    return body["embedding"]