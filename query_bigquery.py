# importing foofe librarry
from google.cloud import bigquery
from google.oauth2 import service_account

# Set up credentials and create a client object
credentials = service_account.Credentials.from_service_account_file('/home/john/Documents/olist_ecomm_dataset/ecom1-377114-b7a0ef7556bb_BigQuery_PrivateKey.json')
project_id = 'ecom1-377114'

client = bigquery.Client(credentials= credentials,project=project_id)

# Define SQL
query = """
    SELECT *
    FROM olist_dw.customer_dim
    LIMIT 3
"""

#Run SQL
query_job = client.query(query)
results = query_job.result() # Wait for the job to complete.

for row in results:
    print(row)