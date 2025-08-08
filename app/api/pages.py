from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, PlainTextResponse
import os

router = APIRouter()

# Get the absolute path of the templates directory
templates_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "templates")
templates = Jinja2Templates(directory=templates_dir)

@router.get("/", response_class=HTMLResponse, name="index")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.get("/shop", response_class=HTMLResponse)
async def shop(request: Request):
    return templates.TemplateResponse("shop.html", {"request": request})

@router.get("/shop/success", response_class=HTMLResponse)
async def shop_success(request: Request, session_id: str = None):
    return templates.TemplateResponse("shop_success.html", {
        "request": request,
        "session_id": session_id
    })

@router.get("/shop/cancel", response_class=HTMLResponse)
async def shop_cancel(request: Request):
    return templates.TemplateResponse("shop_cancel.html", {"request": request})

@router.get("/gallery", response_class=HTMLResponse, name="gallery")
async def gallery(request: Request):
    return templates.TemplateResponse("gallery.html", {"request": request})

@router.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

@router.get("/contact", response_class=HTMLResponse)
async def contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request}) 

@router.get("/donate", response_class=HTMLResponse, name="donate")
async def donate(request: Request):
    return templates.TemplateResponse("donate.html", {"request": request})

@router.get("/community-outreach", response_class=HTMLResponse)
async def community_outreach(request: Request):
    return templates.TemplateResponse("community-outreach.html", {"request": request})

@router.get("/events", response_class=HTMLResponse)
async def events(request: Request):
    return templates.TemplateResponse("events.html", {"request": request})

@router.get("/teach-me-how-to-pray", response_class=HTMLResponse)
async def teach_me_how_to_pray(request: Request):
    return templates.TemplateResponse("Teach_Me_How_To_Pray.html", {"request": request})

@router.get("/donate/success", response_class=HTMLResponse)
async def donate_success(request: Request, session_id: str = None):
    return templates.TemplateResponse("donate_success.html", {
        "request": request,
        "session_id": session_id
    })

@router.get("/donate/cancel", response_class=HTMLResponse)
async def donate_cancel(request: Request):
    return templates.TemplateResponse("donate_cancel.html", {"request": request})

@router.get("/_da-verify-12b8085f1665b211c45e49b411b6add8.jerichohomestead.org", response_class=PlainTextResponse)
async def domain_verification():
    return "12b8085f1665b211c45e49b411b6add8"
