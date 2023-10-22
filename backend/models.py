from sqlalchemy import Column, Integer, String, Boolean,DateTime
from config.database_config import Base
class Resource(Base):
    __tablename__ = 'resources'
    resource_id = Column(Integer, primary_key=True)
    resource_title= Column(String(255))
    resource_subtitle = Column(String(255))
    resource_link = Column(String(255))
    resource_type = Column(String(255))
    resource_domain = Column(String(255))
    resource_img_path = Column(String(255))
    is_active = Column(Boolean)
    creation_date = Column(DateTime)

