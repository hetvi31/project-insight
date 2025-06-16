
from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
import parsers

import google.generativeai as genai

load_dotenv()
app = FastAPI()

origins = ["http://localhost:8501"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

@app.post("/upload")
async def upload_and_parse_file(file: UploadFile = File(...)):
    content = await file.read()
    parsed_data = parsers.parse_data(content, file.filename)
    if not parsed_data:
        raise HTTPException(status_code=400, detail="Unsupported file type")
    return parsed_data

@app.post("/chat")
async def chat_with_llm(message: str = Form(...), context: str = Form(...)):
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # prompt = f"Based on the following data context, answer the user's query.\n\nContext:\n{context}\n\nUser Query: {message}"
        prompt = f"""
You are a smart data analysis assistant. Given a dataset provided in the 'Context' below and a user query, follow these steps:

1. Understand the structure and content of the dataset.
2. Identify what the user is asking — whether it's about trends, comparisons, aggregations, filtering, statistics, anomalies, or insights.
3. Perform any required operations such as:
   - Grouping and aggregating (e.g. totals by month/category)
   - Calculating statistics (mean, median, etc.)
   - Identifying patterns or anomalies
   - Filtering or transforming data
4. Give analysis results in a clear, concise manner, don't show raw data unless specifically requested.
5. Use tables or bullet points where appropriate for clarity.

If any assumptions need to be made due to incomplete data, mention them clearly.

---  
Context:\n{context}  
---  
User Query:\n{message}
"""

        response = model.generate_content(prompt)
        
        return {"reply": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Google Gemini API Error: {str(e)}")


