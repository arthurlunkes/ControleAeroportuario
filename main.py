import json
from fastapi import FastAPI,  HTTPException, Request, Response
from datetime import datetime

app = FastAPI()

id_counter = 1


class Aeronave:
    def __init__(self, nome: str, horario_chegada: datetime, horario_partida: datetime):
        global id_counter
        self.id = id_counter
        id_counter += 1
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
@app.post('/patio')
async def adicionar_aeronave(request: Request):
    body = await request.json()

    if 'nome' not in body or 'horario_chegada' not in body or 'horario_partida' not in body:
        raise HTTPException(status_code=400, detail="Campos incompletos na requisição")

    nova_aeronave = Aeronave(
        nome=body['nome'],
        horario_chegada=body['horario_chegada'],
        horario_partida=body['horario_partida']
    )

    patio.append(nova_aeronave)
    return {"message": "Aeronave adicionada com sucesso", "aeronave": nova_aeronave}

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