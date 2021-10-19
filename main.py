import json
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
 
 
with open("menu.json", "r") as read_file:
    data = json.load(read_file)
app = FastAPI()
@app.get('/')
def root():
    return{'Menu': 'Item'}

@app.get('/menu')
async def read_all_menu():
    return data

@app.get('/menu/{item_id}')
async def read_menu(item_id: int):
    for menu_item in data['menu']:
        if menu_item['id'] == item_id:
            return menu_item
    raise HTTPException(
        status_code=1, detail=f'Item not found'
    )

@app.post('/menu')
async def add_menu(name: str):
    id = 1
    if (len(data['menu']) > 0):
        id = data['menu'][len(data['menu'])-1]['id']+1
    data_baru = {'id': id, 'name': name}
    data['menu'].append(dict(data_baru))
    read_file.close()
    with open("menu.json", "w") as write_file:
        json.dump(data, write_file, indent=3)
    write_file.close()

    return (data_baru)
    raise HTTPException(
        status_code = 2, detail=f'Internal Server Error'
    )

@app.put('/menu/{item_id}')
async def update_menu(item_id: int, name: str):
    for menu_item in data['menu']:
        if menu_item['id'] == item_id:
            menu_item['name'] = name
            
            read_file.close()
            with open("menu.json", "w") as write_file:
                json.dump(data, write_file, indent=3)
            write_file.close()

            return("Data updated!")

    raise HTTPException(
        status_code=3, detail=f'Item not found'
    )

@app.delete('/menu/{item_id}')
async def delete_menu(item_id: int):
    for menu_item in data['menu']:
        if menu_item['id'] == item_id:
            data['menu'].remove(menu_item)
            
            read_file.close()
            with open("menu.json", "w") as write_file:
                json.dump(data, write_file, indent=3)
            write_file.close()

            return("Data deleted!")

    raise HTTPException(
        status_code=4, detail=f'Item not found'
    )