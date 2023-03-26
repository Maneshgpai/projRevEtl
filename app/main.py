import os
from typing import List
import argparse
import re
from google.cloud import bigquery
from google.oauth2 import service_account

# Supported data sources
googleBigQry = "bigquery"
dataSrcs = [googleBigQry]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--datasource", type=str, required=True,
                        help="Enter the Data source, options are bigquery")
    parser.add_argument("--credentials", type=str, required=True,
                        help="Enter the URL for credentials file")
    parser.add_argument("--projectid", type=str, required=True,
                        help="Enter the Big Query Project ID")
    args = parser.parse_args()
    data_src = args.datasource
    credentials = args.credentials
    projectid = args.projectid

    if (validate_datasource(data_src)):

        client = connectSrc(data_src, credentials, projectid)

        # Add additional logic to display schema and return the SQL formed
        # Give a drag+drop UI and a SQL writing UI
        query = getSQL(data_src, client)

        results = runSQL(data_src, client, query)

    else:
        raise ValueError(
            f"Submitted data source {data_src}, is not supported! Only Google BigQuery is supported currently."
        )


def validate_datasource(prompt: str) -> bool:
    res = 1
    if prompt not in dataSrcs:
        res = 0
    return res


def connectSrc(data_src, credentials, projectID):
    if data_src == googleBigQry:
        # Start: hardcoded for testing
        # credentials = service_account.Credentials.from_service_account_file(credentials)
        credentials = service_account.Credentials.from_service_account_file(
            '/home/john/Documents/revEtlUser_GCP_Bigquery_key/revEtlUser_GCP_Bigquery_key.json')
        projectID = 'ecom1-377114'
        # End: hardcoded for testing
        client = bigquery.Client(credentials=credentials, project=projectID)
    return client


def getSQL(data_src, client):
    if data_src == googleBigQry:
        # query = str(input("Enter the SQL query:"))
        # Show the first name and mail id of customers who have purchased atleast 3 times between Jan-2018 to Mar-2018 and have given review rating of 2 or below
        query = """select distinct cust.first_name, cust.email_address as email, cust.contact_number1 as contact, date(ordr.order_purchase_timestamp), ordr.review_score, count(distinct ordr.order_id) as nbr_of_orders from olist_dw.customer_dim cust inner join olist_dw.order_dim ordr on ordr.cuid = cust.cuid where date(ordr.order_purchase_timestamp) between '2018-01-01' and '2018-03-31' and ordr.review_score <= 2 group by cust.first_name, cust.email_address, cust.contact_number1, date(ordr.order_purchase_timestamp), ordr.review_score having count(distinct ordr.order_id) >= 3"""
        # query = """select distinct cust.first_name, cust.email_address as email, cust.contact_number1 as contact, date(ordr.order_purchase_timestamp), ordr.review_score, count(distinct ordr.order_id) as nbr_of_orders from olist_dw.customer_dim cust inner join olist_dw.order_dim ordr on ordr.cuid = cust.cuid group by cust.first_name, cust.email_address, cust.contact_number1, date(ordr.order_purchase_timestamp), ordr.review_score """
        return query


def runSQL(data_src, client, query):
    if data_src == googleBigQry:
        query_job = client.query(query)
        results = query_job.result()
        return results


if __name__ == "__main__":
    main()
