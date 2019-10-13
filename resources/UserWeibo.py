from flask import request
from flask_restful import Resource
from Model import db, UserWeibo, UserWeiboSchema

userweibos_schema = UserWeiboSchema(many=True)
userweibo_schema = UserWeiboSchema()

class UserWeiboResource(Resource):
    def get(self):
        userweibos = UserWeibo.query.all()
        userweibos = userweibos_schema.dump(userweibos).data
        return {'status': 'success', 'data': userweibos}, 200
    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = userweibo_schema.load(json_data)
        if errors:
            return errors, 422
        userweibo = UserWeibo.query.filter_by(id=data['id']).first()
        if userweibo:
            return {'message': 'UserWeibo already exists'}, 400
        userweibo = UserWeibo(
            user_id=json_data['user_id'],
            weibo_id=json_data['weibo_id']
            )

        db.session.add(userweibo)
        db.session.commit()

        result = userweibo_schema.dump(userweibo).data

        return { "status": 'success', 'data': result }, 201

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = userweibo_schema.load(json_data)
        if errors:
            return errors, 422
        userweibo = UserWeibo.query.filter_by(id=data['id']).first()
        if not userweibo:
            return {'message': 'UserWeibo does not exist'}, 400
        userweibo.user_id = data['user_id']
        userweibo.weibo_id = data['weibo_id']
        db.session.commit()

        result = userweibo_schema.dump(userweibo).data

        return { "status": 'success', 'data': result }, 204

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = userweibo_schema.load(json_data)
        if errors:
            return errors, 422
        userweibo = UserWeibo.query.filter_by(id=data['id']).delete()
        db.session.commit()

        result = userweibo_schema.dump(userweibo).data

        return { "status": 'success', 'data': result}, 204
