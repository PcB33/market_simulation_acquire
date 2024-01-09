# -*- coding: utf-8 -*-
    
    
import numpy as np
import random as random 
import time  
import matplotlib.pyplot as plt
    
def game():  
    #1: cheap
    #2: medium
    #3: expensive
    class Hotel:
    
        def __init__(self,g,value,name1):
            self.size = 0
            self.stock = 25
            self.group = g
            self.value = value
            self.name = name1
            
        def adsize(self,n):
            self.size += n
            
        def sellstock(self,n):
            self.stock -= n
            
        def recstock(self,n):
            self.stock += n
        
        def info(self):
            return self.size, self.stock, self.group
        
        def reference(self):
            if self.group == 1:
                if self.size ==2:
                    return chart(2)
                elif self.size ==3:
                    return chart(3)
                elif self.size ==4:
                    return chart(4)
                elif self.size ==5:
                    return chart(5)
                elif self.size >= 6 and self.size <= 10:
                    return chart(6)
                elif self.size >= 11 and self.size <= 20:
                    return chart(7)
                elif self.size >= 21 and self.size <= 30:
                    return chart(8)
                elif self.size >= 31 and self.size <= 40:
                    return chart(9)
                elif self.size >= 41:
                    return chart(10)
                
            elif self.group == 2:
                if self.size ==2:
                    return chart(3)
                elif self.size ==3:
                    return chart(3)
                elif self.size ==4:
                    return chart(5)
                elif self.size ==5:
                    return chart(6)
                elif self.size >= 6 and self.size <= 10:
                    return chart(7)
                elif self.size >= 11 and self.size <= 20:
                    return chart(8)
                elif self.size >= 21 and self.size <= 30:
                    return chart(9)
                elif self.size >= 31 and self.size <= 40:
                    return chart(10)
                elif self.size >= 41:
                    return chart(11)
                
            elif self.group == 3:
                if self.size ==2:
                    return chart(4)
                elif self.size ==3:
                    return chart(5)
                elif self.size ==4:
                    return chart(6)
                elif self.size ==5:
                    return chart(7)
                elif self.size >= 6 and self.size <= 10:
                    return chart(8)
                elif self.size >= 11 and self.size <= 20:
                    return chart(9)
                elif self.size >= 21 and self.size <= 30:
                    return chart(10)
                elif self.size >= 31 and self.size <= 40:
                    return chart(11)
                elif self.size >= 41:
                    return chart(12)
    
    class Player_dumb:
   
        def __init__(self,g,name1):
            self.money = g
            self.stock_tower=0
            self.stock_continental = 0
            self.stock_american = 0
            self.stock_imperial = 0
            self.stock_festival = 0
            self.stock_sackson = 0 
            self.stock_worldwide = 0
            self.tiles = []
            self.name = name1
            self.wins = 0
        
        def drawtile(self,alltiles):
            a = random.randint(0,len(alltiles)-1)
            tile = alltiles.pop(a)
            #print(tile)
            self.tiles.append(tile)
            #self.add(tile)
            return
        
        #def placetile...remove tile and call global placetile()
        def placetile_player(self, x0):
            for i in range(6):
                #print(i)
                #print("length:",len(self.tiles))
                tile = self.tiles[i]
                if tile[0] == x0[0] and tile[1]==x0[1]:
                    self.tiles.pop(i)
                    break
            placetile(x0,self)
            #print(x0,"has been placed on the board")
            return
        
        #TODO
        def decide_placetile(self):
            eligible_tiles = []
            for i in range(6):
                if is_legal(self.tiles[i])==True:
                    eligible_tiles.append(self.tiles[i])
                  
            tries=0
            while len(eligible_tiles)==0:
                for i in range(6):
                    #print("# tiles:", len(self.tiles))
                    a = self.tiles.pop(5-i)
                    alltiles.append(a)
                    
                for i in range(6):
                    self.drawtile(alltiles)
                    
                for i in range(6):
                    if is_legal(self.tiles[i])==True:
                        eligible_tiles.append(self.tiles[i])  
                tries+=1
                if tries>=10:
                    return True
                
            for i in range(len(eligible_tiles)):
                info = tile_info(eligible_tiles[i])
                summ = sum(info[j] for j in range(4))
                if summ != 0:
                    self.placetile_player(eligible_tiles[i])
                    return False
            self.placetile_player(eligible_tiles[0]) #dumb
            return False
            
        #TODO    
        def decide_merge_stock(self,big,small):
            n = self.info_stock(small.value)
            self.sellstock(small.value,n)
            
            
        #TODO
        def buy_stock(self):
            exist_hotels = is_hotel()
                
            if self.money >=3000:
                n = 3
            elif self.money >=1500:
                n = 2
            else:
                n=1
                #print(len(exist_hotels))
                #print(n)
            if len(exist_hotels) != 0:     
                d = random.randint(0,len(exist_hotels)-1)
                    #print(d)
                buy_hotel = exist_hotels[d]
                price,useless, useless2 = buy_hotel.reference()
                if self.money - n*price > 500 and buy_hotel.stock >= n:
                    self.getstock(buy_hotel.value,n)
                    #print(self.name,"has purchased",n,"stocks from",buy_hotel.name)
            
                
        def set_money(self,cash):
            self.money += cash
            
            
        def info(self):
            return self.money, self.stock_tower, self.stock_continental, self.stock_american, self.stock_imperial, self.stock_festival, self.stock_sackson ,self.stock_worldwide
            
        def info_stock(self,value):
            if value == tower.value:
                return self.stock_tower
            elif value == continental.value:
                return self.stock_continental
            elif value == american.value:
                return self.stock_american
            elif value == imperial.value:
                return self.stock_imperial
            elif value == festival.value:
                return self.stock_festival
            elif value == sackson.value:
                return self.stock_sackson
            elif value == worldwide.value:
                return self.stock_worldwide
            
        def sellstock(self,value,n):
            price,useless, useless2 = eval_hotel(value).reference()
            self.set_money(n*price)
            if value == tower.value:
                self.stock_tower -= n
                tower.recstock(n)
            elif value == continental.value:
                self.stock_continental -= n
                continental.recstock(n)
            elif value == american.value:
                self.stock_american -= n
                american.recstock(n)
            elif value == imperial.value:
                self.stock_imperial -= n
                imperial.recstock(n)
            elif value == festival.value:
                self.stock_festival -= n
                festival.recstock(n)
            elif value == sackson.value:
                self.stock_sackson -= n
                sackson.recstock(n)
            elif value == worldwide.value:
                self.stock_worldwide -= n
                worldwide.recstock(n)
        
        def getstock(self,value,n,free=False):
            price,useless, useless2 = eval_hotel(value).reference()
            if free==False:
                self.set_money(-n*price)
            if value == tower.value:
               self.stock_tower += n
               tower.sellstock(n)
            elif value == continental.value:
               self.stock_continental += n
               continental.sellstock(n)
            elif value == american.value:
               self.stock_american += n
               american.sellstock(n)
            elif value == imperial.value:
               self.stock_imperial += n
               imperial.sellstock(n)
            elif value == festival.value:
               self.stock_festival += n
               festival.sellstock(n)
            elif value == sackson.value:
               self.stock_sackson += n
               sackson.sellstock(n)
            elif value == worldwide.value:
               self.stock_worldwide += n
               worldwide.sellstock(n)
         
        #decide...stupid 
        def decide_merge(self,hotel1,hotel2):
            return hotel1,hotel2
        
        def decide_triple_merge(self,hotel1,hotel2,hotel3):
            return hotel1,hotel2,hotel3
        
        def decide_double_merge(self,hotel1,hotel2):
            return hotel1,hotel2
        
        def decide_quad_merge(self,hotel1,hotel2,hotel3,hotel4):
            return hotel1,hotel2,hotel3,hotel4
        
        def decide_newhotel(self):
            for i in range(2,9):
                if eval_hotel(i).size==0:
                    return eval_hotel(i)
    
    class Player_normal:
   
        def __init__(self,g,name1):
            self.money = g
            self.stock_tower=0
            self.stock_continental = 0
            self.stock_american = 0
            self.stock_imperial = 0
            self.stock_festival = 0
            self.stock_sackson = 0 
            self.stock_worldwide = 0
            self.tiles = []
            self.name = name1
            #defense matrix
            self.A1=np.array([[0,0,0,0,0,0,0,4],
                              [0,0,0,0,0,0,50,6],
                              [0,0,0,0,0,50,50,8],
                              [0,0,0,0,50,50,100,10],
                              [0,0,0,50,50,100,100,12],
                              [0,0,50,50,100,100,22,14],
                              [0,50,50,100,100,24,24,16],
                              [0,50,100,100,24,24,15,18]]) #50->buy 1 stock, 100->buy two stocks
        
            #inthehunt matrix
            #row corresponds to deficit-1,coloumn to number of stock available from hotel
            self.A2=np.array([[0,20,100,100,100,20,12,16],
                              [0,0,20,24,24,12,8,13],
                              [0,0,0,20,12,10,8,10]])
        
            #brown coefficients
            self.A3=np.array([0.5,0.5,2,1])
            
            #alpha coefficients
            self.A4=np.array([0.1,0.02])
            
            #hold onto stock matrix
            #first coloumn:turn, second coulumn:stocks of other players, 
            #thrid coloumn:own stock, 4th coloumn:b
            #Attention: the fourth coloumn must be <= the third coloumn
            self.A5=np.array([[30,0,2,2],
                              [30,2,4,4],
                              [50,0,2,2],
                              [50,2,4,4]])
        
            #graph to determine how much money is spent    
            self.A6=np.array([-1/600,35/3])
            
            #matrix which awards points for tile placement; 0:maj in small, 1-4:min small and cash problems
            #5:maj big and enough in small to defend lead, 6: would become maj in big, 
            #7:hotel would be created,8:enlarge majority,9:enlarge minority
            self.A7=np.array([20,2000,10,3000,8,12,15,13,4,2])
            
            #coefficient that determines whether the player spreads his buys
            self.A8=3
            
            #money below which to sell stock, ratio when to go for 2:1 trade
            self.A9=np.array([3000,2.5])
            
            #initial advantage matrix
            self.A10=np.array([10,9,8,5])
        
        def drawtile(self,alltiles):
            a = random.randint(0,len(alltiles)-1)
            tile = alltiles.pop(a)
            #print(tile)
            self.tiles.append(tile)
            #self.add(tile)
            return
        
        #def placetile...remove tile and call global placetile()
        def placetile_player(self, x0):
            for i in range(6):
                #print(i)
                #print("length:",len(self.tiles))
                tile = self.tiles[i]
                if tile[0] == x0[0] and tile[1]==x0[1]:
                    self.tiles.pop(i)
                    break
            #print(x0,"has been placed on the board")
            placetile(x0,self)
            return
        
        
        def decide_placetile(self):
            eligible_tiles = []
            for i in range(6):
                if is_legal(self.tiles[i])==True:
                    eligible_tiles.append(self.tiles[i])
            
            tries=0
            while len(eligible_tiles)==0:
                for i in range(6):
                    #print("# tiles:", len(self.tiles))
                    a = self.tiles.pop(5-i)
                    alltiles.append(a)
                    
                for i in range(6):
                    self.drawtile(alltiles)
                    
                for i in range(6):
                    if is_legal(self.tiles[i])==True:
                        eligible_tiles.append(self.tiles[i])  
                tries+=1
                if tries>=10:
                    return True
            points=[]
            for i in range(len(eligible_tiles)):
                p=0
                tile=eligible_tiles[i]
                info=tile_info(tile)
                infosort=np.sort(tile_info(tile))
                n = 0 #number of non-empty tiles
                for k in range(len(info)):
                    if info[k] !=0:
                        n += 1
                n1=0 #number of single tiles
                for k in range(len(info)):
                    if info[k] ==1:
                        n1 += 1
                #number of hotels surrounding tile
                m = 0
                m1 = []
                for k in range(4):
                    if info[k] > 1:
                        b = True
                        for j in range(len(m1)):
                            if info[k]==m1[j]:
                                b = False
                        m1.append(info[k]) 
                        if b ==True:
                            m+=1
                if m==2:
                    hotel1=eval_hotel(infosort[3])
                    if infosort[3]!=infosort[2]:
                        hotel2=eval_hotel(infosort[2])
                    elif infosort[3]!=infosort[1]:
                        hotel2=eval_hotel(infosort[1])
                    else:
                        hotel2=eval_hotel(infosort[0])
                    if hotel1.size>=hotel2.size:
                        big=hotel1
                        small=hotel2
                    else:
                        big=hotel2
                        small=hotel1
                    maj,minn=majmin(small)
                    majb,minnb=majmin(big)
                    c=0
                    #majority small
                    for j in range(len(maj)):
                        if maj[j].name==self.name:
                            p+=self.A7[0]
                            c=10
                    #minority small and in need of money
                    for j in range(len(minn)):
                        if minn[j].name==self.name and self.money<self.A7[1]:
                            p+=self.A7[2]
                            c=10
                        elif minn[j].name==self.name and self.money<self.A7[3]:
                            p+=self.A7[4]
                            c=10
                    #majority in big and enough stock in small to defend lead
                    for j in range(len(majb)):
                        if majb[j].name==self.name and self.difference_to_maj(big)>-self.difference_to_maj(small)/2:
                            p+=self.A7[5]
                            c=10
                    #if you can become majority of big
                    for j in range(len(minnb)):
                        if -self.difference_to_maj(big)<(self.info_stock(small.value)/2-majb[-1].info_stock(small.value)/2):
                            p+=self.A7[6]
                            c=10
                   
                            
                    
                    
                    p=p-10+c
                if m==3:
                    hotel1=eval_hotel(infosort[3])
                    if infosort[2]!=infosort[3]:
                        hotel2=eval_hotel(infosort[2])
                        if infosort[1]!=infosort[2]:
                            hotel3=eval_hotel(infosort[1])
                        else:
                            hotel3=eval_hotel(infosort[0])
                        
                    else:
                        hotel2=eval_hotel(infosort[1])
                        hotel3=eval_hotel(infosort[0])
                        
                    if hotel1.size>hotel2.size and hotel1.size>hotel3.size:
                        big=hotel1
                        small1=hotel2
                        small2=hotel3
                    elif hotel2.size>hotel1.size and hotel2.size>hotel3.size:
                        big=hotel2
                        small1=hotel1
                        small2=hotel3
                    elif hotel3.size>hotel1.size and hotel3.size>hotel2.size:
                        big=hotel3
                        small1=hotel1
                        small2=hotel2
                    else:
                        big=hotel1
                        small1=hotel2
                        small2=hotel3
                    
                    c=0
                    maj1,minn1=majmin(small1)
                    for j in range(len(maj1)):
                        if maj1[j].name==self.name:
                            p+=self.A7[0]
                            c=10
                    maj2,minn2=majmin(small2)
                    for j in range(len(maj2)):
                        if maj2[j].name==self.name:
                            p+=self.A7[0]
                            c=10
                    majb,minnb=majmin(big)
                    for j in range(len(majb)):
                        if majb[j].name==self.name and (self.difference_to_maj(big)>-self.difference_to_maj(small1)/2 or self.difference_to_maj(big)>-self.difference_to_maj(small2)/2):
                            p+=self.A7[5]
                            c=10
                    for j in range(len(minn1)):
                       if minn1[j].name==self.name and self.money<self.A7[1]:
                           p+=self.A7[2]
                           c=10
                       elif minn1[j].name==self.name and self.money<self.A7[3]:
                           p+=self.A7[4]
                           c=10
                    for j in range(len(minn2)):
                       if minn2[j].name==self.name and self.money<self.A7[1]:
                           p+=self.A7[2]
                           c=10
                       elif minn2[j].name==self.name and self.money<self.A7[3]:
                           p+=self.A7[4]
                           c=10
                    p=p-10+c
                    
                if m==0 and n>0:
                    c=0
                    for j in range(2,9):
                        if eval_hotel(j).size==0 and self.info_stock(j)>0:
                            p+=self.A7[7]
                            c=5
                            break
                    #This is not a mistake!!
                    p=p+5-c
                
                if m==1:
                    adjhotel=eval_hotel(infosort[3])
                    maj,minn=majmin(adjhotel)
                    c=0
                    for j in range(len(maj)):
                        if maj[j].name==self.name:
                            p+=self.A7[8]
                            c=2
                    for j in range(len(minn)):
                        if minn[j].name==self.name:
                            p+=self.A7[9]
                            c=2
                    p=p-2+c
                
                points.append(p)
            
            besttilenumber=0
            for i in range(len(eligible_tiles)-1):
                if points[i+1]>points[besttilenumber]:
                    besttilenumber = i+1
            besttile=eligible_tiles[besttilenumber]
            self.placetile_player(besttile)
            return False
            
      
        def decide_merge_stock(self,big,small):
            n=self.info_stock(small.value)
            m=big.stock
            b=0
            while(self.money<self.A9[0] and n>=1):
                self.sellstock(small.value,1)
                n-=1
            if self.difference_to_maj(big)>=-n/2 and m>=n/2:
                while(m>=1 and n>=2):
                    self.getstock(big.value,1,free=True)
                    self.sellstock(small.value,2,free=True)
                    m-=1
                    n-=2
                    #print(self.name,"has traded 2",small.name,"stocks for 1",big.name,"stock")
            bigprice, useless1,useless2=big.reference()
            smallprice, useless3,useless4=small.reference()
            if bigprice>=self.A9[1]*smallprice:
                while(m>=1 and n>=2):
                    self.getstock(big.value,1,free=True)
                    self.sellstock(small.value,2,free=True)
                    m-=1
                    n-=2
                    #print(self.name,"has traded 2",small.name,"stocks for 1",big.name,"stock")
            stocks=self.other_player_stocks(small)
            b=hold_stock(stocks,n,self.A5)
            self.sellstock(small.value,n-b)
            #print(self.name,"has held on to",b,"stocks and sold",n-b,"stocks")
            
            
        def other_player_stocks(self,hotel):
            stocks=[]
            if self.name !=player1:
                stocks.append(player1.info_stock(hotel.value))
            if self.name !=player2:
                stocks.append(player2.info_stock(hotel.value))
            if self.name !=player3:
                stocks.append(player3.info_stock(hotel.value))
            if self.name !=player4:
                stocks.append(player4.info_stock(hotel.value))
            stocks=np.sort(stocks)
                
            return stocks
        
        def difference_to_maj(self,hotel):
            stocks=self.other_player_stocks(hotel)
            return self.info_stock(hotel.value)-stocks[2]
                
            
        #TODO
        def buy_stock(self):
            
            m1,t1,c1,a1,i1,f1,s1,w1 = player1.info()
            m2,t2,c2,a2,i2,f2,s2,w2 = player2.info()
            m3,t3,c3,a3,i3,f3,s3,w3 = player3.info()
            m4,t4,c4,a4,i4,f4,s4,w4 = player4.info()
            
            w_stock=np.sort([w1,w2,w3,w4])
            s_stock=np.sort([s1,s2,s3,s4])
            f_stock=np.sort([f1,f2,f3,f4])
            i_stock=np.sort([i1,i2,i3,i4])
            a_stock=np.sort([a1,a2,a3,a4])
            c_stock=np.sort([c1,c2,c3,c4])
            t_stock=np.sort([t1,t2,t3,t4])
            
            #Points for each stock and if the player should particularly buy 1 or 2
            w,s,f,i,a,c,t=0,0,0,0,0,0,0
            w1s,w2s,s1s,s2s,f1s,f2s,i1s,i2s,a1s,a2s,c1s,c2s,t1s,t2s=False,False,False,False,False,False,False,False,False,False,False,False,False,False
            
            if worldwide.size>0:
                if w_stock[3]==self.stock_worldwide and w_stock[2]==0:
                    w,w1s,w2s=initial_advantage(w_stock,self.A10)
                elif self.stock_worldwide==w_stock[3]:
                    w,w1s,w2s=defence(w_stock,worldwide,self.A1)
                elif (w_stock[3]-self.stock_worldwide)<=3:
                    w,w1s,w2s=inthehunt(w_stock,self.stock_worldwide,worldwide,self.A2)
                else:
                    w,w1s,w2s=browns(w_stock,self.stock_worldwide,worldwide,self.A1,self.A2,self.A3)
                
                w_alpha=alpha(worldwide,self.tiles,self.A4)
                w*=w_alpha
                
            if sackson.size>0:
                if s_stock[3]==self.stock_sackson and s_stock[2]==0:
                    s,s1s,s2s=initial_advantage(s_stock,self.A10)
                elif self.stock_sackson==s_stock[3]:
                    s,s1s,s2s=defence(s_stock,sackson,self.A1)
                elif (s_stock[3]-self.stock_sackson)<=3:
                    s,s1s,s2s=inthehunt(s_stock,self.stock_sackson,sackson,self.A2)
                else:
                    s,s1s,s2s=browns(s_stock,self.stock_sackson,sackson,self.A1,self.A2,self.A3)
            
            s_alpha=alpha(sackson,self.tiles,self.A4)
            s*=s_alpha
            
            if festival.size>0:
                if f_stock[3]==self.stock_festival and f_stock[2]==0:
                    f,f1s,f2s=initial_advantage(f_stock,self.A10)
                elif self.stock_festival==f_stock[3]:
                    f,f1s,f2s=defence(f_stock,festival,self.A1)
                elif (f_stock[3]-self.stock_festival)<=3:
                    f,f1s,f2s=inthehunt(f_stock,self.stock_festival,festival,self.A2)
                else:
                    f,f1s,f2s=browns(f_stock,self.stock_festival,festival,self.A1,self.A2,self.A3)
                
                f_alpha=alpha(festival,self.tiles,self.A4)
                f*=f_alpha
            
            if imperial.size>0:
                if i_stock[3]==self.stock_imperial and i_stock[2]==0:
                    i,i1s,i2s=initial_advantage(i_stock,self.A10)
                elif self.stock_imperial==i_stock[3]:
                    i,i1s,i2s=defence(i_stock,imperial,self.A1)
                elif (i_stock[3]-self.stock_imperial)<=3:
                    i,i1s,i2s=inthehunt(i_stock,self.stock_imperial,imperial,self.A2)
                else:
                    i,i1s,i2s=browns(i_stock,self.stock_imperial,imperial,self.A1,self.A2,self.A3)
                
                i_alpha=alpha(imperial,self.tiles,self.A4)
                i*=i_alpha
                
            if american.size>0:
                if a_stock[3]==self.stock_american and a_stock[2]==0:
                    a,a1s,a2s=initial_advantage(a_stock,self.A10)
                elif self.stock_american==a_stock[3]:
                    a,a1s,a2s=defence(a_stock,american,self.A1)
                elif (a_stock[3]-self.stock_american)<=3:
                    a,a1s,a2s=inthehunt(a_stock,self.stock_american,american,self.A2)
                else:
                    a,a1s,a2s=browns(a_stock,self.stock_american,american,self.A1,self.A2,self.A3)
                
                a_alpha=alpha(american,self.tiles,self.A4)
                a*=a_alpha
            
            if continental.size>0:
                if c_stock[3]==self.stock_continental and c_stock[2]==0:
                    c,c1s,c2s=initial_advantage(c_stock,self.A10)
                elif self.stock_continental==c_stock[3]:
                    c,c1s,c2s=defence(c_stock,continental,self.A1)
                elif (c_stock[3]-self.stock_continental)<=3:
                    c,c1s,c2s=inthehunt(c_stock,self.stock_continental,continental,self.A2)
                else:
                    c,c1s,c2s=browns(c_stock,self.stock_continental,continental,self.A1,self.A2,self.A3)
                
                c_alpha=alpha(continental,self.tiles,self.A4)
                c*=c_alpha
            
            if tower.size>0:
                if t_stock[3]==self.stock_tower and t_stock[2]==0:
                    t,t1s,t2s=initial_advantage(t_stock,self.A10)
                elif self.stock_tower==t_stock[3]:
                    t,t1s,t2s=defence(t_stock,tower,self.A1)
                elif (t_stock[3]-self.stock_tower)<=3:
                    t,t1s,t2s=inthehunt(t_stock,self.stock_tower,tower,self.A2)
                else:
                    t,t1s,t2s=browns(t_stock,self.stock_tower,tower,self.A1,self.A2,self.A3)
                
                t_alpha=alpha(tower,self.tiles,self.A4)
                t*=t_alpha
            
            points=np.array([w,s,f,i,a,c,t])
            points2=[]
            for i in range(7):
                points2.append(points[i])
            points2=np.sort(points2)
            for i in range(7):
                #achtung bei gleichstand wird das hotel mit dem tieferen value gewählt
                if points[i]==points2[6]:
                    favhotel=eval_hotel(i+2)
            splitt=False        
            if points2[6]-points2[5]<=self.A8 and points2[5]!=0:
                splitt=True
                for i in range(7):
                    #achtung bei gleichstand wird das hotel mit dem tieferen value gewählt
                    if points[i]==points2[5]:
                        favhotel2=eval_hotel(i+2)
                        
                
            
            smallbuys=np.array([[w1s,s1s,f1s,i1s,a1s,c1s,t1s],
                                [w2s,s2s,f2s,i2s,a2s,c2s,t2s]])
            
            p=3
            list1s=[]
            list2s=[]
            for i in range(2,9):
                if smallbuys[0,i-2]==True:
                    list1s.append(eval_hotel(i))
                if smallbuys[1,i-2]==True:
                    list2s.append(eval_hotel(i))
                    
            a=len(list1s)
            b=len(list2s)
            if a+2*b<=3:
                for i in range(len(list1s)):
                    buy_hotel = list1s[i]
                    price,useless, useless2 = buy_hotel.reference()
                    if self.money>=price and buy_hotel.stock>=1:
                        self.getstock(buy_hotel.value,1)
                        p-=1
                        #print(self.name,"has purchased",1,"stock from",buy_hotel.name)
                for i in range(len(list2s)):
                    buy_hotel = list2s[i]
                    price,useless, useless2 = buy_hotel.reference()
                    if self.money>=price*2 and buy_hotel.stock>=2:
                        self.getstock(buy_hotel.value,2)
                        p-=2
                        #print(self.name,"has purchased",2,"stocks from",buy_hotel.name)
            elif a+2*b>3:
                list3=list1s+list2s
                list4=[]
                for i in range(len(list3)):
                    list4.append(points[list3[i].value-2])
                list4.sort()
                for k in range(3):
                    n1 = len(list4)
                    l = 0
                    for i in range(n1): 
                        if points[list3[l].value-2]==list4[-1]:
                            buy_hotel=list3[l]
                            price,useless, useless2 = buy_hotel.reference()
                            if smallbuys[0,buy_hotel.value-2]==True:
                                n=1
                            else:
                                n=2
                            if self.money>=price*n and p>=n and buy_hotel.stock>=n:
                                self.getstock(buy_hotel.value,n)
                                p-=n
                                #print(self.name,"has purchased",n,"stocks from",buy_hotel.name)
                                list3.pop(l)
                                l-=1
                                list4.pop(-1)
                        l+=1
        
            if points[favhotel.value-2]>=self.A6[0]*self.money+self.A6[1] and points[favhotel.value-2]!=0:
                if splitt==True:
                    price,useless, useless2 = favhotel.reference()
                    if self.money>=price*2 and p>=2 and favhotel.stock>=2:
                        self.getstock(favhotel.value,2)
                        p-=2
                        #print(self.name,"has purchased",2,"stocks from",favhotel.name)
                    price2,useless3, useless4 = favhotel.reference()
                    if self.money>=price2*1 and p>=1 and favhotel2.stock>=1:
                        self.getstock(favhotel2.value,1)
                        p-=1
                        #print(self.name,"has purchased",1,"stock from",favhotel2.name)
                elif splitt==False:
                    price,useless, useless2 = favhotel.reference()
                    if self.money>=price*p and favhotel.stock>=p:
                        self.getstock(favhotel.value,p)
                        #print(self.name,"has purchased",p,"stocks from",favhotel.name)
            
            
                
        def set_money(self,cash):
            self.money += cash
            
            
        def info(self):
            return self.money, self.stock_tower, self.stock_continental, self.stock_american, self.stock_imperial, self.stock_festival, self.stock_sackson ,self.stock_worldwide
            
        def info_stock(self,value):
            if value == tower.value:
                return self.stock_tower
            elif value == continental.value:
                return self.stock_continental
            elif value == american.value:
                return self.stock_american
            elif value == imperial.value:
                return self.stock_imperial
            elif value == festival.value:
                return self.stock_festival
            elif value == sackson.value:
                return self.stock_sackson
            elif value == worldwide.value:
                return self.stock_worldwide
            
        def sellstock(self,value,n,free=False):
            price,useless, useless2 = eval_hotel(value).reference()
            if free==False:
                self.set_money(n*price)
            if value == tower.value:
                self.stock_tower -= n
                tower.recstock(n)
            elif value == continental.value:
                self.stock_continental -= n
                continental.recstock(n)
            elif value == american.value:
                self.stock_american -= n
                american.recstock(n)
            elif value == imperial.value:
                self.stock_imperial -= n
                imperial.recstock(n)
            elif value == festival.value:
                self.stock_festival -= n
                festival.recstock(n)
            elif value == sackson.value:
                self.stock_sackson -= n
                sackson.recstock(n)
            elif value == worldwide.value:
                self.stock_worldwide -= n
                worldwide.recstock(n)
        
        def getstock(self,value,n,free=False):
            price,useless, useless2 = eval_hotel(value).reference()
            if free==False:
                self.set_money(-n*price)
            if value == tower.value:
               self.stock_tower += n
               tower.sellstock(n)
            elif value == continental.value:
               self.stock_continental += n
               continental.sellstock(n)
            elif value == american.value:
               self.stock_american += n
               american.sellstock(n)
            elif value == imperial.value:
               self.stock_imperial += n
               imperial.sellstock(n)
            elif value == festival.value:
               self.stock_festival += n
               festival.sellstock(n)
            elif value == sackson.value:
               self.stock_sackson += n
               sackson.sellstock(n)
            elif value == worldwide.value:
               self.stock_worldwide += n
               worldwide.sellstock(n)
         
        #decide...stupid 
        def decide_merge(self,hotel1,hotel2):
            m1,t1,c1,a1,i1,f1,s1,w1=self.info()
            hilfsarray=np.array([w1,s1,f1,i1,a1,c1,t1])
    
            maj1,minn1 = majmin(hotel1)
            maj2,minn2 = majmin(hotel2)
            M1=False
            m1=False
            M2=False
            m2=False
            for i in range(len(maj1)):
                if maj1[i].name==self.name:
                    M1=True
            for i in range(len(minn1)):
                if minn1[i].name==self.name:
                    m1=True
            for i in range(len(maj2)):
                if maj2[i].name==self.name:
                    M2=True
            for i in range(len(minn2)):
                if minn2[i].name==self.name:
                    m2=True
            
            if M1==True and M2==False:
                if np.abs(hilfsarray[hotel1.value-2]-hotel1.stock)<=5 and hilfsarray[hotel1.value-2]>=5 and self.money>=3000:
                    return hotel1,hotel2
                else: 
                    return hotel2,hotel1
            elif M2==True and M1==False:
                if np.abs(hilfsarray[hotel2.value-2]-hotel2.stock)<=5 and hilfsarray[hotel2.value-2]>=5 and self.money>=3000:
                    return hotel2,hotel1
                else: 
                    return hotel1,hotel2
                
            elif M1==True and M2 == True:
                if self.difference_to_maj(hotel1)>=self.difference_to_maj(hotel2):
                    return hotel1,hotel2
                else:
                    return hotel2,hotel1
                
            elif m1==True and m2==False:
                if np.abs(hilfsarray[hotel1.value-2]-hotel1.stock)<=5 and hilfsarray[hotel1.value-2]>=5 and self.money>=3000:
                    return hotel1,hotel2
                else: 
                    return hotel2,hotel1
            elif m2==True and m1==False:
                if np.abs(hilfsarray[hotel2.value-2]-hotel2.stock)<=5 and hilfsarray[hotel2.value-2]>=5 and self.money>=3000:
                    return hotel2,hotel1
                else: 
                    return hotel1,hotel2
           
            elif m1==True and m2 == True:
                if self.difference_to_maj(hotel1)<=self.info_stock(hotel1.value)/2:
                    return hotel1,hotel2
                elif self.difference_to_maj(hotel2)<=self.info_stock(hotel1.value)/2:
                    return hotel2,hotel1
                elif self.money>=3000 and hilfsarray[hotel1.value-2]>=hilfsarray[hotel2.value-2]:
                    return hotel1,hotel2
                elif self.money>=3000 and hilfsarray[hotel1.value-2]<hilfsarray[hotel2.value-2]:
                    return hotel2,hotel1
                elif self.money<3000 and hilfsarray[hotel1.value-2]>=hilfsarray[hotel2.value-2]:
                    return hotel2,hotel1
                elif self.money>=3000 and hilfsarray[hotel1.value-2]<hilfsarray[hotel2.value-2]:
                    return hotel1,hotel2
            else:
                if hilfsarray[hotel1.value-2]>=hilfsarray[hotel2.value-2]:
                    return hotel1,hotel2
                else:
                    return hotel2,hotel1
            
        
        def decide_triple_merge(self,hotel1,hotel2,hotel3):
            big,small=self.decide_merge(hotel1,hotel2)
            a,b = self.decide_merge(big,hotel3)
            return a,b,small
        
        def decide_double_merge(self,hotel1,hotel2):
            return self.decide_merge(hotel1,hotel2)
        
        def decide_quad_merge(self,hotel1,hotel2,hotel3,hotel4):
            big,small1,small2=self.decide_triple_merge(hotel1,hotel2,hotel3)
            a,b = self.decide_merge(big,hotel4)
            return a,b,small1,small2
        
        def decide_newhotel(self):
            m1,t1,c1,a1,i1,f1,s1,w1 = self.info()
            stocks=np.array([w1,s1,f1,i1,a1,c1,t1])
            hlist=[]
            hlist2=[]
            for i in range(2,9):
                if eval_hotel(i).size==0:
                    hlist.append(eval_hotel(i))
                    hlist2.append(eval_hotel(i))
            prefhotel=hlist[0]
            for i in range(len(hlist)):
                if stocks[hlist[i].value-2]>stocks[prefhotel.value-2]:
                    prefhotel=hlist[i]
            if stocks[prefhotel.value-2]>0:
                return prefhotel
            for k in range(7):
                for i in range(len(hlist2)):
                    if hlist2[i].stock<25:
                        hlist2.pop(len(hlist2)-1-i)
                        break
            if len(hlist2)>0:
                r = random.randint(0,len(hlist2)-1)
                return hlist2[r]
            else:
                r = random.randint(0,len(hlist)-1)
                return hlist[r]
    
    class Player_offensive:
   
        def __init__(self,g,name1):
            self.money = g
            self.stock_tower=0
            self.stock_continental = 0
            self.stock_american = 0
            self.stock_imperial = 0
            self.stock_festival = 0
            self.stock_sackson = 0 
            self.stock_worldwide = 0
            self.tiles = []
            self.name = name1
            #defense matrix
            #row corresponds to lead, coloumn to number of stocks available from that hotel
            self.A1=np.array([[0,0,0,0,0,0,0,1],
                              [0,0,0,0,0,0,0,1.5],
                              [0,0,0,0,0,0,0,2],
                              [0,0,0,0,0,0,0,2.2],
                              [0,0,0,50,0,0,0,3],
                              [0,0,50,50,0,0,5,0],
                              [0,50,50,100,0,12,12,1],
                              [0,50,100,100,12,12,4,4.5]]) #50->buy 1 stock, 100->buy two stocks
            
                #inthehunt matrix
                #row corresponds to deficit-1,coloumn to number of stock available from hotel
            self.A2=np.array([[0,20,100,100,100,22,18,20],
                              [0,0,20,24,24,18,12,15],
                              [0,0,0,20,18,15,10,12]])
        
            #brown coefficients
            self.A3=np.array([0.7,0.7,6,3])
            
            #alpha coefficients
            self.A4=np.array([0.1,0.02])
            
            #hold onto stock matrix
            #first coloumn:turn, second coulumn:stocks of other players, 
            #thrid coloumn:own stock, 4th coloumn:b
            #Attention: the fourth coloumn must be <= the third coloumn
            self.A5=np.array([[30,0,5,5],
                              [30,2,8,8],
                              [50,0,5,5],
                              [50,2,8,8]])
        
            #graph to determine how much money is spent    
            self.A6=np.array([-1/200,17/3])
            
            #matrix which awards points for tile placement; 0:maj in small, 1-4:min small and cash problems
            #5:maj big and enough in small to defend lead, 6: would become maj in big, 
            #7:hotel would be created,8:enlarge majority,9:enlarge minority
            self.A7=np.array([15,1000,6,1500,3,12,22,16,4,2])
            
            #coefficient that determines whether the player spreads his buys
            self.A8=8
            
            #money below which to sell stock, ratio when to go for 2:1 trade
            self.A9=np.array([1500,3])
            
            #initial advantage matrix
            self.A10=np.array([8,3,2,1])
        
        def drawtile(self,alltiles):
            a = random.randint(0,len(alltiles)-1)
            tile = alltiles.pop(a)
            #print(tile)
            self.tiles.append(tile)
            #self.add(tile)
            return
        
        #def placetile...remove tile and call global placetile()
        def placetile_player(self, x0):
            for i in range(6):
                #print(i)
                #print("length:",len(self.tiles))
                tile = self.tiles[i]
                if tile[0] == x0[0] and tile[1]==x0[1]:
                    self.tiles.pop(i)
                    break
            #print(x0,"has been placed on the board")
            placetile(x0,self)
            return
        
        
        def decide_placetile(self):
            eligible_tiles = []
            for i in range(6):
                if is_legal(self.tiles[i])==True:
                    eligible_tiles.append(self.tiles[i])
            
            tries=0
            while len(eligible_tiles)==0:
                for i in range(6):
                    #print("# tiles:", len(self.tiles))
                    a = self.tiles.pop(5-i)
                    alltiles.append(a)
                    
                for i in range(6):
                    self.drawtile(alltiles)
                    
                for i in range(6):
                    if is_legal(self.tiles[i])==True:
                        eligible_tiles.append(self.tiles[i])  
                tries+=1
                if tries>=10:
                    return True
            points=[]
            for i in range(len(eligible_tiles)):
                p=0
                tile=eligible_tiles[i]
                info=tile_info(tile)
                infosort=np.sort(tile_info(tile))
                n = 0 #number of non-empty tiles
                for k in range(len(info)):
                    if info[k] !=0:
                        n += 1
                n1=0 #number of single tiles
                for k in range(len(info)):
                    if info[k] ==1:
                        n1 += 1
                #number of hotels surrounding tile
                m = 0
                m1 = []
                for k in range(4):
                    if info[k] > 1:
                        b = True
                        for j in range(len(m1)):
                            if info[k]==m1[j]:
                                b = False
                        m1.append(info[k]) 
                        if b ==True:
                            m+=1
                if m==2:
                    hotel1=eval_hotel(infosort[3])
                    if infosort[3]!=infosort[2]:
                        hotel2=eval_hotel(infosort[2])
                    elif infosort[3]!=infosort[1]:
                        hotel2=eval_hotel(infosort[1])
                    else:
                        hotel2=eval_hotel(infosort[0])
                    if hotel1.size>=hotel2.size:
                        big=hotel1
                        small=hotel2
                    else:
                        big=hotel2
                        small=hotel1
                    maj,minn=majmin(small)
                    majb,minnb=majmin(big)
                    c=0
                    #majority small
                    for j in range(len(maj)):
                        if maj[j].name==self.name:
                            p+=self.A7[0]
                            c=10
                    #minority small and in need of money
                    for j in range(len(minn)):
                        if minn[j].name==self.name and self.money<self.A7[1]:
                            p+=self.A7[2]
                            c=10
                        elif minn[j].name==self.name and self.money<self.A7[3]:
                            p+=self.A7[4]
                            c=10
                    #majority in big and enough stock in small to defend lead
                    for j in range(len(majb)):
                        if majb[j].name==self.name and self.difference_to_maj(big)>-self.difference_to_maj(small)/2:
                            p+=self.A7[5]
                            c=10
                    #if you can become majority of big
                    for j in range(len(minnb)):
                        if -self.difference_to_maj(big)<(self.info_stock(small.value)/2-majb[-1].info_stock(small.value)/2):
                            p+=self.A7[6]
                            c=10
                   
                            
                    
                    
                    p=p-10+c
                if m==3:
                    hotel1=eval_hotel(infosort[3])
                    if infosort[2]!=infosort[3]:
                        hotel2=eval_hotel(infosort[2])
                        if infosort[1]!=infosort[2]:
                            hotel3=eval_hotel(infosort[1])
                        else:
                            hotel3=eval_hotel(infosort[0])
                        
                    else:
                        hotel2=eval_hotel(infosort[1])
                        hotel3=eval_hotel(infosort[0])
                        
                    if hotel1.size>hotel2.size and hotel1.size>hotel3.size:
                        big=hotel1
                        small1=hotel2
                        small2=hotel3
                    elif hotel2.size>hotel1.size and hotel2.size>hotel3.size:
                        big=hotel2
                        small1=hotel1
                        small2=hotel3
                    elif hotel3.size>hotel1.size and hotel3.size>hotel2.size:
                        big=hotel3
                        small1=hotel1
                        small2=hotel2
                    else:
                        big=hotel1
                        small1=hotel2
                        small2=hotel3
                    
                    c=0
                    maj1,minn1=majmin(small1)
                    for j in range(len(maj1)):
                        if maj1[j].name==self.name:
                            p+=self.A7[0]
                            c=10
                    maj2,minn2=majmin(small2)
                    for j in range(len(maj2)):
                        if maj2[j].name==self.name:
                            p+=self.A7[0]
                            c=10
                    majb,minnb=majmin(big)
                    for j in range(len(majb)):
                        if majb[j].name==self.name and (self.difference_to_maj(big)>-self.difference_to_maj(small1)/2 or self.difference_to_maj(big)>-self.difference_to_maj(small2)/2):
                            p+=self.A7[5]
                            c=10
                    for j in range(len(minn1)):
                       if minn1[j].name==self.name and self.money<self.A7[1]:
                           p+=self.A7[2]
                           c=10
                       elif minn1[j].name==self.name and self.money<self.A7[3]:
                           p+=self.A7[4]
                           c=10
                    for j in range(len(minn2)):
                       if minn2[j].name==self.name and self.money<self.A7[1]:
                           p+=self.A7[2]
                           c=10
                       elif minn2[j].name==self.name and self.money<self.A7[3]:
                           p+=self.A7[4]
                           c=10
                    p=p-10+c
                    
                if m==0 and n>0:
                    c=0
                    for j in range(2,9):
                        if eval_hotel(j).size==0 and self.info_stock(j)>0:
                            p+=self.A7[7]
                            c=5
                            break
                    #This is not a mistake!!
                    p=p+5-c
                
                if m==1:
                    adjhotel=eval_hotel(infosort[3])
                    maj,minn=majmin(adjhotel)
                    c=0
                    for j in range(len(maj)):
                        if maj[j].name==self.name:
                            p+=self.A7[8]
                            c=2
                    for j in range(len(minn)):
                        if minn[j].name==self.name:
                            p+=self.A7[9]
                            c=2
                    p=p-2+c
                
                points.append(p)
            
            besttilenumber=0
            for i in range(len(eligible_tiles)-1):
                if points[i+1]>points[besttilenumber]:
                    besttilenumber = i+1
            besttile=eligible_tiles[besttilenumber]
            self.placetile_player(besttile)
            return False
            
      
        def decide_merge_stock(self,big,small):
            n=self.info_stock(small.value)
            m=big.stock
            b=0
            while(self.money<self.A9[0] and n>=1):
                self.sellstock(small.value,1)
                n-=1
            if self.difference_to_maj(big)>=-n/2 and m>=n/2:
                while(m>=1 and n>=2):
                    self.getstock(big.value,1,free=True)
                    self.sellstock(small.value,2,free=True)
                    m-=1
                    n-=2
                    #print(self.name,"has traded 2",small.name,"stocks for 1",big.name,"stock")
            bigprice, useless1,useless2=big.reference()
            smallprice, useless3,useless4=small.reference()
            if bigprice>=self.A9[1]*smallprice:
                while(m>=1 and n>=2):
                    self.getstock(big.value,1,free=True)
                    self.sellstock(small.value,2,free=True)
                    m-=1
                    n-=2
                    #print(self.name,"has traded 2",small.name,"stocks for 1",big.name,"stock")
            stocks=self.other_player_stocks(small)
            b=hold_stock(stocks,n,self.A5)
            self.sellstock(small.value,n-b)
            #print(self.name,"has held on to",b,"stocks and sold",n-b,"stocks")
            
            
        def other_player_stocks(self,hotel):
            stocks=[]
            if self.name !=player1:
                stocks.append(player1.info_stock(hotel.value))
            if self.name !=player2:
                stocks.append(player2.info_stock(hotel.value))
            if self.name !=player3:
                stocks.append(player3.info_stock(hotel.value))
            if self.name !=player4:
                stocks.append(player4.info_stock(hotel.value))
            stocks=np.sort(stocks)
                
            return stocks
        
        def difference_to_maj(self,hotel):
            stocks=self.other_player_stocks(hotel)
            return self.info_stock(hotel.value)-stocks[2]
                
            
        #TODO
        def buy_stock(self):
            
            m1,t1,c1,a1,i1,f1,s1,w1 = player1.info()
            m2,t2,c2,a2,i2,f2,s2,w2 = player2.info()
            m3,t3,c3,a3,i3,f3,s3,w3 = player3.info()
            m4,t4,c4,a4,i4,f4,s4,w4 = player4.info()
            
            w_stock=np.sort([w1,w2,w3,w4])
            s_stock=np.sort([s1,s2,s3,s4])
            f_stock=np.sort([f1,f2,f3,f4])
            i_stock=np.sort([i1,i2,i3,i4])
            a_stock=np.sort([a1,a2,a3,a4])
            c_stock=np.sort([c1,c2,c3,c4])
            t_stock=np.sort([t1,t2,t3,t4])
            
            #Points for each stock and if the player should particularly buy 1 or 2
            w,s,f,i,a,c,t=0,0,0,0,0,0,0
            w1s,w2s,s1s,s2s,f1s,f2s,i1s,i2s,a1s,a2s,c1s,c2s,t1s,t2s=False,False,False,False,False,False,False,False,False,False,False,False,False,False
            
            if worldwide.size>0:
                if w_stock[3]==self.stock_worldwide and w_stock[2]==0:
                    w,w1s,w2s=initial_advantage(w_stock,self.A10)
                elif self.stock_worldwide==w_stock[3]:
                    w,w1s,w2s=defence(w_stock,worldwide,self.A1)
                elif (w_stock[3]-self.stock_worldwide)<=3:
                    w,w1s,w2s=inthehunt(w_stock,self.stock_worldwide,worldwide,self.A2)
                else:
                    w,w1s,w2s=browns(w_stock,self.stock_worldwide,worldwide,self.A1,self.A2,self.A3)
                
                w_alpha=alpha(worldwide,self.tiles,self.A4)
                w*=w_alpha
                
            if sackson.size>0:
                if s_stock[3]==self.stock_sackson and s_stock[2]==0:
                    s,s1s,s2s=initial_advantage(s_stock,self.A10)
                elif self.stock_sackson==s_stock[3]:
                    s,s1s,s2s=defence(s_stock,sackson,self.A1)
                elif (s_stock[3]-self.stock_sackson)<=3:
                    s,s1s,s2s=inthehunt(s_stock,self.stock_sackson,sackson,self.A2)
                else:
                    s,s1s,s2s=browns(s_stock,self.stock_sackson,sackson,self.A1,self.A2,self.A3)
            
            s_alpha=alpha(sackson,self.tiles,self.A4)
            s*=s_alpha
            
            if festival.size>0:
                if f_stock[3]==self.stock_festival and f_stock[2]==0:
                    f,f1s,f2s=initial_advantage(f_stock,self.A10)
                elif self.stock_festival==f_stock[3]:
                    f,f1s,f2s=defence(f_stock,festival,self.A1)
                elif (f_stock[3]-self.stock_festival)<=3:
                    f,f1s,f2s=inthehunt(f_stock,self.stock_festival,festival,self.A2)
                else:
                    f,f1s,f2s=browns(f_stock,self.stock_festival,festival,self.A1,self.A2,self.A3)
                
                f_alpha=alpha(festival,self.tiles,self.A4)
                f*=f_alpha
            
            if imperial.size>0:
                if i_stock[3]==self.stock_imperial and i_stock[2]==0:
                    i,i1s,i2s=initial_advantage(i_stock,self.A10)
                elif self.stock_imperial==i_stock[3]:
                    i,i1s,i2s=defence(i_stock,imperial,self.A1)
                elif (i_stock[3]-self.stock_imperial)<=3:
                    i,i1s,i2s=inthehunt(i_stock,self.stock_imperial,imperial,self.A2)
                else:
                    i,i1s,i2s=browns(i_stock,self.stock_imperial,imperial,self.A1,self.A2,self.A3)
                
                i_alpha=alpha(imperial,self.tiles,self.A4)
                i*=i_alpha
                
            if american.size>0:
                if a_stock[3]==self.stock_american and a_stock[2]==0:
                    a,a1s,a2s=initial_advantage(a_stock,self.A10)
                elif self.stock_american==a_stock[3]:
                    a,a1s,a2s=defence(a_stock,american,self.A1)
                elif (a_stock[3]-self.stock_american)<=3:
                    a,a1s,a2s=inthehunt(a_stock,self.stock_american,american,self.A2)
                else:
                    a,a1s,a2s=browns(a_stock,self.stock_american,american,self.A1,self.A2,self.A3)
                
                a_alpha=alpha(american,self.tiles,self.A4)
                a*=a_alpha
            
            if continental.size>0:
                if c_stock[3]==self.stock_continental and c_stock[2]==0:
                    c,c1s,c2s=initial_advantage(c_stock,self.A10)
                elif self.stock_continental==c_stock[3]:
                    c,c1s,c2s=defence(c_stock,continental,self.A1)
                elif (c_stock[3]-self.stock_continental)<=3:
                    c,c1s,c2s=inthehunt(c_stock,self.stock_continental,continental,self.A2)
                else:
                    c,c1s,c2s=browns(c_stock,self.stock_continental,continental,self.A1,self.A2,self.A3)
                
                c_alpha=alpha(continental,self.tiles,self.A4)
                c*=c_alpha
            
            if tower.size>0:
                if t_stock[3]==self.stock_tower and t_stock[2]==0:
                    t,t1s,t2s=initial_advantage(t_stock,self.A10)
                elif self.stock_tower==t_stock[3]:
                    t,t1s,t2s=defence(t_stock,tower,self.A1)
                elif (t_stock[3]-self.stock_tower)<=3:
                    t,t1s,t2s=inthehunt(t_stock,self.stock_tower,tower,self.A2)
                else:
                    t,t1s,t2s=browns(t_stock,self.stock_tower,tower,self.A1,self.A2,self.A3)
                
                t_alpha=alpha(tower,self.tiles,self.A4)
                t*=t_alpha
            
            points=np.array([w,s,f,i,a,c,t])
            points2=[]
            for i in range(7):
                points2.append(points[i])
            points2=np.sort(points2)
            for i in range(7):
                #achtung bei gleichstand wird das hotel mit dem tieferen value gewählt
                if points[i]==points2[6]:
                    favhotel=eval_hotel(i+2)
            splitt=False        
            if points2[6]-points2[5]<=self.A8 and points2[5]!=0:
                splitt=True
                for i in range(7):
                    #achtung bei gleichstand wird das hotel mit dem tieferen value gewählt
                    if points[i]==points2[5]:
                        favhotel2=eval_hotel(i+2)
                        
                
            
            smallbuys=np.array([[w1s,s1s,f1s,i1s,a1s,c1s,t1s],
                                [w2s,s2s,f2s,i2s,a2s,c2s,t2s]])
            
            p=3
            list1s=[]
            list2s=[]
            for i in range(2,9):
                if smallbuys[0,i-2]==True:
                    list1s.append(eval_hotel(i))
                if smallbuys[1,i-2]==True:
                    list2s.append(eval_hotel(i))
                    
            a=len(list1s)
            b=len(list2s)
            if a+2*b<=3:
                for i in range(len(list1s)):
                    buy_hotel = list1s[i]
                    price,useless, useless2 = buy_hotel.reference()
                    if self.money>=price and buy_hotel.stock>=1:
                        self.getstock(buy_hotel.value,1)
                        p-=1
                        #print(self.name,"has purchased",1,"stock from",buy_hotel.name)
                for i in range(len(list2s)):
                    buy_hotel = list2s[i]
                    price,useless, useless2 = buy_hotel.reference()
                    if self.money>=price*2 and buy_hotel.stock>=2:
                        self.getstock(buy_hotel.value,2)
                        p-=2
                        #print(self.name,"has purchased",2,"stocks from",buy_hotel.name)
            elif a+2*b>3:
                list3=list1s+list2s
                list4=[]
                for i in range(len(list3)):
                    list4.append(points[list3[i].value-2])
                list4.sort()
                for k in range(3):
                    n1 = len(list4)
                    l = 0
                    for i in range(n1): 
                        if points[list3[l].value-2]==list4[-1]:
                            buy_hotel=list3[l]
                            price,useless, useless2 = buy_hotel.reference()
                            if smallbuys[0,buy_hotel.value-2]==True:
                                n=1
                            else:
                                n=2
                            if self.money>=price*n and p>=n and buy_hotel.stock>=n:
                                self.getstock(buy_hotel.value,n)
                                p-=n
                                #print(self.name,"has purchased",n,"stocks from",buy_hotel.name)
                                list3.pop(l)
                                l-=1
                                list4.pop(-1)
                        l+=1 
    
            if points[favhotel.value-2]>=self.A6[0]*self.money+self.A6[1] and points[favhotel.value-2]!=0:
                if splitt==True:
                    price,useless, useless2 = favhotel.reference()
                    if self.money>=price*2 and p>=2 and favhotel.stock>=2:
                        self.getstock(favhotel.value,2)
                        p-=2
                        #print(self.name,"has purchased",2,"stocks from",favhotel.name)
                    price2,useless3, useless4 = favhotel.reference()
                    if self.money>=price2*1 and p>=1 and favhotel2.stock>=1:
                        self.getstock(favhotel2.value,1)
                        p-=1
                        #print(self.name,"has purchased",1,"stock from",favhotel2.name)
                elif splitt==False:
                    price,useless, useless2 = favhotel.reference()
                    if self.money>=price*p and favhotel.stock>=p:
                        self.getstock(favhotel.value,p)
                        #print(self.name,"has purchased",p,"stocks from",favhotel.name)
            
            
                
        def set_money(self,cash):
            self.money += cash
            
            
        def info(self):
            return self.money, self.stock_tower, self.stock_continental, self.stock_american, self.stock_imperial, self.stock_festival, self.stock_sackson ,self.stock_worldwide
            
        def info_stock(self,value):
            if value == tower.value:
                return self.stock_tower
            elif value == continental.value:
                return self.stock_continental
            elif value == american.value:
                return self.stock_american
            elif value == imperial.value:
                return self.stock_imperial
            elif value == festival.value:
                return self.stock_festival
            elif value == sackson.value:
                return self.stock_sackson
            elif value == worldwide.value:
                return self.stock_worldwide
            
        def sellstock(self,value,n,free=False):
            price,useless, useless2 = eval_hotel(value).reference()
            if free==False:
                self.set_money(n*price)
            if value == tower.value:
                self.stock_tower -= n
                tower.recstock(n)
            elif value == continental.value:
                self.stock_continental -= n
                continental.recstock(n)
            elif value == american.value:
                self.stock_american -= n
                american.recstock(n)
            elif value == imperial.value:
                self.stock_imperial -= n
                imperial.recstock(n)
            elif value == festival.value:
                self.stock_festival -= n
                festival.recstock(n)
            elif value == sackson.value:
                self.stock_sackson -= n
                sackson.recstock(n)
            elif value == worldwide.value:
                self.stock_worldwide -= n
                worldwide.recstock(n)
        
        def getstock(self,value,n,free=False):
            price,useless, useless2 = eval_hotel(value).reference()
            if free==False:
                self.set_money(-n*price)
            if value == tower.value:
               self.stock_tower += n
               tower.sellstock(n)
            elif value == continental.value:
               self.stock_continental += n
               continental.sellstock(n)
            elif value == american.value:
               self.stock_american += n
               american.sellstock(n)
            elif value == imperial.value:
               self.stock_imperial += n
               imperial.sellstock(n)
            elif value == festival.value:
               self.stock_festival += n
               festival.sellstock(n)
            elif value == sackson.value:
               self.stock_sackson += n
               sackson.sellstock(n)
            elif value == worldwide.value:
               self.stock_worldwide += n
               worldwide.sellstock(n)
         
        #decide...stupid 
        def decide_merge(self,hotel1,hotel2):
            m1,t1,c1,a1,i1,f1,s1,w1=self.info()
            hilfsarray=np.array([w1,s1,f1,i1,a1,c1,t1])
    
            maj1,minn1 = majmin(hotel1)
            maj2,minn2 = majmin(hotel2)
            M1=False
            m1=False
            M2=False
            m2=False
            for i in range(len(maj1)):
                if maj1[i].name==self.name:
                    M1=True
            for i in range(len(minn1)):
                if minn1[i].name==self.name:
                    m1=True
            for i in range(len(maj2)):
                if maj2[i].name==self.name:
                    M2=True
            for i in range(len(minn2)):
                if minn2[i].name==self.name:
                    m2=True
            
            if M1==True and M2==False:
                if np.abs(hilfsarray[hotel1.value-2]-hotel1.stock)<=5 and hilfsarray[hotel1.value-2]>=5 and self.money>=3000:
                    return hotel1,hotel2
                else: 
                    return hotel2,hotel1
            elif M2==True and M1==False:
                if np.abs(hilfsarray[hotel2.value-2]-hotel2.stock)<=5 and hilfsarray[hotel2.value-2]>=5 and self.money>=3000:
                    return hotel2,hotel1
                else: 
                    return hotel1,hotel2
                
            elif M1==True and M2 == True:
                if self.difference_to_maj(hotel1)>=self.difference_to_maj(hotel2):
                    return hotel1,hotel2
                else:
                    return hotel2,hotel1
                
            elif m1==True and m2==False:
                if np.abs(hilfsarray[hotel1.value-2]-hotel1.stock)<=5 and hilfsarray[hotel1.value-2]>=5 and self.money>=3000:
                    return hotel1,hotel2
                else: 
                    return hotel2,hotel1
            elif m2==True and m1==False:
                if np.abs(hilfsarray[hotel2.value-2]-hotel2.stock)<=5 and hilfsarray[hotel2.value-2]>=5 and self.money>=3000:
                    return hotel2,hotel1
                else: 
                    return hotel1,hotel2
           
            elif m1==True and m2 == True:
                if self.difference_to_maj(hotel1)<=self.info_stock(hotel1.value)/2:
                    return hotel1,hotel2
                elif self.difference_to_maj(hotel2)<=self.info_stock(hotel1.value)/2:
                    return hotel2,hotel1
                elif self.money>=3000 and hilfsarray[hotel1.value-2]>=hilfsarray[hotel2.value-2]:
                    return hotel1,hotel2
                elif self.money>=3000 and hilfsarray[hotel1.value-2]<hilfsarray[hotel2.value-2]:
                    return hotel2,hotel1
                elif self.money<3000 and hilfsarray[hotel1.value-2]>=hilfsarray[hotel2.value-2]:
                    return hotel2,hotel1
                elif self.money>=3000 and hilfsarray[hotel1.value-2]<hilfsarray[hotel2.value-2]:
                    return hotel1,hotel2
            else:
                if hilfsarray[hotel1.value-2]>=hilfsarray[hotel2.value-2]:
                    return hotel1,hotel2
                else:
                    return hotel2,hotel1
            
        
        def decide_triple_merge(self,hotel1,hotel2,hotel3):
            big,small=self.decide_merge(hotel1,hotel2)
            a,b = self.decide_merge(big,hotel3)
            return a,b,small
        
        def decide_double_merge(self,hotel1,hotel2):
            return self.decide_merge(hotel1,hotel2)
        
        def decide_quad_merge(self,hotel1,hotel2,hotel3,hotel4):
            big,small1,small2=self.decide_triple_merge(hotel1,hotel2,hotel3)
            a,b = self.decide_merge(big,hotel4)
            return a,b,small1,small2
        
        def decide_newhotel(self):
            m1,t1,c1,a1,i1,f1,s1,w1 = self.info()
            stocks=np.array([w1,s1,f1,i1,a1,c1,t1])
            hlist=[]
            hlist2=[]
            for i in range(2,9):
                if eval_hotel(i).size==0:
                    hlist.append(eval_hotel(i))
                    hlist2.append(eval_hotel(i))
            prefhotel=hlist[0]
            for i in range(len(hlist)):
                if stocks[hlist[i].value-2]>stocks[prefhotel.value-2]:
                    prefhotel=hlist[i]
            if stocks[prefhotel.value-2]>0:
                return prefhotel
            for k in range(7):
                for i in range(len(hlist2)):
                    if hlist2[i].stock<25:
                        hlist2.pop(len(hlist2)-1-i)
                        break
            if len(hlist2)>0:
                r = random.randint(0,len(hlist2)-1)
                return hlist2[r]
            else:
                r = random.randint(0,len(hlist)-1)
                return hlist[r]
            
    class Player_conservative:
   
        def __init__(self,g,name1):
            self.money = g
            self.stock_tower=0
            self.stock_continental = 0
            self.stock_american = 0
            self.stock_imperial = 0
            self.stock_festival = 0
            self.stock_sackson = 0 
            self.stock_worldwide = 0
            self.tiles = []
            self.name = name1
            #defense matrix
            self.A1=np.array([[0,0,0,0,0,0,0,5],
                              [0,0,0,0,0,0,50,6],
                              [0,0,0,0,0,50,50,8],
                              [0,0,0,0,50,50,100,10],
                              [0,0,0,50,50,100,100,15],
                              [0,0,50,50,100,100,22,16],
                              [0,50,50,100,100,24,24,18],
                              [0,50,100,100,24,24,17,20]]) #50->buy 1 stock, 100->buy two stocks
            
            #inthehunt matrix
            #row corresponds to deficit-1,coloumn to number of stock available from hotel
            self.A2=np.array([[0,17,100,24,24,17,7,10],
                              [0,0,17,24,24,6,5,8],
                              [0,0,0,17,8,7,6,7]])
        
            #brown coefficients
            self.A3=np.array([0.4,0.4,1,0.5])
            
            #alpha coefficients
            self.A4=np.array([0.1,0.02])
            
            #hold onto stock matrix
            #first coloumn:turn, second coulumn:stocks of other players, 
            #thrid coloumn:own stock, 4th coloumn:b
            #Attention: the fourth coloumn must be <= the third coloumn
            self.A5=np.array([[30,0,2,1],
                              [30,2,4,1],
                              [50,0,2,0],
                              [50,2,4,0]])
        
            #graph to determine how much money is spent  
            #self.A6=np.array([-1/200,17/3])#Variant offensive
            self.A6=np.array([-1/800,50/3])
            
            #matrix which awards points for tile placement; 0:maj in small, 1-4:min small and cash problems
            #5:maj big and enough in small to defend lead, 6: would become maj in big, 
            #7:hotel would be created,8:enlarge majority,9:enlarge minority
            self.A7=np.array([20,2500,12,3500,10,15,14,11,6,3])
            
            #coefficient that determines whether the player spreads his buys
            self.A8=3
            
            #money below which to sell stock, ratio when to go for 2:1 trade
            self.A9=np.array([4000,2.5])
            
            #initial advantage matrix
            self.A10=np.array([13,9,7,6])
        
        def drawtile(self,alltiles):
            a = random.randint(0,len(alltiles)-1)
            tile = alltiles.pop(a)
            #print(tile)
            self.tiles.append(tile)
            #self.add(tile)
            return
        
        #def placetile...remove tile and call global placetile()
        def placetile_player(self, x0):
            for i in range(6):
                #print(i)
                #print("length:",len(self.tiles))
                tile = self.tiles[i]
                if tile[0] == x0[0] and tile[1]==x0[1]:
                    self.tiles.pop(i)
                    break
            #print(x0,"has been placed on the board")
            placetile(x0,self)
            return
        
        
        def decide_placetile(self):
            eligible_tiles = []
            for i in range(6):
                if is_legal(self.tiles[i])==True:
                    eligible_tiles.append(self.tiles[i])
            
            tries=0
            while len(eligible_tiles)==0:
                for i in range(6):
                    #print("# tiles:", len(self.tiles))
                    a = self.tiles.pop(5-i)
                    alltiles.append(a)
                    
                for i in range(6):
                    self.drawtile(alltiles)
                    
                for i in range(6):
                    if is_legal(self.tiles[i])==True:
                        eligible_tiles.append(self.tiles[i])  
                tries+=1
                if tries>=10:
                    return True
            points=[]
            for i in range(len(eligible_tiles)):
                p=0
                tile=eligible_tiles[i]
                info=tile_info(tile)
                infosort=np.sort(tile_info(tile))
                n = 0 #number of non-empty tiles
                for k in range(len(info)):
                    if info[k] !=0:
                        n += 1
                n1=0 #number of single tiles
                for k in range(len(info)):
                    if info[k] ==1:
                        n1 += 1
                #number of hotels surrounding tile
                m = 0
                m1 = []
                for k in range(4):
                    if info[k] > 1:
                        b = True
                        for j in range(len(m1)):
                            if info[k]==m1[j]:
                                b = False
                        m1.append(info[k]) 
                        if b ==True:
                            m+=1
                if m==2:
                    hotel1=eval_hotel(infosort[3])
                    if infosort[3]!=infosort[2]:
                        hotel2=eval_hotel(infosort[2])
                    elif infosort[3]!=infosort[1]:
                        hotel2=eval_hotel(infosort[1])
                    else:
                        hotel2=eval_hotel(infosort[0])
                    if hotel1.size>=hotel2.size:
                        big=hotel1
                        small=hotel2
                    else:
                        big=hotel2
                        small=hotel1
                    maj,minn=majmin(small)
                    majb,minnb=majmin(big)
                    c=0
                    #majority small
                    for j in range(len(maj)):
                        if maj[j].name==self.name:
                            p+=self.A7[0]
                            c=10
                    #minority small and in need of money
                    for j in range(len(minn)):
                        if minn[j].name==self.name and self.money<self.A7[1]:
                            p+=self.A7[2]
                            c=10
                        elif minn[j].name==self.name and self.money<self.A7[3]:
                            p+=self.A7[4]
                            c=10
                    #majority in big and enough stock in small to defend lead
                    for j in range(len(majb)):
                        if majb[j].name==self.name and self.difference_to_maj(big)>-self.difference_to_maj(small)/2:
                            p+=self.A7[5]
                            c=10
                    #if you can become majority of big
                    for j in range(len(minnb)):
                        if -self.difference_to_maj(big)<(self.info_stock(small.value)/2-majb[-1].info_stock(small.value)/2):
                            p+=self.A7[6]
                            c=10
                   
                            
                    
                    
                    p=p-10+c
                if m==3:
                    hotel1=eval_hotel(infosort[3])
                    if infosort[2]!=infosort[3]:
                        hotel2=eval_hotel(infosort[2])
                        if infosort[1]!=infosort[2]:
                            hotel3=eval_hotel(infosort[1])
                        else:
                            hotel3=eval_hotel(infosort[0])
                        
                    else:
                        hotel2=eval_hotel(infosort[1])
                        hotel3=eval_hotel(infosort[0])
                        
                    if hotel1.size>hotel2.size and hotel1.size>hotel3.size:
                        big=hotel1
                        small1=hotel2
                        small2=hotel3
                    elif hotel2.size>hotel1.size and hotel2.size>hotel3.size:
                        big=hotel2
                        small1=hotel1
                        small2=hotel3
                    elif hotel3.size>hotel1.size and hotel3.size>hotel2.size:
                        big=hotel3
                        small1=hotel1
                        small2=hotel2
                    else:
                        big=hotel1
                        small1=hotel2
                        small2=hotel3
                    
                    c=0
                    maj1,minn1=majmin(small1)
                    for j in range(len(maj1)):
                        if maj1[j].name==self.name:
                            p+=self.A7[0]
                            c=10
                    maj2,minn2=majmin(small2)
                    for j in range(len(maj2)):
                        if maj2[j].name==self.name:
                            p+=self.A7[0]
                            c=10
                    majb,minnb=majmin(big)
                    for j in range(len(majb)):
                        if majb[j].name==self.name and (self.difference_to_maj(big)>-self.difference_to_maj(small1)/2 or self.difference_to_maj(big)>-self.difference_to_maj(small2)/2):
                            p+=self.A7[5]
                            c=10
                    for j in range(len(minn1)):
                       if minn1[j].name==self.name and self.money<self.A7[1]:
                           p+=self.A7[2]
                           c=10
                       elif minn1[j].name==self.name and self.money<self.A7[3]:
                           p+=self.A7[4]
                           c=10
                    for j in range(len(minn2)):
                       if minn2[j].name==self.name and self.money<self.A7[1]:
                           p+=self.A7[2]
                           c=10
                       elif minn2[j].name==self.name and self.money<self.A7[3]:
                           p+=self.A7[4]
                           c=10
                    p=p-10+c
                    
                if m==0 and n>0:
                    c=0
                    for j in range(2,9):
                        if eval_hotel(j).size==0 and self.info_stock(j)>0:
                            p+=self.A7[7]
                            c=5
                            break
                    #This is not a mistake!!
                    p=p+5-c
                
                if m==1:
                    adjhotel=eval_hotel(infosort[3])
                    maj,minn=majmin(adjhotel)
                    c=0
                    for j in range(len(maj)):
                        if maj[j].name==self.name:
                            p+=self.A7[8]
                            c=2
                    for j in range(len(minn)):
                        if minn[j].name==self.name:
                            p+=self.A7[9]
                            c=2
                    p=p-2+c
                
                points.append(p)
            
            besttilenumber=0
            for i in range(len(eligible_tiles)-1):
                if points[i+1]>points[besttilenumber]:
                    besttilenumber = i+1
            besttile=eligible_tiles[besttilenumber]
            self.placetile_player(besttile)
            return False
            
      
        def decide_merge_stock(self,big,small):
            n=self.info_stock(small.value)
            m=big.stock
            b=0
            while(self.money<self.A9[0] and n>=1):
                self.sellstock(small.value,1)
                n-=1
            if self.difference_to_maj(big)>=-n/2 and m>=n/2:
                while(m>=1 and n>=2):
                    self.getstock(big.value,1,free=True)
                    self.sellstock(small.value,2,free=True)
                    m-=1
                    n-=2
                    #print(self.name,"has traded 2",small.name,"stocks for 1",big.name,"stock")
            bigprice, useless1,useless2=big.reference()
            smallprice, useless3,useless4=small.reference()
            if bigprice>=self.A9[1]*smallprice:
                while(m>=1 and n>=2):
                    self.getstock(big.value,1,free=True)
                    self.sellstock(small.value,2,free=True)
                    m-=1
                    n-=2
                    #print(self.name,"has traded 2",small.name,"stocks for 1",big.name,"stock")
            stocks=self.other_player_stocks(small)
            b=hold_stock(stocks,n,self.A5)
            self.sellstock(small.value,n-b)
            #print(self.name,"has held on to",b,"stocks and sold",n-b,"stocks")
            
            
        def other_player_stocks(self,hotel):
            stocks=[]
            if self.name !=player1:
                stocks.append(player1.info_stock(hotel.value))
            if self.name !=player2:
                stocks.append(player2.info_stock(hotel.value))
            if self.name !=player3:
                stocks.append(player3.info_stock(hotel.value))
            if self.name !=player4:
                stocks.append(player4.info_stock(hotel.value))
            stocks=np.sort(stocks)
                
            return stocks
        
        def difference_to_maj(self,hotel):
            stocks=self.other_player_stocks(hotel)
            return self.info_stock(hotel.value)-stocks[2]
                
            
        #TODO
        def buy_stock(self):
            
            m1,t1,c1,a1,i1,f1,s1,w1 = player1.info()
            m2,t2,c2,a2,i2,f2,s2,w2 = player2.info()
            m3,t3,c3,a3,i3,f3,s3,w3 = player3.info()
            m4,t4,c4,a4,i4,f4,s4,w4 = player4.info()
            
            w_stock=np.sort([w1,w2,w3,w4])
            s_stock=np.sort([s1,s2,s3,s4])
            f_stock=np.sort([f1,f2,f3,f4])
            i_stock=np.sort([i1,i2,i3,i4])
            a_stock=np.sort([a1,a2,a3,a4])
            c_stock=np.sort([c1,c2,c3,c4])
            t_stock=np.sort([t1,t2,t3,t4])
            
            #Points for each stock and if the player should particularly buy 1 or 2
            w,s,f,i,a,c,t=0,0,0,0,0,0,0
            w1s,w2s,s1s,s2s,f1s,f2s,i1s,i2s,a1s,a2s,c1s,c2s,t1s,t2s=False,False,False,False,False,False,False,False,False,False,False,False,False,False
            
            if worldwide.size>0:
                if w_stock[3]==self.stock_worldwide and w_stock[2]==0:
                    w,w1s,w2s=initial_advantage(w_stock,self.A10)
                elif self.stock_worldwide==w_stock[3]:
                    w,w1s,w2s=defence(w_stock,worldwide,self.A1)
                elif (w_stock[3]-self.stock_worldwide)<=3:
                    w,w1s,w2s=inthehunt(w_stock,self.stock_worldwide,worldwide,self.A2)
                else:
                    w,w1s,w2s=browns(w_stock,self.stock_worldwide,worldwide,self.A1,self.A2,self.A3)
                
                w_alpha=alpha(worldwide,self.tiles,self.A4)
                w*=w_alpha
                
            if sackson.size>0:
                if s_stock[3]==self.stock_sackson and s_stock[2]==0:
                    s,s1s,s2s=initial_advantage(s_stock,self.A10)
                elif self.stock_sackson==s_stock[3]:
                    s,s1s,s2s=defence(s_stock,sackson,self.A1)
                elif (s_stock[3]-self.stock_sackson)<=3:
                    s,s1s,s2s=inthehunt(s_stock,self.stock_sackson,sackson,self.A2)
                else:
                    s,s1s,s2s=browns(s_stock,self.stock_sackson,sackson,self.A1,self.A2,self.A3)
            
            s_alpha=alpha(sackson,self.tiles,self.A4)
            s*=s_alpha
            
            if festival.size>0:
                if f_stock[3]==self.stock_festival and f_stock[2]==0:
                    f,f1s,f2s=initial_advantage(f_stock,self.A10)
                elif self.stock_festival==f_stock[3]:
                    f,f1s,f2s=defence(f_stock,festival,self.A1)
                elif (f_stock[3]-self.stock_festival)<=3:
                    f,f1s,f2s=inthehunt(f_stock,self.stock_festival,festival,self.A2)
                else:
                    f,f1s,f2s=browns(f_stock,self.stock_festival,festival,self.A1,self.A2,self.A3)
                
                f_alpha=alpha(festival,self.tiles,self.A4)
                f*=f_alpha
            
            if imperial.size>0:
                if i_stock[3]==self.stock_imperial and i_stock[2]==0:
                    i,i1s,i2s=initial_advantage(i_stock,self.A10)
                elif self.stock_imperial==i_stock[3]:
                    i,i1s,i2s=defence(i_stock,imperial,self.A1)
                elif (i_stock[3]-self.stock_imperial)<=3:
                    i,i1s,i2s=inthehunt(i_stock,self.stock_imperial,imperial,self.A2)
                else:
                    i,i1s,i2s=browns(i_stock,self.stock_imperial,imperial,self.A1,self.A2,self.A3)
                
                i_alpha=alpha(imperial,self.tiles,self.A4)
                i*=i_alpha
                
            if american.size>0:
                if a_stock[3]==self.stock_american and a_stock[2]==0:
                    a,a1s,a2s=initial_advantage(a_stock,self.A10)
                elif self.stock_american==a_stock[3]:
                    a,a1s,a2s=defence(a_stock,american,self.A1)
                elif (a_stock[3]-self.stock_american)<=3:
                    a,a1s,a2s=inthehunt(a_stock,self.stock_american,american,self.A2)
                else:
                    a,a1s,a2s=browns(a_stock,self.stock_american,american,self.A1,self.A2,self.A3)
                
                a_alpha=alpha(american,self.tiles,self.A4)
                a*=a_alpha
            
            if continental.size>0:
                if c_stock[3]==self.stock_continental and c_stock[2]==0:
                    c,c1s,c2s=initial_advantage(c_stock,self.A10)
                elif self.stock_continental==c_stock[3]:
                    c,c1s,c2s=defence(c_stock,continental,self.A1)
                elif (c_stock[3]-self.stock_continental)<=3:
                    c,c1s,c2s=inthehunt(c_stock,self.stock_continental,continental,self.A2)
                else:
                    c,c1s,c2s=browns(c_stock,self.stock_continental,continental,self.A1,self.A2,self.A3)
                
                c_alpha=alpha(continental,self.tiles,self.A4)
                c*=c_alpha
            
            if tower.size>0:
                if t_stock[3]==self.stock_tower and t_stock[2]==0:
                    t,t1s,t2s=initial_advantage(t_stock,self.A10)
                elif self.stock_tower==t_stock[3]:
                    t,t1s,t2s=defence(t_stock,tower,self.A1)
                elif (t_stock[3]-self.stock_tower)<=3:
                    t,t1s,t2s=inthehunt(t_stock,self.stock_tower,tower,self.A2)
                else:
                    t,t1s,t2s=browns(t_stock,self.stock_tower,tower,self.A1,self.A2,self.A3)
                
                t_alpha=alpha(tower,self.tiles,self.A4)
                t*=t_alpha
            
            points=np.array([w,s,f,i,a,c,t])
            points2=[]
            for i in range(7):
                points2.append(points[i])
            points2=np.sort(points2)
            for i in range(7):
                #achtung bei gleichstand wird das hotel mit dem tieferen value gewählt
                if points[i]==points2[6]:
                    favhotel=eval_hotel(i+2)
            splitt=False        
            if points2[6]-points2[5]<=self.A8 and points2[5]!=0:
                splitt=True
                for i in range(7):
                    #achtung bei gleichstand wird das hotel mit dem tieferen value gewählt
                    if points[i]==points2[5]:
                        favhotel2=eval_hotel(i+2)
                        
                
            
            smallbuys=np.array([[w1s,s1s,f1s,i1s,a1s,c1s,t1s],
                                [w2s,s2s,f2s,i2s,a2s,c2s,t2s]])
            
            p=3
            list1s=[]
            list2s=[]
            for i in range(2,9):
                if smallbuys[0,i-2]==True:
                    list1s.append(eval_hotel(i))
                if smallbuys[1,i-2]==True:
                    list2s.append(eval_hotel(i))
                    
            a=len(list1s)
            b=len(list2s)
            if a+2*b<=3:
                for i in range(len(list1s)):
                    buy_hotel = list1s[i]
                    price,useless, useless2 = buy_hotel.reference()
                    if self.money>=price and buy_hotel.stock>=1:
                        self.getstock(buy_hotel.value,1)
                        p-=1
                        #print(self.name,"has purchased",1,"stock from",buy_hotel.name)
                for i in range(len(list2s)):
                    buy_hotel = list2s[i]
                    price,useless, useless2 = buy_hotel.reference()
                    if self.money>=price*2 and buy_hotel.stock>=2:
                        self.getstock(buy_hotel.value,2)
                        p-=2
                        #print(self.name,"has purchased",2,"stocks from",buy_hotel.name)
            elif a+2*b>3:
                list3=list1s+list2s
                list4=[]
                for i in range(len(list3)):
                    list4.append(points[list3[i].value-2])
                list4.sort()
                for k in range(3):
                    n1 = len(list4)
                    l = 0
                    for i in range(n1): 
                        if points[list3[l].value-2]==list4[-1]:
                            buy_hotel=list3[l]
                            price,useless, useless2 = buy_hotel.reference()
                            if smallbuys[0,buy_hotel.value-2]==True:
                                n=1
                            else:
                                n=2
                            if self.money>=price*n and p>=n and buy_hotel.stock>=n:
                                self.getstock(buy_hotel.value,n)
                                p-=n
                                #print(self.name,"has purchased",n,"stocks from",buy_hotel.name)
                                list3.pop(l)
                                l-=1
                                list4.pop(-1)
                        l+=1 
    
            if points[favhotel.value-2]>=self.A6[0]*self.money+self.A6[1] and points[favhotel.value-2]!=0:
                if splitt==True:
                    price,useless, useless2 = favhotel.reference()
                    if self.money>=price*2 and p>=2 and favhotel.stock>=2:
                        self.getstock(favhotel.value,2)
                        p-=2
                        #print(self.name,"has purchased",2,"stocks from",favhotel.name)
                    price2,useless3, useless4 = favhotel.reference()
                    if self.money>=price2*1 and p>=1 and favhotel2.stock>=1:
                        self.getstock(favhotel2.value,1)
                        p-=1
                        #print(self.name,"has purchased",1,"stock from",favhotel2.name)
                elif splitt==False:
                    price,useless, useless2 = favhotel.reference()
                    if self.money>=price*p and favhotel.stock>=p:
                        self.getstock(favhotel.value,p)
                        #print(self.name,"has purchased",p,"stocks from",favhotel.name)
            
            
                
        def set_money(self,cash):
            self.money += cash
            
            
        def info(self):
            return self.money, self.stock_tower, self.stock_continental, self.stock_american, self.stock_imperial, self.stock_festival, self.stock_sackson ,self.stock_worldwide
            
        def info_stock(self,value):
            if value == tower.value:
                return self.stock_tower
            elif value == continental.value:
                return self.stock_continental
            elif value == american.value:
                return self.stock_american
            elif value == imperial.value:
                return self.stock_imperial
            elif value == festival.value:
                return self.stock_festival
            elif value == sackson.value:
                return self.stock_sackson
            elif value == worldwide.value:
                return self.stock_worldwide
            
        def sellstock(self,value,n,free=False):
            price,useless, useless2 = eval_hotel(value).reference()
            if free==False:
                self.set_money(n*price)
            if value == tower.value:
                self.stock_tower -= n
                tower.recstock(n)
            elif value == continental.value:
                self.stock_continental -= n
                continental.recstock(n)
            elif value == american.value:
                self.stock_american -= n
                american.recstock(n)
            elif value == imperial.value:
                self.stock_imperial -= n
                imperial.recstock(n)
            elif value == festival.value:
                self.stock_festival -= n
                festival.recstock(n)
            elif value == sackson.value:
                self.stock_sackson -= n
                sackson.recstock(n)
            elif value == worldwide.value:
                self.stock_worldwide -= n
                worldwide.recstock(n)
        
        def getstock(self,value,n,free=False):
            price,useless, useless2 = eval_hotel(value).reference()
            if free==False:
                self.set_money(-n*price)
            if value == tower.value:
               self.stock_tower += n
               tower.sellstock(n)
            elif value == continental.value:
               self.stock_continental += n
               continental.sellstock(n)
            elif value == american.value:
               self.stock_american += n
               american.sellstock(n)
            elif value == imperial.value:
               self.stock_imperial += n
               imperial.sellstock(n)
            elif value == festival.value:
               self.stock_festival += n
               festival.sellstock(n)
            elif value == sackson.value:
               self.stock_sackson += n
               sackson.sellstock(n)
            elif value == worldwide.value:
               self.stock_worldwide += n
               worldwide.sellstock(n)
         
        #decide...stupid 
        def decide_merge(self,hotel1,hotel2):
            m1,t1,c1,a1,i1,f1,s1,w1=self.info()
            hilfsarray=np.array([w1,s1,f1,i1,a1,c1,t1])
    
            maj1,minn1 = majmin(hotel1)
            maj2,minn2 = majmin(hotel2)
            M1=False
            m1=False
            M2=False
            m2=False
            for i in range(len(maj1)):
                if maj1[i].name==self.name:
                    M1=True
            for i in range(len(minn1)):
                if minn1[i].name==self.name:
                    m1=True
            for i in range(len(maj2)):
                if maj2[i].name==self.name:
                    M2=True
            for i in range(len(minn2)):
                if minn2[i].name==self.name:
                    m2=True
            
            if M1==True and M2==False:
                if np.abs(hilfsarray[hotel1.value-2]-hotel1.stock)<=5 and hilfsarray[hotel1.value-2]>=5 and self.money>=3000:
                    return hotel1,hotel2
                else: 
                    return hotel2,hotel1
            elif M2==True and M1==False:
                if np.abs(hilfsarray[hotel2.value-2]-hotel2.stock)<=5 and hilfsarray[hotel2.value-2]>=5 and self.money>=3000:
                    return hotel2,hotel1
                else: 
                    return hotel1,hotel2
                
            elif M1==True and M2 == True:
                if self.difference_to_maj(hotel1)>=self.difference_to_maj(hotel2):
                    return hotel1,hotel2
                else:
                    return hotel2,hotel1
                
            elif m1==True and m2==False:
                if np.abs(hilfsarray[hotel1.value-2]-hotel1.stock)<=5 and hilfsarray[hotel1.value-2]>=5 and self.money>=3000:
                    return hotel1,hotel2
                else: 
                    return hotel2,hotel1
            elif m2==True and m1==False:
                if np.abs(hilfsarray[hotel2.value-2]-hotel2.stock)<=5 and hilfsarray[hotel2.value-2]>=5 and self.money>=3000:
                    return hotel2,hotel1
                else: 
                    return hotel1,hotel2
           
            elif m1==True and m2 == True:
                if self.difference_to_maj(hotel1)<=self.info_stock(hotel1.value)/2:
                    return hotel1,hotel2
                elif self.difference_to_maj(hotel2)<=self.info_stock(hotel1.value)/2:
                    return hotel2,hotel1
                elif self.money>=3000 and hilfsarray[hotel1.value-2]>=hilfsarray[hotel2.value-2]:
                    return hotel1,hotel2
                elif self.money>=3000 and hilfsarray[hotel1.value-2]<hilfsarray[hotel2.value-2]:
                    return hotel2,hotel1
                elif self.money<3000 and hilfsarray[hotel1.value-2]>=hilfsarray[hotel2.value-2]:
                    return hotel2,hotel1
                elif self.money>=3000 and hilfsarray[hotel1.value-2]<hilfsarray[hotel2.value-2]:
                    return hotel1,hotel2
            else:
                if hilfsarray[hotel1.value-2]>=hilfsarray[hotel2.value-2]:
                    return hotel1,hotel2
                else:
                    return hotel2,hotel1
            
        
        def decide_triple_merge(self,hotel1,hotel2,hotel3):
            big,small=self.decide_merge(hotel1,hotel2)
            a,b = self.decide_merge(big,hotel3)
            return a,b,small
        
        def decide_double_merge(self,hotel1,hotel2):
            return self.decide_merge(hotel1,hotel2)
        
        def decide_quad_merge(self,hotel1,hotel2,hotel3,hotel4):
            big,small1,small2=self.decide_triple_merge(hotel1,hotel2,hotel3)
            a,b = self.decide_merge(big,hotel4)
            return a,b,small1,small2
        
        def decide_newhotel(self):
            m1,t1,c1,a1,i1,f1,s1,w1 = self.info()
            stocks=np.array([w1,s1,f1,i1,a1,c1,t1])
            hlist=[]
            hlist2=[]
            for i in range(2,9):
                if eval_hotel(i).size==0:
                    hlist.append(eval_hotel(i))
                    hlist2.append(eval_hotel(i))
            prefhotel=hlist[0]
            for i in range(len(hlist)):
                if stocks[hlist[i].value-2]>stocks[prefhotel.value-2]:
                    prefhotel=hlist[i]
            if stocks[prefhotel.value-2]>0:
                return prefhotel
            for k in range(7):
                for i in range(len(hlist2)):
                    if hlist2[i].stock<25:
                        hlist2.pop(len(hlist2)-1-i)
                        break
            if len(hlist2)>0:
                r = random.randint(0,len(hlist2)-1)
                return hlist2[r]
            else:
                r = random.randint(0,len(hlist)-1)
                return hlist[r]
            
    class Player_large_hotels:
   
        def __init__(self,g,name1):
            self.money = g
            self.stock_tower=0
            self.stock_continental = 0
            self.stock_american = 0
            self.stock_imperial = 0
            self.stock_festival = 0
            self.stock_sackson = 0 
            self.stock_worldwide = 0
            self.tiles = []
            self.name = name1
            #defense matrix
            self.A1=np.array([[0,0,0,0,0,0,0,4],
                              [0,0,0,0,0,0,50,6],
                              [0,0,0,0,0,50,50,8],
                              [0,0,0,0,50,50,100,10],
                              [0,0,0,50,50,100,100,12],
                              [0,0,50,50,100,100,22,14],
                              [0,50,50,100,100,24,24,16],
                              [0,50,100,100,24,24,15,18]]) #50->buy 1 stock, 100->buy two stocks
        
            #inthehunt matrix
            #row corresponds to deficit-1,coloumn to number of stock available from hotel
            self.A2=np.array([[0,20,100,100,100,20,12,16],
                              [0,0,20,24,24,12,8,13],
                              [0,0,0,20,12,10,8,10]])
        
            #brown coefficients
            self.A3=np.array([0.5,0.5,2,1])
            
            #alpha coefficients
            self.A4=np.array([0.4,0.02])
            
            #hold onto stock matrix
            #first coloumn:turn, second coulumn:stocks of other players, 
            #thrid coloumn:own stock, 4th coloumn:b
            #Attention: the fourth coloumn must be <= the third coloumn
            self.A5=np.array([[30,0,2,2],
                              [30,2,4,4],
                              [50,0,2,2],
                              [50,2,4,4]])
        
            #graph to determine how much money is spent    
            self.A6=np.array([-1/600,35/3])
            
            #matrix which awards points for tile placement; 0:maj in small, 1-4:min small and cash problems
            #5:maj big and enough in small to defend lead, 6: would become maj in big, 
            #7:hotel would be created,8:enlarge majority,9:enlarge minority
            self.A7=np.array([20,2000,10,3000,8,12,15,13,4,2])
            
            #coefficient that determines whether the player spreads his buys
            self.A8=3
            
            #money below which to sell stock, ratio when to go for 2:1 trade
            self.A9=np.array([3000,2.5])
            
            #initial advantage matrix
            self.A10=np.array([10,9,8,5])
        
        def drawtile(self,alltiles):
            a = random.randint(0,len(alltiles)-1)
            tile = alltiles.pop(a)
            #print(tile)
            self.tiles.append(tile)
            #self.add(tile)
            return
        
        #def placetile...remove tile and call global placetile()
        def placetile_player(self, x0):
            for i in range(6):
                #print(i)
                #print("length:",len(self.tiles))
                tile = self.tiles[i]
                if tile[0] == x0[0] and tile[1]==x0[1]:
                    self.tiles.pop(i)
                    break
            #print(x0,"has been placed on the board")
            placetile(x0,self)
            return
        
        
        def decide_placetile(self):
            eligible_tiles = []
            for i in range(6):
                if is_legal(self.tiles[i])==True:
                    eligible_tiles.append(self.tiles[i])
            
            tries=0
            while len(eligible_tiles)==0:
                for i in range(6):
                    #print("# tiles:", len(self.tiles))
                    a = self.tiles.pop(5-i)
                    alltiles.append(a)
                    
                for i in range(6):
                    self.drawtile(alltiles)
                    
                for i in range(6):
                    if is_legal(self.tiles[i])==True:
                        eligible_tiles.append(self.tiles[i])  
                tries+=1
                if tries>=10:
                    return True
            points=[]
            for i in range(len(eligible_tiles)):
                p=0
                tile=eligible_tiles[i]
                info=tile_info(tile)
                infosort=np.sort(tile_info(tile))
                n = 0 #number of non-empty tiles
                for k in range(len(info)):
                    if info[k] !=0:
                        n += 1
                n1=0 #number of single tiles
                for k in range(len(info)):
                    if info[k] ==1:
                        n1 += 1
                #number of hotels surrounding tile
                m = 0
                m1 = []
                for k in range(4):
                    if info[k] > 1:
                        b = True
                        for j in range(len(m1)):
                            if info[k]==m1[j]:
                                b = False
                        m1.append(info[k]) 
                        if b ==True:
                            m+=1
                if m==2:
                    hotel1=eval_hotel(infosort[3])
                    if infosort[3]!=infosort[2]:
                        hotel2=eval_hotel(infosort[2])
                    elif infosort[3]!=infosort[1]:
                        hotel2=eval_hotel(infosort[1])
                    else:
                        hotel2=eval_hotel(infosort[0])
                    if hotel1.size>=hotel2.size:
                        big=hotel1
                        small=hotel2
                    else:
                        big=hotel2
                        small=hotel1
                    maj,minn=majmin(small)
                    majb,minnb=majmin(big)
                    c=0
                    #majority small
                    for j in range(len(maj)):
                        if maj[j].name==self.name:
                            p+=self.A7[0]
                            c=10
                    #minority small and in need of money
                    for j in range(len(minn)):
                        if minn[j].name==self.name and self.money<self.A7[1]:
                            p+=self.A7[2]
                            c=10
                        elif minn[j].name==self.name and self.money<self.A7[3]:
                            p+=self.A7[4]
                            c=10
                    #majority in big and enough stock in small to defend lead
                    for j in range(len(majb)):
                        if majb[j].name==self.name and self.difference_to_maj(big)>-self.difference_to_maj(small)/2:
                            p+=self.A7[5]
                            c=10
                    #if you can become majority of big
                    for j in range(len(minnb)):
                        if -self.difference_to_maj(big)<(self.info_stock(small.value)/2-majb[-1].info_stock(small.value)/2):
                            p+=self.A7[6]
                            c=10
                   
                            
                    
                    
                    p=p-10+c
                if m==3:
                    hotel1=eval_hotel(infosort[3])
                    if infosort[2]!=infosort[3]:
                        hotel2=eval_hotel(infosort[2])
                        if infosort[1]!=infosort[2]:
                            hotel3=eval_hotel(infosort[1])
                        else:
                            hotel3=eval_hotel(infosort[0])
                        
                    else:
                        hotel2=eval_hotel(infosort[1])
                        hotel3=eval_hotel(infosort[0])
                        
                    if hotel1.size>hotel2.size and hotel1.size>hotel3.size:
                        big=hotel1
                        small1=hotel2
                        small2=hotel3
                    elif hotel2.size>hotel1.size and hotel2.size>hotel3.size:
                        big=hotel2
                        small1=hotel1
                        small2=hotel3
                    elif hotel3.size>hotel1.size and hotel3.size>hotel2.size:
                        big=hotel3
                        small1=hotel1
                        small2=hotel2
                    else:
                        big=hotel1
                        small1=hotel2
                        small2=hotel3
                    
                    c=0
                    maj1,minn1=majmin(small1)
                    for j in range(len(maj1)):
                        if maj1[j].name==self.name:
                            p+=self.A7[0]
                            c=10
                    maj2,minn2=majmin(small2)
                    for j in range(len(maj2)):
                        if maj2[j].name==self.name:
                            p+=self.A7[0]
                            c=10
                    majb,minnb=majmin(big)
                    for j in range(len(majb)):
                        if majb[j].name==self.name and (self.difference_to_maj(big)>-self.difference_to_maj(small1)/2 or self.difference_to_maj(big)>-self.difference_to_maj(small2)/2):
                            p+=self.A7[5]
                            c=10
                    for j in range(len(minn1)):
                       if minn1[j].name==self.name and self.money<self.A7[1]:
                           p+=self.A7[2]
                           c=10
                       elif minn1[j].name==self.name and self.money<self.A7[3]:
                           p+=self.A7[4]
                           c=10
                    for j in range(len(minn2)):
                       if minn2[j].name==self.name and self.money<self.A7[1]:
                           p+=self.A7[2]
                           c=10
                       elif minn2[j].name==self.name and self.money<self.A7[3]:
                           p+=self.A7[4]
                           c=10
                    p=p-10+c
                    
                if m==0 and n>0:
                    c=0
                    for j in range(2,9):
                        if eval_hotel(j).size==0 and self.info_stock(j)>0:
                            p+=self.A7[7]
                            c=5
                            break
                    #This is not a mistake!!
                    p=p+5-c
                
                if m==1:
                    adjhotel=eval_hotel(infosort[3])
                    maj,minn=majmin(adjhotel)
                    c=0
                    for j in range(len(maj)):
                        if maj[j].name==self.name:
                            p+=self.A7[8]
                            c=2
                    for j in range(len(minn)):
                        if minn[j].name==self.name:
                            p+=self.A7[9]
                            c=2
                    p=p-2+c
                
                points.append(p)
            
            besttilenumber=0
            for i in range(len(eligible_tiles)-1):
                if points[i+1]>points[besttilenumber]:
                    besttilenumber = i+1
            besttile=eligible_tiles[besttilenumber]
            self.placetile_player(besttile)
            return False
            
      
        def decide_merge_stock(self,big,small):
            n=self.info_stock(small.value)
            m=big.stock
            b=0
            while(self.money<self.A9[0] and n>=1):
                self.sellstock(small.value,1)
                n-=1
            if self.difference_to_maj(big)>=-n/2 and m>=n/2:
                while(m>=1 and n>=2):
                    self.getstock(big.value,1,free=True)
                    self.sellstock(small.value,2,free=True)
                    m-=1
                    n-=2
                    #print(self.name,"has traded 2",small.name,"stocks for 1",big.name,"stock")
            bigprice, useless1,useless2=big.reference()
            smallprice, useless3,useless4=small.reference()
            if bigprice>=self.A9[1]*smallprice:
                while(m>=1 and n>=2):
                    self.getstock(big.value,1,free=True)
                    self.sellstock(small.value,2,free=True)
                    m-=1
                    n-=2
                    #print(self.name,"has traded 2",small.name,"stocks for 1",big.name,"stock")
            stocks=self.other_player_stocks(small)
            b=hold_stock(stocks,n,self.A5)
            self.sellstock(small.value,n-b)
            #print(self.name,"has held on to",b,"stocks and sold",n-b,"stocks")
            
            
        def other_player_stocks(self,hotel):
            stocks=[]
            if self.name !=player1:
                stocks.append(player1.info_stock(hotel.value))
            if self.name !=player2:
                stocks.append(player2.info_stock(hotel.value))
            if self.name !=player3:
                stocks.append(player3.info_stock(hotel.value))
            if self.name !=player4:
                stocks.append(player4.info_stock(hotel.value))
            stocks=np.sort(stocks)
                
            return stocks
        
        def difference_to_maj(self,hotel):
            stocks=self.other_player_stocks(hotel)
            return self.info_stock(hotel.value)-stocks[2]
                
            
        #TODO
        def buy_stock(self):
            
            m1,t1,c1,a1,i1,f1,s1,w1 = player1.info()
            m2,t2,c2,a2,i2,f2,s2,w2 = player2.info()
            m3,t3,c3,a3,i3,f3,s3,w3 = player3.info()
            m4,t4,c4,a4,i4,f4,s4,w4 = player4.info()
            
            w_stock=np.sort([w1,w2,w3,w4])
            s_stock=np.sort([s1,s2,s3,s4])
            f_stock=np.sort([f1,f2,f3,f4])
            i_stock=np.sort([i1,i2,i3,i4])
            a_stock=np.sort([a1,a2,a3,a4])
            c_stock=np.sort([c1,c2,c3,c4])
            t_stock=np.sort([t1,t2,t3,t4])
            
            #Points for each stock and if the player should particularly buy 1 or 2
            w,s,f,i,a,c,t=0,0,0,0,0,0,0
            w1s,w2s,s1s,s2s,f1s,f2s,i1s,i2s,a1s,a2s,c1s,c2s,t1s,t2s=False,False,False,False,False,False,False,False,False,False,False,False,False,False
            
            if worldwide.size>0:
                if w_stock[3]==self.stock_worldwide and w_stock[2]==0:
                    w,w1s,w2s=initial_advantage(w_stock,self.A10)
                elif self.stock_worldwide==w_stock[3]:
                    w,w1s,w2s=defence(w_stock,worldwide,self.A1)
                elif (w_stock[3]-self.stock_worldwide)<=3:
                    w,w1s,w2s=inthehunt(w_stock,self.stock_worldwide,worldwide,self.A2)
                else:
                    w,w1s,w2s=browns(w_stock,self.stock_worldwide,worldwide,self.A1,self.A2,self.A3)
                
                w_alpha=alpha(worldwide,self.tiles,self.A4)
                w*=w_alpha
                
            if sackson.size>0:
                if s_stock[3]==self.stock_sackson and s_stock[2]==0:
                    s,s1s,s2s=initial_advantage(s_stock,self.A10)
                elif self.stock_sackson==s_stock[3]:
                    s,s1s,s2s=defence(s_stock,sackson,self.A1)
                elif (s_stock[3]-self.stock_sackson)<=3:
                    s,s1s,s2s=inthehunt(s_stock,self.stock_sackson,sackson,self.A2)
                else:
                    s,s1s,s2s=browns(s_stock,self.stock_sackson,sackson,self.A1,self.A2,self.A3)
            
            s_alpha=alpha(sackson,self.tiles,self.A4)
            s*=s_alpha
            
            if festival.size>0:
                if f_stock[3]==self.stock_festival and f_stock[2]==0:
                    f,f1s,f2s=initial_advantage(f_stock,self.A10)
                elif self.stock_festival==f_stock[3]:
                    f,f1s,f2s=defence(f_stock,festival,self.A1)
                elif (f_stock[3]-self.stock_festival)<=3:
                    f,f1s,f2s=inthehunt(f_stock,self.stock_festival,festival,self.A2)
                else:
                    f,f1s,f2s=browns(f_stock,self.stock_festival,festival,self.A1,self.A2,self.A3)
                
                f_alpha=alpha(festival,self.tiles,self.A4)
                f*=f_alpha
            
            if imperial.size>0:
                if i_stock[3]==self.stock_imperial and i_stock[2]==0:
                    i,i1s,i2s=initial_advantage(i_stock,self.A10)
                elif self.stock_imperial==i_stock[3]:
                    i,i1s,i2s=defence(i_stock,imperial,self.A1)
                elif (i_stock[3]-self.stock_imperial)<=3:
                    i,i1s,i2s=inthehunt(i_stock,self.stock_imperial,imperial,self.A2)
                else:
                    i,i1s,i2s=browns(i_stock,self.stock_imperial,imperial,self.A1,self.A2,self.A3)
                
                i_alpha=alpha(imperial,self.tiles,self.A4)
                i*=i_alpha
                
            if american.size>0:
                if a_stock[3]==self.stock_american and a_stock[2]==0:
                    a,a1s,a2s=initial_advantage(a_stock,self.A10)
                elif self.stock_american==a_stock[3]:
                    a,a1s,a2s=defence(a_stock,american,self.A1)
                elif (a_stock[3]-self.stock_american)<=3:
                    a,a1s,a2s=inthehunt(a_stock,self.stock_american,american,self.A2)
                else:
                    a,a1s,a2s=browns(a_stock,self.stock_american,american,self.A1,self.A2,self.A3)
                
                a_alpha=alpha(american,self.tiles,self.A4)
                a*=a_alpha
            
            if continental.size>0:
                if c_stock[3]==self.stock_continental and c_stock[2]==0:
                    c,c1s,c2s=initial_advantage(c_stock,self.A10)
                elif self.stock_continental==c_stock[3]:
                    c,c1s,c2s=defence(c_stock,continental,self.A1)
                elif (c_stock[3]-self.stock_continental)<=3:
                    c,c1s,c2s=inthehunt(c_stock,self.stock_continental,continental,self.A2)
                else:
                    c,c1s,c2s=browns(c_stock,self.stock_continental,continental,self.A1,self.A2,self.A3)
                
                c_alpha=alpha(continental,self.tiles,self.A4)
                c*=c_alpha
            
            if tower.size>0:
                if t_stock[3]==self.stock_tower and t_stock[2]==0:
                    t,t1s,t2s=initial_advantage(t_stock,self.A10)
                elif self.stock_tower==t_stock[3]:
                    t,t1s,t2s=defence(t_stock,tower,self.A1)
                elif (t_stock[3]-self.stock_tower)<=3:
                    t,t1s,t2s=inthehunt(t_stock,self.stock_tower,tower,self.A2)
                else:
                    t,t1s,t2s=browns(t_stock,self.stock_tower,tower,self.A1,self.A2,self.A3)
                
                t_alpha=alpha(tower,self.tiles,self.A4)
                t*=t_alpha
            
            points=np.array([w,s,f,i,a,c,t])
            points2=[]
            for i in range(7):
                points2.append(points[i])
            points2=np.sort(points2)
            for i in range(7):
                #achtung bei gleichstand wird das hotel mit dem tieferen value gewählt
                if points[i]==points2[6]:
                    favhotel=eval_hotel(i+2)
            splitt=False        
            if points2[6]-points2[5]<=self.A8 and points2[5]!=0:
                splitt=True
                for i in range(7):
                    #achtung bei gleichstand wird das hotel mit dem tieferen value gewählt
                    if points[i]==points2[5]:
                        favhotel2=eval_hotel(i+2)
                        
                
            
            smallbuys=np.array([[w1s,s1s,f1s,i1s,a1s,c1s,t1s],
                                [w2s,s2s,f2s,i2s,a2s,c2s,t2s]])
            
            p=3
            list1s=[]
            list2s=[]
            for i in range(2,9):
                if smallbuys[0,i-2]==True:
                    list1s.append(eval_hotel(i))
                if smallbuys[1,i-2]==True:
                    list2s.append(eval_hotel(i))
                    
            a=len(list1s)
            b=len(list2s)
            if a+2*b<=3:
                for i in range(len(list1s)):
                    buy_hotel = list1s[i]
                    price,useless, useless2 = buy_hotel.reference()
                    if self.money>=price and buy_hotel.stock>=1:
                        self.getstock(buy_hotel.value,1)
                        p-=1
                        #print(self.name,"has purchased",1,"stock from",buy_hotel.name)
                for i in range(len(list2s)):
                    buy_hotel = list2s[i]
                    price,useless, useless2 = buy_hotel.reference()
                    if self.money>=price*2 and buy_hotel.stock>=2:
                        self.getstock(buy_hotel.value,2)
                        p-=2
                        #print(self.name,"has purchased",2,"stocks from",buy_hotel.name)
            elif a+2*b>3:
                list3=list1s+list2s
                list4=[]
                for i in range(len(list3)):
                    list4.append(points[list3[i].value-2])
                list4.sort()
                for k in range(3):
                    n1 = len(list4)
                    l = 0
                    for i in range(n1): 
                        if points[list3[l].value-2]==list4[-1]:
                            buy_hotel=list3[l]
                            price,useless, useless2 = buy_hotel.reference()
                            if smallbuys[0,buy_hotel.value-2]==True:
                                n=1
                            else:
                                n=2
                            if self.money>=price*n and p>=n and buy_hotel.stock>=n:
                                self.getstock(buy_hotel.value,n)
                                p-=n
                                #print(self.name,"has purchased",n,"stocks from",buy_hotel.name)
                                list3.pop(l)
                                l-=1
                                list4.pop(-1)
                        l+=1 
    
            if points[favhotel.value-2]>=self.A6[0]*self.money+self.A6[1] and points[favhotel.value-2]!=0:
                if splitt==True:
                    price,useless, useless2 = favhotel.reference()
                    if self.money>=price*2 and p>=2 and favhotel.stock>=2:
                        self.getstock(favhotel.value,2)
                        p-=2
                        #print(self.name,"has purchased",2,"stocks from",favhotel.name)
                    price2,useless3, useless4 = favhotel.reference()
                    if self.money>=price2*1 and p>=1 and favhotel2.stock>=1:
                        self.getstock(favhotel2.value,1)
                        p-=1
                        #print(self.name,"has purchased",1,"stock from",favhotel2.name)
                elif splitt==False:
                    price,useless, useless2 = favhotel.reference()
                    if self.money>=price*p and favhotel.stock>=p:
                        self.getstock(favhotel.value,p)
                        #print(self.name,"has purchased",p,"stocks from",favhotel.name)
            
            
                
        def set_money(self,cash):
            self.money += cash
            
            
        def info(self):
            return self.money, self.stock_tower, self.stock_continental, self.stock_american, self.stock_imperial, self.stock_festival, self.stock_sackson ,self.stock_worldwide
            
        def info_stock(self,value):
            if value == tower.value:
                return self.stock_tower
            elif value == continental.value:
                return self.stock_continental
            elif value == american.value:
                return self.stock_american
            elif value == imperial.value:
                return self.stock_imperial
            elif value == festival.value:
                return self.stock_festival
            elif value == sackson.value:
                return self.stock_sackson
            elif value == worldwide.value:
                return self.stock_worldwide
            
        def sellstock(self,value,n,free=False):
            price,useless, useless2 = eval_hotel(value).reference()
            if free==False:
                self.set_money(n*price)
            if value == tower.value:
                self.stock_tower -= n
                tower.recstock(n)
            elif value == continental.value:
                self.stock_continental -= n
                continental.recstock(n)
            elif value == american.value:
                self.stock_american -= n
                american.recstock(n)
            elif value == imperial.value:
                self.stock_imperial -= n
                imperial.recstock(n)
            elif value == festival.value:
                self.stock_festival -= n
                festival.recstock(n)
            elif value == sackson.value:
                self.stock_sackson -= n
                sackson.recstock(n)
            elif value == worldwide.value:
                self.stock_worldwide -= n
                worldwide.recstock(n)
        
        def getstock(self,value,n,free=False):
            price,useless, useless2 = eval_hotel(value).reference()
            if free==False:
                self.set_money(-n*price)
            if value == tower.value:
               self.stock_tower += n
               tower.sellstock(n)
            elif value == continental.value:
               self.stock_continental += n
               continental.sellstock(n)
            elif value == american.value:
               self.stock_american += n
               american.sellstock(n)
            elif value == imperial.value:
               self.stock_imperial += n
               imperial.sellstock(n)
            elif value == festival.value:
               self.stock_festival += n
               festival.sellstock(n)
            elif value == sackson.value:
               self.stock_sackson += n
               sackson.sellstock(n)
            elif value == worldwide.value:
               self.stock_worldwide += n
               worldwide.sellstock(n)
         
        #decide...stupid 
        def decide_merge(self,hotel1,hotel2):
            m1,t1,c1,a1,i1,f1,s1,w1=self.info()
            hilfsarray=np.array([w1,s1,f1,i1,a1,c1,t1])
    
            maj1,minn1 = majmin(hotel1)
            maj2,minn2 = majmin(hotel2)
            M1=False
            m1=False
            M2=False
            m2=False
            for i in range(len(maj1)):
                if maj1[i].name==self.name:
                    M1=True
            for i in range(len(minn1)):
                if minn1[i].name==self.name:
                    m1=True
            for i in range(len(maj2)):
                if maj2[i].name==self.name:
                    M2=True
            for i in range(len(minn2)):
                if minn2[i].name==self.name:
                    m2=True
            
            if M1==True and M2==False:
                if np.abs(hilfsarray[hotel1.value-2]-hotel1.stock)<=5 and hilfsarray[hotel1.value-2]>=5 and self.money>=3000:
                    return hotel1,hotel2
                else: 
                    return hotel2,hotel1
            elif M2==True and M1==False:
                if np.abs(hilfsarray[hotel2.value-2]-hotel2.stock)<=5 and hilfsarray[hotel2.value-2]>=5 and self.money>=3000:
                    return hotel2,hotel1
                else: 
                    return hotel1,hotel2
                
            elif M1==True and M2 == True:
                if self.difference_to_maj(hotel1)>=self.difference_to_maj(hotel2):
                    return hotel1,hotel2
                else:
                    return hotel2,hotel1
                
            elif m1==True and m2==False:
                if np.abs(hilfsarray[hotel1.value-2]-hotel1.stock)<=5 and hilfsarray[hotel1.value-2]>=5 and self.money>=3000:
                    return hotel1,hotel2
                else: 
                    return hotel2,hotel1
            elif m2==True and m1==False:
                if np.abs(hilfsarray[hotel2.value-2]-hotel2.stock)<=5 and hilfsarray[hotel2.value-2]>=5 and self.money>=3000:
                    return hotel2,hotel1
                else: 
                    return hotel1,hotel2
           
            elif m1==True and m2 == True:
                if self.difference_to_maj(hotel1)<=self.info_stock(hotel1.value)/2:
                    return hotel1,hotel2
                elif self.difference_to_maj(hotel2)<=self.info_stock(hotel1.value)/2:
                    return hotel2,hotel1
                elif self.money>=3000 and hilfsarray[hotel1.value-2]>=hilfsarray[hotel2.value-2]:
                    return hotel1,hotel2
                elif self.money>=3000 and hilfsarray[hotel1.value-2]<hilfsarray[hotel2.value-2]:
                    return hotel2,hotel1
                elif self.money<3000 and hilfsarray[hotel1.value-2]>=hilfsarray[hotel2.value-2]:
                    return hotel2,hotel1
                elif self.money>=3000 and hilfsarray[hotel1.value-2]<hilfsarray[hotel2.value-2]:
                    return hotel1,hotel2
            else:
                if hilfsarray[hotel1.value-2]>=hilfsarray[hotel2.value-2]:
                    return hotel1,hotel2
                else:
                    return hotel2,hotel1
            
        
        def decide_triple_merge(self,hotel1,hotel2,hotel3):
            big,small=self.decide_merge(hotel1,hotel2)
            a,b = self.decide_merge(big,hotel3)
            return a,b,small
        
        def decide_double_merge(self,hotel1,hotel2):
            return self.decide_merge(hotel1,hotel2)
        
        def decide_quad_merge(self,hotel1,hotel2,hotel3,hotel4):
            big,small1,small2=self.decide_triple_merge(hotel1,hotel2,hotel3)
            a,b = self.decide_merge(big,hotel4)
            return a,b,small1,small2
        
        def decide_newhotel(self):
            m1,t1,c1,a1,i1,f1,s1,w1 = self.info()
            stocks=np.array([w1,s1,f1,i1,a1,c1,t1])
            hlist=[]
            hlist2=[]
            for i in range(2,9):
                if eval_hotel(i).size==0:
                    hlist.append(eval_hotel(i))
                    hlist2.append(eval_hotel(i))
            prefhotel=hlist[0]
            for i in range(len(hlist)):
                if stocks[hlist[i].value-2]>stocks[prefhotel.value-2]:
                    prefhotel=hlist[i]
            if stocks[prefhotel.value-2]>0:
                return prefhotel
            for k in range(7):
                for i in range(len(hlist2)):
                    if hlist2[i].stock<25:
                        hlist2.pop(len(hlist2)-1-i)
                        break
            if len(hlist2)>0:
                r = random.randint(0,len(hlist2)-1)
                return hlist2[r]
            else:
                r = random.randint(0,len(hlist)-1)
                return hlist[r]
            
    
    class Player_small_hotels:
   
        def __init__(self,g,name1):
            self.money = g
            self.stock_tower=0
            self.stock_continental = 0
            self.stock_american = 0
            self.stock_imperial = 0
            self.stock_festival = 0
            self.stock_sackson = 0 
            self.stock_worldwide = 0
            self.tiles = []
            self.name = name1
            #defense matrix
            self.A1=np.array([[0,0,0,0,0,0,0,4],
                              [0,0,0,0,0,0,50,6],
                              [0,0,0,0,0,50,50,8],
                              [0,0,0,0,50,50,100,10],
                              [0,0,0,50,50,100,100,12],
                              [0,0,50,50,100,100,22,14],
                              [0,50,50,100,100,24,24,16],
                              [0,50,100,100,24,24,15,18]]) #50->buy 1 stock, 100->buy two stocks
        
            #inthehunt matrix
            #row corresponds to deficit-1,coloumn to number of stock available from hotel
            self.A2=np.array([[0,20,100,100,100,20,12,16],
                              [0,0,20,24,24,12,8,13],
                              [0,0,0,20,12,10,8,10]])
        
            #brown coefficients
            self.A3=np.array([0.5,0.5,2,1])
            
            #alpha coefficients
            self.A4=np.array([-0.15,0.02])
            
            #hold onto stock matrix
            #first coloumn:turn, second coulumn:stocks of other players, 
            #thrid coloumn:own stock, 4th coloumn:b
            #Attention: the fourth coloumn must be <= the third coloumn
            self.A5=np.array([[30,0,2,2],
                              [30,2,4,4],
                              [50,0,2,2],
                              [50,2,4,4]])
        
            #graph to determine how much money is spent    
            self.A6=np.array([-1/600,35/3])
            
            #matrix which awards points for tile placement; 0:maj in small, 1-4:min small and cash problems
            #5:maj big and enough in small to defend lead, 6: would become maj in big, 
            #7:hotel would be created,8:enlarge majority,9:enlarge minority
            self.A7=np.array([20,2000,10,3000,8,12,15,13,4,2])
            
            #coefficient that determines whether the player spreads his buys
            self.A8=3
            
            #money below which to sell stock, ratio when to go for 2:1 trade
            self.A9=np.array([3000,2.5])
            
            #initial advantage matrix
            self.A10=np.array([10,9,8,5])
        
        def drawtile(self,alltiles):
            a = random.randint(0,len(alltiles)-1)
            tile = alltiles.pop(a)
            #print(tile)
            self.tiles.append(tile)
            #self.add(tile)
            return
        
        #def placetile...remove tile and call global placetile()
        def placetile_player(self, x0):
            for i in range(6):
                #print(i)
                #print("length:",len(self.tiles))
                tile = self.tiles[i]
                if tile[0] == x0[0] and tile[1]==x0[1]:
                    self.tiles.pop(i)
                    break
            #print(x0,"has been placed on the board")
            placetile(x0,self)
            return
        
        
        def decide_placetile(self):
            eligible_tiles = []
            for i in range(6):
                if is_legal(self.tiles[i])==True:
                    eligible_tiles.append(self.tiles[i])
            
            tries=0
            while len(eligible_tiles)==0:
                for i in range(6):
                    #print("# tiles:", len(self.tiles))
                    a = self.tiles.pop(5-i)
                    alltiles.append(a)
                    
                for i in range(6):
                    self.drawtile(alltiles)
                    
                for i in range(6):
                    if is_legal(self.tiles[i])==True:
                        eligible_tiles.append(self.tiles[i])  
                tries+=1
                if tries>=10:
                    return True
            points=[]
            for i in range(len(eligible_tiles)):
                p=0
                tile=eligible_tiles[i]
                info=tile_info(tile)
                infosort=np.sort(tile_info(tile))
                n = 0 #number of non-empty tiles
                for k in range(len(info)):
                    if info[k] !=0:
                        n += 1
                n1=0 #number of single tiles
                for k in range(len(info)):
                    if info[k] ==1:
                        n1 += 1
                #number of hotels surrounding tile
                m = 0
                m1 = []
                for k in range(4):
                    if info[k] > 1:
                        b = True
                        for j in range(len(m1)):
                            if info[k]==m1[j]:
                                b = False
                        m1.append(info[k]) 
                        if b ==True:
                            m+=1
                if m==2:
                    hotel1=eval_hotel(infosort[3])
                    if infosort[3]!=infosort[2]:
                        hotel2=eval_hotel(infosort[2])
                    elif infosort[3]!=infosort[1]:
                        hotel2=eval_hotel(infosort[1])
                    else:
                        hotel2=eval_hotel(infosort[0])
                    if hotel1.size>=hotel2.size:
                        big=hotel1
                        small=hotel2
                    else:
                        big=hotel2
                        small=hotel1
                    maj,minn=majmin(small)
                    majb,minnb=majmin(big)
                    c=0
                    #majority small
                    for j in range(len(maj)):
                        if maj[j].name==self.name:
                            p+=self.A7[0]
                            c=10
                    #minority small and in need of money
                    for j in range(len(minn)):
                        if minn[j].name==self.name and self.money<self.A7[1]:
                            p+=self.A7[2]
                            c=10
                        elif minn[j].name==self.name and self.money<self.A7[3]:
                            p+=self.A7[4]
                            c=10
                    #majority in big and enough stock in small to defend lead
                    for j in range(len(majb)):
                        if majb[j].name==self.name and self.difference_to_maj(big)>-self.difference_to_maj(small)/2:
                            p+=self.A7[5]
                            c=10
                    #if you can become majority of big
                    for j in range(len(minnb)):
                        if -self.difference_to_maj(big)<(self.info_stock(small.value)/2-majb[-1].info_stock(small.value)/2):
                            p+=self.A7[6]
                            c=10
                   
                            
                    
                    
                    p=p-10+c
                if m==3:
                    hotel1=eval_hotel(infosort[3])
                    if infosort[2]!=infosort[3]:
                        hotel2=eval_hotel(infosort[2])
                        if infosort[1]!=infosort[2]:
                            hotel3=eval_hotel(infosort[1])
                        else:
                            hotel3=eval_hotel(infosort[0])
                        
                    else:
                        hotel2=eval_hotel(infosort[1])
                        hotel3=eval_hotel(infosort[0])
                        
                    if hotel1.size>hotel2.size and hotel1.size>hotel3.size:
                        big=hotel1
                        small1=hotel2
                        small2=hotel3
                    elif hotel2.size>hotel1.size and hotel2.size>hotel3.size:
                        big=hotel2
                        small1=hotel1
                        small2=hotel3
                    elif hotel3.size>hotel1.size and hotel3.size>hotel2.size:
                        big=hotel3
                        small1=hotel1
                        small2=hotel2
                    else:
                        big=hotel1
                        small1=hotel2
                        small2=hotel3
                    
                    c=0
                    maj1,minn1=majmin(small1)
                    for j in range(len(maj1)):
                        if maj1[j].name==self.name:
                            p+=self.A7[0]
                            c=10
                    maj2,minn2=majmin(small2)
                    for j in range(len(maj2)):
                        if maj2[j].name==self.name:
                            p+=self.A7[0]
                            c=10
                    majb,minnb=majmin(big)
                    for j in range(len(majb)):
                        if majb[j].name==self.name and (self.difference_to_maj(big)>-self.difference_to_maj(small1)/2 or self.difference_to_maj(big)>-self.difference_to_maj(small2)/2):
                            p+=self.A7[5]
                            c=10
                    for j in range(len(minn1)):
                       if minn1[j].name==self.name and self.money<self.A7[1]:
                           p+=self.A7[2]
                           c=10
                       elif minn1[j].name==self.name and self.money<self.A7[3]:
                           p+=self.A7[4]
                           c=10
                    for j in range(len(minn2)):
                       if minn2[j].name==self.name and self.money<self.A7[1]:
                           p+=self.A7[2]
                           c=10
                       elif minn2[j].name==self.name and self.money<self.A7[3]:
                           p+=self.A7[4]
                           c=10
                    p=p-10+c
                    
                if m==0 and n>0:
                    c=0
                    for j in range(2,9):
                        if eval_hotel(j).size==0 and self.info_stock(j)>0:
                            p+=self.A7[7]
                            c=5
                            break
                    #This is not a mistake!!
                    p=p+5-c
                
                if m==1:
                    adjhotel=eval_hotel(infosort[3])
                    maj,minn=majmin(adjhotel)
                    c=0
                    for j in range(len(maj)):
                        if maj[j].name==self.name:
                            p+=self.A7[8]
                            c=2
                    for j in range(len(minn)):
                        if minn[j].name==self.name:
                            p+=self.A7[9]
                            c=2
                    p=p-2+c
                
                points.append(p)
            
            besttilenumber=0
            for i in range(len(eligible_tiles)-1):
                if points[i+1]>points[besttilenumber]:
                    besttilenumber = i+1
            besttile=eligible_tiles[besttilenumber]
            self.placetile_player(besttile)
            return False
            
      
        def decide_merge_stock(self,big,small):
            n=self.info_stock(small.value)
            m=big.stock
            b=0
            while(self.money<self.A9[0] and n>=1):
                self.sellstock(small.value,1)
                n-=1
            if self.difference_to_maj(big)>=-n/2 and m>=n/2:
                while(m>=1 and n>=2):
                    self.getstock(big.value,1,free=True)
                    self.sellstock(small.value,2,free=True)
                    m-=1
                    n-=2
                    #print(self.name,"has traded 2",small.name,"stocks for 1",big.name,"stock")
            bigprice, useless1,useless2=big.reference()
            smallprice, useless3,useless4=small.reference()
            if bigprice>=self.A9[1]*smallprice:
                while(m>=1 and n>=2):
                    self.getstock(big.value,1,free=True)
                    self.sellstock(small.value,2,free=True)
                    m-=1
                    n-=2
                    #print(self.name,"has traded 2",small.name,"stocks for 1",big.name,"stock")
            stocks=self.other_player_stocks(small)
            b=hold_stock(stocks,n,self.A5)
            self.sellstock(small.value,n-b)
            #print(self.name,"has held on to",b,"stocks and sold",n-b,"stocks")
            
            
        def other_player_stocks(self,hotel):
            stocks=[]
            if self.name !=player1:
                stocks.append(player1.info_stock(hotel.value))
            if self.name !=player2:
                stocks.append(player2.info_stock(hotel.value))
            if self.name !=player3:
                stocks.append(player3.info_stock(hotel.value))
            if self.name !=player4:
                stocks.append(player4.info_stock(hotel.value))
            stocks=np.sort(stocks)
                
            return stocks
        
        def difference_to_maj(self,hotel):
            stocks=self.other_player_stocks(hotel)
            return self.info_stock(hotel.value)-stocks[2]
                
            
        #TODO
        def buy_stock(self):
            
            m1,t1,c1,a1,i1,f1,s1,w1 = player1.info()
            m2,t2,c2,a2,i2,f2,s2,w2 = player2.info()
            m3,t3,c3,a3,i3,f3,s3,w3 = player3.info()
            m4,t4,c4,a4,i4,f4,s4,w4 = player4.info()
            
            w_stock=np.sort([w1,w2,w3,w4])
            s_stock=np.sort([s1,s2,s3,s4])
            f_stock=np.sort([f1,f2,f3,f4])
            i_stock=np.sort([i1,i2,i3,i4])
            a_stock=np.sort([a1,a2,a3,a4])
            c_stock=np.sort([c1,c2,c3,c4])
            t_stock=np.sort([t1,t2,t3,t4])
            
            #Points for each stock and if the player should particularly buy 1 or 2
            w,s,f,i,a,c,t=0,0,0,0,0,0,0
            w1s,w2s,s1s,s2s,f1s,f2s,i1s,i2s,a1s,a2s,c1s,c2s,t1s,t2s=False,False,False,False,False,False,False,False,False,False,False,False,False,False
            
            if worldwide.size>0:
                if w_stock[3]==self.stock_worldwide and w_stock[2]==0:
                    w,w1s,w2s=initial_advantage(w_stock,self.A10)
                elif self.stock_worldwide==w_stock[3]:
                    w,w1s,w2s=defence(w_stock,worldwide,self.A1)
                elif (w_stock[3]-self.stock_worldwide)<=3:
                    w,w1s,w2s=inthehunt(w_stock,self.stock_worldwide,worldwide,self.A2)
                else:
                    w,w1s,w2s=browns(w_stock,self.stock_worldwide,worldwide,self.A1,self.A2,self.A3)
                
                w_alpha=alpha(worldwide,self.tiles,self.A4)
                w*=w_alpha
                
            if sackson.size>0:
                if s_stock[3]==self.stock_sackson and s_stock[2]==0:
                    s,s1s,s2s=initial_advantage(s_stock,self.A10)
                elif self.stock_sackson==s_stock[3]:
                    s,s1s,s2s=defence(s_stock,sackson,self.A1)
                elif (s_stock[3]-self.stock_sackson)<=3:
                    s,s1s,s2s=inthehunt(s_stock,self.stock_sackson,sackson,self.A2)
                else:
                    s,s1s,s2s=browns(s_stock,self.stock_sackson,sackson,self.A1,self.A2,self.A3)
            
            s_alpha=alpha(sackson,self.tiles,self.A4)
            s*=s_alpha
            
            if festival.size>0:
                if f_stock[3]==self.stock_festival and f_stock[2]==0:
                    f,f1s,f2s=initial_advantage(f_stock,self.A10)
                elif self.stock_festival==f_stock[3]:
                    f,f1s,f2s=defence(f_stock,festival,self.A1)
                elif (f_stock[3]-self.stock_festival)<=3:
                    f,f1s,f2s=inthehunt(f_stock,self.stock_festival,festival,self.A2)
                else:
                    f,f1s,f2s=browns(f_stock,self.stock_festival,festival,self.A1,self.A2,self.A3)
                
                f_alpha=alpha(festival,self.tiles,self.A4)
                f*=f_alpha
            
            if imperial.size>0:
                if i_stock[3]==self.stock_imperial and i_stock[2]==0:
                    i,i1s,i2s=initial_advantage(i_stock,self.A10)
                elif self.stock_imperial==i_stock[3]:
                    i,i1s,i2s=defence(i_stock,imperial,self.A1)
                elif (i_stock[3]-self.stock_imperial)<=3:
                    i,i1s,i2s=inthehunt(i_stock,self.stock_imperial,imperial,self.A2)
                else:
                    i,i1s,i2s=browns(i_stock,self.stock_imperial,imperial,self.A1,self.A2,self.A3)
                
                i_alpha=alpha(imperial,self.tiles,self.A4)
                i*=i_alpha
                
            if american.size>0:
                if a_stock[3]==self.stock_american and a_stock[2]==0:
                    a,a1s,a2s=initial_advantage(a_stock,self.A10)
                elif self.stock_american==a_stock[3]:
                    a,a1s,a2s=defence(a_stock,american,self.A1)
                elif (a_stock[3]-self.stock_american)<=3:
                    a,a1s,a2s=inthehunt(a_stock,self.stock_american,american,self.A2)
                else:
                    a,a1s,a2s=browns(a_stock,self.stock_american,american,self.A1,self.A2,self.A3)
                
                a_alpha=alpha(american,self.tiles,self.A4)
                a*=a_alpha
            
            if continental.size>0:
                if c_stock[3]==self.stock_continental and c_stock[2]==0:
                    c,c1s,c2s=initial_advantage(c_stock,self.A10)
                elif self.stock_continental==c_stock[3]:
                    c,c1s,c2s=defence(c_stock,continental,self.A1)
                elif (c_stock[3]-self.stock_continental)<=3:
                    c,c1s,c2s=inthehunt(c_stock,self.stock_continental,continental,self.A2)
                else:
                    c,c1s,c2s=browns(c_stock,self.stock_continental,continental,self.A1,self.A2,self.A3)
                
                c_alpha=alpha(continental,self.tiles,self.A4)
                c*=c_alpha
            
            if tower.size>0:
                if t_stock[3]==self.stock_tower and t_stock[2]==0:
                    t,t1s,t2s=initial_advantage(t_stock,self.A10)
                elif self.stock_tower==t_stock[3]:
                    t,t1s,t2s=defence(t_stock,tower,self.A1)
                elif (t_stock[3]-self.stock_tower)<=3:
                    t,t1s,t2s=inthehunt(t_stock,self.stock_tower,tower,self.A2)
                else:
                    t,t1s,t2s=browns(t_stock,self.stock_tower,tower,self.A1,self.A2,self.A3)
                
                t_alpha=alpha(tower,self.tiles,self.A4)
                t*=t_alpha
            
            points=np.array([w,s,f,i,a,c,t])
            points2=[]
            for i in range(7):
                points2.append(points[i])
            points2=np.sort(points2)
            for i in range(7):
                #achtung bei gleichstand wird das hotel mit dem tieferen value gewählt
                if points[i]==points2[6]:
                    favhotel=eval_hotel(i+2)
            splitt=False        
            if points2[6]-points2[5]<=self.A8 and points2[5]!=0:
                splitt=True
                for i in range(7):
                    #achtung bei gleichstand wird das hotel mit dem tieferen value gewählt
                    if points[i]==points2[5]:
                        favhotel2=eval_hotel(i+2)
                        
                
            
            smallbuys=np.array([[w1s,s1s,f1s,i1s,a1s,c1s,t1s],
                                [w2s,s2s,f2s,i2s,a2s,c2s,t2s]])
            
            p=3
            list1s=[]
            list2s=[]
            for i in range(2,9):
                if smallbuys[0,i-2]==True:
                    list1s.append(eval_hotel(i))
                if smallbuys[1,i-2]==True:
                    list2s.append(eval_hotel(i))
                    
            a=len(list1s)
            b=len(list2s)
            if a+2*b<=3:
                for i in range(len(list1s)):
                    buy_hotel = list1s[i]
                    price,useless, useless2 = buy_hotel.reference()
                    if self.money>=price and buy_hotel.stock>=1:
                        self.getstock(buy_hotel.value,1)
                        p-=1
                        #print(self.name,"has purchased",1,"stock from",buy_hotel.name)
                for i in range(len(list2s)):
                    buy_hotel = list2s[i]
                    price,useless, useless2 = buy_hotel.reference()
                    if self.money>=price*2 and buy_hotel.stock>=2:
                        self.getstock(buy_hotel.value,2)
                        p-=2
                        #print(self.name,"has purchased",2,"stocks from",buy_hotel.name)
            elif a+2*b>3:
                list3=list1s+list2s
                list4=[]
                for i in range(len(list3)):
                    list4.append(points[list3[i].value-2])
                list4.sort()
                for k in range(3):
                    n1 = len(list4)
                    l = 0
                    for i in range(n1): 
                        if points[list3[l].value-2]==list4[-1]:
                            buy_hotel=list3[l]
                            price,useless, useless2 = buy_hotel.reference()
                            if smallbuys[0,buy_hotel.value-2]==True:
                                n=1
                            else:
                                n=2
                            if self.money>=price*n and p>=n and buy_hotel.stock>=n:
                                self.getstock(buy_hotel.value,n)
                                p-=n
                                #print(self.name,"has purchased",n,"stocks from",buy_hotel.name)
                                list3.pop(l)
                                l-=1
                                list4.pop(-1)
                        l+=1 
    
            if points[favhotel.value-2]>=self.A6[0]*self.money+self.A6[1] and points[favhotel.value-2]!=0:
                if splitt==True:
                    price,useless, useless2 = favhotel.reference()
                    if self.money>=price*2 and p>=2 and favhotel.stock>=2:
                        self.getstock(favhotel.value,2)
                        p-=2
                        #print(self.name,"has purchased",2,"stocks from",favhotel.name)
                    price2,useless3, useless4 = favhotel.reference()
                    if self.money>=price2*1 and p>=1 and favhotel2.stock>=1:
                        self.getstock(favhotel2.value,1)
                        p-=1
                        #print(self.name,"has purchased",1,"stock from",favhotel2.name)
                elif splitt==False:
                    price,useless, useless2 = favhotel.reference()
                    if self.money>=price*p and favhotel.stock>=p:
                        self.getstock(favhotel.value,p)
                        #print(self.name,"has purchased",p,"stocks from",favhotel.name)
            
            
                
        def set_money(self,cash):
            self.money += cash
            
            
        def info(self):
            return self.money, self.stock_tower, self.stock_continental, self.stock_american, self.stock_imperial, self.stock_festival, self.stock_sackson ,self.stock_worldwide
            
        def info_stock(self,value):
            if value == tower.value:
                return self.stock_tower
            elif value == continental.value:
                return self.stock_continental
            elif value == american.value:
                return self.stock_american
            elif value == imperial.value:
                return self.stock_imperial
            elif value == festival.value:
                return self.stock_festival
            elif value == sackson.value:
                return self.stock_sackson
            elif value == worldwide.value:
                return self.stock_worldwide
            
        def sellstock(self,value,n,free=False):
            price,useless, useless2 = eval_hotel(value).reference()
            if free==False:
                self.set_money(n*price)
            if value == tower.value:
                self.stock_tower -= n
                tower.recstock(n)
            elif value == continental.value:
                self.stock_continental -= n
                continental.recstock(n)
            elif value == american.value:
                self.stock_american -= n
                american.recstock(n)
            elif value == imperial.value:
                self.stock_imperial -= n
                imperial.recstock(n)
            elif value == festival.value:
                self.stock_festival -= n
                festival.recstock(n)
            elif value == sackson.value:
                self.stock_sackson -= n
                sackson.recstock(n)
            elif value == worldwide.value:
                self.stock_worldwide -= n
                worldwide.recstock(n)
        
        def getstock(self,value,n,free=False):
            price,useless, useless2 = eval_hotel(value).reference()
            if free==False:
                self.set_money(-n*price)
            if value == tower.value:
               self.stock_tower += n
               tower.sellstock(n)
            elif value == continental.value:
               self.stock_continental += n
               continental.sellstock(n)
            elif value == american.value:
               self.stock_american += n
               american.sellstock(n)
            elif value == imperial.value:
               self.stock_imperial += n
               imperial.sellstock(n)
            elif value == festival.value:
               self.stock_festival += n
               festival.sellstock(n)
            elif value == sackson.value:
               self.stock_sackson += n
               sackson.sellstock(n)
            elif value == worldwide.value:
               self.stock_worldwide += n
               worldwide.sellstock(n)
         
        #decide...stupid 
        def decide_merge(self,hotel1,hotel2):
            m1,t1,c1,a1,i1,f1,s1,w1=self.info()
            hilfsarray=np.array([w1,s1,f1,i1,a1,c1,t1])
    
            maj1,minn1 = majmin(hotel1)
            maj2,minn2 = majmin(hotel2)
            M1=False
            m1=False
            M2=False
            m2=False
            for i in range(len(maj1)):
                if maj1[i].name==self.name:
                    M1=True
            for i in range(len(minn1)):
                if minn1[i].name==self.name:
                    m1=True
            for i in range(len(maj2)):
                if maj2[i].name==self.name:
                    M2=True
            for i in range(len(minn2)):
                if minn2[i].name==self.name:
                    m2=True
            
            if M1==True and M2==False:
                if np.abs(hilfsarray[hotel1.value-2]-hotel1.stock)<=5 and hilfsarray[hotel1.value-2]>=5 and self.money>=3000:
                    return hotel1,hotel2
                else: 
                    return hotel2,hotel1
            elif M2==True and M1==False:
                if np.abs(hilfsarray[hotel2.value-2]-hotel2.stock)<=5 and hilfsarray[hotel2.value-2]>=5 and self.money>=3000:
                    return hotel2,hotel1
                else: 
                    return hotel1,hotel2
                
            elif M1==True and M2 == True:
                if self.difference_to_maj(hotel1)>=self.difference_to_maj(hotel2):
                    return hotel1,hotel2
                else:
                    return hotel2,hotel1
                
            elif m1==True and m2==False:
                if np.abs(hilfsarray[hotel1.value-2]-hotel1.stock)<=5 and hilfsarray[hotel1.value-2]>=5 and self.money>=3000:
                    return hotel1,hotel2
                else: 
                    return hotel2,hotel1
            elif m2==True and m1==False:
                if np.abs(hilfsarray[hotel2.value-2]-hotel2.stock)<=5 and hilfsarray[hotel2.value-2]>=5 and self.money>=3000:
                    return hotel2,hotel1
                else: 
                    return hotel1,hotel2
           
            elif m1==True and m2 == True:
                if self.difference_to_maj(hotel1)<=self.info_stock(hotel1.value)/2:
                    return hotel1,hotel2
                elif self.difference_to_maj(hotel2)<=self.info_stock(hotel1.value)/2:
                    return hotel2,hotel1
                elif self.money>=3000 and hilfsarray[hotel1.value-2]>=hilfsarray[hotel2.value-2]:
                    return hotel1,hotel2
                elif self.money>=3000 and hilfsarray[hotel1.value-2]<hilfsarray[hotel2.value-2]:
                    return hotel2,hotel1
                elif self.money<3000 and hilfsarray[hotel1.value-2]>=hilfsarray[hotel2.value-2]:
                    return hotel2,hotel1
                elif self.money>=3000 and hilfsarray[hotel1.value-2]<hilfsarray[hotel2.value-2]:
                    return hotel1,hotel2
            else:
                if hilfsarray[hotel1.value-2]>=hilfsarray[hotel2.value-2]:
                    return hotel1,hotel2
                else:
                    return hotel2,hotel1
            
        
        def decide_triple_merge(self,hotel1,hotel2,hotel3):
            big,small=self.decide_merge(hotel1,hotel2)
            a,b = self.decide_merge(big,hotel3)
            return a,b,small
        
        def decide_double_merge(self,hotel1,hotel2):
            return self.decide_merge(hotel1,hotel2)
        
        def decide_quad_merge(self,hotel1,hotel2,hotel3,hotel4):
            big,small1,small2=self.decide_triple_merge(hotel1,hotel2,hotel3)
            a,b = self.decide_merge(big,hotel4)
            return a,b,small1,small2
        
        def decide_newhotel(self):
            m1,t1,c1,a1,i1,f1,s1,w1 = self.info()
            stocks=np.array([w1,s1,f1,i1,a1,c1,t1])
            hlist=[]
            hlist2=[]
            for i in range(2,9):
                if eval_hotel(i).size==0:
                    hlist.append(eval_hotel(i))
                    hlist2.append(eval_hotel(i))
            prefhotel=hlist[0]
            for i in range(len(hlist)):
                if stocks[hlist[i].value-2]>stocks[prefhotel.value-2]:
                    prefhotel=hlist[i]
            if stocks[prefhotel.value-2]>0:
                return prefhotel
            for k in range(7):
                for i in range(len(hlist2)):
                    if hlist2[i].stock<25:
                        hlist2.pop(len(hlist2)-1-i)
                        break
            if len(hlist2)>0:
                r = random.randint(0,len(hlist2)-1)
                return hlist2[r]
            else:
                r = random.randint(0,len(hlist)-1)
                return hlist[r]
            
    class Player_adapt:
   
        def __init__(self,g,name1):
            self.money = g
            self.stock_tower=0
            self.stock_continental = 0
            self.stock_american = 0
            self.stock_imperial = 0
            self.stock_festival = 0
            self.stock_sackson = 0 
            self.stock_worldwide = 0
            self.tiles = []
            self.name = name1
            
            var=np.array([0.0,0.49,-0.12,-2.0,-3.78,0.2,0.0,-2.0,-1.5])
            #goodvar=np.array([3.75,0.389,-0.2,-0.0,0.0,0.0,8.0,6.0,-3.77])
            #good example:var=np.array([1.5,0.1225,-0.02,-2.0,0.0,0.0,4.0,0.0,-1.5])
            
            
            #defense matrix
            self.A1=np.array([[0,0,0,0,0,0,0,4],
                              [0,0,0,0,0,0,50,6],
                              [0,0,0,0,0,50,50,8],
                              [0,0,0,0,50,50,100,10],
                              [0,0,0,50,50,100,100,12],
                              [0,0,50,50,100,100,22,14],
                              [0,50,50,100,100,24,24,16],
                              [0,50,100,100,24,24,15,18]]) #50->buy 1 stock, 100->buy two stocks
        
            #inthehunt matrix
            #row corresponds to deficit-1,coloumn to number of stock available from hotel
            self.A2=np.array([[0,20+var[0],100,100,100,20+var[0],12+var[0],16+var[0]],
                              [0,0,20+var[0],24+var[0],24+var[0],12+var[0],8+var[0],13+var[0]],
                              [0,0,0,20+var[0],12+var[0],10+var[0],8+var[0],10+var[0]]])
        
            #brown coefficients
            self.A3=np.array([0.5+var[1],0.5+var[1],2+20*var[1],1+20*var[1]])
            
            #alpha coefficients
            self.A4=np.array([0.1+var[2],0.02])
            
            #hold onto stock matrix
            #first coloumn:turn, second coulumn:stocks of other players, 
            #thrid coloumn:own stock, 4th coloumn:b
            #Attention: the fourth coloumn must be <= the third coloumn
            self.A5=np.array([[30,0,2,2],
                              [30,2,4,4],
                              [50,0,2,2],
                              [50,2,4,4]])
        
            #graph to determine how much money is spent    
            self.A6=np.array([-1/600-(1/600*var[3])/(35/3),35/3+var[3]])
            
            #matrix which awards points for tile placement; 0:maj in small, 1-4:min small and cash problems
            #5:maj big and enough in small to defend lead, 6: would become maj in big, 
            #7:hotel would be created,8:enlarge majority,9:enlarge minority
            self.A7=np.array([17+var[7],2000+200*var[3],10+var[3],3000+300*var[3],8+var[3],12,15,13.5+var[6],6+var[8],3+1/2*var[8]])
            
            #coefficient that determines whether the player spreads his buys
            self.A8=3+var[4]
            
            #money below which to sell stock, ratio when to go for 2:1 trade
            self.A9=np.array([3000+300*var[3],2.5])
            
            #initial advantage matrix
            self.A10=2*np.array([10*(var[5]+1),9*(var[5]+1),8*(var[5]+1),5*(var[5]+1)])
        
        def drawtile(self,alltiles):
            a = random.randint(0,len(alltiles)-1)
            tile = alltiles.pop(a)
            #print(tile)
            self.tiles.append(tile)
            #self.add(tile)
            return
        
        #def placetile...remove tile and call global placetile()
        def placetile_player(self, x0):
            for i in range(6):
                #print(i)
                #print("length:",len(self.tiles))
                tile = self.tiles[i]
                if tile[0] == x0[0] and tile[1]==x0[1]:
                    self.tiles.pop(i)
                    break
            #print(x0,"has been placed on the board")
            placetile(x0,self)
            return
        
        
        def decide_placetile(self):
            eligible_tiles = []
            for i in range(6):
                if is_legal(self.tiles[i])==True:
                    eligible_tiles.append(self.tiles[i])
            
            tries=0
            while len(eligible_tiles)==0:
                for i in range(6):
                    #print("# tiles:", len(self.tiles))
                    a = self.tiles.pop(5-i)
                    alltiles.append(a)
                    
                for i in range(6):
                    self.drawtile(alltiles)
                    
                for i in range(6):
                    if is_legal(self.tiles[i])==True:
                        eligible_tiles.append(self.tiles[i])  
                tries+=1
                if tries>=10:
                    return True
            points=[]
            for i in range(len(eligible_tiles)):
                p=0
                tile=eligible_tiles[i]
                info=tile_info(tile)
                infosort=np.sort(tile_info(tile))
                n = 0 #number of non-empty tiles
                for k in range(len(info)):
                    if info[k] !=0:
                        n += 1
                n1=0 #number of single tiles
                for k in range(len(info)):
                    if info[k] ==1:
                        n1 += 1
                #number of hotels surrounding tile
                m = 0
                m1 = []
                for k in range(4):
                    if info[k] > 1:
                        b = True
                        for j in range(len(m1)):
                            if info[k]==m1[j]:
                                b = False
                        m1.append(info[k]) 
                        if b ==True:
                            m+=1
                if m==2:
                    hotel1=eval_hotel(infosort[3])
                    if infosort[3]!=infosort[2]:
                        hotel2=eval_hotel(infosort[2])
                    elif infosort[3]!=infosort[1]:
                        hotel2=eval_hotel(infosort[1])
                    else:
                        hotel2=eval_hotel(infosort[0])
                    if hotel1.size>=hotel2.size:
                        big=hotel1
                        small=hotel2
                    else:
                        big=hotel2
                        small=hotel1
                    maj,minn=majmin(small)
                    majb,minnb=majmin(big)
                    c=0
                    #majority small
                    for j in range(len(maj)):
                        if maj[j].name==self.name:
                            p+=self.A7[0]
                            c=10
                    #minority small and in need of money
                    for j in range(len(minn)):
                        if minn[j].name==self.name and self.money<self.A7[1]:
                            p+=self.A7[2]
                            c=10
                        elif minn[j].name==self.name and self.money<self.A7[3]:
                            p+=self.A7[4]
                            c=10
                    #majority in big and enough stock in small to defend lead
                    for j in range(len(majb)):
                        if majb[j].name==self.name and self.difference_to_maj(big)>-self.difference_to_maj(small)/2:
                            p+=self.A7[5]
                            c=10
                    #if you can become majority of big
                    for j in range(len(minnb)):
                        if -self.difference_to_maj(big)<(self.info_stock(small.value)/2-majb[-1].info_stock(small.value)/2):
                            p+=self.A7[6]
                            c=10
                   
                            
                    
                    
                    p=p-10+c
                if m==3:
                    hotel1=eval_hotel(infosort[3])
                    if infosort[2]!=infosort[3]:
                        hotel2=eval_hotel(infosort[2])
                        if infosort[1]!=infosort[2]:
                            hotel3=eval_hotel(infosort[1])
                        else:
                            hotel3=eval_hotel(infosort[0])
                        
                    else:
                        hotel2=eval_hotel(infosort[1])
                        hotel3=eval_hotel(infosort[0])
                        
                    if hotel1.size>hotel2.size and hotel1.size>hotel3.size:
                        big=hotel1
                        small1=hotel2
                        small2=hotel3
                    elif hotel2.size>hotel1.size and hotel2.size>hotel3.size:
                        big=hotel2
                        small1=hotel1
                        small2=hotel3
                    elif hotel3.size>hotel1.size and hotel3.size>hotel2.size:
                        big=hotel3
                        small1=hotel1
                        small2=hotel2
                    else:
                        big=hotel1
                        small1=hotel2
                        small2=hotel3
                    
                    c=0
                    maj1,minn1=majmin(small1)
                    for j in range(len(maj1)):
                        if maj1[j].name==self.name:
                            p+=self.A7[0]
                            c=10
                    maj2,minn2=majmin(small2)
                    for j in range(len(maj2)):
                        if maj2[j].name==self.name:
                            p+=self.A7[0]
                            c=10
                    majb,minnb=majmin(big)
                    for j in range(len(majb)):
                        if majb[j].name==self.name and (self.difference_to_maj(big)>-self.difference_to_maj(small1)/2 or self.difference_to_maj(big)>-self.difference_to_maj(small2)/2):
                            p+=self.A7[5]
                            c=10
                    for j in range(len(minn1)):
                       if minn1[j].name==self.name and self.money<self.A7[1]:
                           p+=self.A7[2]
                           c=10
                       elif minn1[j].name==self.name and self.money<self.A7[3]:
                           p+=self.A7[4]
                           c=10
                    for j in range(len(minn2)):
                       if minn2[j].name==self.name and self.money<self.A7[1]:
                           p+=self.A7[2]
                           c=10
                       elif minn2[j].name==self.name and self.money<self.A7[3]:
                           p+=self.A7[4]
                           c=10
                    p=p-10+c
                    
                if m==0 and n>0:
                    c=0
                    for j in range(2,9):
                        if eval_hotel(j).size==0 and self.info_stock(j)>0:
                            p+=self.A7[7]
                            c=5
                            break
                    #This is not a mistake!!
                    p=p+5-c
                
                if m==1:
                    adjhotel=eval_hotel(infosort[3])
                    maj,minn=majmin(adjhotel)
                    c=0
                    for j in range(len(maj)):
                        if maj[j].name==self.name:
                            p+=self.A7[8]
                            c=2
                    for j in range(len(minn)):
                        if minn[j].name==self.name:
                            p+=self.A7[9]
                            c=2
                    p=p-2+c
                
                points.append(p)
            
            besttilenumber=0
            for i in range(len(eligible_tiles)-1):
                if points[i+1]>points[besttilenumber]:
                    besttilenumber = i+1
            besttile=eligible_tiles[besttilenumber]
            self.placetile_player(besttile)
            return False
            
      
        def decide_merge_stock(self,big,small):
            n=self.info_stock(small.value)
            m=big.stock
            b=0
            while(self.money<self.A9[0] and n>=1):
                self.sellstock(small.value,1)
                n-=1
            if self.difference_to_maj(big)>=-n/2 and m>=n/2:
                while(m>=1 and n>=2):
                    self.getstock(big.value,1,free=True)
                    self.sellstock(small.value,2,free=True)
                    m-=1
                    n-=2
                    #print(self.name,"has traded 2",small.name,"stocks for 1",big.name,"stock")
            bigprice, useless1,useless2=big.reference()
            smallprice, useless3,useless4=small.reference()
            if bigprice>=self.A9[1]*smallprice:
                while(m>=1 and n>=2):
                    self.getstock(big.value,1,free=True)
                    self.sellstock(small.value,2,free=True)
                    m-=1
                    n-=2
                    #print(self.name,"has traded 2",small.name,"stocks for 1",big.name,"stock")
            stocks=self.other_player_stocks(small)
            b=hold_stock(stocks,n,self.A5)
            self.sellstock(small.value,n-b)
            #print(self.name,"has held on to",b,"stocks and sold",n-b,"stocks")
            
            
        def other_player_stocks(self,hotel):
            stocks=[]
            if self.name !=player1:
                stocks.append(player1.info_stock(hotel.value))
            if self.name !=player2:
                stocks.append(player2.info_stock(hotel.value))
            if self.name !=player3:
                stocks.append(player3.info_stock(hotel.value))
            if self.name !=player4:
                stocks.append(player4.info_stock(hotel.value))
            stocks=np.sort(stocks)
                
            return stocks
        
        def difference_to_maj(self,hotel):
            stocks=self.other_player_stocks(hotel)
            return self.info_stock(hotel.value)-stocks[2]
                
            
        #TODO
        def buy_stock(self):
            
            m1,t1,c1,a1,i1,f1,s1,w1 = player1.info()
            m2,t2,c2,a2,i2,f2,s2,w2 = player2.info()
            m3,t3,c3,a3,i3,f3,s3,w3 = player3.info()
            m4,t4,c4,a4,i4,f4,s4,w4 = player4.info()
            
            w_stock=np.sort([w1,w2,w3,w4])
            s_stock=np.sort([s1,s2,s3,s4])
            f_stock=np.sort([f1,f2,f3,f4])
            i_stock=np.sort([i1,i2,i3,i4])
            a_stock=np.sort([a1,a2,a3,a4])
            c_stock=np.sort([c1,c2,c3,c4])
            t_stock=np.sort([t1,t2,t3,t4])
            
            #Points for each stock and if the player should particularly buy 1 or 2
            w,s,f,i,a,c,t=0,0,0,0,0,0,0
            w1s,w2s,s1s,s2s,f1s,f2s,i1s,i2s,a1s,a2s,c1s,c2s,t1s,t2s=False,False,False,False,False,False,False,False,False,False,False,False,False,False
            
            if worldwide.size>0:
                if w_stock[3]==self.stock_worldwide and w_stock[2]==0:
                    w,w1s,w2s=initial_advantage(w_stock,self.A10)
                elif self.stock_worldwide==w_stock[3]:
                    w,w1s,w2s=defence(w_stock,worldwide,self.A1)
                elif (w_stock[3]-self.stock_worldwide)<=3:
                    w,w1s,w2s=inthehunt(w_stock,self.stock_worldwide,worldwide,self.A2)
                else:
                    w,w1s,w2s=browns(w_stock,self.stock_worldwide,worldwide,self.A1,self.A2,self.A3)
                
                w_alpha=alpha(worldwide,self.tiles,self.A4)
                w*=w_alpha
                
            if sackson.size>0:
                if s_stock[3]==self.stock_sackson and s_stock[2]==0:
                    s,s1s,s2s=initial_advantage(s_stock,self.A10)
                elif self.stock_sackson==s_stock[3]:
                    s,s1s,s2s=defence(s_stock,sackson,self.A1)
                elif (s_stock[3]-self.stock_sackson)<=3:
                    s,s1s,s2s=inthehunt(s_stock,self.stock_sackson,sackson,self.A2)
                else:
                    s,s1s,s2s=browns(s_stock,self.stock_sackson,sackson,self.A1,self.A2,self.A3)
            
            s_alpha=alpha(sackson,self.tiles,self.A4)
            s*=s_alpha
            
            if festival.size>0:
                if f_stock[3]==self.stock_festival and f_stock[2]==0:
                    f,f1s,f2s=initial_advantage(f_stock,self.A10)
                elif self.stock_festival==f_stock[3]:
                    f,f1s,f2s=defence(f_stock,festival,self.A1)
                elif (f_stock[3]-self.stock_festival)<=3:
                    f,f1s,f2s=inthehunt(f_stock,self.stock_festival,festival,self.A2)
                else:
                    f,f1s,f2s=browns(f_stock,self.stock_festival,festival,self.A1,self.A2,self.A3)
                
                f_alpha=alpha(festival,self.tiles,self.A4)
                f*=f_alpha
            
            if imperial.size>0:
                if i_stock[3]==self.stock_imperial and i_stock[2]==0:
                    i,i1s,i2s=initial_advantage(i_stock,self.A10)
                elif self.stock_imperial==i_stock[3]:
                    i,i1s,i2s=defence(i_stock,imperial,self.A1)
                elif (i_stock[3]-self.stock_imperial)<=3:
                    i,i1s,i2s=inthehunt(i_stock,self.stock_imperial,imperial,self.A2)
                else:
                    i,i1s,i2s=browns(i_stock,self.stock_imperial,imperial,self.A1,self.A2,self.A3)
                
                i_alpha=alpha(imperial,self.tiles,self.A4)
                i*=i_alpha
                
            if american.size>0:
                if a_stock[3]==self.stock_american and a_stock[2]==0:
                    a,a1s,a2s=initial_advantage(a_stock,self.A10)
                elif self.stock_american==a_stock[3]:
                    a,a1s,a2s=defence(a_stock,american,self.A1)
                elif (a_stock[3]-self.stock_american)<=3:
                    a,a1s,a2s=inthehunt(a_stock,self.stock_american,american,self.A2)
                else:
                    a,a1s,a2s=browns(a_stock,self.stock_american,american,self.A1,self.A2,self.A3)
                
                a_alpha=alpha(american,self.tiles,self.A4)
                a*=a_alpha
            
            if continental.size>0:
                if c_stock[3]==self.stock_continental and c_stock[2]==0:
                    c,c1s,c2s=initial_advantage(c_stock,self.A10)
                elif self.stock_continental==c_stock[3]:
                    c,c1s,c2s=defence(c_stock,continental,self.A1)
                elif (c_stock[3]-self.stock_continental)<=3:
                    c,c1s,c2s=inthehunt(c_stock,self.stock_continental,continental,self.A2)
                else:
                    c,c1s,c2s=browns(c_stock,self.stock_continental,continental,self.A1,self.A2,self.A3)
                
                c_alpha=alpha(continental,self.tiles,self.A4)
                c*=c_alpha
            
            if tower.size>0:
                if t_stock[3]==self.stock_tower and t_stock[2]==0:
                    t,t1s,t2s=initial_advantage(t_stock,self.A10)
                elif self.stock_tower==t_stock[3]:
                    t,t1s,t2s=defence(t_stock,tower,self.A1)
                elif (t_stock[3]-self.stock_tower)<=3:
                    t,t1s,t2s=inthehunt(t_stock,self.stock_tower,tower,self.A2)
                else:
                    t,t1s,t2s=browns(t_stock,self.stock_tower,tower,self.A1,self.A2,self.A3)
                
                t_alpha=alpha(tower,self.tiles,self.A4)
                t*=t_alpha
            
            points=np.array([w,s,f,i,a,c,t])
            points2=[]
            for i in range(7):
                points2.append(points[i])
            points2=np.sort(points2)
            for i in range(7):
                #achtung bei gleichstand wird das hotel mit dem tieferen value gewählt
                if points[i]==points2[6]:
                    favhotel=eval_hotel(i+2)
            splitt=False        
            if points2[6]-points2[5]<=self.A8 and points2[5]!=0:
                splitt=True
                for i in range(7):
                    #achtung bei gleichstand wird das hotel mit dem tieferen value gewählt
                    if points[i]==points2[5]:
                        favhotel2=eval_hotel(i+2)
                        
                
            
            smallbuys=np.array([[w1s,s1s,f1s,i1s,a1s,c1s,t1s],
                                [w2s,s2s,f2s,i2s,a2s,c2s,t2s]])
            
            p=3
            list1s=[]
            list2s=[]
            for i in range(2,9):
                if smallbuys[0,i-2]==True:
                    list1s.append(eval_hotel(i))
                if smallbuys[1,i-2]==True:
                    list2s.append(eval_hotel(i))
                    
            a=len(list1s)
            b=len(list2s)
            if a+2*b<=3:
                for i in range(len(list1s)):
                    buy_hotel = list1s[i]
                    price,useless, useless2 = buy_hotel.reference()
                    if self.money>=price and buy_hotel.stock>=1:
                        self.getstock(buy_hotel.value,1)
                        p-=1
                        #print(self.name,"has purchased",1,"stock from",buy_hotel.name)
                for i in range(len(list2s)):
                    buy_hotel = list2s[i]
                    price,useless, useless2 = buy_hotel.reference()
                    if self.money>=price*2 and buy_hotel.stock>=2:
                        self.getstock(buy_hotel.value,2)
                        p-=2
                        #print(self.name,"has purchased",2,"stocks from",buy_hotel.name)
            elif a+2*b>3:
                list3=list1s+list2s
                list4=[]
                for i in range(len(list3)):
                    list4.append(points[list3[i].value-2])
                list4.sort()
                for k in range(3):
                    n1 = len(list4)
                    l = 0
                    for i in range(n1): 
                        if points[list3[l].value-2]==list4[-1]:
                            buy_hotel=list3[l]
                            price,useless, useless2 = buy_hotel.reference()
                            if smallbuys[0,buy_hotel.value-2]==True:
                                n=1
                            else:
                                n=2
                            if self.money>=price*n and p>=n and buy_hotel.stock>=n:
                                self.getstock(buy_hotel.value,n)
                                p-=n
                                #print(self.name,"has purchased",n,"stocks from",buy_hotel.name)
                                list3.pop(l)
                                l-=1
                                list4.pop(-1)
                        l+=1 
    
            if points[favhotel.value-2]>=self.A6[0]*self.money+self.A6[1] and points[favhotel.value-2]!=0:
                if splitt==True:
                    price,useless, useless2 = favhotel.reference()
                    if self.money>=price*2 and p>=2 and favhotel.stock>=2:
                        self.getstock(favhotel.value,2)
                        p-=2
                        #print(self.name,"has purchased",2,"stocks from",favhotel.name)
                    price2,useless3, useless4 = favhotel.reference()
                    if self.money>=price2*1 and p>=1 and favhotel2.stock>=1:
                        self.getstock(favhotel2.value,1)
                        p-=1
                        #print(self.name,"has purchased",1,"stock from",favhotel2.name)
                elif splitt==False:
                    price,useless, useless2 = favhotel.reference()
                    if self.money>=price*p and favhotel.stock>=p:
                        self.getstock(favhotel.value,p)
                        #print(self.name,"has purchased",p,"stocks from",favhotel.name)
            
            
                
        def set_money(self,cash):
            self.money += cash
            
            
        def info(self):
            return self.money, self.stock_tower, self.stock_continental, self.stock_american, self.stock_imperial, self.stock_festival, self.stock_sackson ,self.stock_worldwide
            
        def info_stock(self,value):
            if value == tower.value:
                return self.stock_tower
            elif value == continental.value:
                return self.stock_continental
            elif value == american.value:
                return self.stock_american
            elif value == imperial.value:
                return self.stock_imperial
            elif value == festival.value:
                return self.stock_festival
            elif value == sackson.value:
                return self.stock_sackson
            elif value == worldwide.value:
                return self.stock_worldwide
            
        def sellstock(self,value,n,free=False):
            price,useless, useless2 = eval_hotel(value).reference()
            if free==False:
                self.set_money(n*price)
            if value == tower.value:
                self.stock_tower -= n
                tower.recstock(n)
            elif value == continental.value:
                self.stock_continental -= n
                continental.recstock(n)
            elif value == american.value:
                self.stock_american -= n
                american.recstock(n)
            elif value == imperial.value:
                self.stock_imperial -= n
                imperial.recstock(n)
            elif value == festival.value:
                self.stock_festival -= n
                festival.recstock(n)
            elif value == sackson.value:
                self.stock_sackson -= n
                sackson.recstock(n)
            elif value == worldwide.value:
                self.stock_worldwide -= n
                worldwide.recstock(n)
        
        def getstock(self,value,n,free=False):
            price,useless, useless2 = eval_hotel(value).reference()
            if free==False:
                self.set_money(-n*price)
            if value == tower.value:
               self.stock_tower += n
               tower.sellstock(n)
            elif value == continental.value:
               self.stock_continental += n
               continental.sellstock(n)
            elif value == american.value:
               self.stock_american += n
               american.sellstock(n)
            elif value == imperial.value:
               self.stock_imperial += n
               imperial.sellstock(n)
            elif value == festival.value:
               self.stock_festival += n
               festival.sellstock(n)
            elif value == sackson.value:
               self.stock_sackson += n
               sackson.sellstock(n)
            elif value == worldwide.value:
               self.stock_worldwide += n
               worldwide.sellstock(n)
         
        #decide...stupid 
        def decide_merge(self,hotel1,hotel2):
            m1,t1,c1,a1,i1,f1,s1,w1=self.info()
            hilfsarray=np.array([w1,s1,f1,i1,a1,c1,t1])
    
            maj1,minn1 = majmin(hotel1)
            maj2,minn2 = majmin(hotel2)
            M1=False
            m1=False
            M2=False
            m2=False
            for i in range(len(maj1)):
                if maj1[i].name==self.name:
                    M1=True
            for i in range(len(minn1)):
                if minn1[i].name==self.name:
                    m1=True
            for i in range(len(maj2)):
                if maj2[i].name==self.name:
                    M2=True
            for i in range(len(minn2)):
                if minn2[i].name==self.name:
                    m2=True
            
            if M1==True and M2==False:
                if np.abs(hilfsarray[hotel1.value-2]-hotel1.stock)<=5 and hilfsarray[hotel1.value-2]>=5 and self.money>=3000:
                    return hotel1,hotel2
                else: 
                    return hotel2,hotel1
            elif M2==True and M1==False:
                if np.abs(hilfsarray[hotel2.value-2]-hotel2.stock)<=5 and hilfsarray[hotel2.value-2]>=5 and self.money>=3000:
                    return hotel2,hotel1
                else: 
                    return hotel1,hotel2
                
            elif M1==True and M2 == True:
                if self.difference_to_maj(hotel1)>=self.difference_to_maj(hotel2):
                    return hotel1,hotel2
                else:
                    return hotel2,hotel1
                
            elif m1==True and m2==False:
                if np.abs(hilfsarray[hotel1.value-2]-hotel1.stock)<=5 and hilfsarray[hotel1.value-2]>=5 and self.money>=3000:
                    return hotel1,hotel2
                else: 
                    return hotel2,hotel1
            elif m2==True and m1==False:
                if np.abs(hilfsarray[hotel2.value-2]-hotel2.stock)<=5 and hilfsarray[hotel2.value-2]>=5 and self.money>=3000:
                    return hotel2,hotel1
                else: 
                    return hotel1,hotel2
           
            elif m1==True and m2 == True:
                if self.difference_to_maj(hotel1)<=self.info_stock(hotel1.value)/2:
                    return hotel1,hotel2
                elif self.difference_to_maj(hotel2)<=self.info_stock(hotel1.value)/2:
                    return hotel2,hotel1
                elif self.money>=3000 and hilfsarray[hotel1.value-2]>=hilfsarray[hotel2.value-2]:
                    return hotel1,hotel2
                elif self.money>=3000 and hilfsarray[hotel1.value-2]<hilfsarray[hotel2.value-2]:
                    return hotel2,hotel1
                elif self.money<3000 and hilfsarray[hotel1.value-2]>=hilfsarray[hotel2.value-2]:
                    return hotel2,hotel1
                elif self.money>=3000 and hilfsarray[hotel1.value-2]<hilfsarray[hotel2.value-2]:
                    return hotel1,hotel2
            else:
                if hilfsarray[hotel1.value-2]>=hilfsarray[hotel2.value-2]:
                    return hotel1,hotel2
                else:
                    return hotel2,hotel1
            
        
        def decide_triple_merge(self,hotel1,hotel2,hotel3):
            big,small=self.decide_merge(hotel1,hotel2)
            a,b = self.decide_merge(big,hotel3)
            return a,b,small
        
        def decide_double_merge(self,hotel1,hotel2):
            return self.decide_merge(hotel1,hotel2)
        
        def decide_quad_merge(self,hotel1,hotel2,hotel3,hotel4):
            big,small1,small2=self.decide_triple_merge(hotel1,hotel2,hotel3)
            a,b = self.decide_merge(big,hotel4)
            return a,b,small1,small2
        
        def decide_newhotel(self):
            m1,t1,c1,a1,i1,f1,s1,w1 = self.info()
            stocks=np.array([w1,s1,f1,i1,a1,c1,t1])
            hlist=[]
            hlist2=[]
            for i in range(2,9):
                if eval_hotel(i).size==0:
                    hlist.append(eval_hotel(i))
                    hlist2.append(eval_hotel(i))
            prefhotel=hlist[0]
            for i in range(len(hlist)):
                if stocks[hlist[i].value-2]>stocks[prefhotel.value-2]:
                    prefhotel=hlist[i]
            if stocks[prefhotel.value-2]>0:
                return prefhotel
            for k in range(7):
                for i in range(len(hlist2)):
                    if hlist2[i].stock<25:
                        hlist2.pop(len(hlist2)-1-i)
                        break
            if len(hlist2)>0:
                r = random.randint(0,len(hlist2)-1)
                return hlist2[r]
            else:
                r = random.randint(0,len(hlist)-1)
                return hlist[r]
            
            
    class Player_entrepreneur:
   
        def __init__(self,g,name1):
            self.money = g
            self.stock_tower=0
            self.stock_continental = 0
            self.stock_american = 0
            self.stock_imperial = 0
            self.stock_festival = 0
            self.stock_sackson = 0 
            self.stock_worldwide = 0
            self.tiles = []
            self.name = name1
            #defense matrix
            self.A1=np.array([[0,0,0,0,0,0,0,4],
                              [0,0,0,0,0,0,50,6],
                              [0,0,0,0,0,50,50,8],
                              [0,0,0,0,50,50,100,10],
                              [0,0,0,50,50,100,100,12],
                              [0,0,50,50,100,100,22,14],
                              [0,50,50,100,100,24,24,16],
                              [0,50,100,100,24,24,15,18]]) #50->buy 1 stock, 100->buy two stocks
        
            #inthehunt matrix
            #row corresponds to deficit-1,coloumn to number of stock available from hotel
            self.A2=np.array([[0,20,100,100,100,20,12,16],
                              [0,0,20,24,24,12,8,13],
                              [0,0,0,20,12,10,8,10]])
        
            #brown coefficients
            self.A3=np.array([0.5,0.5,2,1])
            
            #alpha coefficients
            self.A4=np.array([0.1,0.02])
            
            #hold onto stock matrix
            #first coloumn:turn, second coulumn:stocks of other players, 
            #thrid coloumn:own stock, 4th coloumn:b
            #Attention: the fourth coloumn must be <= the third coloumn
            self.A5=np.array([[30,0,2,2],
                              [30,2,4,4],
                              [50,0,2,2],
                              [50,2,4,4]])
        
            #graph to determine how much money is spent    
            self.A6=np.array([-1/600,35/3])
            
            #matrix which awards points for tile placement; 0:maj in small, 1-4:min small and cash problems
            #5:maj big and enough in small to defend lead, 6: would become maj in big, 
            #7:hotel would be created,8:enlarge majority,9:enlarge minority
            self.A7=np.array([20,2000,10,3000,8,12,15,17,4,2])
            
            #coefficient that determines whether the player spreads his buys
            self.A8=3
            
            #money below which to sell stock, ratio when to go for 2:1 trade
            self.A9=np.array([3000,2.5])
            
            #initial advantage matrix
            self.A10=np.array([20,18,16,10])
        
        def drawtile(self,alltiles):
            a = random.randint(0,len(alltiles)-1)
            tile = alltiles.pop(a)
            #print(tile)
            self.tiles.append(tile)
            #self.add(tile)
            return
        
        #def placetile...remove tile and call global placetile()
        def placetile_player(self, x0):
            for i in range(6):
                #print(i)
                #print("length:",len(self.tiles))
                tile = self.tiles[i]
                if tile[0] == x0[0] and tile[1]==x0[1]:
                    self.tiles.pop(i)
                    break
            #print(x0,"has been placed on the board")
            placetile(x0,self)
            return
        
        
        def decide_placetile(self):
            eligible_tiles = []
            for i in range(6):
                if is_legal(self.tiles[i])==True:
                    eligible_tiles.append(self.tiles[i])
            
            tries=0
            while len(eligible_tiles)==0:
                for i in range(6):
                    #print("# tiles:", len(self.tiles))
                    a = self.tiles.pop(5-i)
                    alltiles.append(a)
                    
                for i in range(6):
                    self.drawtile(alltiles)
                    
                for i in range(6):
                    if is_legal(self.tiles[i])==True:
                        eligible_tiles.append(self.tiles[i])  
                tries+=1
                if tries>=10:
                    return True
            points=[]
            for i in range(len(eligible_tiles)):
                p=0
                tile=eligible_tiles[i]
                info=tile_info(tile)
                infosort=np.sort(tile_info(tile))
                n = 0 #number of non-empty tiles
                for k in range(len(info)):
                    if info[k] !=0:
                        n += 1
                n1=0 #number of single tiles
                for k in range(len(info)):
                    if info[k] ==1:
                        n1 += 1
                #number of hotels surrounding tile
                m = 0
                m1 = []
                for k in range(4):
                    if info[k] > 1:
                        b = True
                        for j in range(len(m1)):
                            if info[k]==m1[j]:
                                b = False
                        m1.append(info[k]) 
                        if b ==True:
                            m+=1
                if m==2:
                    hotel1=eval_hotel(infosort[3])
                    if infosort[3]!=infosort[2]:
                        hotel2=eval_hotel(infosort[2])
                    elif infosort[3]!=infosort[1]:
                        hotel2=eval_hotel(infosort[1])
                    else:
                        hotel2=eval_hotel(infosort[0])
                    if hotel1.size>=hotel2.size:
                        big=hotel1
                        small=hotel2
                    else:
                        big=hotel2
                        small=hotel1
                    maj,minn=majmin(small)
                    majb,minnb=majmin(big)
                    c=0
                    #majority small
                    for j in range(len(maj)):
                        if maj[j].name==self.name:
                            p+=self.A7[0]
                            c=10
                    #minority small and in need of money
                    for j in range(len(minn)):
                        if minn[j].name==self.name and self.money<self.A7[1]:
                            p+=self.A7[2]
                            c=10
                        elif minn[j].name==self.name and self.money<self.A7[3]:
                            p+=self.A7[4]
                            c=10
                    #majority in big and enough stock in small to defend lead
                    for j in range(len(majb)):
                        if majb[j].name==self.name and self.difference_to_maj(big)>-self.difference_to_maj(small)/2:
                            p+=self.A7[5]
                            c=10
                    #if you can become majority of big
                    for j in range(len(minnb)):
                        if -self.difference_to_maj(big)<(self.info_stock(small.value)/2-majb[-1].info_stock(small.value)/2):
                            p+=self.A7[6]
                            c=10
                   
                            
                    
                    
                    p=p-10+c
                if m==3:
                    hotel1=eval_hotel(infosort[3])
                    if infosort[2]!=infosort[3]:
                        hotel2=eval_hotel(infosort[2])
                        if infosort[1]!=infosort[2]:
                            hotel3=eval_hotel(infosort[1])
                        else:
                            hotel3=eval_hotel(infosort[0])
                        
                    else:
                        hotel2=eval_hotel(infosort[1])
                        hotel3=eval_hotel(infosort[0])
                        
                    if hotel1.size>hotel2.size and hotel1.size>hotel3.size:
                        big=hotel1
                        small1=hotel2
                        small2=hotel3
                    elif hotel2.size>hotel1.size and hotel2.size>hotel3.size:
                        big=hotel2
                        small1=hotel1
                        small2=hotel3
                    elif hotel3.size>hotel1.size and hotel3.size>hotel2.size:
                        big=hotel3
                        small1=hotel1
                        small2=hotel2
                    else:
                        big=hotel1
                        small1=hotel2
                        small2=hotel3
                    
                    c=0
                    maj1,minn1=majmin(small1)
                    for j in range(len(maj1)):
                        if maj1[j].name==self.name:
                            p+=self.A7[0]
                            c=10
                    maj2,minn2=majmin(small2)
                    for j in range(len(maj2)):
                        if maj2[j].name==self.name:
                            p+=self.A7[0]
                            c=10
                    majb,minnb=majmin(big)
                    for j in range(len(majb)):
                        if majb[j].name==self.name and (self.difference_to_maj(big)>-self.difference_to_maj(small1)/2 or self.difference_to_maj(big)>-self.difference_to_maj(small2)/2):
                            p+=self.A7[5]
                            c=10
                    for j in range(len(minn1)):
                       if minn1[j].name==self.name and self.money<self.A7[1]:
                           p+=self.A7[2]
                           c=10
                       elif minn1[j].name==self.name and self.money<self.A7[3]:
                           p+=self.A7[4]
                           c=10
                    for j in range(len(minn2)):
                       if minn2[j].name==self.name and self.money<self.A7[1]:
                           p+=self.A7[2]
                           c=10
                       elif minn2[j].name==self.name and self.money<self.A7[3]:
                           p+=self.A7[4]
                           c=10
                    p=p-10+c
                    
                if m==0 and n>0:
                    c=0
                    for j in range(2,9):
                        if eval_hotel(j).size==0 and self.info_stock(j)>0:
                            p+=self.A7[7]
                            c=5
                            break
                    #This is not a mistake!!
                    p=p+5-c
                
                if m==1:
                    adjhotel=eval_hotel(infosort[3])
                    maj,minn=majmin(adjhotel)
                    c=0
                    for j in range(len(maj)):
                        if maj[j].name==self.name:
                            p+=self.A7[8]
                            c=2
                    for j in range(len(minn)):
                        if minn[j].name==self.name:
                            p+=self.A7[9]
                            c=2
                    p=p-2+c
                
                points.append(p)
            
            besttilenumber=0
            for i in range(len(eligible_tiles)-1):
                if points[i+1]>points[besttilenumber]:
                    besttilenumber = i+1
            besttile=eligible_tiles[besttilenumber]
            self.placetile_player(besttile)
            return False
            
      
        def decide_merge_stock(self,big,small):
            n=self.info_stock(small.value)
            m=big.stock
            b=0
            while(self.money<self.A9[0] and n>=1):
                self.sellstock(small.value,1)
                n-=1
            if self.difference_to_maj(big)>=-n/2 and m>=n/2:
                while(m>=1 and n>=2):
                    self.getstock(big.value,1,free=True)
                    self.sellstock(small.value,2,free=True)
                    m-=1
                    n-=2
                    #print(self.name,"has traded 2",small.name,"stocks for 1",big.name,"stock")
            bigprice, useless1,useless2=big.reference()
            smallprice, useless3,useless4=small.reference()
            if bigprice>=self.A9[1]*smallprice:
                while(m>=1 and n>=2):
                    self.getstock(big.value,1,free=True)
                    self.sellstock(small.value,2,free=True)
                    m-=1
                    n-=2
                    #print(self.name,"has traded 2",small.name,"stocks for 1",big.name,"stock")
            stocks=self.other_player_stocks(small)
            b=hold_stock(stocks,n,self.A5)
            self.sellstock(small.value,n-b)
            #print(self.name,"has held on to",b,"stocks and sold",n-b,"stocks")
            
            
        def other_player_stocks(self,hotel):
            stocks=[]
            if self.name !=player1:
                stocks.append(player1.info_stock(hotel.value))
            if self.name !=player2:
                stocks.append(player2.info_stock(hotel.value))
            if self.name !=player3:
                stocks.append(player3.info_stock(hotel.value))
            if self.name !=player4:
                stocks.append(player4.info_stock(hotel.value))
            stocks=np.sort(stocks)
                
            return stocks
        
        def difference_to_maj(self,hotel):
            stocks=self.other_player_stocks(hotel)
            return self.info_stock(hotel.value)-stocks[2]
                
            
        #TODO
        def buy_stock(self):
            
            m1,t1,c1,a1,i1,f1,s1,w1 = player1.info()
            m2,t2,c2,a2,i2,f2,s2,w2 = player2.info()
            m3,t3,c3,a3,i3,f3,s3,w3 = player3.info()
            m4,t4,c4,a4,i4,f4,s4,w4 = player4.info()
            
            w_stock=np.sort([w1,w2,w3,w4])
            s_stock=np.sort([s1,s2,s3,s4])
            f_stock=np.sort([f1,f2,f3,f4])
            i_stock=np.sort([i1,i2,i3,i4])
            a_stock=np.sort([a1,a2,a3,a4])
            c_stock=np.sort([c1,c2,c3,c4])
            t_stock=np.sort([t1,t2,t3,t4])
            
            #Points for each stock and if the player should particularly buy 1 or 2
            w,s,f,i,a,c,t=0,0,0,0,0,0,0
            w1s,w2s,s1s,s2s,f1s,f2s,i1s,i2s,a1s,a2s,c1s,c2s,t1s,t2s=False,False,False,False,False,False,False,False,False,False,False,False,False,False
            
            if worldwide.size>0:
                if w_stock[3]==self.stock_worldwide and w_stock[2]==0:
                    w,w1s,w2s=initial_advantage(w_stock,self.A10)
                elif self.stock_worldwide==w_stock[3]:
                    w,w1s,w2s=defence(w_stock,worldwide,self.A1)
                elif (w_stock[3]-self.stock_worldwide)<=3:
                    w,w1s,w2s=inthehunt(w_stock,self.stock_worldwide,worldwide,self.A2)
                else:
                    w,w1s,w2s=browns(w_stock,self.stock_worldwide,worldwide,self.A1,self.A2,self.A3)
                
                w_alpha=alpha(worldwide,self.tiles,self.A4)
                w*=w_alpha
                
            if sackson.size>0:
                if s_stock[3]==self.stock_sackson and s_stock[2]==0:
                    s,s1s,s2s=initial_advantage(s_stock,self.A10)
                elif self.stock_sackson==s_stock[3]:
                    s,s1s,s2s=defence(s_stock,sackson,self.A1)
                elif (s_stock[3]-self.stock_sackson)<=3:
                    s,s1s,s2s=inthehunt(s_stock,self.stock_sackson,sackson,self.A2)
                else:
                    s,s1s,s2s=browns(s_stock,self.stock_sackson,sackson,self.A1,self.A2,self.A3)
            
            s_alpha=alpha(sackson,self.tiles,self.A4)
            s*=s_alpha
            
            if festival.size>0:
                if f_stock[3]==self.stock_festival and f_stock[2]==0:
                    f,f1s,f2s=initial_advantage(f_stock,self.A10)
                elif self.stock_festival==f_stock[3]:
                    f,f1s,f2s=defence(f_stock,festival,self.A1)
                elif (f_stock[3]-self.stock_festival)<=3:
                    f,f1s,f2s=inthehunt(f_stock,self.stock_festival,festival,self.A2)
                else:
                    f,f1s,f2s=browns(f_stock,self.stock_festival,festival,self.A1,self.A2,self.A3)
                
                f_alpha=alpha(festival,self.tiles,self.A4)
                f*=f_alpha
            
            if imperial.size>0:
                if i_stock[3]==self.stock_imperial and i_stock[2]==0:
                    i,i1s,i2s=initial_advantage(i_stock,self.A10)
                elif self.stock_imperial==i_stock[3]:
                    i,i1s,i2s=defence(i_stock,imperial,self.A1)
                elif (i_stock[3]-self.stock_imperial)<=3:
                    i,i1s,i2s=inthehunt(i_stock,self.stock_imperial,imperial,self.A2)
                else:
                    i,i1s,i2s=browns(i_stock,self.stock_imperial,imperial,self.A1,self.A2,self.A3)
                
                i_alpha=alpha(imperial,self.tiles,self.A4)
                i*=i_alpha
                
            if american.size>0:
                if a_stock[3]==self.stock_american and a_stock[2]==0:
                    a,a1s,a2s=initial_advantage(a_stock,self.A10)
                elif self.stock_american==a_stock[3]:
                    a,a1s,a2s=defence(a_stock,american,self.A1)
                elif (a_stock[3]-self.stock_american)<=3:
                    a,a1s,a2s=inthehunt(a_stock,self.stock_american,american,self.A2)
                else:
                    a,a1s,a2s=browns(a_stock,self.stock_american,american,self.A1,self.A2,self.A3)
                
                a_alpha=alpha(american,self.tiles,self.A4)
                a*=a_alpha
            
            if continental.size>0:
                if c_stock[3]==self.stock_continental and c_stock[2]==0:
                    c,c1s,c2s=initial_advantage(c_stock,self.A10)
                elif self.stock_continental==c_stock[3]:
                    c,c1s,c2s=defence(c_stock,continental,self.A1)
                elif (c_stock[3]-self.stock_continental)<=3:
                    c,c1s,c2s=inthehunt(c_stock,self.stock_continental,continental,self.A2)
                else:
                    c,c1s,c2s=browns(c_stock,self.stock_continental,continental,self.A1,self.A2,self.A3)
                
                c_alpha=alpha(continental,self.tiles,self.A4)
                c*=c_alpha
            
            if tower.size>0:
                if t_stock[3]==self.stock_tower and t_stock[2]==0:
                    t,t1s,t2s=initial_advantage(t_stock,self.A10)
                elif self.stock_tower==t_stock[3]:
                    t,t1s,t2s=defence(t_stock,tower,self.A1)
                elif (t_stock[3]-self.stock_tower)<=3:
                    t,t1s,t2s=inthehunt(t_stock,self.stock_tower,tower,self.A2)
                else:
                    t,t1s,t2s=browns(t_stock,self.stock_tower,tower,self.A1,self.A2,self.A3)
                
                t_alpha=alpha(tower,self.tiles,self.A4)
                t*=t_alpha
            
            points=np.array([w,s,f,i,a,c,t])
            points2=[]
            for i in range(7):
                points2.append(points[i])
            points2=np.sort(points2)
            for i in range(7):
                #achtung bei gleichstand wird das hotel mit dem tieferen value gewählt
                if points[i]==points2[6]:
                    favhotel=eval_hotel(i+2)
            splitt=False        
            if points2[6]-points2[5]<=self.A8 and points2[5]!=0:
                splitt=True
                for i in range(7):
                    #achtung bei gleichstand wird das hotel mit dem tieferen value gewählt
                    if points[i]==points2[5]:
                        favhotel2=eval_hotel(i+2)
                        
                
            
            smallbuys=np.array([[w1s,s1s,f1s,i1s,a1s,c1s,t1s],
                                [w2s,s2s,f2s,i2s,a2s,c2s,t2s]])
            
            p=3
            list1s=[]
            list2s=[]
            for i in range(2,9):
                if smallbuys[0,i-2]==True:
                    list1s.append(eval_hotel(i))
                if smallbuys[1,i-2]==True:
                    list2s.append(eval_hotel(i))
                    
            a=len(list1s)
            b=len(list2s)
            if a+2*b<=3:
                for i in range(len(list1s)):
                    buy_hotel = list1s[i]
                    price,useless, useless2 = buy_hotel.reference()
                    if self.money>=price and buy_hotel.stock>=1:
                        self.getstock(buy_hotel.value,1)
                        p-=1
                        #print(self.name,"has purchased",1,"stock from",buy_hotel.name)
                for i in range(len(list2s)):
                    buy_hotel = list2s[i]
                    price,useless, useless2 = buy_hotel.reference()
                    if self.money>=price*2 and buy_hotel.stock>=2:
                        self.getstock(buy_hotel.value,2)
                        p-=2
                        #print(self.name,"has purchased",2,"stocks from",buy_hotel.name)
            elif a+2*b>3:
                list3=list1s+list2s
                list4=[]
                for i in range(len(list3)):
                    list4.append(points[list3[i].value-2])
                list4.sort()
                for k in range(3):
                    n1 = len(list4)
                    l = 0
                    for i in range(n1): 
                        if points[list3[l].value-2]==list4[-1]:
                            buy_hotel=list3[l]
                            price,useless, useless2 = buy_hotel.reference()
                            if smallbuys[0,buy_hotel.value-2]==True:
                                n=1
                            else:
                                n=2
                            if self.money>=price*n and p>=n and buy_hotel.stock>=n:
                                self.getstock(buy_hotel.value,n)
                                p-=n
                                #print(self.name,"has purchased",n,"stocks from",buy_hotel.name)
                                list3.pop(l)
                                l-=1
                                list4.pop(-1)
                        l+=1 
    
            if points[favhotel.value-2]>=self.A6[0]*self.money+self.A6[1] and points[favhotel.value-2]!=0:
                if splitt==True:
                    price,useless, useless2 = favhotel.reference()
                    if self.money>=price*2 and p>=2 and favhotel.stock>=2:
                        self.getstock(favhotel.value,2)
                        p-=2
                        #print(self.name,"has purchased",2,"stocks from",favhotel.name)
                    price2,useless3, useless4 = favhotel.reference()
                    if self.money>=price2*1 and p>=1 and favhotel2.stock>=1:
                        self.getstock(favhotel2.value,1)
                        p-=1
                        #print(self.name,"has purchased",1,"stock from",favhotel2.name)
                elif splitt==False:
                    price,useless, useless2 = favhotel.reference()
                    if self.money>=price*p and favhotel.stock>=p:
                        self.getstock(favhotel.value,p)
                        #print(self.name,"has purchased",p,"stocks from",favhotel.name)
            
            
                
        def set_money(self,cash):
            self.money += cash
            
            
        def info(self):
            return self.money, self.stock_tower, self.stock_continental, self.stock_american, self.stock_imperial, self.stock_festival, self.stock_sackson ,self.stock_worldwide
            
        def info_stock(self,value):
            if value == tower.value:
                return self.stock_tower
            elif value == continental.value:
                return self.stock_continental
            elif value == american.value:
                return self.stock_american
            elif value == imperial.value:
                return self.stock_imperial
            elif value == festival.value:
                return self.stock_festival
            elif value == sackson.value:
                return self.stock_sackson
            elif value == worldwide.value:
                return self.stock_worldwide
            
        def sellstock(self,value,n,free=False):
            price,useless, useless2 = eval_hotel(value).reference()
            if free==False:
                self.set_money(n*price)
            if value == tower.value:
                self.stock_tower -= n
                tower.recstock(n)
            elif value == continental.value:
                self.stock_continental -= n
                continental.recstock(n)
            elif value == american.value:
                self.stock_american -= n
                american.recstock(n)
            elif value == imperial.value:
                self.stock_imperial -= n
                imperial.recstock(n)
            elif value == festival.value:
                self.stock_festival -= n
                festival.recstock(n)
            elif value == sackson.value:
                self.stock_sackson -= n
                sackson.recstock(n)
            elif value == worldwide.value:
                self.stock_worldwide -= n
                worldwide.recstock(n)
        
        def getstock(self,value,n,free=False):
            price,useless, useless2 = eval_hotel(value).reference()
            if free==False:
                self.set_money(-n*price)
            if value == tower.value:
               self.stock_tower += n
               tower.sellstock(n)
            elif value == continental.value:
               self.stock_continental += n
               continental.sellstock(n)
            elif value == american.value:
               self.stock_american += n
               american.sellstock(n)
            elif value == imperial.value:
               self.stock_imperial += n
               imperial.sellstock(n)
            elif value == festival.value:
               self.stock_festival += n
               festival.sellstock(n)
            elif value == sackson.value:
               self.stock_sackson += n
               sackson.sellstock(n)
            elif value == worldwide.value:
               self.stock_worldwide += n
               worldwide.sellstock(n)
         
        #decide...stupid 
        def decide_merge(self,hotel1,hotel2):
            m1,t1,c1,a1,i1,f1,s1,w1=self.info()
            hilfsarray=np.array([w1,s1,f1,i1,a1,c1,t1])
    
            maj1,minn1 = majmin(hotel1)
            maj2,minn2 = majmin(hotel2)
            M1=False
            m1=False
            M2=False
            m2=False
            for i in range(len(maj1)):
                if maj1[i].name==self.name:
                    M1=True
            for i in range(len(minn1)):
                if minn1[i].name==self.name:
                    m1=True
            for i in range(len(maj2)):
                if maj2[i].name==self.name:
                    M2=True
            for i in range(len(minn2)):
                if minn2[i].name==self.name:
                    m2=True
            
            if M1==True and M2==False:
                if np.abs(hilfsarray[hotel1.value-2]-hotel1.stock)<=5 and hilfsarray[hotel1.value-2]>=5 and self.money>=3000:
                    return hotel1,hotel2
                else: 
                    return hotel2,hotel1
            elif M2==True and M1==False:
                if np.abs(hilfsarray[hotel2.value-2]-hotel2.stock)<=5 and hilfsarray[hotel2.value-2]>=5 and self.money>=3000:
                    return hotel2,hotel1
                else: 
                    return hotel1,hotel2
                
            elif M1==True and M2 == True:
                if self.difference_to_maj(hotel1)>=self.difference_to_maj(hotel2):
                    return hotel1,hotel2
                else:
                    return hotel2,hotel1
                
            elif m1==True and m2==False:
                if np.abs(hilfsarray[hotel1.value-2]-hotel1.stock)<=5 and hilfsarray[hotel1.value-2]>=5 and self.money>=3000:
                    return hotel1,hotel2
                else: 
                    return hotel2,hotel1
            elif m2==True and m1==False:
                if np.abs(hilfsarray[hotel2.value-2]-hotel2.stock)<=5 and hilfsarray[hotel2.value-2]>=5 and self.money>=3000:
                    return hotel2,hotel1
                else: 
                    return hotel1,hotel2
           
            elif m1==True and m2 == True:
                if self.difference_to_maj(hotel1)<=self.info_stock(hotel1.value)/2:
                    return hotel1,hotel2
                elif self.difference_to_maj(hotel2)<=self.info_stock(hotel1.value)/2:
                    return hotel2,hotel1
                elif self.money>=3000 and hilfsarray[hotel1.value-2]>=hilfsarray[hotel2.value-2]:
                    return hotel1,hotel2
                elif self.money>=3000 and hilfsarray[hotel1.value-2]<hilfsarray[hotel2.value-2]:
                    return hotel2,hotel1
                elif self.money<3000 and hilfsarray[hotel1.value-2]>=hilfsarray[hotel2.value-2]:
                    return hotel2,hotel1
                elif self.money>=3000 and hilfsarray[hotel1.value-2]<hilfsarray[hotel2.value-2]:
                    return hotel1,hotel2
            else:
                if hilfsarray[hotel1.value-2]>=hilfsarray[hotel2.value-2]:
                    return hotel1,hotel2
                else:
                    return hotel2,hotel1
            
        
        def decide_triple_merge(self,hotel1,hotel2,hotel3):
            big,small=self.decide_merge(hotel1,hotel2)
            a,b = self.decide_merge(big,hotel3)
            return a,b,small
        
        def decide_double_merge(self,hotel1,hotel2):
            return self.decide_merge(hotel1,hotel2)
        
        def decide_quad_merge(self,hotel1,hotel2,hotel3,hotel4):
            big,small1,small2=self.decide_triple_merge(hotel1,hotel2,hotel3)
            a,b = self.decide_merge(big,hotel4)
            return a,b,small1,small2
        
        def decide_newhotel(self):
            m1,t1,c1,a1,i1,f1,s1,w1 = self.info()
            stocks=np.array([w1,s1,f1,i1,a1,c1,t1])
            hlist=[]
            hlist2=[]
            for i in range(2,9):
                if eval_hotel(i).size==0:
                    hlist.append(eval_hotel(i))
                    hlist2.append(eval_hotel(i))
            prefhotel=hlist[0]
            for i in range(len(hlist)):
                if stocks[hlist[i].value-2]>stocks[prefhotel.value-2]:
                    prefhotel=hlist[i]
            if stocks[prefhotel.value-2]>0:
                return prefhotel
            for k in range(7):
                for i in range(len(hlist2)):
                    if hlist2[i].stock<25:
                        hlist2.pop(len(hlist2)-1-i)
                        break
            if len(hlist2)>0:
                r = random.randint(0,len(hlist2)-1)
                return hlist2[r]
            else:
                r = random.randint(0,len(hlist)-1)
                return hlist[r]
            
    
    def merge(hotel1,hotel2,babo,n):
        #print("merging hotels",hotel1.name,'and',hotel2.name)
        if hotel1.size > hotel2.size:
            big = hotel1
            small = hotel2     
        elif hotel1.size < hotel2.size:
            big = hotel2
            small = hotel1
        elif hotel1.size == hotel2.size:
            big,small=babo.decide_merge(hotel1,hotel2)
            
       
        maj,minn = majmin(small)
        big.adsize(small.size+n)
        
        #set_money aufrufen um bonus auszuzahlen
        pr, majo, mino = small.reference()
        if len(maj) > 1:
            bonus = (majo +mino)/len(maj)
            for i in range(len(maj)):
                maj[i].set_money(bonus)
        else:
            maj[0].set_money(majo)
            if len(minn) == 0:
                maj[0].set_money(mino)
            else:
                for i in range(len(minn)):
                    minn[i].set_money(mino/len(minn))
        
        #ask babo
        babo.decide_merge_stock(big,small)
        
        
        #ask next_player(babo)
        next1 = next_player(babo)
        next1.decide_merge_stock(big,small)
        next2 = next_player(next1)
        next2.decide_merge_stock(big,small)
        next3 = next_player(next2)
        next3.decide_merge_stock(big,small)
        
        #covvert tiles of small hotel to big hotel
        for i in range(9):
            for j in range(12):
                if board[i,j]==small.value:
                    board[i,j]=big.value
        
        small.size = 0
        #print()
        return big
    
    def hotel_rank(hotel):
        a=1
        for i in range(2,9):
            if eval_hotel(i).size>hotel.size:
                a+=1
        return a
    
    def initial_advantage(stocklist,A):
        if stocklist[3]>3:
            return A[3],False,False
        elif stocklist[3]==3:
            return A[2],True,False
        elif stocklist[3]==2:
            return A[1],False,True
        elif stocklist[3]==1:
            return A[0],False,False
    
    def defence(stocklist,hotel,A):
        lead=stocklist[3]-stocklist[2]
        if lead>hotel.stock:
            return 0,False,False
        if stocklist[3]>=13:
            return 0,False,False
        
        if lead>6:
            row = 0
        elif lead==6:
            row=1
        elif lead==5:
            row=2
        elif lead==4:
            row=3
        elif lead==3:
            row=4
        elif lead==2:
            row=5
        elif lead==1:
            row=6
        elif lead==0:
            row=7
        
        if hotel.stock>6:
            coulumn=7
        else:
            coulumn=hotel.stock
        
        res=A[row,coulumn]
        if res==50:
            return 1,True,False
        elif res == 100:
            return 1,False,True
        else:
            return res,False,False
    
    def inthehunt(stocklist,playerstock,hotel,A):
        deficit=stocklist[3]-playerstock
        if deficit>hotel.stock:
            return 0,False,False
        
        row=deficit-1
        if hotel.stock>6:
            coulumn=7
        else:
            coulumn=hotel.stock
        
        res=A[row,coulumn]
        if res == 100:
            return 1,False,True
        else:
            return res,False,False
    
    def browns(stocklist,playerstock,hotel,A1,A2,A3):
        deficit=stocklist[2]-playerstock
        #player is the minority shareholder
        if deficit==0:
            minlist=[]
            for i in range(3):
                minlist.append(stocklist[i])
            minlist.append(0)
            minlist.sort()
            res,h1s,h2s=defence(minlist,hotel,A1)
            return A3[0]*res,h1s,h2s
        
        #player is not the minority shareholder but 3 or less shares behind
        elif deficit<=3:
            minlist=[]
            for i in range(3):
                minlist.append(stocklist[i])
            minlist.append(0)
            minlist.sort()
            res,h1s,h2s=inthehunt(minlist,playerstock,hotel,A2)
            return A3[1]*res,h1s,h2s
        
        #player is not the minority and far behind
        else:
            if deficit<=5:
                return A3[2],False,False
            else:
                return A3[3],False,False
    
    def alpha(hotel,tiles,A):
        a=1
        b=np.sqrt(hotel.size)*A[0]
        a+=b
        c=hotel.group*A[1]
        a+=c
        #add information about tiles!
        return a
    
    def hold_stock(stocks,n,A):
        b=0
        for i in range(A[:,0].size):
            if turn<=A[i,0] and stocks[2]<=A[i,1] and n>=A[i,2]:
                b=A[i,3]
                break
        return b
        
    def eval_hotel(n):
        if n==2:
            return worldwide
        if n==3:
            return sackson
        if n==4:
            return festival
        if n==5:
            return imperial
        if n==6:
            return american
        if n==7:
            return continental
        if n==8:
            return tower
        
    def majmin(hotel):
        # determine Majority, minority player
        m1,t1,c1,a1,i1,f1,s1,w1 = player1.info()
        m2,t2,c2,a2,i2,f2,s2,w2 = player2.info()
        m3,t3,c3,a3,i3,f3,s3,w3 = player3.info()
        m4,t4,c4,a4,i4,f4,s4,w4 = player4.info()
        
        maj = []
        minn = []
                    
        ttot = np.array([[w1,s1,f1,i1,a1,c1,t1],
                         [w2,s2,f2,i2,a2,c2,t2],
                         [w3,s3,f3,i3,a3,c3,t3],
                         [w4,s4,f4,i4,a4,c4,t4]])
        for i in range(2,9):
            if hotel.value==i:
                tt = [ttot[0,i-2],ttot[1,i-2],ttot[2,i-2],ttot[3,i-2]]
                tt.sort()
                s = tt[2]
                t = tt[3]
                if t == ttot[0,i-2]:
                    maj.append(player1)
                if t == ttot[1,i-2]:
                    maj.append(player2)
                if t == ttot[2,i-2]:
                    maj.append(player3)
                if t == ttot[3,i-2]:
                    maj.append(player4)
            
                if len(maj)<2 and s!= 0:
                    if s == ttot[0,i-2]:
                        minn.append(player1)
                    if s == ttot[1,i-2]:
                        minn.append(player2)
                    if s == ttot[2,i-2]:
                        minn.append(player3)
                    if s == ttot[3,i-2]:
                        minn.append(player4)
        return maj,minn
    
    def is_legal(x0):
        info = tile_info(x0)
        if worldwide.size !=0 and sackson.size !=0 and festival.size !=0 and imperial.size!=0 and american.size!=0 and continental.size!=0 and tower.size!=0:
            for i in range(4):
                if info[i]==1:
                    return False
        info.sort()
        a = 0
        for i in range(3):
            if info[i] > 1:
                if eval_hotel(info[i]).size >10 and info[i]!=info[i+1]:
                    a+=1
                    
        if info[3]>1:
            if eval_hotel(info[3]).size >10:
                a+=1
            
        if a > 1 :
            return False
        
        return True
    
    def is_hotel():
        hot = []
        for i in range(2,9):
            a =eval_hotel(i)
            if a.size >0:
                hot.append(a)
        return hot
            
    
    def tile_info(x0):
        
        up=1
        left=1
        down=1
        right=1
        
        if x0[0]==0 or board[x0[0]-1,x0[1]]==0:
            up=0
           
        if x0[1]==0 or board[x0[0],x0[1]-1]==0:
            left=0
            
        if x0[0]==8 or board[x0[0]+1,x0[1]]==0:
            down=0
            
        if x0[1]==11 or board[x0[0],x0[1]+1]==0:
            right=0
        
        if up!=0:
            up=board[x0[0]-1,x0[1]]
        if left!=0:
            left=board[x0[0],x0[1]-1]
        if down!=0:
            down=board[x0[0]+1,x0[1]]
        if right!=0:
            right=board[x0[0],x0[1]+1]
        
        info=[up,left,down,right]
        return info
    
    
    def hotel_creation(size,x0,info,player):
        newhotel = player.decide_newhotel()
        newhotel.adsize(size)
        
        if newhotel.stock != 0: 
            player.getstock(newhotel.value,1,True)
        
        x = newhotel.value
        board[x0[0],x0[1]]=x
        if info[0]==1:
            board[x0[0]-1,x0[1]]=x
        if info[1]==1:
            board[x0[0],x0[1]-1]=x
        if info[2]==1:
            board[x0[0]+1,x0[1]]=x
        if info[3]==1:
            board[x0[0],x0[1]+1]=x
        #print(newhotel.name,"has been created")
        #print()
        return 
        
    
    def placetile(x0,player):
    
        info=tile_info(x0)
        infosort=[]
        for i in range(4):
            infosort.append(info[i])
        infosort.sort()
        n = 0 #number of non-empty tiles
        for i in range(len(info)):
            if info[i] !=0:
                n += 1
        n0=4-n #number of empty tiles
        n1=0 #number of single tiles
        for i in range(len(info)):
            if info[i] ==1:
                n1 += 1
        
        #number of hotels surrounding tile
        m = 0
        m1 = []
        for i in range(4):
            if info[i] > 1:
                b = True
                for j in range(len(m1)):
                    if info[i]==m1[j]:
                        b = False
                m1.append(info[i]) 
                if b ==True:
                    m+=1
        
        #only tile placement        
        if n==0:
            board[x0[0],x0[1]]=1
            
        #hotel creation  
        if n1>=1 and (n0+n1)==4:
            newsize=n1+1
            hotel_creation(newsize,x0,info,player)
        
        #hotel growth
        if m == 1:
            for i in range(4):
                if info[i]!=0 and info[i]!=1:
                    x=info[i]
            
            if x==2:
                worldwide.adsize(n1+1)
            if x==3:
                sackson.adsize(n1+1)
            if x==4:
                festival.adsize(n1+1)
            if x==5:
                imperial.adsize(n1+1)
            if x==6:
                american.adsize(n1+1)
            if x==7:
                continental.adsize(n1+1)
            if x==8:
                tower.adsize(n1+1)
            
            board[x0[0],x0[1]]=x
            if info[0]==1:
                board[x0[0]-1,x0[1]]=x
            if info[1]==1:
                board[x0[0],x0[1]-1]=x
            if info[2]==1:
                board[x0[0]+1,x0[1]]=x
            if info[3]==1:
                board[x0[0],x0[1]+1]=x
        
        
        #merge 2 hotels
        elif m == 2:
            hotel1=eval_hotel(infosort[3])
            if infosort[3]!=infosort[2]:
                hotel2=eval_hotel(infosort[2])
            elif infosort[3]!=infosort[1]:
                hotel2=eval_hotel(infosort[1])
            else:
                hotel2=eval_hotel(infosort[0])
                
            newhotel = merge(hotel1,hotel2,player,n1+1)
            
            x=newhotel.value
            board[x0[0],x0[1]]=x
            if info[0]==1:
                board[x0[0]-1,x0[1]]=x
            if info[1]==1:
                board[x0[0],x0[1]-1]=x
            if info[2]==1:
                board[x0[0]+1,x0[1]]=x
            if info[3]==1:
                board[x0[0],x0[1]+1]=x
        
        
        #merge 3 hotels
        elif m==3:
            #print("merging 3 hotels")
            hotel1=eval_hotel(infosort[3])
            if infosort[2]!=infosort[3]:
                hotel2=eval_hotel(infosort[2])
                if infosort[1]!=infosort[2]:
                    hotel3=eval_hotel(infosort[1])
                else:
                    hotel3=eval_hotel(infosort[0])
                
            else:
                hotel2=eval_hotel(infosort[1])
                hotel3=eval_hotel(infosort[0])
            
            hlist=[hotel1,hotel2,hotel3]
            
            if hotel1.size>hotel2.size and hotel1.size>hotel3.size:
                big=hotel1
            elif hotel2.size>hotel1.size and hotel2.size>hotel3.size:
                big=hotel2
            elif hotel3.size>hotel1.size and hotel3.size>hotel2.size:
                big=hotel3
            elif hotel1.size==hotel2.size and hotel1.size>hotel3.size:
                big,small1=player.decide_merge(hotel1,hotel2)
                small2=hotel3
            elif hotel3.size==hotel2.size and hotel3.size>hotel1.size:
                big,small1=player.decide_merge(hotel3,hotel2)
                small2=hotel1
            elif hotel1.size==hotel3.size and hotel1.size>hotel2.size:
                big,small1=player.decide_merge(hotel1,hotel3)
                small2=hotel2
            else:
                big,small1,small2=player.decide_triple_merge(hotel1,hotel2,hotel3)
                
            for i in range(3):
                #print("hlist:",len(hlist))
                #print(2-i)
                if hlist[2-i]==big:
                    hlist.pop(2-i)
            if hlist[0].size>hlist[1].size:
                small1=hlist[0]
                small2=hlist[1]
            elif hlist[1].size>hlist[0].size:
                small1=hlist[1]
                small2=hlist[0]
            elif hlist[1].size==hlist[0].size:
                small1,small2=player.decide_double_merge(hlist[0],hlist[1])
            newhotel1=merge(big,small1,player,n1+1)
            newhotel2=merge(newhotel1,small2,player,0)
            
            x=newhotel2.value
            board[x0[0],x0[1]]=x
            if info[0]==1:
                board[x0[0]-1,x0[1]]=x
            if info[1]==1:
                board[x0[0],x0[1]-1]=x
            if info[2]==1:
                board[x0[0]+1,x0[1]]=x
            if info[3]==1:
                board[x0[0],x0[1]+1]=x
        
            
        #merge 4 hotels
        elif m==4:
            #print("merging 4 hotels")
            hotel1=eval_hotel(infosort[3])
            hotel2=eval_hotel(infosort[2])
            hotel3=eval_hotel(infosort[1])
            hotel4=eval_hotel(infosort[0])
            
            hlist=[hotel1,hotel2,hotel3,hotel4]
            hlist1=[hotel1,hotel2,hotel3,hotel4]
            a=0
            b=0
            c=0
            
            if hotel1.size>hotel2.size and hotel1.size>hotel3.size and hotel1.size>hotel4.size:
                big=hotel1
                a=1
            elif hotel2.size>hotel1.size and hotel2.size>hotel3.size and hotel2.size>hotel4.size:
                big=hotel2
                a=1
            elif hotel3.size>hotel2.size and hotel3.size>hotel1.size and hotel3.size>hotel4.size:
                big=hotel3
                a=1
            elif hotel4.size>hotel2.size and hotel4.size>hotel3.size and hotel4.size>hotel1.size:
                big=hotel4
                a=1
        
            
            if a==1:
                
                for i in range(4):
                    if hlist1[3-i]==big:
                        hlist1.pop(3-i)
                        
                if hlist1[0].size == hlist1[1].size and hlist1[0].size > hlist1[2].size:
                    small1,small2=player.decide_double_merge(hlist1[0],hlist1[1])
                    small3=hlist1[2]
                    c=1
                        
                elif hlist1[0].size == hlist1[2].size and hlist1[0].size > hlist1[1].size:
                    small1,small2=player.decide_double_merge(hlist1[0],hlist1[2])
                    small3=hlist1[1]
                    c=1
                    
                elif hlist1[2].size == hlist1[1].size and hlist1[1].size > hlist1[0].size:
                    small1,small2=player.decide_double_merge(hlist1[2],hlist1[1])
                    small3=hlist1[0]
                    c=1
                        
                elif hlist1[0].size==hlist1[1] and hlist1[0].size==hlist1[2].size:
                    small1,small2,small3=player.decide_triple_merge(hlist[0],hlist1[1],hlist1[2])
                    c=1
                
                elif hlist1[0].size>hlist1[1].size and hlist1[0].size>hlist1[2].size:
                    small1 = hlist1[0]
                elif hlist1[1].size>hlist1[0].size and hlist1[1].size>hlist1[2].size:
                    small1 = hlist1[1]
                elif hlist1[2].size>hlist1[1].size and hlist1[2].size>hlist1[0].size:
                    small1 = hlist1[2]
                else:
                    small1=hlist1[0]
                
                if c==0:
                    for i in range(3):
                        if hlist1[2-i]==small1:
                            hlist1.pop(2-i)
                    if hlist1[0].size>hlist1[1].size:
                        small2=hlist1[0]
                        small3=hlist1[1]
                    elif hlist1[1].size>hlist1[0].size:
                        small2=hlist1[1]
                        small3=hlist1[0]
                    elif hlist1[1].size==hlist1[0].size:
                        small2,small3=player.decide_double_merge(hlist1[0],hlist1[1])
            
                
            elif hotel1.size == hotel2.size and hotel1.size > hotel3.size and hotel1.size > hotel4.size:
                big,small1=player.decide_merge(hotel1,hotel2)
                b=1
                    
            elif hotel1.size == hotel3.size and hotel1.size > hotel2.size and hotel1.size > hotel4.size:
                big,small1=player.decide_merge(hotel1,hotel3)
                b=1
                    
            elif hotel1.size == hotel4.size and hotel1.size > hotel3.size and hotel1.size > hotel2.size:
                big,small1=player.decide_merge(hotel1,hotel4)
                b=1
                    
            elif hotel3.size == hotel2.size and hotel3.size > hotel1.size and hotel3.size > hotel4.size:
                big,small1=player.decide_merge(hotel3,hotel2)
                b=1
                    
            elif hotel4.size == hotel2.size and hotel4.size > hotel3.size and hotel4.size > hotel1.size:
                big,small1=player.decide_merge(hotel4,hotel2)
                b=1
                    
            elif hotel3.size == hotel4.size and hotel3.size > hotel1.size and hotel3.size > hotel2.size:
                big,small1=player.decide_merge(hotel3,hotel4)
                b=1
                
            if b==1:
                for i in range(4):
                    if hlist[3-i]== big:
                         hlist.pop(3-i)
                    elif hlist[3-i]==small1:
                        hlist.pop(3-i)
                if hlist[0].size>hlist[1].size:
                    small2=hlist[0]
                    small3=hlist[1]
                elif hlist[1].size>hlist[0].size:
                    small2=hlist[1]
                    small3=hlist[0]
                elif hlist[1].size==hlist[0].size:
                    small2,small3=player.decide_double_merge(hlist[0],hlist[1])
            
            elif hotel1.size==hotel2.size and hotel1.size>hotel3.size:
                big,small1,small2=player.decide_triple_merge(hotel1,hotel2,hotel4)
                small3=hotel3
            elif hotel1.size==hotel2.size and hotel1.size>hotel4.size:
                big,small1,small2=player.decide_triple_merge(hotel1,hotel2,hotel3)
                small3=hotel4
            elif hotel2.size==hotel3.size and hotel2.size>hotel1.size:
                big,small1,small2=player.decide_triple_merge(hotel4,hotel2,hotel3)
                small3=hotel1
            elif hotel1.size==hotel3.size and hotel1.size>hotel2.size:
                big,small1,small2=player.decide_triple_merge(hotel1,hotel4,hotel3)
                small3=hotel2
            elif hotel1.size == hotel2.size and hotel1.size==hotel3.size and hotel1.size==hotel4.size:
                big,small1,small2,small3=player.quad_merge(hotel1,hotel2,hotel3,hotel4)
            
            newhotel1=merge(big,small1,player,n1+1)
            newhotel2=merge(newhotel1,small2,player,0)
            newhotel3=merge(newhotel2,small3,player,0)
            
            x=newhotel3.value
            board[x0[0],x0[1]]=x
            
        return
            
            
    def chart(n):
        return n*100.,n*1000.,n*500.
    
    #wrong
    def is_adjacent(x0,x1):
        if abs(x0[0]-x1[0]) == 1 :
            return True
        elif abs(x0[1]-x1[1]) == 1 :
            return True
        return False
    
    
    def next_player(player):
        if player == player1:
            return player2
        elif player == player2:
            return player3
        elif player == player3:
            return player4
        elif player == player4:
            return player1
        
    def first_player():
        a = random.randint(1,4)
        if a == 1:
            return player1
        elif a == 2:
            return player2
        elif a == 3:
            return player3
        elif a == 4:
            return player4
        
    def is_gameover():
        #if turn ==20:
            #return True
        if len(alltiles)==0:
            #print("No more tiles")
            return True
        
        for i in range (2,9):
            if eval_hotel(i).size >=41:
                return True
        a=0
        b=0
        for i in range(2,9):
            if eval_hotel(i).size >=11:
                a+=1
            elif eval_hotel(i).size == 0:
                b+=1
        if a+b == 7 and a>3:
            return True
        return False
    
    
    def gameover():
        for i in range(2,9):
            hotel = eval_hotel(i)
            if hotel.size !=0:
                #print("hotel: ",hotel.name)
                # determine Majority, minority player
                m1,t1,c1,a1,i1,f1,s1,w1 = player1.info()
                m2,t2,c2,a2,i2,f2,s2,w2 = player2.info()
                m3,t3,c3,a3,i3,f3,s3,w3 = player3.info()
                m4,t4,c4,a4,i4,f4,s4,w4 = player4.info()
                
                maj = []
                minn = []
                            
                ttot = np.array([[w1,s1,f1,i1,a1,c1,t1],
                                 [w2,s2,f2,i2,a2,c2,t2],
                                 [w3,s3,f3,i3,a3,c3,t3],
                                 [w4,s4,f4,i4,a4,c4,t4]])
                
                tt = [ttot[0,i-2],ttot[1,i-2],ttot[2,i-2],ttot[3,i-2]]
                tt.sort()
                s = tt[2]
                t = tt[3]
                if t == ttot[0,i-2]:
                    maj.append(player1)
                if t == ttot[1,i-2]:
                    maj.append(player2)
                if t == ttot[2,i-2]:
                    maj.append(player3)
                if t == ttot[3,i-2]:
                    maj.append(player4)
                    
                if len(maj)<2 and s!= 0:
                    if s == ttot[0,i-2]:
                        minn.append(player1)
                    if s == ttot[1,i-2]:
                        minn.append(player2)
                    if s == ttot[2,i-2]:
                        minn.append(player3)
                    if s == ttot[3,i-2]:
                        minn.append(player4)
                '''    
                for k in range(len(maj)):
                    print("Majority",k+1,":",maj[k].name)
                    
                for k in range(len(minn)):
                    print("Minority",k+1,":",minn[k].name)
                '''
                
                #set_money aufrufen um bonus auszuzahlen
                
                pr, majo, mino = hotel.reference()
                
                if len(maj) > 1:
                    bonus = (majo +mino)/len(maj)
                    for h in range(len(maj)):
                        maj[h].set_money(bonus)
                else:
                    maj[0].set_money(majo)
                    if len(minn) == 0:
                        maj[0].set_money(mino)
                    else:
                        for h in range(len(minn)):
                            minn[h].set_money(mino/len(minn))
                    
                player1.sellstock(hotel.value,ttot[0,i-2])
                player2.sellstock(hotel.value,ttot[1,i-2])
                player3.sellstock(hotel.value,ttot[2,i-2])
                player4.sellstock(hotel.value,ttot[3,i-2])
            
        money1 = player1.money
        money2 = player2.money
        money3 = player3.money
        money4 = player4.money
    
        
        ranking = [money1,money2,money3,money4]
        ranking.sort()
        '''
        print("Money Player1:", money1)
        print("Money Player2:", money2)
        print("Money Player3:", money3)
        print("Money Player4:", money4)
        print()
        '''
        
        """
        if ranking[3] == player1.money:
            print("Winner:","player1")
        
        if ranking[3] == player2.money:
            print("Winner:","player2")
        
        if ranking[3] == player3.money:
            print("Winner:","player3")
         
        if ranking[3] == player4.money:
            print("Winner:","player4")
        """
        plranking=[]
        for i in range(4):
            if ranking[3-i] == player1.money:
                plranking.append(player1.name)
            
            elif ranking[3-i] == player2.money:
                plranking.append(player2.name)
                
            elif ranking[3-i] == player3.money:
                plranking.append(player3.name)
                
            elif ranking[3-i] == player4.money:
                plranking.append(player4.name)
                
       
            
        return plranking
    
    def status():
        print()
        print(board)
        print()
        
        m1,t1,c1,a1,i1,f1,s1,w1=player1.info()
        m2,t2,c2,a2,i2,f2,s2,w2=player2.info()
        m3,t3,c3,a3,i3,f3,s3,w3=player3.info()
        m4,t4,c4,a4,i4,f4,s4,w4=player4.info()
        
        print("player 1:",m1,t1,c1,a1,i1,f1,s1,w1)
        print("player 2:",m2,t2,c2,a2,i2,f2,s2,w2)
        print("player 3:",m3,t3,c3,a3,i3,f3,s3,w3)
        print("player 4:",m4,t4,c4,a4,i4,f4,s4,w4)
        print()
        print("Tower:      ",tower.info())
        print("Continental:",continental.info())
        print("American:   ",american.info())
        print("Imerial:    ",imperial.info())
        print("Festival:   ",festival.info())
        print("Sackson:    ",sackson.info())
        print("Worldwide:  ",worldwide.info())
        
        print()
        
        return
        
    
        
    #Game start
        
    board = np.zeros((9,12))
        
    alltiles = []
    for i in range(12):
        for j in range(9):
            alltiles.append(np.array([j,i]))
        
    worldwide = Hotel(1,2,"worldwide")     #2
    sackson = Hotel(1,3,"sackson")         #3
    festival = Hotel(2,4,"festival")       #4
    imperial = Hotel(2,5,"imperial")       #5
    american = Hotel(2,6,"american")       #6
    continental = Hotel(3,7,"continental") #7
    tower = Hotel(3,8,"tower")             #8
                
    player1 = Player_adapt(6000,"player1")
    player2 = Player_dumb(6000,"player2")
    player3 = Player_entrepreneur(6000,"player3")
    player4 = Player_small_hotels(6000,"player4")
        
    activeplayer = first_player()
        
    for i in range(6):
        #print(i)
        player1.drawtile(alltiles)
        player2.drawtile(alltiles)
        player3.drawtile(alltiles)
        player4.drawtile(alltiles)
        #print(player1.tiles)
        #print()
        #print(player2.tiles)
        
    #print("initialisation complete")
    #print(board)
    #print("Player1 tiles:",player1.tiles)
        
    a = False
    b=False
    turn = 0
    while a == False and b==False:
        #print("-------------------------------------------------------")
        turn += 1
        #print("Turn:",turn)
        #print("It is",activeplayer.name,"turn")
        #print()
        #print()
        #print(board)
        #print()
            
        b=activeplayer.decide_placetile()
        activeplayer.buy_stock()
        activeplayer.drawtile(alltiles)
        #status()
        
        activeplayer = next_player(activeplayer)
        a = is_gameover()
        
    plranking=gameover()
    return plranking

t1=time.time()
p1=np.array([0,0,0,0])
p2=np.array([0,0,0,0])
p3=np.array([0,0,0,0])
p4=np.array([0,0,0,0])   

for i in range(1000):
    rank=game()
    for j in range(4):
        if rank[j]=="player1":
            p1[j]+=1
        if rank[j]=="player2":
            p2[j]+=1
        if rank[j]=="player3":
            p3[j]+=1
        if rank[j]=="player4":
            p4[j]+=1

t2=time.time()
            
            
p=np.array([p1[0],p2[0],p3[0],p4[0]])
x=("1","2","3","4")
plt.bar(x,p,width=0.5)
plt.xlabel("players")
plt.ylabel("wins")
plt.show()

print()
print(p1)
print()
print(p2)
print()
print(p3)
print()
print(p4)
print()
print("Time:",t2-t1)
print()

print("We are all Patriots!!!")