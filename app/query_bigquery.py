import os
from typing import List
import argparse
import re
# from google.cloud import bigquery
# from google.oauth2 import service_account

MAX_INPUT_LENGTH = 32


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=str, required=True)
    args = parser.parse_args()
    user_input = args.input

    print(f"User input: {user_input}")
    if (user_input):
        generate_branding_snippet(user_input)
        generate_keywords(user_input)
    else:
        raise ValueError(
            f"Input length is too long. Must be under {MAX_INPUT_LENGTH}. Submitted input is {user_input}"
        )


# def validate_length(prompt: str) -> bool:
#     return len(prompt) <= MAX_INPUT_LENGTH


# def generate_keywords(prompt: str) -> List[str]:
#     # Load your API key from an environment variable or secret management service
#     print("Calling function generate_keywords")

#     # response = openai.Completion.create(
#     #     engine="davinci-instruct-beta-v3", prompt=enriched_prompt, max_tokens=32
#     # )

#     # Extract output text.
#     # keywords_text: str = response["choices"][0]["text"]

#     # Strip whitespace.
#     keywords_text = keywords_text.strip()
#     keywords_array = re.split(",|\n|;|-", keywords_text)
#     keywords_array = [k.lower().strip() for k in keywords_array]
#     keywords_array = [k for k in keywords_array if len(k) > 0]

#     print(f"Keywords: {keywords_array}")
#     return keywords_array


# def generate_branding_snippet(prompt: str) -> str:
#     # Load your API key from an environment variable or secret management service
#     openai.api_key = os.getenv("OPENAI_API_KEY")
#     enriched_prompt = f"Generate upbeat branding snippet for {prompt}: "
#     print(enriched_prompt)

#     response = openai.Completion.create(
#         engine="davinci-instruct-beta-v3", prompt=enriched_prompt, max_tokens=32
#     )

#     # Extract output text.
#     branding_text: str = response["choices"][0]["text"]

#     # Strip whitespace.
#     branding_text = branding_text.strip()

#     # Add ... to truncated statements.
#     last_char = branding_text[-1]
#     if last_char not in {".", "!", "?"}:
#         branding_text += "..."

#     print(f"Snippet: {branding_text}")
#     return branding_text





# Set up credentials and create a client object
# credentials = service_account.Credentials.from_service_account_file('/home/john/Documents/olist_ecomm_dataset/ecom1-377114-b7a0ef7556bb_BigQuery_PrivateKey.json')
# project_id = 'ecom1-377114'

# client = bigquery.Client(credentials= credentials,project=project_id)

# # Define SQL
# query = """
#     SELECT *
#     FROM olist_dw.customer_dim
#     LIMIT 3
# """

# #Run SQL
# query_job = client.query(query)
# results = query_job.result() # Wait for the job to complete.

# for row in results:
#     print(row)


if __name__ == "__main__":
    main()