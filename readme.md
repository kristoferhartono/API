Pengerjaan menggunakan VS Code dengan terminal linux(WSL) dengan bahasa Python3

Download pip python3
- sudo apt-get install software-properties-common
- sudo apt-add-repository universe
- sudo apt-get update
- sudo apt-get install python3-pip

Selanjutnya, setup Virtual Environment 
- pipenv install                #install virtual environment
- pipenv shell                  #aktivasi virtual env
(Kedua command diatas dimasukkan dalam file env.sh)

Install FastAPI :
- pip3 install fastapi          #install FastAPI

Install Uvicorn:
- pipenv install uvicorn        #install uvicorn
- uvicorn main:app --reload     #menjalankan server uvicorn (dimasukkan dalam file run.sh)

Setelah menjalankan uvicorn, buka IP:port yang muncul di terminal di browser lalu tambahkan "/docs" setelah link tersebut untuk mencoba fungsi-fungsi yang sudah dibuat

Contoh : http://127.0.0.1:8000/docs

Kristofer Hartono
18219102