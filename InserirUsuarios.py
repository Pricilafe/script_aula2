#!/usr/bin/env python3

import subprocess

#define o nome de usuário e senha do novo usuário

new_user_name = "pricila"
new_user_password = "pris123"

#cria o usuário no sistema linux

subprocess.run(["sudo","useradd",new_user_name])
subprocess.run(["sudo","passwd",new_user_name], input=f"{new_user_password}\n{new_user_password}\n".encode())


