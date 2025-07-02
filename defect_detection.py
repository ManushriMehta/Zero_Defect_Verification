
import streamlit as st
import tensorflow as tf
from keras.layers import TFSMLayer
import numpy as np
from PIL import Image

model = TFSMLayer("saved_model", call_endpoint="serving_default")

with open("labels.txt", "r") as f:
    labels = [line.strip().split(" ", 1)[1].lower() for line in f.readlines()]

def predict(image):
    img = image.resize((224, 224))
    img_array = np.asarray(img) / 255.0
    img_array = np.expand_dims(img_array.astype(np.float32), axis=0)
    result = model(img_array)
    output_tensor = list(result.values())[0]
    predictions = output_tensor.numpy()[0]
    class_index = np.argmax(predictions)
    confidence = predictions[class_index]
    return labels[class_index], confidence

st.set_page_config(page_title="Zero Defect Verification", layout="centered")
st.title("🛡️ Zero Defect Packaging Verification")
st.markdown("Ensure your packaging is verified **accurately** using AI-powered detection.")

mode = st.radio("Choose Mode", ["📸 Upload Image", "📷 Use Webcam"])

if mode == "📸 Upload Image":
    uploaded = st.file_uploader("Upload a test image...", type=["jpg", "jpeg", "png"])
    if uploaded:
        image = Image.open(uploaded)
        st.image(image, caption="Uploaded Image", use_container_width=True)
        label, confidence = predict(image)
        st.markdown(f"**Prediction:** `{label}` ({confidence*100:.2f}%)")
        if label == "good":
            st.success("✅ Status: Good (No Defect Detected)")
        else:
            st.error("❌ Status: Defective Packaging")

elif mode == "📷 Use Webcam":
    st.info("Click 'Take Photo' to capture an image from your webcam.")
    cam_image = st.camera_input("Take a photo")

    if cam_image:
        image = Image.open(cam_image)
        st.image(image, caption="Captured Image", use_container_width=True)
        label, confidence = predict(image)
        st.markdown(f"**Prediction:** `{label}` ({confidence*100:.2f}%)")
        if label == "good":
            st.success("✅ Status: Good (No Defect Detected)")
        else:
            st.error("❌ Status: Defective Packaging")

st.caption("© Intel AI X GTU | Zero Defect Verification Created by Team ID:G00029")
