from fastapi import FastAPI,Body
from pydantic import BaseModel
from typing import Optional
from database import auth,db

app = FastAPI()

def user_detail(users_by_name):
    detail_list = []
    for key in users_by_name.keys():
        detail = db.child("companies").child(key).get().val()
        detail_list.append(detail)
    return detail_list

def company_detail(companies_by_name):
    detail_list = []
    for key in companies_by_name.keys():
        detail = db.child("users").child(key).get().val()
        detail_list.append(detail)
    return detail_list

@app.get('/get/user/{path}')
async def path_and_query_params(path: str):
    users_by_name = db.child("users").child(path).child("used_company").get().val()
    user_detail_list = user_detail(users_by_name)
    cname_list = [i["cname"] for i in user_detail_list]
    local_list = [i["local"] for i in user_detail_list]
    return {'user': f"{path}", 'company_name': cname_list, "local": local_list}

@app.get('/get/company/{path}')
async def path_and_query_params(path: str):
    companies_by_name = db.child("companies").child(path).child("user_list").get().val()
    company_detail_list = company_detail(companies_by_name)
    user_list = [i["name"] for i in company_detail_list]
    return {'company': f"{path}", 'user_name': user_list}