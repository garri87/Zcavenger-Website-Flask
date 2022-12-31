from itsdangerous import URLSafeTimedSerializer

s= URLSafeTimedSerializer("bf555faaghwlhDS3fdseES")

token = 'ImdhcnJpODdAaG90bWFpbC5jb20i.Y68RJg.I2Ay300XrtA2xSVUL8zsHuaAmGw'
mail= s.loads(token, salt='mail-confirm')


print(mail)