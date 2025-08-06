from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {
        
        
        "mesaj":"Salut din FastAPI!" 
            
            
            "." 
            }




@app.get("/about") #http://localhost:8000/about
def about():
    return {'despre' : {'Despre pagina'}}





@app.get("/data")
def index():
    return {"data":{"RAHELA"}}




@app.get("/hello")   #http://localhost:8000/hello
def salut():
    return {"mesaj": "Aceasta este o altă rută"}
