import assemblyai as aai
import streamlit as st
import uuid
import gc
import base64
from pathlib import Path
import os
from dotenv import load_dotenv
import json
import pandas as pd
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go

# Load environment variables from .env file
load_dotenv()

# Set API key from environment variable
aai.settings.api_key = os.getenv("ASSEMBLYAI_API_KEY")

# Configure page - CRITICAL: This must be first
st.set_page_config(
    page_title="EchoSense - Audio Intelligence Platform",
    page_icon="🎧",
    layout="wide",
    initial_sidebar_state="expanded"  # Force sidebar to be expanded
)

# Initialize session state
if "id" not in st.session_state:
    st.session_state.id = uuid.uuid4()
    st.session_state.file_cache = {}
    st.session_state.analysis_history = []
    st.session_state.export_ready = False

# FIXED CSS - Removed problematic positioning that was hiding sidebar
st.markdown("""
<style>
/* Import Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

* {
    font-family: 'Inter', sans-serif;
}

/* Main app background */
.stApp {
    background: #0a0b0f;
}

/* Sidebar styling - FIXED positioning issues */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #1a1d26 0%, #0f1117 100%);
    border-right: 1px solid rgba(255, 255, 255, 0.05);
}

/* Sidebar content */
section[data-testid="stSidebar"] > div {
    padding-top: 1rem;
}

/* Sidebar headers */
section[data-testid="stSidebar"] h2, 
section[data-testid="stSidebar"] h3 {
    color: #fff !important;
    font-weight: 600 !important;
    margin-bottom: 1rem !important;
    margin-top: 1.5rem !important;
    text-transform: uppercase;
    font-size: 0.85rem !important;
    letter-spacing: 0.02em;
}

/* File uploader styling */
section[data-testid="stSidebar"] .stFileUploader > div {
    background: rgba(255, 255, 255, 0.03) !important;
    backdrop-filter: blur(10px) !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    border-radius: 16px !important;
    padding: 1.5rem !important;
    margin-bottom: 1rem !important;
}

/* File uploader button */
section[data-testid="stSidebar"] button {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 12px !important;
    font-weight: 600 !important;
    padding: 0.75rem 1rem !important;
    margin-top: 0.5rem !important;
}

/* Main content area */
.main .block-container {
    max-width: 1200px;
    padding: 2rem 1rem;
}

/* Hide Streamlit header */
header[data-testid="stHeader"] {
    background: transparent;
    height: 0;
}

/* Main heading with gradient */
.main-header {
    background: linear-gradient(135deg, #00d4ff 0%, #7b2ff7 50%, #ff2d55 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    font-size: 3.5rem !important;
    font-weight: 800 !important;
    text-align: center !important;
    margin-bottom: 0.5rem !important;
}

.subtitle {
    color: rgba(255, 255, 255, 0.6) !important;
    text-align: center !important;
    font-size: 1.1rem !important;
    margin-bottom: 3rem !important;
}

/* Feature cards */
.metric-card {
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.05) 0%, rgba(255, 255, 255, 0.02) 100%) !important;
    backdrop-filter: blur(10px) !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    border-radius: 20px !important;
    padding: 2rem !important;
    margin-bottom: 2rem !important;
    transition: all 0.4s ease !important;
}

.metric-card:hover {
    transform: translateY(-4px) !important;
    border-color: rgba(125, 47, 247, 0.3) !important;
    box-shadow: 0 20px 40px rgba(125, 47, 247, 0.2) !important;
}

/* Text colors */
h1, h2, h3, h4, h5, h6, p, div, span, li {
    color: #fff;
}

/* Tabs styling */
.stTabs [data-baseweb="tab-list"] {
    background: transparent !important;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1) !important;
}

.stTabs [data-baseweb="tab"] {
    color: rgba(255, 255, 255, 0.6) !important;
    background: transparent !important;
    font-weight: 500 !important;
}

.stTabs [aria-selected="true"] {
    color: #fff !important;
    border-bottom: 2px solid #7b2ff7 !important;
}

/* Alert messages */
.stAlert {
    background: rgba(255, 255, 255, 0.03) !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    border-radius: 12px !important;
    color: #fff !important;
}

/* Chat input - FIXED positioning */
.stChatInput {
    background: rgba(10, 11, 15, 0.95) !important;
    border-top: 1px solid rgba(255, 255, 255, 0.1) !important;
}

/* Logo container */
.logo-container {
    text-align: center;
    margin-bottom: 2rem;
    padding: 1.5rem;
    background: rgba(255, 255, 255, 0.02);
    border-radius: 16px;
    border: 1px solid rgba(255, 255, 255, 0.05);
}

.brand-text {
    font-size: 1.8rem;
    font-weight: 700;
    background: linear-gradient(135deg, #00d4ff, #7b2ff7);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.brand-tagline {
    color: rgba(255, 255, 255, 0.5);
    font-size: 0.9rem;
    margin-top: 0.5rem;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

/* Feature icon */
.feature-icon {
    font-size: 2.5rem !important;
    margin-bottom: 1rem !important;
    display: inline-block !important;
}

/* Advanced feature cards */
.advanced-feature {
    background: rgba(125, 47, 247, 0.1);
    border: 1px solid rgba(125, 47, 247, 0.2);
    border-radius: 12px;
    padding: 1rem;
    margin-bottom: 1rem;
    transition: all 0.3s ease;
}

.advanced-feature:hover {
    background: rgba(125, 47, 247, 0.15);
    transform: translateX(4px);
}

/* Stats card */
.stats-card {
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.03) 0%, rgba(255, 255, 255, 0.01) 100%);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 16px;
    padding: 1.5rem;
    margin-bottom: 1rem;
}

/* Scrollbar styling */
::-webkit-scrollbar {
    width: 8px;
    height: 8px;
}

::-webkit-scrollbar-track {
    background: rgba(255, 255, 255, 0.02);
}

::-webkit-scrollbar-thumb {
    background: rgba(125, 47, 247, 0.3);
    border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
    background: rgba(125, 47, 247, 0.5);
}
</style>
""", unsafe_allow_html=True)

def format_file_size(size_bytes):
    """Format file size in human readable format"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.1f} TB"

def timestamp_string(milliseconds):
    """Convert milliseconds to HH:MM:SS format"""
    seconds = milliseconds // 1000
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{hours:02}:{minutes:02}:{seconds:02}"

def display_transcription(transcript):
    """Display transcription with timestamps"""
    st.subheader("📝 Full Transcription")
    
    # Word count
    word_count = len(transcript.text.split())
    st.metric("Word Count", f"{word_count:,}")
    
    # Search functionality
    search_term = st.text_input("🔍 Search in transcript", placeholder="Enter keywords...")
    
    # Display sentences with timestamps
    sentences = transcript.get_sentences()
    for sentence in sentences:
        text_to_display = sentence.text
        
        # Highlight search terms
        if search_term and search_term.lower() in sentence.text.lower():
            text_to_display = f"**{sentence.text}**"
        
        col1, col2 = st.columns([1, 10])
        with col1:
            st.caption(timestamp_string(sentence.start))
        with col2:
            st.write(text_to_display)

def display_summary(transcript):
    """Display summary with key metrics"""
    st.subheader("📋 Executive Summary")
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        duration = transcript.audio_duration if hasattr(transcript, 'audio_duration') else 0
        st.metric("Duration", f"{duration//60:.0f}m {duration%60:.0f}s")
    with col2:
        words = len(transcript.text.split())
        st.metric("Words", f"{words:,}")
    with col3:
        speakers = len(set(u.speaker for u in transcript.utterances)) if hasattr(transcript, 'utterances') else 0
        st.metric("Speakers", speakers)
    with col4:
        confidence = transcript.confidence if hasattr(transcript, 'confidence') else 0.95
        st.metric("Confidence", f"{confidence:.1%}")
    
    # Summary text
    st.info(transcript.summary)

def display_speakers(transcript):
    """Display speaker analysis"""
    st.subheader("👥 Speaker Analysis")
    
    if not hasattr(transcript, 'utterances'):
        st.warning("Speaker diarization not available")
        return
    
    # Calculate speaker statistics
    speaker_data = {}
    for utterance in transcript.utterances:
        speaker = str(utterance.speaker)
        if speaker not in speaker_data:
            speaker_data[speaker] = {"count": 0, "words": 0}
        speaker_data[speaker]["count"] += 1
        speaker_data[speaker]["words"] += len(utterance.text.split())
    
    # Display metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Speakers", len(speaker_data))
    with col2:
        st.metric("Total Utterances", len(transcript.utterances))
    with col3:
        avg_words = sum(s["words"] for s in speaker_data.values()) / len(speaker_data) if speaker_data else 0
        st.metric("Avg Words/Speaker", f"{avg_words:.0f}")
    
    # Create visualization
    if speaker_data:
        df = pd.DataFrame([
            {"Speaker": f"Speaker {k}", "Words": v["words"], "Utterances": v["count"]}
            for k, v in speaker_data.items()
        ])
        
        # Pie chart
        fig = px.pie(df, values='Words', names='Speaker', title="Word Distribution by Speaker")
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font_color='white'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Speaker dialogue
    st.subheader("Speaker Dialogue")
    for utterance in transcript.utterances[:10]:  # Show first 10
        with st.container():
            col1, col2 = st.columns([1, 10])
            with col1:
                st.write(f"**Speaker {utterance.speaker}**")
            with col2:
                st.write(utterance.text)
    
    if len(transcript.utterances) > 10:
        with st.expander(f"View all {len(transcript.utterances)} utterances"):
            for utterance in transcript.utterances[10:]:
                st.write(f"**Speaker {utterance.speaker}**: {utterance.text}")

def display_sentiment(transcript):
    """Display sentiment analysis"""
    st.subheader("😊 Sentiment Analysis")
    
    if not hasattr(transcript, 'sentiment_analysis'):
        st.warning("Sentiment analysis not available")
        return
    
    # Count sentiments
    sentiment_counts = {"POSITIVE": 0, "NEUTRAL": 0, "NEGATIVE": 0}
    for sent in transcript.sentiment_analysis:
        sentiment = str(sent.sentiment).upper()
        if "POSITIVE" in sentiment:
            sentiment_counts["POSITIVE"] += 1
        elif "NEGATIVE" in sentiment:
            sentiment_counts["NEGATIVE"] += 1
        else:
            sentiment_counts["NEUTRAL"] += 1
    
    # Display metrics
    total = sum(sentiment_counts.values())
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("😊 Positive", sentiment_counts["POSITIVE"], 
                 f"{sentiment_counts['POSITIVE']/total*100:.1f}%" if total else "0%")
    with col2:
        st.metric("😐 Neutral", sentiment_counts["NEUTRAL"],
                 f"{sentiment_counts['NEUTRAL']/total*100:.1f}%" if total else "0%")
    with col3:
        st.metric("😞 Negative", sentiment_counts["NEGATIVE"],
                 f"{sentiment_counts['NEGATIVE']/total*100:.1f}%" if total else "0%")
    
    # Sentiment timeline
    if sentiment_counts:
        df = pd.DataFrame([
            {"Sentiment": k, "Count": v, "Percentage": v/total*100}
            for k, v in sentiment_counts.items()
        ])
        
        fig = px.bar(df, x="Sentiment", y="Count", title="Sentiment Distribution",
                    color="Sentiment", color_discrete_map={
                        "POSITIVE": "#4caf50",
                        "NEUTRAL": "#9e9e9e", 
                        "NEGATIVE": "#f44336"
                    })
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font_color='white'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Detailed sentiment
    with st.expander("View Detailed Sentiment Analysis"):
        for sent in transcript.sentiment_analysis[:20]:  # Show first 20
            sentiment_type = str(sent.sentiment).upper()
            if "POSITIVE" in sentiment_type:
                st.success(f"Speaker {sent.speaker}: {sent.text}")
            elif "NEGATIVE" in sentiment_type:
                st.error(f"Speaker {sent.speaker}: {sent.text}")
            else:
                st.info(f"Speaker {sent.speaker}: {sent.text}")

def display_topics(transcript):
    """Display topic analysis"""
    st.subheader("🏷️ Topic Analysis")
    
    if not hasattr(transcript, 'iab_categories') or not transcript.iab_categories:
        st.warning("Topic analysis not available")
        return
    
    topics = sorted(transcript.iab_categories.summary.items(), key=lambda x: x[1], reverse=True)[:10]
    
    if topics:
        # Create DataFrame
        df = pd.DataFrame(topics, columns=["Topic", "Relevance"])
        df["Percentage"] = df["Relevance"] * 100
        
        # Bar chart
        fig = px.bar(df, x="Percentage", y="Topic", orientation='h',
                    title="Top Topics by Relevance")
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font_color='white',
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Topic cards
        for topic, relevance in topics[:6]:
            col1, col2 = st.columns([4, 1])
            with col1:
                st.write(f"**{topic}**")
            with col2:
                st.write(f"{relevance*100:.1f}%")
            st.progress(relevance)

def display_chat(transcript):
    """Display chat interface"""
    st.subheader("💬 AI Assistant")
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Suggested questions if no messages
    if not st.session_state.messages:
        st.info("Ask me anything about your audio! Try: 'What are the main topics?' or 'Summarize the key points'")
        
        # Quick action buttons
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("📋 Get Summary"):
                prompt = "Provide a concise summary of the main points"
                st.session_state.messages.append({"role": "user", "content": prompt})
                st.rerun()
        with col2:
            if st.button("🎯 Key Topics"):
                prompt = "What are the main topics discussed?"
                st.session_state.messages.append({"role": "user", "content": prompt})
                st.rerun()
        with col3:
            if st.button("📝 Action Items"):
                prompt = "List any action items or next steps mentioned"
                st.session_state.messages.append({"role": "user", "content": prompt})
                st.rerun()
    
    # Display messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask about your audio..."):
        # Add user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)
        
        # Generate response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    result = transcript.lemur.task(
                        f"Based on the transcript, answer: {prompt}",
                        final_model=aai.LemurModel.claude3_5_sonnet
                    )
                    response = result.response.strip()
                except Exception as e:
                    response = f"I encountered an error: {str(e)}. Please try rephrasing your question."
            
            st.write(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Clear chat button
    if st.button("🔄 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

def main():
    # Sidebar
    with st.sidebar:
        # Logo and branding
        st.markdown("""
        <div class="logo-container">
            <div class="brand-text">
                🎧 EchoSense
            </div>
            <div class="brand-tagline">Audio Intelligence Platform</div>
        </div>
        """, unsafe_allow_html=True)
        
        # File uploader
        st.markdown("### Upload Audio")
        
        audio_file = st.file_uploader(
            "Select file",
            type=['wav', 'mp3', 'mp4', 'm4a', 'flac', 'aac', 'ogg'],
            help="Supported: WAV, MP3, MP4, M4A, FLAC, AAC, OGG"
        )
        
        if audio_file:
            st.success("✅ File uploaded!")
            st.audio(audio_file)
            
            # File details
            with st.container():
                st.markdown("#### File Details")
                st.write(f"**Name:** {audio_file.name}")
                st.write(f"**Size:** {format_file_size(audio_file.size)}")
                st.write(f"**Type:** {audio_file.type}")
            
            # Processing options
            with st.expander("⚙️ Settings"):
                speakers = st.slider("Expected Speakers", 1, 10, 2)
                auto_lang = st.checkbox("Auto Language Detection", True)
                enhanced = st.checkbox("Enhanced Analysis", True)
        
        # Recent analyses
        st.markdown("---")
        st.markdown("### Recent Analyses")
        
        if st.session_state.analysis_history:
            for item in st.session_state.analysis_history[-3:]:
                st.info(f"📄 {item}")
        else:
            st.caption("No recent analyses")
    
    # Main content
    st.markdown('<h1 class="main-header">🎧 EchoSense</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Transform Audio into Actionable Intelligence</p>', unsafe_allow_html=True)
    
    if not audio_file:
        # Welcome screen
        st.markdown("### Welcome! Upload an audio file to begin.")
        
        # Features
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div class="metric-card">
                <div class="feature-icon">🎯</div>
                <h4>Smart Transcription</h4>
                <p>Industry-leading accuracy with timestamps</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="metric-card">
                <div class="feature-icon">😊</div>
                <h4>Sentiment Analysis</h4>
                <p>Detect emotions and conversation tone</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="metric-card">
                <div class="feature-icon">💬</div>
                <h4>AI Assistant</h4>
                <p>Chat with your audio using AI</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Additional features
        st.markdown("### Core Features")
        features = [
            "✅ Multi-speaker diarization",
            "✅ 100+ language support",
            "✅ Topic modeling & categorization",
            "✅ Intelligent summarization",
            "✅ Export in multiple formats",
            "✅ Real-time Q&A with Claude 3.5"
        ]
        
        col1, col2 = st.columns(2)
        for i, feature in enumerate(features):
            with col1 if i % 2 == 0 else col2:
                st.write(feature)
    
    else:
        # Process audio
        if "transcript" not in st.session_state or st.session_state.get("current_file") != audio_file.name:
            with st.spinner("🎧 Processing audio with AssemblyAI..."):
                try:
                    config = aai.TranscriptionConfig(
                        speaker_labels=True,
                        iab_categories=True,
                        sentiment_analysis=True,
                        summarization=True,
                        language_detection=True,
                        speakers_expected=2
                    )
                    
                    transcriber = aai.Transcriber()
                    st.session_state.transcript = transcriber.transcribe(audio_file, config=config)
                    st.session_state.current_file = audio_file.name
                    
                    # Add to history
                    st.session_state.analysis_history.append(audio_file.name)
                    
                except Exception as e:
                    st.error(f"Error processing audio: {str(e)}")
                    st.stop()
            
            st.success("✅ Analysis complete!")
        
        # Display results in tabs
        tabs = st.tabs([
            "📝 Transcription",
            "📋 Summary", 
            "👥 Speakers",
            "😊 Sentiment",
            "🏷️ Topics",
            "💬 Chat"
        ])
        
        with tabs[0]:
            display_transcription(st.session_state.transcript)
        
        with tabs[1]:
            display_summary(st.session_state.transcript)
        
        with tabs[2]:
            display_speakers(st.session_state.transcript)
        
        with tabs[3]:
            display_sentiment(st.session_state.transcript)
        
        with tabs[4]:
            display_topics(st.session_state.transcript)
        
        with tabs[5]:
            display_chat(st.session_state.transcript)

if __name__ == "__main__":
    main()