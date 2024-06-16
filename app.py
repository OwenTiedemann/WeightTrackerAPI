from litestar import Litestar, get
import motor.motor_asyncio
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_TOKEN = os.environ['MONGO_TOKEN']
database_client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_TOKEN)
information_database = database_client["weight_tracker"]
information_collection = information_database["information"]


@get("/")
async def ping() -> str:
    return "pong"


@get("/api/weight-tracker/information")
async def get_information() -> list[dict[str, str]]:
    return await information_collection.find().to_list(length=None)


app = Litestar([ping, get_information])
