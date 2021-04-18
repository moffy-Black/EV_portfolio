from database import SessionLocal
from models import Company, User

db = SessionLocal()

def seed():
    cname = [
        "Alfa",
        "Beta",
        "Ganm"
    ]
    local = [
        "東京都港区芝公園4丁目2-8",
        "東京都文京区後楽1丁目3-61",
        "東京都台東区浅草2丁目3番1号"
    ]

    company = [Company(companyname=companyname,local=local) for (companyname,local) in zip(cname,local)]

    user = User(username='Emile')

    db.add(user)
    db.add(company[2])
    db.commit

if __name__ == '__main__':
    BOS = '\033[92m'  # 緑色表示用
    EOS = '\033[0m'

    print(f'{BOS}Seeding data...{EOS}')
    seed()
