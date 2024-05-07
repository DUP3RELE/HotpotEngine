@app.route('/events', methods=['POST'])
def create_working_hours():
    data = request.json
    working_hours = WorkingHours(title=data['title'], start_time=data['start_time'], end_time=data['end_time'], employee_id=data['employee_id'])
    db.session.add(WorkingHours)
    db.session.commit()
    return jsonify(workingHours.id), 201

@app.route('/events/<int:event_id>', methods=['GET'])
def get_working_hours(worker_id):
    working_hours = WorkingHours.query.get_or_404(worker_id)
    return jsonify({'title': event.title, 'start_time': event.start_time.isoformat(), 'end_time': event.end_time.isoformat()})