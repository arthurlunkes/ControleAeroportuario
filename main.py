from fastapi import FastAPI,  HTTPException
from datetime import datetime

app = FastAPI()

class Aeronave:
    id: int
    nome: str
    horario_chegada: datetime
    horario_partida: datetime

# Dicionário para armazenar as aeronaves em memória
aeronaves = {}

@app.get()

# Lucas
@app.post()

# Arthur
@app.patch()

#Antonio
@app.delete()

# Rota para excluir uma aeronave com base no ID
@app.delete("/aeronaves/{aeronave_id}")
def excluir_aeronave(aeronave_id: int):
    # Verifica se a aeronave existe
    if aeronave_id not in aeronaves:
        raise HTTPException(status_code=404, detail="Aeronave não encontrada")
    
    aeronave_excluida = aeronaves.pop(aeronave_id)
    return aeronave_excluida