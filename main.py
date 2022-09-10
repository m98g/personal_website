import os
from pathlib import Path
from fastapi import Request
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
# for compressing the app.css file
from fastapi.middleware.gzip import GZipMiddleware

from form import ContactForm

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(GZipMiddleware)
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def index(request:Request):
    return templates.TemplateResponse("base.html", {"request": request})

@app.get("/projects")
async def projects(request:Request):
    return templates.TemplateResponse("projects.html", {"request": request})

@app.get("/studies")
async def studies(request:Request):
    return templates.TemplateResponse("studies.html", {"request": request})

@app.get("/contact")
async def about_me(request:Request):
    return templates.TemplateResponse("contact.html", {"request": request})

@app.get("/ba_code")
async def ba_code(request:Request):
    return templates.TemplateResponse("ba_code.html", {"request": request})

# downloads: paths and routes
# atm placeholder names

downloadfolder = Path("/static/downloads/")

ba_file = downloadfolder / "ba.pdf"

ba_md = downloadfolder / "ba.Rmd"

third_party_path = downloadfolder / "third_party.pdf"

johnston_rep_path = downloadfolder / "johnston_rep.pdf"

cv_path = downloadfolder / "cv.txt"

# the pdf of the study
@app.get("/ba")
async def ba(request:Request):
    file_name = "ba.pdf"
    file_path = os.getcwd() + "/" + str(ba_file)
    return FileResponse(path=file_path, media_type='application/octet-stream', filename=file_name)

@app.get("/third_party")
async def ba(request:Request):
    file_name = "third_party.pdf"
    file_path = os.getcwd() + "/" + str(third_party_path)
    return FileResponse(path=file_path, media_type='application/octet-stream', filename=file_name)

@app.get("/johnston")
async def ba(request:Request):
    file_name = "johnston_rep.pdf"
    file_path = os.getcwd() + "/" + str(johnston_rep_path)
    return FileResponse(path=file_path, media_type='application/octet-stream', filename=file_name)

@app.get("/cv")
async def ba(request:Request):
    file_name = "cv.pdf"
    file_path = os.getcwd() + "/" + str(cv_path)
    return FileResponse(path=file_path, media_type='application/octet-stream', filename=file_name)

@app.get("/ba_r_md")
async def ba(request:Request):
    file_name = "ba.Rmd"
    file_path = os.getcwd() + "/" + str(ba_md)
    return FileResponse(path=file_path, media_type='application/octet-stream', filename=file_name)

# responses for r markdown files knitted as html

@app.get("/ba_r_html")
async def ba(request:Request):
    return templates.TemplateResponse("ba.html", {"request": request})

# only larsen as hmtl doc and johnston as a pdf study with the code in the github repo
@app.get("/larsen_html")
async def larsen(request:Request):
    return templates.TemplateResponse("replication_larsen.html", {"request": request})

@app.get("/hungergames_r_html")
async def hungergames(request:Request):
    return templates.TemplateResponse("hungergames.html", {"request": request})

@app.get("/janeausten_r_html")
async def janeausten(request:Request):
    return templates.TemplateResponse("janeausten.html", {"request": request})

# recieve form data and send email

@app.post("/form")
async def form_func(request: Request):
    form = ContactForm(request)
    await form.load_data()
    form_data = [form.name, form.email, form.message]
    with open("messages.txt", 'a') as m:
        m.write("\n".join(form_data))
        m.write("\n\n")
    return templates.TemplateResponse("contact.html", {"request": request})