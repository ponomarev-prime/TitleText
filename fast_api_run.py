from typing import Union

from fastapi import FastAPI, Query

from logger import logger

app = FastAPI()


@app.get("/")
def read_root():
    logger.debug("Received request on root endpoint")
    return {"Hello": "World"}

@app.get("/titlegen")
async def generate_title(
    the_text: str = Query(..., description="Text to be printed"),
    background_colour: str = Query(..., description="Background color for printer"),
):
    return {
        "the_text": the_text,
        "background_colour": background_colour,
    }

if __name__ == "__main__":
    logger.debug('Fast api app started')
    import uvicorn
    uvicorn.run(app, port=8000, host="localhost")