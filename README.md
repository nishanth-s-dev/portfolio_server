## Setup
- Clone the repository
- Install the dependencies using `pip install -r requirements.txt`
- Create a `.env` file in the root directory and add the following variables 
  - `FLASK_APP=run.py` 
  - `DB_USERNAME=<your_db_username>` 
  - `DB_PASSWORD=<your_db_password>` 
- Run the application using `flask run`

## Endpoints :
### Base URL : `https://localhost:5005/api`

### GET
- /api
- /api/players
- /api/players/<player_id>
- /api/projects/
- /api/projects/<project_id>
- /api/connections
- /api/connections/<connection_id>
