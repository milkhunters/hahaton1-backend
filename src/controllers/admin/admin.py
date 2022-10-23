from fastapi import APIRouter
from config import load_docs

from views import ErrorAPIResponse

router = APIRouter(responses={"400": {"model": ErrorAPIResponse}})
docs = load_docs("admin.ini")
