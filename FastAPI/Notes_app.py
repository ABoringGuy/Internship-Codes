from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
app=FastAPI()

class NoteCreation(BaseModel):
    title: str
    content: str

class Note(NoteCreation):
    id: int
    created_at: datetime
    updated_at: datetime

notes_db: list[Note]=[]
note_id_counter=1

"""We sent NoteCreation rather than Note in parameter of function. If we sent Note then it would have asked us to
input all parameters like id, created_at, updated_at."""
@app.post("/notes", response_model=Note)
def create_note(note: NoteCreation):
    global note_id_counter
    new_note =Note(id=note_id_counter, title=note.title, content=note.content, created_at=datetime.now(), updated_at=datetime.now())
    notes_db.append(new_note)
    note_id_counter+=1

    return new_note

@app.get("/notes", response_model=list[Note])
def get_notes():
    return notes_db

@app.get("/notes/{note_id}", response_model=Note)
def get_note(note_id: int):
    for note in notes_db:
        if note.id == note_id:
            return note

    raise HTTPException(status_code=404, detail="Note not found")


@app.delete("/notes/{note_id}", response_model=Note)
def remove_note(note_id: int):
    for note in notes_db:
        if note.id == note_id:
            notes_db.remove(note)
    raise HTTPException(status_code=404, detail="Note not found")

@app.put("/notes/{note_id}", response_model=Note)
def update_note(note_id: int, updated_note: NoteCreation):
    for note in notes_db:
        if note.id == note_id:
            note.title = updated_note.title
            note.content = updated_note.content
            note.updated_at = datetime.now()
            return note

    raise HTTPException(status_code=404, detail="Note not found")
