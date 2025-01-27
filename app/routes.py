from flask import render_template, request, jsonify
from flask_socketio import SocketIO, emit
import cv2
import pytesseract
from datetime import datetime
from app.models import vehicle_logs, available_slots
from app import app, socketio

@app.route('/')
def dashboard():
    return render_template('dashboard.html', logs=vehicle_logs, slots=available_slots)

@socketio.on('connect')
def handle_connection():
    emit('update_dashboard', {"logs": vehicle_logs, "slots": available_slots})

@app.route('/process_image', methods=['POST'])
def process_image():
    global available_slots
    image_file = request.files['image']
    image_path = f"uploads/{image_file.filename}"
    image_file.save(image_path)

    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    plate_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_indian_plate_number.xmll')
    plates = plate_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    plate_text = "Unknown"
    for (x, y, w, h) in plates:
        plate = gray[y:y+h, x:x+w]
        plate_text = pytesseract.image_to_string(plate, config='--psm 8').strip()

    vehicle_logs.append({
        "plate": plate_text,
        "time_in": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "time_out": None,
        "fee": None
    })
    available_slots -= 1

    socketio.emit('update_dashboard', {"logs": vehicle_logs, "slots": available_slots})

    return jsonify({"message": "Vehicle processed", "plate": plate_text})

@app.route('/checkout', methods=['POST'])
def checkout():
    global available_slots
    plate = request.json['plate']
    for log in vehicle_logs:
        if log['plate'] == plate and log['time_out'] is None:
            log['time_out'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            duration = (datetime.strptime(log['time_out'], "%Y-%m-%d %H:%M:%S") - datetime.strptime(log['time_in'], "%Y-%m-%d %H:%M:%S")).total_seconds() / 3600
            log['fee'] = round(duration * 50, 2)
            available_slots += 1
            socketio.emit('update_dashboard', {"logs": vehicle_logs, "slots": available_slots})
            return jsonify({"message": "Checkout complete", "fee": log['fee']})

    return jsonify({"error": "Vehicle not found or already checked out"})
