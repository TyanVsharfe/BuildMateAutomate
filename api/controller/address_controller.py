from fastapi import APIRouter

from api.data import address
from api.model.Address import AddressCreate

address_routes = APIRouter()


@address_routes.post('/create')
def insert_address(addressRequest: AddressCreate):
    flat = addressRequest.flat
    building = addressRequest.building
    city = addressRequest.city
    street = addressRequest.street
    creator_id = addressRequest.creator_id
    address.create_address(flat, building, city, street, creator_id)
    return 'Адрес создан'


@address_routes.delete('/delete')
def delete_address(city, street, building, flat):
    address.delete_address(city, street, building, flat)
