# 🛡️ Zero-Defect Packaging Verification using AI

An AI-powered web application designed to detect defective packaging in real-time using image classification. Built with a pre-trained model from Teachable Machine and deployed via Streamlit, this project aims to eliminate human error and improve quality assurance in packaging lines.

---

## 📌 Objective

- Identify key packaging defects using AI.
- Build a robust image classification model.
- Provide real-time feedback in the packaging line.
- Achieve ≥ 95% defect detection accuracy.
- Ensure ease of use for non-technical staff.

---

## 🛠️ Technologies Used

### 👨‍💻 Programming Languages
- Python 3

### ⚙️ Frameworks & Libraries
- Streamlit (Web App)
- TensorFlow & Keras (Model Inference)
- NumPy, OpenCV, Pillow (Image Handling)

### 📁 Model
- Exported TensorFlow SavedModel from [Teachable Machine](https://teachablemachine.withgoogle.com/)
- Integrated using `keras.layers.TFSMLayer` (Keras 3-compatible)

---

## 🎯 Features

- Upload image or use webcam to test packaging
- AI-based classification into `Good` or `Defective`
- Real-time prediction with confidence percentage
- Visual status feedback (✅ Good / ❌ Defective)
- Lightweight and easy-to-deploy

---

## 📦 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/zero-defect-verification.git
   cd zero-defect-verification
