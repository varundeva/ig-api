from flask import jsonify
from app.api.utils import mask_email,mask_phone

def get_users():
    users = [
        {'id': 1, 'name': 'John Doe','email':'abasasdvb@gmail.com','phone':'9214523658'},
        {'id': 2, 'name': 'Jane Smith','email':'abasasdvb@gmail.com','phone':'9214523658'},
        {'id': 3, 'name': 'Bob Johnson','email':'abasasdvb@gmail.com','phone':'9214523658'}
    ]
     # Mask the user's email and phone using the utility functions
    
    for user in users:
        maskedEmail = mask_email(user['email'])
        maskedPhone = mask_phone(user['phone'])
        user['email'] = maskedEmail
        user['phone'] = maskedPhone
    return jsonify(users)

def get_user(user_id):
    user = {'id': user_id, 'name': 'John Doe'}
    return jsonify(user)

def create_user(user_data):
    user = {'id': 4, 'name': user_data['name']}
    return jsonify(user)

def update_user(user_id, user_data):
    user = {'id': user_id, 'name': user_data['name']}
    return jsonify(user)

def delete_user(user_id):
    return jsonify({'message': 'User deleted successfully'})
