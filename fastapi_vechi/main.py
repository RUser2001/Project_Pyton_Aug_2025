from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel
import uvicorn 
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/',response_class=HTMLResponse)
def read_root():
   return '<h1>Proiectul vechi ruleaza corect.</h1>'


@app.get("/blog")
def index(limit: int=10, published:bool=True,sort:Optional[str]=None):
    if limit >100:
        raise HTTPException(status_code=400, detail='Limit cannot be greater than100')
    
    if published:
       return {'data':f'{limit} published blogs from de db', 'sort':sort}
    else:
       return {'data':f'{limit} blogs from the db', 'sort':sort}

@app.get('/sun/{id}/unpublished')
def unpublished(id):
    return {'sun': id}


@app.get("/blog/{id}") #http://localhost:8001/blog/"orice"
def about(id: str):
    return {'data' : id}


@app.get("/blog/{id}/comments") 
def comments(id):
    return {'data' : ['1' ,'2']} 


@app.get("/data") 
def abc():
    return {"data":{"RAHELA"}}


@app.get("/hello")   #http://localhost:8001/hello
def salut():
    return {"mesaj": "Aceasta este o altă rută"}

class Blog(BaseModel):
    title: str
    body: str
    published: Optional [bool]


@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': f"Blog is created as {blog.title}"}

#if __name__ == "__main__":
    #uvicorn.run(app, host="127.0.0.1", port=9000)
