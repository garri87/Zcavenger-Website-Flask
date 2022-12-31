from itsdangerous import URLSafeSerializer, SignatureExpired

secretkey = ''

s = URLSafeSerializer(secretkey)