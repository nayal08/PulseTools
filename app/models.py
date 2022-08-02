from ast import Str
import email
from email.policy import default
from enum import unique
from operator import index
import string
from sqlalchemy import Column, ForeignKey, Integer, String,TIMESTAMP
from config import Base


class Influencers(Base):
    __tablename__ ="influencers"

    id = Column(Integer, primary_key=True, auto_increment=True)
    full_name=Column(String,default=None)
    email=Column(String,default=None,unique=True,index=True)
    upvotes=Column(Integer,unique=True, index=True,default=0)
    downvotes=Column(Integer,unique=True, index=True,default=0)
    rating=Column(Integer,unique=True, index=True,default=0)
    youtube_link=Column(String,default=None,unique=True,index=True)
    bio=Column(String,default=None,unique=True,index=True)
    add_ts=Column(TIMESTAMP)
    update_ts=Column(TIMESTAMP, default=None)

class SocialLinks(Base):
    __tablename__="social_links"

    id = Column(Integer, primary_key=True, auto_increment=True, index=True)
    influencer_id=Column(Integer,ForeignKey(Influencers.id))
    website=Column(String, default=None)
    telegram=Column(String, default=None)
    twitter=Column(String, default=None)
    github=Column(String, default=None)
    unicrypt=Column(String,default=None)
    discord=Column(String,default=None)
    update_ts=Column(TIMESTAMP, default=None)
    

class Reactions(Base):
    __tablename__="reactions"
    id = Column(Integer, primary_key=True, auto_increment=True)
    influencer_id=Column(Integer,ForeignKey(Influencers.id))
    super_duper=Column(Integer,unique=True, index=True,default=0)
    smiley=Column(Integer,unique=True, index=True,default=0)
    heart=Column(Integer,unique=True, index=True,default=0)
    dislike=Column(Integer,unique=True, index=True,default=0)
    update_ts=Column(TIMESTAMP, default=None)

class Achievements(Base):
    __tablename__="achivements"
    id = Column(Integer, primary_key=True)
    influencer_id=Column(Integer,ForeignKey(Influencers.id))
    founder=Column(String, default=None)
    investor=Column(String, default=None)
    whale=Column(String, default=None)
    influencer=Column(String, default=None)
    update_ts=Column(TIMESTAMP, default=None)










