'''
Why use 'List' typing importation:
Since the new python versions you don't need to use this typing
you can use 'list' type, but, the python 3.8 version is still
been used in some projects
'''
from typing import List # python 3.8
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.pets import PetsTable

class PetsRepository:
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def list_pets(self) -> List[PetsTable]:
        with self.__db_connection as db:
            try:
                pets = db.session.query(PetsTable).all()
                return pets
            except NoResultFound:
                return []

    def delete_pets(self, name: str) -> None:
        with self.__db_connection as db:
            try:
                (
                    db.session
                    .query(PetsTable)
                    .filter(PetsTable.name == name)
                    .delete()
                )
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception
