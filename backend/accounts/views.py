# from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

User = get_user_model()

class SignUpView(APIView):
    def post(self, request):
        try:
            username = request.data.get('username')
            password1 = request.data.get('password1')
            password2 = request.data.get('password2')

            if password1 != password2:
                raise ValidationError('password mismatch', code='password_mismatch')

            # 회원가입 성공 시 user에 값 저장 및 토큰 생성
            user = User.objects.create_user(username=username, password=password1)
            token, created = Token.objects.get_or_create(user=user)

            # 토큰 담아서 전송
            return Response({"token": token.key}, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            # 에러 케이스 1. 비밀번호가 일치하지 않는 경우
            if e.code=="password_mismatch":
                return Response({"error": "pw_mismatch"}, status=status.HTTP_400_BAD_REQUEST)
            # 에러 케이스 2. 이미 사용 중인 아이디인 경우
            elif "unique" in e.error_dict.get("username", []):
                return Response({"error": "occupied"}, status=status.HTTP_400_BAD_REQUEST)
            # 에러 케이스 3. 기타 경우
            else:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
