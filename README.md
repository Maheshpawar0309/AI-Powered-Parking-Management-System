# Real-Time Parking Management System 🚗

A **Real-Time Parking Management System** designed to streamline parking operations using AI-powered license plate recognition, real-time slot tracking, automated payment processing, and an intuitive dashboard interface. This project leverages computer vision, machine learning, and web technologies to provide a complete parking management solution.



## Features 🌟

1. **License Plate Recognition (LPR):**
   - Detects and recognizes vehicle license plates in real-time using OpenCV Haar cascades and Optical Character Recognition (OCR).
   - Automates vehicle entry and exit processes.

2. **Parking Slot Management:**
   - Tracks the availability of parking slots using real-time camera feeds and segmentation models.
   - Dynamically updates parking slot statuses on the dashboard.

3. **Automated Payment Processing:**
   - Calculates parking fees based on the duration of vehicle stay.
   - Integrates with payment gateways for seamless and secure transactions.

4. **Smart Dashboard:**
   - Web-based user interface for administrators.
   - Monitors vehicle logs, available parking slots, and payment statuses in real-time.

---

## Project Structure 📂

real_time_parking_system/ ├── app/ │ ├── init.py # Initializes the Flask app │ ├── routes.py # Handles all application routes and logic │ ├── models.py # Defines data models (e.g., logs, slot status) │ ├── templates/ # HTML templates for the web interface │ │ ├── dashboard.html │ ├── static/ # Static files for styling │ │ ├── styles.css ├── haarcascades/ │ ├── haarcascade_russian_plate_number.xml # Haar cascade for license plate detection ├── uploads/ # Temporary storage for uploaded images ├── main.py # Entry point for the application ├── requirements.txt # Python dependencies ├── Procfile # Deployment configuration for Heroku ├── runtime.txt # Python runtime version for Heroku ├── README.md # Project documentation

## Technologies Used 💻

- **Languages:** Python, HTML, CSS
- **Frameworks:** Flask, OpenCV
- **Tools & Libraries:** 
  - OpenCV for Computer Vision
  - Tesseract OCR for Text Recognition
  - Flask for Backend Development
  - SQLite for Database
- **Cloud Platforms:** Heroku/AWS/Azure (for deployment)

---

## How It Works ⚙️

1. **Vehicle Entry:**
   - The system captures the license plate image as the vehicle enters the parking area.
   - The LPR module extracts and records the license plate number.
   - The system assigns an available slot and updates the dashboard.

2. **Real-Time Slot Tracking:**
   - The parking area is monitored via a camera feed.
   - Slot availability is dynamically tracked and displayed on the dashboard.

3. **Vehicle Exit:**
   - The system captures the license plate image again during exit.
   - Calculates the parking duration and fees.
   - Deducts the charges automatically from the registered account.

4. **Smart Dashboard:**
   - Administrators can view:
     - Vehicle logs (entry/exit times, license numbers, duration, and fees).
     - Current parking slot status (occupied/available).
     - Payment details for each vehicle.

---

## Setup Instructions 🛠️

### Prerequisites:
- Python 3.8 or later
- Pip (Python package manager)
- Virtual Environment (recommended


Future Enhancements 🛠️
Add AI Models: Improve license plate detection accuracy using advanced deep learning models like YOLO or TensorFlow.
Mobile App: Create a companion mobile app for user convenience.
Multi-Language Support: Add support for multiple languages on the dashboard.


Acknowledgments 🙏
Sanjivani Group of Institutes for project guidance.
Open-source contributors of OpenCV and Flask.
