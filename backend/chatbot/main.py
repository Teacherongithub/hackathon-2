import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import google.generativeai as genai

# 1. Initialize FastAPI
app = FastAPI()

# 2. Add CORS Middleware (The "Bridge" between port 3000 and 8001)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows your Docusaurus site to connect
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3. Configure Gemini (Replace with your actual API key if not in Env)
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

# 4. Define Data Models
class ChatRequest(BaseModel):
    message: str

# 5. Chat Endpoint
@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    try:
        response = model.generate_content(request.message)
        return {"response": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 6. Health Check (Optional but helpful)
@app.get("/")
async def root():
    return {"status": "Backend is running on Port 8001"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)