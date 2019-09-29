from flask_restful import reqparse

user_parser_post = reqparse.RequestParser()
user_parser_get = reqparse.RequestParser()

user_parser_post.add_argument(
    'name', help='Name field cannot be blank', required=True, type=str)
user_parser_post.add_argument(
    'email', help='Email field cannot be blank', required=True, type=str)
user_parser_post.add_argument(
    'password', help='Password field cannot be blank', required=True, type=str)
user_parser_post.add_argument(
    'institution', help='Institution field cannot be blank', required=True, type=str)

user_parser_get.add_argument('name')
user_parser_get.add_argument('email')
user_parser_get.add_argument('institution')
