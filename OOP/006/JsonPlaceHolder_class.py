class JsonPlaceHolder():
    def __init__(self, userId:str, id:str, title:str, body:str):
        self.__userId = userId
        self.__id = id
        self.__title = title
        self.__body = body
    
    def show(self):
        print(f'''
              >>> UserId: {self.__userId}
              >>> Id: {self.__id}
              >>> Title: {self.__title}
              >>> Body: {self.__body}
              -------------------------
              ''')