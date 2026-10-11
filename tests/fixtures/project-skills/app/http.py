"""Static FastAPI transport input; no server is started by the fixture builder."""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from .domain import Inventory, Reservation


class ReserveInput(BaseModel):
    quantity: int = Field(gt=0, strict=True)


app = FastAPI()
inventory = Inventory(10)


@app.post("/reservations")
def reserve(body: ReserveInput) -> Reservation:
    try:
        return inventory.reserve(body.quantity)
    except ValueError as error:
        raise HTTPException(status_code=409, detail="invalid_quantity") from error


@app.get("/reservations/{reservation_id}")
def get(reservation_id: str) -> Reservation:
    try:
        return inventory.get(reservation_id)
    except KeyError as error:
        raise HTTPException(status_code=404, detail="reservation_not_found") from error
