from rest_framework import serializers

from .models import (CustomUser, UserImage, UserFile)


class UserImageSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(default=serializers.CurrentUserDefault(), read_only=True)

    class Meta:
        model = UserImage
        fields = "__all__"


class UserFileSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(default=serializers.CurrentUserDefault(), read_only=True)

    class Meta:
        model = UserFile
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["username", "login", "password", "inn", "logo", "caption", "contacts", "rating", "cards",
                  "comments", "favourites", "images", "files"]
        optional_fields = ["favourites", "images", "logo", "caption",
                           "contacts", "rating", "cards", "comments", "files"]

    def create(self, validated_data):
        login = validated_data["login"]
        flag = True
        contacts = {}
        if len(login) == 12 and login[0] == "+":
            for n in login[1:]:
                if not (n.isdigit()):
                    flag = False
            if flag:
                contacts = {"phone": validated_data["login"]}
        else:
            if login.count("@") == 1:
                if len(login[:login.index('@')]) > 64 or len(login) > 254:
                    flag = False
                if login[0] == '@' or login[-1] == '@' or login[0] == '.' or login[-1] == '.' or login.count(' ') > 0:
                    flag = False
                if flag:
                    contacts = {"email": validated_data["login"]}
            else:
                contacts = {}
        user = CustomUser(username=validated_data["username"], login=validated_data["login"], inn=validated_data["inn"],
                          contacts=contacts)
        user.set_password(validated_data["password"])
        user.save()
        return user
