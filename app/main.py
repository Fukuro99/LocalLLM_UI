from fastapi import Depends, FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlmodel import Session

from .crud import create_note, delete_note, list_notes, toggle_note
from .db import get_session, init_db
from .openai_service import generate_note_suggestion

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.on_event("startup")
def on_startup() -> None:
    init_db()


@app.get("/", response_class=HTMLResponse)
def index(request: Request, session: Session = Depends(get_session)) -> HTMLResponse:
    notes = list_notes(session)
    return templates.TemplateResponse(
        "pages/index.html",
        {"request": request, "notes": notes, "suggestion": None},
    )


@app.get("/notes/partial", response_class=HTMLResponse)
def notes_partial(request: Request, session: Session = Depends(get_session)) -> HTMLResponse:
    notes = list_notes(session)
    return templates.TemplateResponse(
        "partials/notes_list.html", {"request": request, "notes": notes}
    )


@app.post("/notes", response_class=HTMLResponse)
def notes_create(
    request: Request,
    title: str = Form(...),
    session: Session = Depends(get_session),
) -> HTMLResponse:
    create_note(session, title=title)
    notes = list_notes(session)
    return templates.TemplateResponse(
        "partials/notes_list.html", {"request": request, "notes": notes}
    )


@app.post("/notes/{note_id}/toggle", response_class=HTMLResponse)
def notes_toggle(
    request: Request, note_id: int, session: Session = Depends(get_session)
) -> HTMLResponse:
    toggle_note(session, note_id)
    notes = list_notes(session)
    return templates.TemplateResponse(
        "partials/notes_list.html", {"request": request, "notes": notes}
    )


@app.delete("/notes/{note_id}", response_class=HTMLResponse)
def notes_delete(
    request: Request, note_id: int, session: Session = Depends(get_session)
) -> HTMLResponse:
    delete_note(session, note_id)
    notes = list_notes(session)
    return templates.TemplateResponse(
        "partials/notes_list.html", {"request": request, "notes": notes}
    )


@app.post("/notes/assist", response_class=HTMLResponse)
def notes_assist(request: Request, prompt: str = Form(...)) -> HTMLResponse:
    suggestion = generate_note_suggestion(prompt)
    return templates.TemplateResponse(
        "partials/note_suggestion.html",
        {"request": request, "suggestion": suggestion},
    )
