# 🔍 Image Forgery Detector (Fake Image Detector)

A desktop application designed to detect digitally altered or tampered images. The project combines digital image forensics with Deep Learning, utilizing **Error Level Analysis (ELA)** to highlight inconsistencies in image compression levels.

## 🚀 Features
* **Modern GUI Architecture:** Built with CustomTkinter supporting a responsive green theme layout.
* **Error Level Analysis (ELA):** Custom PIL implementation that re-saves images at a specific quality matrix to spot pixel anomalies.
* **Real-time DL Prediction:** Integrates a trained Keras/TensorFlow model (`.h5`) for immediate prediction feedback (Real/Fake).
* **Dynamic Content Loading:** Asynchronous visual image representation and result pop-up frames.

## 🛠️ Tech Stack & Libraries
* **Frontend/GUI:** CustomTkinter, Tkinter
* **Image Processing:** PIL (Pillow), OpenCV
* **Deep Learning/ML:** Keras, TensorFlow, NumPy

## 📦 Getting Started
1. Install requirements:
```bash
   pip install customtkinter pillow tensorflow numpy opencv-python
