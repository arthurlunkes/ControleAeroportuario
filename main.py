import json
from fastapi import FastAPI,  HTTPException, Request, Response
from datetime import datetime

app = FastAPI()

class Aeronave:
    id: int
    nome: str
    horario_chegada: datetime
    horario_partida: datetime

    def __init__(self, id, nome: str, horario_chegada: datetime, horario_partida: datetime):
        self.id = id
        self.nome = nome
        self.horario_chegada = horario_chegada
        self.horario_partida = horario_partida

patio = []

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Arthur
@app.get('/patio')
def listar_aeronaves_patio():
    return patio

# Lucas
#@app.post()

# Arthur
@app.patch('/patio/{aeronave_id}')
async def atualizar_patio(aeronave_id: int, request: Request):
    body = await request.json()

    aeronave = next((a for a in patio if a.id == aeronave_id), None)

    if not aeronave:
        raise HTTPException(status_code=404, detail="Aeronave não encontrada no pátio!")

    aeronave.nome = body['nome']
    aeronave.horario_partida = body['horario_partida']
    aeronave.horario_chegada = body['horario_chegada']

    return aeronave


# Antonio
# Rota para excluir uma aeronave com base no ID
@app.delete("/aeronaves/{aeronave_id}")
def excluir_aeronave(aeronave_id: int):
    # Verifica se a aeronave existe
    if aeronave_id not in patio:
        raise HTTPException(status_code=404, detail="Aeronave não encontrada")
    
    aeronave_excluida = patio.pop(aeronave_id)
    return aeronave_excluida