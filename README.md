# Paddy Disease Detection System 🌾

A web-based Machine Learning application that detects common rice leaf diseases from uploaded images and provides treatment recommendations.

## Features
- Upload rice leaf image
- Detect 4 rice diseases using Deep Learning
- Display disease result
- Show treatment recommendation
- Simple web interface for users

## Diseases Detected
- Bacterial Blight
- Blast
- Brown Spot
- Tungro

## Tech Stack
- Python
- TensorFlow / Keras
- Flask
- HTML
- CSS
- JavaScript

## Project Structure
```bash
paddy-disease/
│
├── dataset/
├── static/
├── templates/
├── app.py
├── train_model.py
├── predict.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone repository

```bash
git clone https://github.com/Dilanka-Lakmal/paddy-disease-detection.git
```

2. Create virtual environment

```bash
python -m venv venv
```

3. Activate virtual environment

```bash
source venv/Scripts/activate
```

4. Install dependencies

```bash
pip install -r requirements.txt
```

5. Run application

```bash
python app.py
```

## Usage
1. Upload rice leaf image
2. Click **Find the Disease**
3. View detected disease and treatment recommendation

## Future Improvements
- Sinhala language support
- Mobile app version
- More disease classes
- Live camera detection

## Author
Dilanka Lakmal
