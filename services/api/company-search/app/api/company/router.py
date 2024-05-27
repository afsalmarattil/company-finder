import os
from typing import List, Optional

from elasticsearch import AsyncElasticsearch
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, HttpUrl

es_host = os.getenv("ES_HOST", "http://localhost:9200")
es = AsyncElasticsearch(hosts=[es_host])

k = os.getenv("K_SIMILAR", 5)

router = APIRouter()


class Company(BaseModel):
    id: str
    linkedin_url: Optional[str] = None
    company_name: Optional[str] = None
    industry: Optional[str] = None
    website: Optional[str] = None
    tagline: Optional[str] = None
    about: Optional[str] = None
    year_founded: Optional[int] = None
    locality: Optional[str] = None
    country: Optional[str] = None
    current_employee_estimate: Optional[int] = None
    keywords: Optional[str] = None


@router.get("/", response_model=dict)
async def get_companies(
    page: int = Query(1, ge=1, description="Page number, starting from 1"),
    page_size: int = Query(10, ge=1, le=100, description="Number of items per page"),
):
    skip = (page - 1) * page_size
    response = await es.search(
        index="companies", body={"query": {"match_all": {}}}, from_=skip, size=page_size
    )
    total_hits = response["hits"]["total"]["value"]
    companies = [
        {**hit["_source"], "id": hit["_id"]} for hit in response["hits"]["hits"]
    ]
    return {
        "total": total_hits,
        "page": page,
        "page_size": page_size,
        "total_pages": (total_hits + page_size - 1) // page_size,
        "results": companies,
    }


@router.get("/{company_id}", response_model=Company)
async def get_company(company_id: str):
    try:
        response = await es.get(index="companies", id=company_id)
        return {**response["_source"], "id": response["_id"]}
    except Exception as e:
        raise HTTPException(status_code=404, detail="Company not found")


@router.get("/search/{name}", response_model=List[Company])
async def search_company(name: str):
    query = {"query": {"match": {"company_name": name}}}
    response = await es.search(index="companies", body=query, size=100)
    return [{**hit["_source"], "id": hit["_id"]} for hit in response["hits"]["hits"]]


@router.get("/similar/{company_id}", response_model=list[Company])
async def similar_companies(company_id: str):
    try:
        company = await es.get(index="companies", id=company_id)
        source = company["_source"]
        industry = source["industry"]
        keywords = source["keywords"]

        query = {
            "query": {
                "bool": {
                    "should": [
                        {"match": {"industry": industry}},
                        {"match": {"keywords": keywords}},
                    ],
                    "must_not": [{"term": {"_id": company_id}}],
                }
            },
            "size": k,
        }

        response = await es.search(index="companies", body=query)
        return [
            {**hit["_source"], "id": hit["_id"]} for hit in response["hits"]["hits"]
        ]
    except Exception as e:
        raise HTTPException(status_code=404, detail="Unable to find similar companies")


@router.on_event("shutdown")
async def shutdown_event():
    await es.close()
