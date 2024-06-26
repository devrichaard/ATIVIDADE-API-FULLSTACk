from routes.produto_routes import router as produto_router
from routes.setor_routes import router as setor_router
from routes.usuario_routes import router as usuario_router
from fastapi import FastAPI
app = FastAPI(title="Todos Problemas Resolvidos + o PUT",
              description=" além do problema de Login que foi resolvido, também resolvi o PUT do Setor que estava com o ID com duplicidade no Header",
              )
@app.get('/health-check',tags=["Richard Ribeiro Rodrigues"]) 
def health_check():
    return True
app.include_router(setor_router)
app.include_router(produto_router)
app.include_router(usuario_router)


if __name__ == "__main__":
    import uvicorn
#                  #nomearquivo#nomeAppMain   
    uvicorn.run("main:app", host="127.0.0.1", port=8004, reload=True)