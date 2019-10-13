from flask import Blueprint
from flask_restful import Api
from resources.Hello import Hello
from resources.Category import CategoryResource
from resources.PostWeibo import PostWeiboResource
from resources.UserWeibo import UserWeiboResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(Hello, '/Hello')
api.add_resource(CategoryResource, '/Category')
api.add_resource(PostWeiboResource, '/PostWeibo')
api.add_resource(UserWeiboResource, '/UserWeibo')


from flask import request, jsonify
from Model import db, UserWeibo, UserWeiboSchema, PostWeibo, PostWeiboSchema
from flask_restful import Resource
postweibos_schema = PostWeiboSchema(many=True)
userweibos_schema = UserWeiboSchema(many=True)
import json

@api_bp.route('/Suggest/')
@api_bp.route('/Suggest/<string:at_user_id>')
def suggest(at_user_id=None):
    if at_user_id is None:
        return 'Supposed to input user id'

    # userweibo = UserWeibo.query.filter_by(user_id=user_id).first()
    # if userweibo:
    #     return jsonify({'message': 'PostWeibo already exists'}, 400)


    postweibo = PostWeibo.query.filter_by(at_user_id=at_user_id)
    postweibo = postweibos_schema.dump(postweibo).data
    postweibo_dumps = json.dumps(postweibo)
    res = [];
    postweibo_json = json.loads(postweibo_dumps)
    for index in range(len(postweibo_json)):
        userweibo = UserWeibo.query.filter_by(weibo_id=postweibo_json[index]["weibo_id"])
        userweibo = userweibos_schema.dump(userweibo).data
        userweibo_dumps = json.dumps(userweibo)
        userweibo_json = json.loads(userweibo_dumps)
        for i in range(len(userweibo_json)):
            relate_weibo_id = UserWeibo.query.filter_by(user_id=userweibo_json[i]['user_id'])
            relate_weibo_id = userweibos_schema.dump(relate_weibo_id).data
            relate_weibo_id_dumps = json.dumps(relate_weibo_id)
            relate_weibo_id_json = json.loads(relate_weibo_id_dumps)
            for ii in range(len(userweibo_json)):
                recommend_user = PostWeibo.query.filter_by(weibo_id=relate_weibo_id[i]["weibo_id"])
                recommend_user = postweibos_schema.dump(recommend_user).data
                recommend_user_dumps = json.dumps(recommend_user)
                recommend_user_json = json.loads(recommend_user_dumps)
                res += recommend_user_json

    return str(res)
