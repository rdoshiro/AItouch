import streamlit as st
import cv2
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
import av

# Title and Description
st.title("Webcam Live Stream")
st.write("This app streams live video from your webcam using WebRTC.")

# WebRTC configuration for live streaming
class VideoTransformer(VideoTransformerBase):
    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")  # Convert frame to ndarray for OpenCV
        img = cv2.flip(img, 1)  # Flip horizontally for a mirror-like view
        return img

# Add the start/stop button for the live stream
webrtc_streamer(
    key="example",
    video_transformer_factory=VideoTransformer,
    rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
    media_stream_constraints={"video": True, "audio": False},
)

st.write("Click 'Start' to begin streaming live from your webcam.")
