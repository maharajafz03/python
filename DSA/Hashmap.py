

class Ashmap:

    def __init__(self):
        self.size = 10
        self.hashlist = [None]*self.size

    def getindex(self, key):
        return hash(key) % self.size
    
    def add(self, key, value):
        index = self.getindex(key)
        # print(index)

        if self.hashlist[index] is None:
            self.hashlist[index] = [[key, value]]
        else:
            sublist = self.hashlist[index]
            for pairs in sublist:
                if pairs[0] == key:
                   pairs[1] = value
                   return pairs[1]
                
            self.hashlist[index].append([key, value])
            
    
    def get(self, key):
        index = self.getindex(key)

        if self.hashlist[index] is None:
        #     ---------- its mean by none index is none                        
            sublist = self.hashlist[index]
            # print(sublist)
            for pairs in sublist:
                if pairs[0] == key:
                   return pairs[1]
                
        else:
            return "key not found"
    
    def __delitem__(self, key):
        index = self.getindex(key)

        if self.hashlist[index] is None:
        #     ---------- its mean by none index is none                        
            sublist = self.hashlist[index] 
            # print(sublist)
            for i,pairs in enumerate (sublist):
                if pairs[0] == key:
                   del sublist[i]
                   return
        else:
            return "key not found"

object = Ashmap()
object.add ("name", "maga")
object.add ("age", "24")
print (object.get("name"))
print (object.get("age"))


