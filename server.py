from fastapi import FastAPI,HTTPException 
from fastapi.responses import FileResponse
import tempfile
import os
app = FastAPI()

@app.get('/',response_class=FileResponse)
async def root():
    arr = os.listdir('nih')
    if len(arr)==0:
        raise HTTPException(status_code=404)
    fd, path = tempfile.mkstemp(suffix='.bat')
    a = ""
    with open('nih/b.bat','r') as f:
        a = f.read()
    with os.fdopen(fd, 'w') as f:
        f.write(a)
    os.remove('nih/b.bat')
    return path
    