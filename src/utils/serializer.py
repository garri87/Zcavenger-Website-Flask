from itsdangerous import URLSafeSerializer, SignatureExpired
import os
from decouple import config

secretkey = config('SECRET_KEY')
s = URLSafeSerializer(secretkey)