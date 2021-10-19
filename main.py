import json
from fastapi import FastAPI, HTTPException, Depends

from auth.auth_handler import signJWT, get_password_hash, verify_password
from auth.auth_bearer import JWTBearer

with open("menu.json", "r") as read_file:
    data = json.load(read_file)
with open("user.json", "r") as read_user:
    data2 = json.load(read_user)

app = FastAPI()

@app.post('/user/register')
async def register(username : str, password : str):
    hashedpw = get_password_hash(password)
    credential = {'username': username, 'password' : hashedpw}
    data2.append(credential)
    with open("user.json", "w") as write_file:
        json.dump(data2, write_file)
    write_file.close()
    return data2

@app.post('/user/login')
async def login(username : str, password : str):
    for data_user in data2:
        if data_user['username'] == username:
            if verify_password(password, data_user['password']):
                return signJWT(username)
            else :
                return('login failed')

@app.get('/')
def root():
    return{'Menu': 'Item'}

@app.get('/menu',dependencies=[Depends(JWTBearer())])
async def read_all_menu():
    return data

@app.get('/menu/{item_id}',dependencies=[Depends(JWTBearer())])
async def read_menu(item_id: int):
    for menu_item in data['menu']:
        if menu_item['id'] == item_id:
            return menu_item
    raise HTTPException(
        status_code=1, detail=f'Item not found'
    )

@app.post('/menu',dependencies=[Depends(JWTBearer())])
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

@app.put('/menu/{item_id}',dependencies=[Depends(JWTBearer())])
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

@app.delete('/menu/{item_id}',dependencies=[Depends(JWTBearer())])
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