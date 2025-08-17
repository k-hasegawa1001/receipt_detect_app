# DBに登録、あるいはフェッチしてきたデータの加工を行うビジネスロジック層
import hashlib


# パスワードをハッシュ化する関数
def password_to_hash(password: str):
    # SHA-256に暗号化
    password_hash = hashlib.sha256(password.encode())
    return password_hash
