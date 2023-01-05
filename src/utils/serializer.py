from itsdangerous import URLSafeSerializer, SignatureExpired
import os

secretkey = os.environ['SECRET_KEY']

s = URLSafeSerializer(secretkey)