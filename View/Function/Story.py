from enum import Enum

class Story(): # 主要放故事簡介
    def __init__(self):
        self.db = {
            1: ["在這個充滿未知與危險的密室中，你必須在兩扇門之間做出選擇。這是一個充滿冒險和探索的故事，讓你感受到冒險和探索的樂趣，並且教會你如何在黑暗中找到光明，如何面對並解決未知的謎題。你將學到2進制和16進制的知識，並且將自己的視野和思想擴展到更廣闊的領域。走過神秘的門，開啟你的冒險之旅吧！", "故事1", "View/Resource/menu/story1.jpg"],
            2: ['在虛擬城市"Binaropolis"中，當一位強大黑客威脅到城市的和平，四位英雄Not, And, Or, Xor挺身而出。他們必須運用各自代表否定、交集、聯集和異或的能力，解開黑客的混淆碼，找出真相。你可以在這一段旅程中，學到Not, And, Or, Xor的邏輯，更深入的了解2進制在資訊領域的應用。\n                (建議先完成故事1後，再選擇此故事)', "故事2", "View/Resource/menu/story2.jpg"],
            3: ['在"Binaropolis"虛擬城市中，四位英雄要再次對抗黑客。他們必須熟悉NAND、NOR、XNOR和Buffer等邏輯運算，並了解訊息傳輸的問題，來解開黑客的傀儡碼。這場冒險不僅要求他們運用邏輯運算，也要克服傳輸錯誤、傳輸衰減和邏輯簡化的挑戰。透過這次的危機，他們的智慧和勇氣將驅使他們繼續保衛城市和平。    (建議先完成故事1, 2後，再選擇此故事)', "故事3", "View/Resource/menu/story3.jpg"]
        }

    def get_intro(self, index):
        return self.db.get(index)[0]

    def get(self, index):
        return self.db.get(index)[1]

    def get_image(self, index):
        return self.db.get(index)[2]

    def get_len(self):
        return len(self.db)
