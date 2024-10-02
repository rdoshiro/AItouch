import av
import streamlit as st
from streamlit_webrtc import WebRtcMode, webrtc_streamer


# Webcam stream handling
def video_frame_callback(frame: av.VideoFrame) -> av.VideoFrame:
    # Convert the video frame to a numpy array (BGR format)
    image = frame.to_ndarray(format="bgr24")
    
    # Simply return the original frame without any modifications
    return av.VideoFrame.from_ndarray(image, format="bgr24")


# Streamlit WebRTC component for webcam streaming
webrtc_ctx = webrtc_streamer(
    key="webcam-stream",
    mode=WebRtcMode.SENDRECV,
    video_frame_callback=video_frame_callback,
    media_stream_constraints={"video": True, "audio": False},  # Only video, no audio
)

# Optionally, you can add a message or instructions
st.markdown("Webcam streaming using Streamlit.")
