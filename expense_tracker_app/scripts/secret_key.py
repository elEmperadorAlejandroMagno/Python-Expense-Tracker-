import secrets

if __name__ == '__main__':
  secret_key = secrets.token_urlsafe(50)
  print(secret_key)
