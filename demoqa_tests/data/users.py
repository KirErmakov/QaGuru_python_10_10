from dataclasses import dataclass
from enum import Enum


class Gender(Enum):
    Male = 'Male'
    Female = 'Female'
    Other = 'Other'


class Hobby(Enum):
    Sports = 'Sports'
    Reading = 'Reading'
    Music = 'Music'


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: Gender
    mobile_num: str
    date_of_birth: str
    subjects: str
    hobbies: Hobby
    photo: str
    current_address: str
    state: str
    city: str


student = User(
    first_name='Kuraj',
    last_name='Bombei',
    email='kjb@gmail.com',
    gender=Gender.Male,
    mobile_num='9876543210',
    date_of_birth='31 December,1991',
    subjects='Computer Science',
    hobbies=Hobby.Sports,
    photo='Rajesh.jpg',
    current_address='Somewhere in India',
    state='NCR',
    city='Delhi'
)
