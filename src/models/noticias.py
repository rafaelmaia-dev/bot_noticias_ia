from sqlalchemy import ForeignKey, String, Text, func

from datetime import datetime

from src.database import Base

from sqlalchemy.orm import Mapped, mapped_column

class Noticia(Base):
    __tablename__ = "noticias"

    id: Mapped[int] = mapped_column(primary_key=True)
    url: Mapped[str] = mapped_column(String(2048), unique=True)
    resumo: Mapped[str | None] = mapped_column(String(2000), nullable=True)
    feed_id: Mapped[int] = mapped_column(ForeignKey("feeds.id"))
    titulo: Mapped[str] = mapped_column(String(500))
    descricao: Mapped[str] = mapped_column(Text())
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

