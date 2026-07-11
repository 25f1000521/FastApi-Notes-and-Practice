from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

posts = [
    {
        "id":"1",
        "author":"Amar Nath",
        "title":"FastApi is very good",
        "description":"fastApi is the fastest framework for backend development"
    },
    {
        "id":"2",
        "author":"Corey Schafer",
        "title":"Pyhton is awesome",
        "description":"In the filed of AI and ML Pyhton is best weapon"
    }
]

@app.get("/posts",response_class= HTMLResponse, include_in_schema= False)
@app.get("/", response_class= HTMLResponse,include_in_schema= False)
def home():
    return f"<h1> {posts[1]['title']}</h1>"

