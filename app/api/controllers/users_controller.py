from flask import jsonify
from app.config import getIgConnection
from instaloader import Profile 
from app.api.utils import getUserMetaInfo

def getProfilePhoto(userName):
    conn = getIgConnection()
    try:
        profile = Profile.from_username(conn,userName)
        return jsonify({
            'status':True,
            'data':{
                'profilePicUrl': profile.profile_pic_url,
            }
    
            
        })
    except Exception as e:
        return jsonify({
            'status': False,
            'message': 'Something went Wrong. Server Error or Profile Not Found',
            'error' : str(e)
        }) , 500


def getMetaData(userId):
    conn = getIgConnection()
    try:
        profile = Profile.from_username(conn,userId)
        return jsonify({
            'status': True,
            'data': getUserMetaInfo(profile)
        })
    except Exception as e:
        return jsonify({
            'status': False,
            'message': 'Something went Wrong. Server Error or Profile Not Found',
            'error' : str(e)
        }) , 500

    