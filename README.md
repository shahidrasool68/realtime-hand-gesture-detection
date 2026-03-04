# realtime-hand-gesture-detection
Real-time hand gesture recognition and finger counting system using OpenCV and MediaPipe. Detects multiple hands and counts fingers using computer vision.



# ✋ Hand Gesture Recognition & Finger Counter

This project is a real-time hand tracking and finger counting system built using **OpenCV** and **MediaPipe**. It detects hands from a webcam feed and counts the number of fingers raised.

---

## 🚀 Features

* Real-time hand detection using webcam
* Detects multiple hands
* Identifies left and right hand
* Counts number of fingers raised
* Displays hand landmarks and connections

---

## 🛠️ Tech Stack

* Python
* OpenCV
* MediaPipe

---

## 📂 Project Structure

```
hand-gesture-recognition-opencv/
│
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

1. Clone the repository:

```
git clone https://github.com/shahidrasool68/hand-gesture-recognition-opencv.git
cd hand-gesture-recognition-opencv
```

2. Install dependencies:

```
pip install -r requirements.txt
```

---

## ▶️ How to Run

```
python main.py
```

* Press **ESC** to exit the application

---

## 🧠 How It Works

* MediaPipe detects 21 hand landmarks
* Landmarks are converted from normalized coordinates to pixel values
* Finger states are determined using:

  * **Thumb** → X-axis comparison
  * **Other fingers** → Y-axis comparison
* Total fingers are counted and displayed

---

## 📸 Output

* Shows webcam feed
* Displays:

  * Hand label (Left / Right)
  * Number of fingers raised
  * Hand skeleton



---




## 📌 Author
Shahid Rasool

