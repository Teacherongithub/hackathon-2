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
import time
from fastapi import FastAPI, Header, HTTPException, BackgroundTasks
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from google import genai
from google.genai import types
from dotenv import load_dotenv

# --------------------------------------------------
# 1. Load environment variables
# --------------------------------------------------
load_dotenv()

# --------------------------------------------------
# 2. Create FastAPI app
# --------------------------------------------------
app = FastAPI(
    title="RAG Chatbot Backend",
    description="FastAPI + Gemini RAG chatbot for ebook",
    version="1.0.0",
)

# --------------------------------------------------
# 3. Enable CORS
# --------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

<<<<<<< HEAD
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
=======
# --------------------------------------------------
# 4. Initialize Gemini client
# --------------------------------------------------
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise RuntimeError("❌ GEMINI_API_KEY not found in .env")

client = genai.Client(api_key=GEMINI_API_KEY)

# --------------------------------------------------
# 5. Security + Constants
# --------------------------------------------------
MY_SECRET_PASSWORD = os.getenv("API_KEY")
if not MY_SECRET_PASSWORD:
    raise RuntimeError("❌ API_KEY not found in .env")

STORE_DISPLAY_NAME = "hackathon_textbook_store"
STORE_NAME_FILE = "store_name.txt"
MODEL_NAME = "gemini-1.5-flash"  # Reliable on free tier

# --------------------------------------------------
# 6. Root / Health Check
# --------------------------------------------------
@app.get("/")
def root():
    return {
        "status": "✅ RAG Chatbot Backend Running",
        "ingest_endpoint": "/ingest",
        "chat_endpoint": "/api/chat",
    }

# --------------------------------------------------
# Helper: Get or create the File Search store
# --------------------------------------------------
def get_or_create_store():
    if os.path.exists(STORE_NAME_FILE):
        with open(STORE_NAME_FILE, "r") as f:
            store_name = f.read().strip()
        print(f"📂 Reusing existing store: {store_name}")
        return store_name

    print("🆕 Creating new File Search store...")
    store = client.file_search_stores.create(
        config={"display_name": STORE_DISPLAY_NAME}
    )
    with open(STORE_NAME_FILE, "w") as f:
        f.write(store.name)
    print(f"✅ Created store: {store.name}")
    return store.name

# --------------------------------------------------
# 7. Document Ingestion (Background Task)
# --------------------------------------------------
def ingest_ebook_documents():
    try:
        print("📚 Starting ebook ingestion...")
        store_name = get_or_create_store()

        docs_path = "./ebook"
        if not os.path.exists(docs_path):
            print("❌ ebook folder not found")
            return

        md_files = []
        for root_dir, _, files in os.walk(docs_path):
            for file in files:
                if file.endswith(".md"):
                    file_path = os.path.join(root_dir, file)
                    md_files.append(file_path)

        print(f"Found {len(md_files)} .md files to upload.")

        for file_path in md_files:
            uploaded = False
            retries = 0
            while not uploaded and retries < 3:
                try:
                    print(f"⬆️ Uploading: {file_path} (attempt {retries + 1})")
                    operation = client.file_search_stores.upload_to_file_search_store(
                        file=file_path,
                        file_search_store_name=store_name,
                    )

                    # Poll until complete
                    while not operation.done:
                        print("⏳ Waiting for upload to finish...")
                        time.sleep(10)  # Longer wait for stability
                        operation = client.operations.get(name=operation.name)

                    if operation.error:
                        raise RuntimeError(f"Upload error: {operation.error}")

                    print(f"✅ Successfully uploaded: {file_path}")
                    uploaded = True

                except Exception as upload_error:
                    retries += 1
                    print(f"⚠️ Upload failed (attempt {retries}): {upload_error}")
                    if retries < 3:
                        print("🔄 Retrying in 15 seconds...")
                        time.sleep(15)
                    else:
                        print(f"❌ Permanently failed to upload: {file_path}")

            # Delay between files to avoid rate limits on free tier
            time.sleep(10)

        print("✅ Ebook ingestion completed (or partially if some failed)")
    except Exception as e:
        print("❌ Critical ingestion error:", str(e))

@app.post("/ingest")
async def ingest(
    background_tasks: BackgroundTasks,
    x_api_key: str = Header(None),
):
    if x_api_key != MY_SECRET_PASSWORD:
        raise HTTPException(status_code=403, detail="Forbidden")
    background_tasks.add_task(ingest_ebook_documents)
    return {"message": "📖 Ebook ingestion started in background. Check console for progress."}

# --------------------------------------------------
# 8. RAG Chat Endpoint
# --------------------------------------------------
@app.post("/api/chat")
async def chat(
    data: dict,
    x_api_key: str = Header(None),
):
    if x_api_key != MY_SECRET_PASSWORD:
        raise HTTPException(status_code=403, detail="Forbidden")

    user_question = data.get("message")
    if not user_question:
        raise HTTPException(status_code=400, detail="Message is missing")

    if not os.path.exists(STORE_NAME_FILE):
        raise HTTPException(status_code=500, detail="No File Search store found. Run /ingest first.")

    with open(STORE_NAME_FILE, "r") as f:
        store_name = f.read().strip()

    def generate_stream():
        try:
            stream = client.models.generate_content_stream(
                model=MODEL_NAME,
                contents=user_question,
                config=types.GenerateContentConfig(
                    system_instruction=(
                        "You are a helpful tutor. "
                        "Answer ONLY using the ebook content. "
                        "If the answer is not in the ebook, say you don't know."
                    ),
                    tools=[
                        types.Tool(
                            file_search=types.FileSearch(
                                file_search_store_names=[store_name]
                            )
                        )
                    ],
                ),
            )
            for chunk in stream:
                if chunk.text:
                    yield chunk.text
        except Exception as e:
            yield f"\n❌ Chat error: {str(e)}"

    return StreamingResponse(generate_stream(), media_type="text/plain")

# --------------------------------------------------
# 9. Run server
# --------------------------------------------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
>>>>>>> 646602f5 (Finilized structure: unified backend and frontend/ebook)
