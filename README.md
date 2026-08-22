# Conference Room Reservation Application

## Overview
For this project, I am building a meeting room reservation system 
application that allows users to create, read, update, and delete (CRUD)
room reservations. The project uses the FastAPI web framework and Pydantic data
validation library. 

## Tech Stack:
- **Python**
- **PostgreSQL**
- **FastAPI**
- **Uvicorn**
- **Pydantic**
- **SQLModel**
- **Alembic**
- **Docker**

## Known Limitations:
1. **Timezone output consistency.** Reservation timestamps are stored
   correctly as timezone-aware UTC instants, and all incoming times are
   required to include timezone information. However, the API currently
   returns timestamps rendered in the server's local timezone rather than
   normalized to UTC (e.g. a time submitted as `14:00Z` may be returned as
   `10:00-04:00`). These represent the identical instant, so this does not
   affect correctness or the double-booking logic — it is purely a display
   inconsistency. A future improvement would normalize all API responses to
   return UTC (Z) consistently, leaving timezone conversion to the client.
