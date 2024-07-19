from app.database.db import Base
from sqlalchemy import Integer, String, Column, BigInteger, DateTime, UniqueConstraint, func, ForeignKey, JSON, Date, Computed
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime, timezone

class ImageModel(Base):
    __tablename__ = 'image'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey('product.id'), nullable=False)
    url: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))

    product = relationship("ProductModel", back_populates="images")