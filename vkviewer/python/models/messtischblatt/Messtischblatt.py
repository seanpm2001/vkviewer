from vkviewer.python.models.Meta import Base
from vkviewer.python.models.messtischblatt.Geometry import Geometry
from vkviewer.python.georef.geometry import createBBoxFromPostGISString
from vkviewer.settings import srid_database

from sqlalchemy import Column, Integer, Boolean, String
from sqlalchemy import desc

from webhelpers.paginate import PageURL_WebOb, Page
from webhelpers.text import urlify

class Messtischblatt(Base):
    __tablename__ = 'messtischblatt'
    __table_args__ = {'extend_existing':True}
    id = Column(Integer, primary_key=True)
    blattnr = Column(String(255))
    dateiname = Column(String(255))
    verzeichnispfad = Column(String(255))
    archivpfad = Column(String(255))
    isttransformiert = Column(Boolean)
    istkomprimiert = Column(Boolean)
    istaktiv = Column(Boolean)
    mdtype = Column(String(255))
    hasgeorefparams = Column(Integer)
    zoomify_properties = Column(String(255))
    zoomify_width = Column(Integer)
    zoomify_height = Column(Integer)
    boundingbox = Column(Geometry)   
    original_path = Column(String(255))

    
    @classmethod
    def all(cls, session):
        return session.query(Messtischblatt).order_by(desc(Messtischblatt.id))
    
    @classmethod
    def allForBlattnr(cls, blattnr, session):
        return session.query(Messtischblatt).filter(Messtischblatt.blattnr == blattnr).order_by(desc(Messtischblatt.id))
    
    @classmethod
    def by_id(cls, id, session):
        return session.query(Messtischblatt).filter(Messtischblatt.id == id).first()
    
    @classmethod
    def get_paginator_forBlattnr(cls, request, blattnr, page=1):
        page_url = PageURL_WebOb(request)
        return Page([{'mtbid':1},{'mtbid':2},{'mtbid':3},{'mtbid':4}], page, url=page_url, items_per_page=10)
        #return Page(Messtischblatt.all(), page, url=page_url, items_per_page=10)

    #BOX(13.6666660308838 51,13.8333339691162 51.1000061035156)', 'time': 1930}, {'id': 71055581, 'extent': 'BOX(13.6666660308838 51,13.8333339691162 51.1000061035156)
    @classmethod
    def getExtent(cls, id, session):
        query = 'SELECT st_extent(st_transform(boundingbox, 900913)) FROM messtischblatt WHERE id = :id;'
        pg_extent = session.execute(query,{'id':id}).fetchone()[0]
        extent = pg_extent.replace(' ',',')[4:-1].split(',')
        parsed_extent = []
        for i in range(0,len(extent)):
            parsed_extent.append(float(extent[i]))
        return parsed_extent
       
    @property
    def slug(self):
        return urlify(self.dateiname)
    
    @property
    def BoundingBoxObj(self):
        return createBBoxFromPostGISString(self.boundingbox, srid_database)
 

  