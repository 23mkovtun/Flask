import datetime
import os

from sqlalchemy import DateTime, String, create_engine, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

PG_USER = os.getenv("PG_USER", "app")
PG_PASSWORD = os.getenv("PG_PASSWORD", "secret")
PG_DB = os.getenv("PG_DB", "app")
PG_HOST = os.getenv("PG_HOST", "127.0.0.1")
PG_PORT = os.getenv("PG_PORT", 5431)

PG_DNS = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}"

engine = create_engine(PG_DNS)
Session = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


class Advertisement(Base):
    __tablename__ = "app_ad"

    id: Mapped[int] = mapped_column(primary_key=True)
    header: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str] = mapped_column(String(200), nullable=False)
    creation_date: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=func.now())
    owner: Mapped[str] = mapped_column(String(50))

    @property
    def dict(self):
        return {
            'id': self.id,
            'header': self.header,
            'description': self.description,
            'creation_date': self.creation_date.isoformat(),
            'owner': self.owner
        }


Base.metadata.create_all(bind=engine)
