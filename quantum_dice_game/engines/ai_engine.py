import requests
import pickle
from .resource_path import *


def enable_watson(api_key):
    # Get IAM Access Token
    iam_url = "https://iam.cloud.ibm.com/identity/token"
    iam_response = requests.post(
        iam_url,
        data={"apikey": api_key, "grant_type": "urn:ibm:params:oauth:grant-type:apikey"},
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )

    # Check if the request was successful
    if iam_response.status_code != 200:
        print("IAM token request failed.")
        print(f"Status Code: {iam_response.status_code}")
        print("Response:", iam_response.text)
        return False

    iam_json = iam_response.json()

    # Check if access token is present
    if "access_token" not in iam_json:
        print("'access_token' not found in IAM response.")
        print("Response JSON:", iam_json)
        return False

    # Save response if valid
    with open(iam_response_path(), 'wb') as f:
        pickle.dump(iam_response, f)

    print("IAM token acquired successfully.")
    return iam_response


def ask_watson(user_request, project_id):
    watsonx_url = "https://us-south.ml.cloud.ibm.com"
    model_id = "ibm/granite-3-2b-instruct"

    with open(iam_response_path(), 'rb') as f:
        iam_response = pickle.load(f)

    access_token = iam_response.json()["access_token"]

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }

    prompt = f"Question: {user_request}\nAnswer in 50 words:"

    payload = {
        "model_id": model_id,
        "input": prompt,
        "parameters": {
            "decoding_method": "sample",
            "max_new_tokens": 100,
            "temperature": 0.7,
            "top_p": 1
        },
        "project_id": project_id
    }

    response = requests.post(
        f"{watsonx_url}/ml/v1/text/generation?version=2024-05-01",
        headers=headers,
        json=payload
    )

    result = response.json()

    # 👇 Debugging output to inspect the actual structure
    print("Full response JSON:")
    print(result)

    if "results" in result:
        generated_text = result["results"][0]["generated_text"]
        return generated_text
    else:
        print("'results' key not found in response.")


def list_watsonx_models(project_id):
    with open(iam_response_path(), 'rb') as f:
        iam_response = pickle.load(f)

    access_token = iam_response.json()["access_token"]

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }

    url = f"https://us-south.ml.cloud.ibm.com/ml/v1/foundation_model_specs?version=2024-05-01&project_id={project_id}"

    response = requests.get(url, headers=headers)
    models = response.json()

    print("Available models:")
