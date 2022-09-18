from fastapi import FastAPI, Depends, status, Response, HTTPException
from . import schemas, models
from .database import SessionLokal, engine
from sqlalchemy.orm import Session

app = FastAPI()

models.Cotigory.metadata.create_all(engine)

def get_db():
  db = SessionLokal()
  try:
    yield db
  finally:
    db.close()

@app.post('/cotigory', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Cotigory, db: Session = Depends(get_db)):
  new_cotigory = models.Cotigory(name=request.name, description=request.description)
  db.add(new_cotigory)
  db.commit()
  db.refresh(new_cotigory)
  return new_cotigory

@app.get('/cotigory')
def all(db: Session = Depends(get_db)):
  cotigorys = db.query(models.Cotigory).all()
  return cotigorys


@app.delete('/cotigory/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destory(id, db: Session = Depends(get_db)):
  cotigory = db.query(models.Cotigory).filter(models.Cotigory.id == id)

  if not cotigory.first():
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
      detail=f"cotigory with the id {id} is not avaibele")

  cotigory.delete(synchronize_session=False)
  db.commit()
  return 'done'

@app.put('/cotigory/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Cotigory, db: Session = Depends(get_db)):
  cotigory = db.query(models.Cotigory).filter(models.Cotigory.id == id)


  if not cotigory.first():
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
      detail=f"cotigory with the id {id} is not avaibele")

  cotigory.update({'name': request.name, 'description': request.description})
  db.commit()

  return 'update'

@app.get('/cotigory/{id}', status_code=200)
def show(id, response: Response, db: Session = Depends(get_db)):
  cotigory = db.query(models.Cotigory).filter(models.Cotigory.id == id).first()

  if not cotigory:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND, detail=f"cotigory with the id {id} is not avaibele"
    )
    # response.status_code = status.HTTP_404_NOT_FOUND

    # return{'detail': f"cotigory with the id {id} is not avaibele"}

  return cotigory 