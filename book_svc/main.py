from fastapi import FastAPI,Request,HTTPException
from fastapi.responses import JSONResponse
from app.core.errors import NotFoundError,ValidationError,DatabaseError
from app.interfaces.api.routes.books import router
from app.middleware.logging import log_requests
app = FastAPI()

app.middleware("http")(log_requests)
@app.exception_handler(NotFoundError)
def not_found_handler(request: Request,exc:NotFoundError):
    return JSONResponse(
        status_code=404,
        content={"error": str(exc)}
    )
    
@app.exception_handler(ValidationError)
def validation_handler(request:Request,exc: ValidationError):
    return JSONResponse(
        status_code=400,
        content={"error":str(exc)}
    )

@app.exception_handler(DatabaseError)
def database_error_handler(request: Request,exc:DatabaseError):
    return JSONResponse(
        status_code=500,
        content={"error": "Database Error occurred"}
    )

@app.exception_handler(Exception)
def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error"}
    )

app.include_router(router,prefix="/books")