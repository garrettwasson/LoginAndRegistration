# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re, bcrypt

class UserManager(models.Manager):
    def reg_validator(self, postData):
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        reg_errors = {}
        hashword = bcrypt.hashpw('password'.encode(),bcrypt.gensalt())

        if len(postData['first_name']) < 1:
            reg_errors["first_name"] = "First name can not be blank!"
        if len(postData['last_name']) < 1:
            reg_errors["last_name"] = "Last name can not be blank!"
        if not email_regex.match(postData['email']):
            reg_errors["email"] = "Invalid email format!"
        if len(postData['password']) < 6:
            reg_errors["password"] = "Password must be at least 6 characters!"
        if postData['confirm_password'] != postData['password']:
            reg_errors["confirm_password"] = "Passwords do not match!"
        return reg_errors
        
    def login_validator(self, postData):
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        login_errors = {}
        if not email_regex.match(postData['email']):
            login_errors["email"] = "Invalid email format!"
        if len(postData['password']) < 6:
            login_errors["password"] = "Password must be at least 6 characters!"
        return login_errors

class User(models.Manager):
    first_name = models.CharField(max_length=255),
    last_name = models.CharField(max_length=255),
    email = models.CharField(max_length=255),
    password = models.CharField(max_length=255),
    updated_at = models.DateTimeField(auto_now = True),
    created_at = models.DateTimeField(auto_now_add = True),
    objects = UserManager()

# Create your models here.
