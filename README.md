# Video-Based RAG Question Answering System

A Retrieval-Augmented Generation (RAG) application that allows users to ask questions about course video content and receive context-aware answers with relevant video timestamps.

The system processes video lectures, converts speech into text, generates embeddings for transcript chunks, retrieves the most relevant content based on semantic similarity, and uses a Large Language Model to generate an answer grounded in the retrieved video content.

## Features

- Converts video files into audio using FFmpeg
- Transcribes audio using OpenAI Whisper
- Supports Hindi-to-English translation during transcription
- Splits video transcripts into timestamped chunks
- Generates semantic embeddings using the BGE-M3 embedding model
- Performs similarity search using cosine similarity
- Retrieves the most relevant transcript chunks
- Generates answers using Llama 3.2 through Ollama
- Provides relevant video timestamps to help users locate the source content
- Restricts responses to information available in the course content

## RAG Pipeline

```text
Video Files
     ↓
Extract Audio using FFmpeg
     ↓
Speech-to-Text using Whisper
     ↓
Timestamped Transcript Chunks
     ↓
Generate Embeddings using BGE-M3
     ↓
Store Embeddings and Metadata
     ↓
User Question
     ↓
Generate Question Embedding
     ↓
Cosine Similarity Search
     ↓
Retrieve Top-K Relevant Chunks
     ↓
Construct Context-Aware Prompt
     ↓
Generate Answer using Llama 3.2
     ↓
Answer with Relevant Video Timestamp
```

## Tech Stack

* Python
* OpenAI Whisper – Speech-to-text transcription
* Ollama – Local LLM and embedding inference
* Llama 3.2 – Answer generation
* BGE-M3 – Text embeddings
* Scikit-learn – Cosine similarity search
* Pandas – Data processing
* Joblib – Embedding persistence
* FFmpeg – Video-to-audio conversion

## Project Workflow
1. Extract Audio from Videos

The processvideos.py script converts video files into MP3 audio files using FFmpeg.

2. Transcribe the Audio

The create_chunks.py script uses Whisper to transcribe the audio and creates timestamped transcript chunks.

Each chunk contains:

-Start timestamp
-End timestamp
-Transcript text

3. Generate Embeddings

The read_chunks.py script generates vector embeddings for each transcript chunk using the BGE-M3 embedding model through Ollama.

The embeddings and transcript metadata are stored in:

embeddings.joblib

4. Retrieve Relevant Context

When a user asks a question:

-The question is converted into an embedding.
-Cosine similarity is calculated between the question embedding and transcript embeddings.
-The top 5 most relevant transcript chunks are retrieved.

5. Generate the Answer

* The retrieved transcript chunks are passed as context to Llama 3.2 through Ollama.

* The model generates an answer based on the retrieved content and provides the relevant video timestamp where the topic is discussed.

## Project Structure

```text
RAG_System/
│
├── videos/                 # Input video files
├── audios/                 # Extracted audio files
├── jsons/                  # Transcribed timestamped chunks
│
├── processvideos.py        # Extracts audio from videos
├── create_chunks.py        # Transcribes audio using Whisper
├── read_chunks.py          # Generates embeddings
├── process_incoming.py     # Retrieves context and generates answers
├── speech2text.py          # Audio transcription utility
│
├── embeddings.joblib       # Stored embeddings and transcript data
├── prompt.txt              # Generated prompt context
├── .gitignore
└── README.md
```

## Setup
1. Clone the Repository

```
git clone <your-repository-url>
cd RAG_System
```
2. Install Dependencies
```
pip install openai-whisper pandas numpy scikit-learn joblib requests
```
FFmpeg is also required for audio extraction.

3. Install and Run Ollama

Install Ollama and download the required models:
```
ollama pull bge-m3
ollama pull llama3.2
```

Make sure the Ollama service is running locally.

## Key Concepts Demonstrated

* Retrieval-Augmented Generation (RAG)
* Semantic Search
* Text Embeddings
* Vector Similarity Search
* Speech-to-Text Processing
* LLM-Based Question Answering
* Prompt Engineering
* Local LLM Inference
* Grounded Question Answering



