from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app) # call restful api
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' # relative path
db = SQLAlchemy(app)

class VPNModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    passwd = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    data_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    last_login = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    user_ip = db.Column(db.String(100), nullable=True)
    
    def __repr__(self):
        return f"VPN(id = {id}, name = {name}, passwd = {passwd}, email = {email}, data_created = {data_created}, last_login = {last_login}, user_ip = {user_ip})"

# with app.app_context():
#     db.create_all()

vpn_put_args = reqparse.RequestParser() # required data below
vpn_put_args.add_argument("user_name", location='form', type=str, help="username is required", required=True)
vpn_put_args.add_argument("passwd", location='form', type=str, help="password is required", required=True)
vpn_put_args.add_argument("email", location='form', type=str, help="email is required", required=True)

vpn_update_args = reqparse.RequestParser()
vpn_update_args.add_argument("user_name", location='form', type=str, help="username is required")
vpn_update_args.add_argument("passwd", location='form', type=str, help="password is required")
vpn_update_args.add_argument("email", location='form', type=str, help="email is required")

resource_fields = {
    'id': fields.Integer,
    'user_name': fields.String,
    'passwd': fields.String,
    'email': fields.String,
    'data_created': fields.String,
    'last_login': fields.String,
    'user_ip': fields.String
}

class VPN(Resource):
    @marshal_with(resource_fields)
    def get(self, vpn_id):
        result = VPNModel.query.filter_by(id=vpn_id).first()
        if not result:
            abort(404, message="could not find vpn with that id...")
        return result
    
    @marshal_with(resource_fields)
    def put(self, vpn_id):
        args = vpn_put_args.parse_args()
        result = VPNModel.query.filter_by(id=vpn_id).first()
        if result:
            abort(409, message="vpn id taken...")
        vpn = VPNModel(id=vpn_id, name=args['user_name'], passwd=args['passwd'], email=args['email'])
        db.session.add(vpn)
        db.session.commit()
        return vpn, 201
    
    @marshal_with(resource_fields)
    def patch(self, vpn_id):
        args = vpn_update_args.parse_args()
        result = VPNModel.query.filter_by(id=vpn_id).first()
        
        if not result:
            abort(404, message="vpn doesn't exist, cannot update...")
            
        if args['user_name']:
            result.user_name = args['user_name']
        if args['passwd']:
            result.passwd = args['passwd']
        if args['email']:
            result.email = args['email']
            
        db.session.commit()
        return result
    
    
    @marshal_with(resource_fields)
    def delete(self, vpn_id):
        del vpn[vpn_id]
        return '', 204

api.add_resource(VPN, "/vpn/<int:vpn_id>")

if __name__ == "__main__":
    app.run(debug=True)