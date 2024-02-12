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


@dataclass
class SimpleUser:
    full_name: str
    email: str
    current_address: str
    permanent_address: str


person = SimpleUser(
    full_name='John Wick',
    email='jwick@gmail.com',
    current_address='121 Mill Neck, Long Island, NY',
    permanent_address='121 Mill Neck, Long Island, NY')
