class Video:
    def __init__(self, linkid, title, lenght, likes, dislikes):
        self.__linkid = linkid
        self.__title = title
        self.__lenght = lenght
        self.__likes = likes
        self.__dislikes = dislikes
    
    def __str__(self):
        return f"https://deustube.com/{self.__linkid}"

    def getLikes(self):
        return self.__likes

    def getLenght(self):
        return self.__lenght
    
class Channel:
    def __init__(self, user, title, subscribers, videos, followed):
        self.__user = user
        self.__title = title
        self.__subscribers = subscribers
        self.__videos = videos
        self.__followed = followed
    
    def __str__(self):
        return f"https://deustube.com/{self.__user}"

    def getUser(self):
        return self.__user
    
    def getFollowed(self):
        return self.__followed
    
    def getVideos(self):
        return self.__videos
    
    def getSubscribers(self):
        return self.__subscribers
    
    def getVidQuant(self):
        return len(self.__videos)
    
class DeusTube:

    def __init__(self):
        self.__main = []
    
    def addChannel(self, channel):
        self.__main.append(channel)

    def showVids(self):
        for channel in self.__main:
            for video in channel.getVideos():
                print(video)

    def showMostLiked(self):
        channel_likes = []
        for channel in self.__main:
            total_likes = 0
            for video in channel.getVideos():
                total_likes += video.getLikes()
            channel_likes.append(total_likes)
        return max(channel_likes)


    def getTotalLenght(self):
        total_lenght = 0
        for channel in self.__main:
            for video in channel.getVideos():
                total_lenght += video.getLenght()
        return total_lenght


    def showUsrInfo(self):
        usr = input("Enter user: ")
        for channel in usr.getFollowed():
            print(channel.getUser())




    def menu(self):
        print("[1] Display All Video URLs")
        print("[2] Most liked channel")
        print("[3] Total Video Lenght on Deustube")
        print("[4] Show user Info")
        select = int(input())

        if select == 1:
            self.showVids()
        elif select == 2:
            print(self.showMostLiked())
        elif select == 3:
            print(self.getTotalLenght())
        elif select == 4:
            self.showUsrInfo()
