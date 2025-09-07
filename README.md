# 🎧 EchoSense - Audio Intelligence Platform

<div align="center">
  
  ![EchoSense Banner](https://img.shields.io/badge/EchoSense-Audio%20Intelligence-gradient?style=for-the-badge&logo=audio-technica&logoColor=white&labelColor=7b2ff7&color=00d4ff)
  
  [![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)](https://www.python.org/)
  [![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-FF4B4B?style=flat-square&logo=streamlit)](https://streamlit.io/)
  [![AssemblyAI](https://img.shields.io/badge/AssemblyAI-Latest-00C9FF?style=flat-square)](https://www.assemblyai.com/)
  [![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
  [![Status](https://img.shields.io/badge/Status-Active-success?style=flat-square)](https://github.com/yourusername/echosense)
  
  **Transform audio into actionable intelligence with cutting-edge AI**

  [Demo](#-demo) • [Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [API](#-api) • [Contributing](#-contributing)

</div>

---

## 🌟 Overview

EchoSense is a powerful audio intelligence platform that leverages AssemblyAI's state-of-the-art models to transform audio content into valuable insights. Built with Streamlit for an intuitive web interface and MCP server for API access, it provides comprehensive audio analysis including transcription, speaker diarization, sentiment analysis, topic detection, and AI-powered Q&A.

## 🏗️ Architecture

```mermaid
graph TB
    subgraph FL["<b>Frontend Layer</b>"]
        A[🎧 Audio Input]:::frontend
        B[📱 Streamlit Web App]:::frontend
        C[🎨 Interactive UI]:::ui
    end
    
    subgraph PP["<b>Processing Pipeline</b>"]
        D[🔄 Audio Processing]:::processing
        E[🧠 AssemblyAI API]:::processing
        F[📊 Data Transformation]:::processing
    end
    
    subgraph IF["<b>Intelligence Features</b>"]
        G[📝 Transcription]:::transcription
        H[👥 Speaker Diarization]:::speaker
        I[😊 Sentiment Analysis]:::sentiment
        J[🏷️ Topic Detection]:::topic
        K[📋 Summarization]:::summary
        L[💬 AI Chat with LeMUR]:::chat
    end
    
    subgraph OL["<b>Output Layer</b>"]
        M[📤 Export Options]:::output
        N[🤖 Real-time Q&A]:::output
        O[JSON/CSV/TXT]:::export
    end
    
    subgraph MS["<b>MCP Server</b>"]
        P[🔌 MCP Server]:::mcp
        Q[API Endpoints]:::mcp
        R[External Integration]:::mcp
    end
    
    A --> B
    B --> C
    B --> D
    D --> E
    E --> F
    F --> G & H & I & J & K & L
    G & H & I & J & K --> M
    L --> N
    M --> O
    E --> P
    P --> Q
    Q --> R
    
    classDef frontend fill:#FF6B6B,stroke:#FF4757,color:#fff,stroke-width:2px
    classDef ui fill:#FFD93D,stroke:#FFA502,color:#2C3E50,stroke-width:2px
    classDef processing fill:#4ECDC4,stroke:#00B894,color:#fff,stroke-width:2px
    classDef transcription fill:#6C5CE7,stroke:#5F3DC4,color:#fff,stroke-width:2px
    classDef speaker fill:#00B894,stroke:#00856A,color:#fff,stroke-width:2px
    classDef sentiment fill:#FDCB6E,stroke:#F39C12,color:#2C3E50,stroke-width:2px
    classDef topic fill:#E17055,stroke:#D63031,color:#fff,stroke-width:2px
    classDef summary fill:#74B9FF,stroke:#0984E3,color:#fff,stroke-width:2px
    classDef chat fill:#A29BFE,stroke:#6C5CE7,color:#fff,stroke-width:2px
    classDef output fill:#96CEB4,stroke:#68B684,color:#2C3E50,stroke-width:2px
    classDef export fill:#DDD,stroke:#AAA,color:#2C3E50,stroke-width:2px
    classDef mcp fill:#DDA0DD,stroke:#B19CD9,color:#fff,stroke-width:2px
```

## 🚀 Features

### Core Capabilities

| Feature | Description | Technology |
|---------|-------------|------------|
| 🎯 **Smart Transcription** | Industry-leading accuracy with precise timestamps | AssemblyAI Core |
| 👥 **Speaker Diarization** | Identify and separate up to 10 speakers | Voice Fingerprinting |
| 😊 **Sentiment Analysis** | Detect emotions and conversation dynamics | NLP Models |
| 📋 **Intelligent Summary** | AI-powered key insights extraction | LeMUR AI |
| 🏷️ **Topic Modeling** | Categorization across 700+ IAB categories | Topic Detection |
| 💬 **Interactive Q&A** | Chat with your audio using Claude 3.5 Sonnet | LeMUR Integration |
| 🌐 **Multi-Language** | Support for 100+ languages | Auto-Detection |
| 📊 **Analytics Dashboard** | Visual insights with Plotly charts | Data Visualization |

### Processing Flow

```mermaid
sequenceDiagram
    participant User
    participant Streamlit
    participant AssemblyAI
    participant LeMUR
    participant MCP Server
    
    User->>Streamlit: Upload Audio File
    Streamlit->>AssemblyAI: Send for Processing
    AssemblyAI-->>AssemblyAI: Transcribe
    AssemblyAI-->>AssemblyAI: Analyze Speakers
    AssemblyAI-->>AssemblyAI: Detect Sentiment
    AssemblyAI-->>AssemblyAI: Extract Topics
    AssemblyAI->>LeMUR: Generate Summary
    LeMUR-->>Streamlit: Return Analysis
    Streamlit->>User: Display Results
    User->>Streamlit: Ask Question
    Streamlit->>LeMUR: Process Query
    LeMUR-->>User: AI Response
    
    Note over MCP Server: Parallel API Access
    MCP Server->>AssemblyAI: Direct API Calls
    MCP Server-->>User: Programmatic Access
```

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- AssemblyAI API key ([Get one here](https://www.assemblyai.com/))
- 2GB RAM minimum
- Modern web browser

### Quick Start

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/echosense.git
cd echosense
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables**
```bash
# Create .env file
echo "ASSEMBLYAI_API_KEY=your_api_key_here" > .env
```

4. **Run the application**
```bash
# Start Streamlit app
streamlit run app.py

# Or start MCP server (optional)
python server.py
```

## 🎮 Usage

### Web Interface

1. **Upload Audio**: Click the upload button in the sidebar
2. **Configure Settings**: Adjust speaker count and analysis options
3. **Process**: Wait for AI analysis (typically 30-60 seconds)
4. **Explore Results**: Navigate through tabs for different insights
5. **Ask Questions**: Use the AI chat for specific queries
6. **Export**: Download results in JSON, CSV, or TXT format

### MCP Server API (Optional)

```python
# Example usage with MCP server
from mcp.client import Client

# Initialize client
client = Client("localhost:8080")

# Transcribe audio
result = client.transcribe_audio("path/to/audio.mp3")

# Get specific features
data = client.get_audio_data(
    text=True,
    speakers=True,
    sentiment=True,
    summary=True
)
```

## 📊 Data Flow Diagram

```mermaid
graph LR
    subgraph Input
        A1[WAV] --> B[Audio Processing]
        A2[MP3] --> B
        A3[MP4] --> B
        A4[M4A] --> B
        A5[FLAC] --> B
    end
    
    subgraph Analysis
        B --> C{AssemblyAI Pipeline}
        C --> D[Transcription Engine]
        C --> E[Speaker Detection]
        C --> F[Sentiment Model]
        C --> G[Topic Classifier]
        C --> H[Summarization]
    end
    
    subgraph Intelligence
        D --> I[Timestamped Text]
        E --> J[Speaker Segments]
        F --> K[Emotion Scores]
        G --> L[IAB Categories]
        H --> M[Key Points]
    end
    
    subgraph Output
        I --> N[Searchable Transcript]
        J --> O[Speaker Analytics]
        K --> P[Sentiment Charts]
        L --> Q[Topic Distribution]
        M --> R[Executive Summary]
        N & O & P & Q & R --> S[💾 Export]
    end
    
    style C fill:#00d4ff
    style S fill:#4caf50
```

## 🛠️ Configuration

### Audio Processing Options

```python
config = aai.TranscriptionConfig(
    speaker_labels=True,        # Enable speaker diarization
    speakers_expected=2,         # Number of expected speakers
    iab_categories=True,         # Topic detection
    sentiment_analysis=True,     # Emotion analysis
    summarization=True,          # Auto-summarization
    language_detection=True,     # Auto-detect language
)
```

### Supported Formats

| Format | Extension | Max Size | Quality |
|--------|-----------|----------|---------|
| WAV | .wav | 5GB | Lossless |
| MP3 | .mp3 | 500MB | High |
| MP4 | .mp4 | 500MB | High |
| M4A | .m4a | 500MB | High |
| FLAC | .flac | 5GB | Lossless |
| AAC | .aac | 500MB | High |
| OGG | .ogg | 500MB | High |

## 📈 Performance Metrics

- **Transcription Accuracy**: 95%+ for clear audio
- **Processing Speed**: ~30 seconds per 5-minute audio
- **Language Support**: 100+ languages
- **Speaker Detection**: Up to 10 speakers
- **Concurrent Users**: 50+ (with proper deployment)

## 🎨 Screenshots

<div align="center">

### Main Dashboard
![Dashboard](assets/screenshots/dashboard.png)
*Clean interface for audio upload with feature overview*

### Analysis Results
![Analysis](assets/screenshots/analysis.png)
*Comprehensive multi-tab view of audio insights*

### AI Chat Interface
![Chat](assets/screenshots/chat.png)
*Interactive Q&A powered by Claude 3.5 Sonnet*

</div>

## 🗂️ Project Structure

```
echosense/
├── app.py                 # Main Streamlit application
├── server.py             # MCP server (optional API)
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (create this)
├── assets/
│   └── screenshots/      # Application screenshots
└── README.md            # This file
```

## 📋 Requirements

```txt
streamlit>=1.28.0
assemblyai>=0.20.0
python-dotenv>=1.0.0
pandas>=1.5.0
plotly>=5.0.0
pillow>=9.0.0
```

## 🚀 Deployment

### Local Development
```bash
streamlit run app.py --server.port 8501
```

### Docker Deployment
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["streamlit", "run", "app.py"]
```

### Cloud Deployment Options
- **Streamlit Cloud**: Free hosting for Streamlit apps
- **Heroku**: Easy deployment with git push
- **AWS EC2**: Scalable infrastructure
- **Google Cloud Run**: Serverless deployment

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guide
- Add unit tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting PR

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [AssemblyAI](https://www.assemblyai.com/) for powerful speech recognition APIs
- [Streamlit](https://streamlit.io/) for the amazing web framework
- [Anthropic](https://www.anthropic.com/) for Claude AI integration
- [Plotly](https://plotly.com/) for interactive visualizations
- [MCP](https://modelcontextprotocol.io/) for standardized AI integration

## 📞 Support

- 📧 Email: shikharpatel566@gmail.com
- 🐛 Issues: [GitHub Issues](https://github.com/yourusername/echosense/issues)

## 🚦 Project Status

![Build Status](https://img.shields.io/github/workflow/status/yourusername/echosense/CI?style=flat-square)
![Last Commit](https://img.shields.io/github/last-commit/yourusername/echosense?style=flat-square)
![Contributors](https://img.shields.io/github/contributors/yourusername/echosense?style=flat-square)
![Stars](https://img.shields.io/github/stars/yourusername/echosense?style=flat-square)

## 🔮 Roadmap

- [ ] Real-time streaming transcription
- [ ] Multi-file batch processing
- [ ] Custom vocabulary support
- [ ] Enhanced speaker identification
- [ ] Mobile application
- [ ] Webhook integrations
- [ ] Advanced export formats (PDF, DOCX)
- [ ] Team collaboration features

---

<div align="center">
  
**Built with ❤️ by the EchoSense Team**

[⬆ Back to Top](#-echosense---audio-intelligence-platform)

</div>
