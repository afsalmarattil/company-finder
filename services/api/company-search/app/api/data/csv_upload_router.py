import io
import os

import pandas as pd
from elasticsearch import AsyncElasticsearch, helpers
from fastapi import APIRouter, File, HTTPException, UploadFile
from fastapi.responses import JSONResponse

router = APIRouter()

es_host = os.getenv("ES_HOST", "http://localhost:9200")
es = AsyncElasticsearch(hosts=[es_host])
index_name = "companies"


async def create_index():
    if await es.indices.exists(index=index_name):
        await es.indices.delete(index=index_name)
    # Recreate the index with the necessary mappings
    mapping = {
        "mappings": {
            "properties": {
                "linkedin_url": {"type": "keyword"},
                "company_name": {"type": "text"},
                "industry": {"type": "text"},
                "website": {"type": "keyword"},
                "tagline": {"type": "text"},
                "about": {"type": "text"},
                "year_founded": {"type": "float"},
                "locality": {"type": "text"},
                "country": {"type": "keyword"},
                "current_employee_estimate": {"type": "integer"},
                "keywords": {"type": "text"},
            }
        }
    }
    await es.indices.create(index=index_name, body=mapping)


@router.post("/upload-csv/")
async def upload_csv(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(
            status_code=400, detail="Invalid file type. Only CSV files are accepted."
        )

    content = await file.read()
    try:
        # Recreate the index to ensure a fresh start
        await create_index()
        df = pd.read_csv(io.StringIO(content.decode("utf-8")))
        await helpers.async_bulk(es, doc_generator(df))
        return JSONResponse(
            content={"message": "File successfully uploaded and indexed"},
            status_code=200,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


async def doc_generator(df):
    for _, row in df.iterrows():
        yield {
            "_index": index_name,
            "_source": {
                key: (row[key] if pd.notna(row[key]) and row[key] != "" else None)
                for key in row.index
                if key != "id"  # Exclude the 'id' column from the source
            },
        }


@router.on_event("shutdown")
async def shutdown_event():
    await es.close()
