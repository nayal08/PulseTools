from typing import Optional
from pydantic import BaseModel, EmailStr
from pydantic.generics import GenericModel

class InfluencerCreate(BaseModel):
    full_name:str
    email:EmailStr
    youtubelink:str
    bio:str

class SocialMediaCreate(BaseModel):
    influencer_id:str
    website:Optional[str]
    telegram:Optional[str]
    twitter:Optional[str]
    github:Optional[str]
    unicrypt:Optional[str]

class ReactionCreate(BaseModel):
    influencer_id:str
    super_duper:Optional[int]
    smiley:Optional[int]
    heart:Optional[int]
    dislike:Optional[int]

class AchievementsCreate(BaseModel):
    influencer_id:str
    founder:Optional[str]
    investor:Optional[str]
    whale:Optional[str]
    influencer:Optional[str]
    





