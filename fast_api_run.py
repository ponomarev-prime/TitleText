from typing import Union

from fastapi import FastAPI, Query

from logger import logger
import json


app = FastAPI()

# Загрузка данных из config_default.json
with open("config_default.json", "r") as default_file:
    config_default = json.load(default_file)

@app.get("/")
def read_root():
    logger.debug("Received request on / endpoint")
    return {"Hello": "World"}

@app.get("/titlegen")
async def generate_title(
    the_text: str = Query(None, description="Text to be printed"),
    background_colour: str = Query(None, description="Background color for printer"),
):
    logger.debug("Received request on /titlegen endpoint")
    # Создание копии config_default
    config_query = config_default.copy()
    
    # Обновление значений из запроса, если они переданы
    if the_text:
        config_query["printer"]["the_text"] = the_text
    if background_colour:
        config_query["printer"]["background_colour"] = background_colour
    
    # Сохранение обновленной конфигурации в файл config_query.json
    with open("config_query.json", "w") as query_file:
        json.dump(config_query, query_file, indent=4)
    logger.debug("Config file generated successfully")
    return {"message": "Config file generated successfully"}


if __name__ == "__main__":
    logger.debug('Fast api app started')
    import uvicorn
    uvicorn.run(app, port=8000, host="localhost")