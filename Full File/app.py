from flask import Flask, render_template, request, jsonify
import os
import json
from datetime import datetime

app = Flask(__name__)

# Contact form submissions stored in memory (use a DB for production)
contact_submissions = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/contact', methods=['POST'])
def contact():
    data = request.get_json()
    if not data:
        return jsonify({'success': False, 'message': 'No data provided'}), 400

    name = data.get('name', '').strip()
    email = data.get('email', '').strip()
    message = data.get('message', '').strip()
    budget = data.get('budget', '').strip()

    if not name or not email or not message:
        return jsonify({'success': False, 'message': 'Name, email and message are required'}), 400

    submission = {
        'name': name,
        'email': email,
        'message': message,
        'budget': budget,
        'timestamp': datetime.utcnow().isoformat()
    }
    contact_submissions.append(submission)

    # Log to console (visible in Render logs)
    print(f"[CONTACT] {submission['timestamp']} | {name} | {email} | Budget: {budget}")

    return jsonify({'success': True, 'message': 'Thanks! I\'ll get back to you within a few hours.'})

@app.route('/health')
def health():
    return jsonify({'status': 'ok', 'timestamp': datetime.utcnow().isoformat()})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
