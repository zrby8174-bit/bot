import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# تحميل المتغيرات من ملف .env
load_dotenv()

# الرابط المعدل ليعمل مع asyncpg
# ملاحظة: تأكد أنك وضعت الرابط الصحيح في إعدادات Render باسم DATABASE_URL
DATABASE_URL = os.getenv("DATABASE_URL")

# التأكد من إضافة +asyncpg للرابط إذا لم تكن موجودة
if DATABASE_URL and not DATABASE_URL.startswith("postgresql+asyncpg"):
    DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://")

# إنشاء محرك قاعدة البيانات المتزامن
engine = create_async_engine(DATABASE_URL, echo=True)

# إنشاء جلسة للتعامل مع قاعدة البيانات
AsyncSessionLocal = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

Base = declarative_base()

# دالة للحصول على جلسة قاعدة البيانات
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

