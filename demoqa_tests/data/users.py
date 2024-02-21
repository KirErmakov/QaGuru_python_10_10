from dataclasses import dataclass
from enum import Enum
from typing import List


class Gender(Enum):
    Male = 'Male'
    Female = 'Female'
    Other = 'Other'


class Hobby(Enum):
    Sports = 1
    Reading = 2
    Music = 3


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: Gender
    mobile_num: str
    date_of_birth: str
    subjects: List[str]
    hobbies: List[Enum]
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
    subjects=['Computer Science', 'Maths'],
    hobbies=[Hobby.Sports, Hobby.Music],
    photo='Rajesh.jpg',
    current_address='Somewhere in India',
    state='NCR',
    city='Delhi'
)
