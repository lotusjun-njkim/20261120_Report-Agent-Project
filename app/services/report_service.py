"""Report Service: 6종 보고서 공통 CRUD/버전/동기화. Repository는 DB, Service는 업무 규칙."""

from datetime import datetime

from sqlalchemy import select

from sqlalchemy.orm import Session

from app.models.report import ReportCategory

from app.repositories import report_repository as repo

def categories(db:Session)->dict:
    rows=db.scalars(select(ReportCategory).order_by(ReportCategory.category_id)).all()
    return {'items':[{'category_id':r.category_id,'code':r.code,'name':r.name,'description':r.description} for r in rows]}

def get_report(db:Session,rid:int)->dict:
    return repo.read_report(db,rid)

def list_reports(db:Session,title:str|None,limit:int,offset:int,
                 category_code:str|None=None,updated_after:datetime|None=None):
    return repo.list_reports(db,title,limit,offset,category_code,updated_after)
