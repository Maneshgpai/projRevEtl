from fastapi import FastAPI, HTTPException
from main import connectSrc, getSQL, runSQL, validate_datasource
import json
from mangum import Mangum

revetl_app = FastAPI()
handler = Mangum(revetl_app)

@revetl_app.get("/connect_to_source")
async def connect_to_source(data_source: str = "bigquery"
                            , credentials: str = "/home/john/Documents/revEtlUser_GCP_Bigquery_key/revEtlUser_GCP_Bigquery_key.json"
                            , project_id: str = "ecom1-377114"):

    if (validate_datasource(data_source)):
        client = connectSrc(data_source, credentials, project_id)
        query = getSQL(data_source, client)
        results = runSQL(data_source, client, query)
        records = [dict(row) for row in results]
        json_obj = json.dumps(str(records))
        return ({json_obj})
    else:
        raise ValueError(
            f"Submitted data source {data_source}, is not supported! Only Google BigQuery is supported currently.")
