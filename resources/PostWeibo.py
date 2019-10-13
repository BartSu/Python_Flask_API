from flask import request
from flask_restful import Resource
from Model import db, PostWeibo, PostWeiboSchema

postweibos_schema = PostWeiboSchema(many=True)
postweibo_schema = PostWeiboSchema()

class PostWeiboResource(Resource):
    def get(self):
        postweibos = PostWeibo.query.all()
        postweibos = postweibos_schema.dump(postweibos).data
        return {'status': 'success', 'data': postweibos}, 200
    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = postweibo_schema.load(json_data)
        if errors:
            return errors, 422
        postweibo = PostWeibo.query.filter_by(id=data['id']).first()
        if postweibo:
            return {'message': 'PostWeibo already exists'}, 400
        postweibo = PostWeibo(
            weibo_id=json_data['weibo_id'],
            at_user_id=json_data['at_user_id']
            )

        db.session.add(postweibo)
        db.session.commit()

        result = postweibo_schema.dump(postweibo).data

        return { "status": 'success', 'data': result }, 201

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = postweibo_schema.load(json_data)
        if errors:
            return errors, 422
        postweibo = PostWeibo.query.filter_by(weibo_id=data['weibo_id']).first()
        if not postweibo:
            return {'message': 'PostWeibo does not exist'}, 400
        postweibo.weibo_id = data['weibo_id']
        postweibo.at_user_id = data['at_user_id']
        db.session.commit()

        result = postweibo_schema.dump(postweibo).data

        return { "status": 'success', 'data': result }, 204

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = postweibo_schema.load(json_data)
        if errors:
            return errors, 422
        postweibo = PostWeibo.query.filter_by(id=data['id']).delete()
        db.session.commit()

        result = postweibo_schema.dump(postweibo).data

        return { "status": 'success', 'data': result}, 204
