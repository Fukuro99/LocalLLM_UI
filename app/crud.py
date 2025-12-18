from sqlmodel import Session, select

from .models import Note

def list_notes(session: Session) -> list[Note]:
    return session.exec(select(Note).order_by(Note.id.desc())).all()

def create_note(session: Session, title: str) -> Note:
    note = Note(title=title)
    session.add(note)
    session.commit()
    session.refresh(note)
    return note

def toggle_note(session: Session, note_id: int) -> None:
    note = session.get(Note, note_id)
    if not note:
        return
    note.done = not note.done
    session.add(note)
    session.commit()

def delete_note(session: Session, note_id: int) -> None:
    note = session.get(Note, note_id)
    if not note:
        return
    session.delete(note)
    session.commit()
