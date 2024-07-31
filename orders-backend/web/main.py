from fastapi import FastAPI, responses, status, Request
from web.orders.routes import router
from starlette.responses import RedirectResponse
from src.orders.exceptions import EOrderDoesNotExist

app = FastAPI()

app.include_router(router, tags=["Orders"])


@app.exception_handler(EOrderDoesNotExist)
async def validation_error(
    request: Request, exc: EOrderDoesNotExist
) -> responses.JSONResponse:
    return responses.JSONResponse(
        {"message": exc.message}, status_code=status.HTTP_400_BAD_REQUEST
    )


@app.get("/")
def main():
    return RedirectResponse(url="/docs")
