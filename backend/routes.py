from fastapi import APIRouter
from config.database_config import get_db
from fastapi import Depends,Request
from sqlalchemy.orm import Session
from models import Resource 
from config.server_config import templates
from jinja2.exceptions import TemplateNotFound
from fastapi.responses import HTMLResponse
router = APIRouter()

@router.get("/")
async def render_home(request:Request):
    return templates.TemplateResponse("index.html",{"request":request})
@router.get("/render/{template_name}")
async def render_html(template_name:str,request:Request):
    try:
        return templates.TemplateResponse(template_name,{"request":request})
    except TemplateNotFound:
        return HTMLResponse("page not found",status_code=500)
@router.get("/documents")
def render_home(domain=None,type=None,keyword=None,db_session:Session=Depends(get_db)):
    query_obj = db_session.query(Resource)
    if domain:
        query_obj = query_obj.filter_by(Resource.resource_domain==domain)
    if type:
        query_obj = query_obj.filter_by(Resource.resource_type==type)
    if keyword:
        query_obj = query_obj.filter_by(Resource.resource_title.contains(keyword) or Resource.resource_subtitle.contains(keyword))
    result = query_obj.all()
    return result
