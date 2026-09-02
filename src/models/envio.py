from src.database import Base

from sqlalchemy import ForeignKey, func

from sqlalchemy.orm import Mapped, mapped_column

from datetime import datetime

class Envio(Base):
    __tablename__ = "envios"

    id: Mapped[int] = mapped_column(primary_key=True)
    noticia_id: Mapped[int] = mapped_column(ForeignKey("noticias.id"))
    telegram_message_id: Mapped[int | None] = mapped_column(unique=True, nullable=True)
    sucesso: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

