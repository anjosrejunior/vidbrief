# 🎥 VidBrief

**Turn hours of video into minutes of reading.**

**VidBrief** is a Python command-line tool (CLI) that automates intelligence extraction from videos. It accurately transcribes audio and uses Artificial Intelligence to generate concise summaries, allowing you to absorb the essential content without watching the entire video.

---

## ✨ Features

* **Automatic Transcription:** Converts spoken content into structured text.
* **AI-Powered Summaries:** Generates a synthesis of key points and valuable insights.
* **Multi-Language Support:** Works with videos in Portuguese, English, and more.
* **Quick Export:** Saves results as `.txt` or `.md` files for later reference.
* **Lightweight and Efficient:** Performance-focused, designed for terminal usage.

---

## 🚀 Getting Started

### Prerequisites

* Python 3.8 or higher  
* An API key (OpenAI, Gemini, or similar), as configured

### Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/vidbrief.git
```

2. Enter the project folder and install dependencies:
```bash
cd vidbrief
pip install -r requirements.txt
``` 
   
3. Install Node.js
```bash
sudo apt update
sudo apt install nodejs
```

4. Install ffmpeg
```bash
sudo apt-get update && apt-get install -y ffmpeg
```

## ⚙️ Configuration
Create a .env file at the root of the project and add your credentials. Just follow the .env_example file.

## 📖 How to Use
To process a video, simply run:
python vidbrief.py --url "https://www.youtube.com/watch?v=EXAMPLE"

The prompt used by the project is located inside the prompts folder, where you can customize it as you see fit.

🛠️ Technologies Used

- Python: Main programming language.
- yt-dlp: An excellent Python library for video extraction.
- Node.js: Required for yt-dlp to function correctly.
- ffmpeg: Required for yt-dlp to function correctly.
- OpenAI: Library used to call the Whisper model for audio transcription.
- LangChain: Used to call the AI model responsible for generating summaries.

🤝 Contributions
Feedback and Pull Requests are very welcome! If you find a bug or have a feature idea, feel free to open an issue.
Built with ☕ by Renato dos Anjos