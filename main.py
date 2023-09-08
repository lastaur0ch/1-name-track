from fastapi import FastAPI
#from datetime import timezone
import datetime

app = FastAPI()

x = datetime.datetime.utcnow()

# Default root endpoint
@app.get("/")
async def root():
  return { "message": "Use slack_name and track as query parameters e.g /api/?slack_name=jjxavier&track=backend" }


@app.get("/api/")
async def read_item(slack_name: str, track: str):
    return {"slack_name": slack_name, "current_day": x.strftime("%A"), "utc_time": f"{x.replace(microsecond=0)}Z", "track": track, "github_file_url": "https://github.com/username/repo/blob/main/file_name.ext", "github_repo_url": "https://github.com/username/repo", "status_code": 200}