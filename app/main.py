##########################################################################################
# Note: conference-room-reservation-app uses the postgreSQL "room_reservations" database.
##########################################################################################
from fastapi import FastAPI
from app.database import SessionDep # create_db_and_tables (removed)
from sqlalchemy import text
from contextlib import asynccontextmanager
from app.models.room import Room        # Note: Do Not Delete even though appears unused.
from app.models.user import User
from app.routers.room import router as rooms_router



# Note: Async required for lifespan pattern
# create_db_and_tables() on startup replaced with tables managed by Alembic
@asynccontextmanager
async def lifespan(app: FastAPI):
    # --- Startup: Nothing needed. Schema managed by Alembic migrations.
    yield       # Sits open handling app's requests
    # --- Shutdown: runs once, after the app stops

# Note: async def lifespan must be declared ABOVE app = FASTAPI(lifespan = lifespan)
app = FastAPI(lifespan=lifespan)

# --- Endpoints ---
@app.get("/health")
def get_health():
    return{"status": "ok"}

# Test endpoint to check database connection
@app.get("/db-check")
def get_db_check(session:SessionDep):
    value = session.connection().execute(text("SELECT 1")).scalar()   #Queries db with "SELECT 1" just echo's "1" back to application
    return{"value": value, "status" : "ok"}                  # Pure SQL must be text( ) and turned back to scalar

# Connect Router --> The Routers store the endpoints
app.include_router(rooms_router)