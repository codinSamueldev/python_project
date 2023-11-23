import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return [1,2,3]

@app.get('/contact')
def get_list():
    return {'name': 'Holiii'}

#Returning html
@app.get('/html/', response_class=HTMLResponse)
async def html_elements():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Look at me</title>
    </head>
    <body>
        <h1>Finally, we can return somethin alive in the web!</h1>
        <button type="submit"></button>
        <div style="width: 250px; height: 250px; background: blue; border-radius: 50%; text-align: center;">
    </body>
    </html>
    """

def run():
    store.get_categories()

if __name__ == '__main__':
    run()