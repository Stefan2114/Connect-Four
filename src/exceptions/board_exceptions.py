


class Board_Exception(Exception):

    def __init__(self, message:str):
        self.__message = message

    def __str__(self):
        return "BOARD EXCEPTION: " + self.__message


class Location_Not_Valid(Board_Exception):

    def __init__(self):
        Board_Exception.__init__(self,"The column is already full")