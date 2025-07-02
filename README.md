
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
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**
   ```bash
   streamlit run app.py
   ```

---

## 📂 Project Structure

```
zero-defect-verification/
├── app.py                # Main Streamlit application
├── saved_model/          # Teachable Machine exported model
├── labels.txt            # Class labels (e.g., 0 good, 1 defective)
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## 📊 Measurable Goals

- ≥ 95% prediction accuracy on test data
- Real-time response ≤ 2 seconds
- Confidence score ≥ 90% for accurate predictions
- Usable by non-technical users with minimal training

---

## 🚀 Future Enhancements

- Add database for storing results and logs
- Multi-defect classification support
- Admin dashboard for defect trends
- Mobile app version

---

## 👥 Contributors
- 🤝 Open to contributions!
---

## 📃 License

This project is for academic/demo purposes. Contact the author for any reuse or deployment queries.

---
