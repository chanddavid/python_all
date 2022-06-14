from imp import source_from_cache


class hajurbuwa:
    a=2
    def __init__(self,game,*args,**kwargs):
        self.game=game
    def play(self):
        print(f"the game name is {self.game}")


class buwa:
    a=3
    def __init__(self,outdoor,place):
        self.outdoor=outdoor
        self.place=place

    def hobbies(self):
        print(f"the outdoor hobbies is {self.outdoor} and is cost {self.place}")


class choro(hajurbuwa,buwa):
    def __init__(self,game,*args, **kwargs):
        self.game=game
        super().__init__(game, *args, **kwargs)

        
obj1=choro("cricket", "")
print(obj1.a)
print(obj1.hobbies())