from fastapi import FastAPI
import datetime

app = FastAPI()


# Default root endpoint
@app.get("/")
async def root():
  return { "message": "Use slack_name and track as query parameters e.g /api/?slack_name=jjxavier&track=backend" }


@app.get("/api")
async def read_item(slack_name: str, track: str):
    x = datetime.datetime.utcnow()
    return {"slack_name": slack_name, "current_day": x.strftime("%A"), "utc_time": x.replace(microsecond=0).isoformat() + "Z", "track": track, "github_file_url": "https://github.com/lastaur0ch/1-name-track/blob/main/main.py", "github_repo_url": "https://github.com/lastaur0ch/1-name-track", "status_code": 200}