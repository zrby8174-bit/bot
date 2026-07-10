import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, DateTime
import datetime

# الرابط يقرأ من إعدادات Render تلقائياً
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()

# جدول الأرشفة لحفظ المنشورات
class MessageArchive(Base):
    __tablename__ = 'message_archive'
    id = Column(Integer, primary_key=True)
    college_name = Column(String)  # اسم الكلية
    message_type = Column(String)  # نوع المنشور (صورة، ملف، نص)
    message_id = Column(Integer)   # معرف الرسالة
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

# إنشاء الجداول عند تشغيل البوت
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
