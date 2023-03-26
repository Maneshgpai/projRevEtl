import os
from typing import List
import argparse
import re
from google.cloud import bigquery
from google.oauth2 import service_account


def main():
    googleBigQry = "gbq"
    # snowflake = "snow"
    print(f"debug 1*********8")
    parser = argparse.ArgumentParser()

    # Add dataSource
    parser.add_argument("--input", "-i", type=str, required=True)
    args = parser.parse_args()
    # data_src = args.input

    # print(f"Data Source given is: {data_src}")

    # if (validate_datasource(data_src)):
    #     print(f"Data Source {data_src} is supported. Connecting...")

    #     if data_src == googleBigQry:

    #         # Based on Data source type, ask additional arguments specific to connect to each data source:
    #         # For Google Biqquery it will be projectID, credentials, query
    #         credentials = service_account.Credentials.from_service_account_file(
    #             '/home/john/Documents/revEtlUser_GCP_Bigquery_key/revEtlUser_GCP_Bigquery_key.json')
    #         projectID = 'ecom1-377114'

    #         print(f"Placeholder to call function to display schema and create SQL")
    #         # Add additional logic to display schema and
    #         # an interface to generate query (drag/drop UI plus writing SQL interface)###############
    #         query = """SELECT * FROM olist_dw.customer_dim LIMIT 3"""
    #         runSql_bigquery(credentials, projectID, query)
    #     # elif data_src == snowflake:
    #     #     runSql_snowflake(credentials, projectID, query)

    # else:
    #     raise ValueError(
    #         f"Submitted data source, {data_src}, is not supported! Only Google BigQuery (Datasrc:gbq) is supported currently."
    #     )

def validate_datasource(prompt: str) -> bool:
    dataSrcs = [googleBigQry]
    res = 1
    if prompt not in dataSrcs:
        res = 0
    return res

def runSql_bigquery(credentials, projectID, query):
    client = bigquery.Client(credentials=credentials, project=projectID)
    query_job = client.query(query)
    results = query_job.result()
    for row in results:
        print(row)

if __name__ == "__main__":
    main()