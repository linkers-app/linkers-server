from flask_restplus import Namespace, Resource, fields
from .db import db

api = Namespace("links", description="링크 서비스")

link_model = api.model("Link", {
  "title": fields.String(required=True, description="링크 이름"),
  "url": fields.String(required=True, description="링크 URL"),
  "user_name": fields.String(required=True, description="링크 소유자 인스타그램 사용자 이름")
})

@api.route("/<user_name>")
class LinkListByUserName(Resource):
  @api.doc('인스타그램 사용자 이름에 해당되는 링크를 반환해 줌.')
  @api.marshal_list_with(link_model)
  def get(self, user_name):
    links = list(db.links.find({
      'user_name': user_name
    }))
    return links
