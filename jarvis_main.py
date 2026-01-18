from fastapi import FastAPI, Request
from commands import handle_command
import uvicorn

app = FastAPI()

@app.post("/ask")
async def ask_jarvis(request: Request):
    data = await request.json()
    user_input = data.get("text", "")
    
    # Process using your existing logic
    # We now capture the text instead of calling a local 'speak' function
    response_text = handle_command(user_input)
    
    return {"speech": response_text}

if __name__ == "__main__":
    # Runs on port 5005
    uvicorn.run(app, host="0.0.0.0", port=5005)
