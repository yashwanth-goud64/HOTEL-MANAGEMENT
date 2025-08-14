from subprocess import*
from os import*
call('color B4',shell=True)
def hotelmanagement():
    print ('''
       ###################################################################
       #                                                                 #
       #                 COMPUTER SCIENCE PROJECT                        #
       #                 ------------------------                        #
       # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #
       # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #                    
       #         H O T E L  M A N A G E M E N T  S Y S T E M             #
       #        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^            #
       #                                                                 #
       #                                                                 #
       #                                                                 #
       #                                                                 #
       #                                                                 #
          ''')
    print ('''




       
               ''')
          
    a=input(" press 'y' to enter  ")
    if(a=='y'):
        system('cls')
        call('color 71',shell=True)
        print ('''


                             !!!!!!!!!!!!!!!!!!!!!!!
              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
              *@                                                     @*
               @*      It's written on the walls of this hotel      *@
               *@                                                   @*
                @*       You go to heaven once you've been to      *@
                *@                                                 @*
                 @*                    hell                       *@
                  @*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@
                              ++++++++++++++++++++++
              ''')
    else:
        hotelmanagement()
    a=input(" press 'y' to enter")
    if(a=='y'):
        mainpage()
    if(option=='exit'):
        hotelmanagement()
    else:
        exit()
def mainpage():
    system('cls')
    call('color 75',shell=True)
    print ('''

                         $$$$$$$$$$$$$$$
              !!!*********************************!!!
                  P R I N C E   A P A R T M E N T
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                ***********************************
          ''')
    print ('''
             ************************************
             *      Press.1-- Hotel INFO        *
             *      Press.2-- Hotel Preview     *
             *      Press.3-- Front Office      *
             *      Press.4-- Banquet           *
             *                                  *
             ************************************
          ''')
    a=input('  Choose to Enter  ')
    if(a=='1'):
        masters()
    if(a=='2'):
        hotelpreview()
    if(a=='3'):
        frontoffice()
    if(a=='4'):
        banquet()
    if(option=='exit'):
        mainpage()
    else:
        mainpage()
def hotelpreview():
    system('cls')
    print ('''
               1-ROOM TYPES
               2-FOOD TYPES
          ''')
    a=input(" choose to enter or press 'b' to go to mainpage ")
    if(a=='1'):
        roomtype()
    if(a=='2'):
        foodtype()
    if(a=='b'):
        mainpage()
    if(option=='exit'):
        mainpage()
    else:
        hotelpreview()
def roomtype():
    print ('''
                 :--R O O M   L A Y O U T   D E T A I L S --:
          ''')
    print ('''
                   DELUX-1
        1-Room              Cost:- Rs 2000 per day
        1-Washroom          Service Tax:- Rs 100
        1-Balcony           Electricity bill charges included as per used units
                   DELUX-2

        2-Rooms             Cost:3500 per day
        1-Washroom          Service Tax:- Rs 200
        1-Balcony           Electricity bill charges included as per used units
                   DELUX-3

        3-Rooms             Cost:5000 per day                 
        2-Washrooms         Service Tax:- Rs 300  
        1-Balcony           Electricity bill charges included as per used units
                   DELUX-4

        2-Rooms             Cost:5500 per day
        1-Hall              Service Tax:- Rs 300
        2-Washroom          Electricity bill charges included as per used units
          ''')
    a=input(" press 'b' to go back")
    if(a=='b'):
        hotelpreview()
    if(option=='exit'):
        mainpage()
    else:
        roomtype()
def foodtype():
    print ('''
                   @@::FOOD MENU::@@
          ''')
    menu()
    a=input(" press 'b' to go back")
    if(a=='b'):
        hotelpreview()
    if(option=='exit'):
        mainpage()
    else:
        foodtype()
def frontoffice():
    system('cls')
    print ('''
                ^^^^^^^^^^^^^^^
                 1-MASTERS
                 2-TRANSACTION
                 3-REPORTS
                ***************
         ''')
    option=input(" press to enter or 'b' for mainpage")
    if(option=='1'):
        masters()
    if(option=='2'):
        transaction()
    if(option=='3'):
        reports()
    if(option=='b'):
        mainpage()
    if(option=='exit'):
        mainpage()
    else:
        frontoffice()
def masters():
    system('cls')
    print ('''

              +++++++++++++++++++++++
              +  1.Hotel Profile    +
              +  2.Tax Master       +
              +  3.Charges Master   +
              +  4.Room Type Master +
              +  5.Floor Master     + 
              +  6.Country          +
              +  7.State            +
              +  8.City             +
              +  9.Proof Type       +
              +++++++++++++++++++++++
          ''')
    option=input("  press 'b' to go back  ")
    if(option=='1'):
        system('cls')
        print ('''

                    ***********************************
                    @ P R I N C E   A P A R T M E N T @
                    ***********************************
                     
          H.NO.727,Near BSE, Sikargarh,Jodhpur,Rajasthan-342001
          
          -----------CONTACT:0180-764218,764432----------------

          ==========E-mail:ppapartment727@gmail.com============
              ''')
    if(option=='2'):
        system('cls')
        print ('''
                now no Tax
              ''')
    if(option=='3'):
        system('cls')
        print ('''
                 no charge now
              ''')
    if(option=='4'):
        system('cls')
        roomtype()
    if(option=='5'):
        system('cls')
        print ('''
                 single floor now
              ''')
    if(option=='6'):
        system('cls')
        print ('''
                  now in INDIA
              ''')
    if(option=='7'):
        system('cls')
        print ('''
                  Rajasthan
              ''')
    if(option=='8'):
        system('cls')
        print ('''
                 jodhpur
              ''')
    if(option=='9'):
        system('cls')
        print ('''
                   **************
                    AADHAR CARD
                   **************

                 *****************
                  DRIVING LICENSE
                 *****************

                    **********
                     VOTER ID
                    **********

            OR ANY GOVERMENTAL APPROVED:
              ''')
    option=input(" Press 'b' to go back ")
    if(option=='b'):
        frontoffice()
    if(option=='exit'):
        mainpage()
    else:
        masters()
def transaction():
    system('cls')
    print ('''
              #__________________#
              
                  1-Booking
                  2-Check-In
                  3-Check-Out

              #___________________#
          ''')
    option=input("  choose to enter or 'b' to go back  ")
    if(option==1):
        booking()
    if(option==2):
        checkin()
    if(option==3):
        checkout()
    if(option=='b'):
        frontoffice()
    if(option=='exit'):
        mainpage()
    else:
        transaction()
def booking():
    system('cls')
    print ('''
            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            %=== B O O K I N G   I N F O R M A T I O N === %
            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
          ''')
    custid=input(' CUSTOMER ID  ')
    name=input(' NAME  ')
    gender=input(' GENDER  ')
    address=input(' ADDRESS  ')
    pincode=input(' PINCODE  ')
    prooftype=input(' PROOF TYPE  ')
    proofvalue=input(' PROOF VALUE  ')
    email=input(' E-MAIL ID  ')
    phoneno=input(' PHONE NO.  ')
    bookinginfo={'CUSTOMER ID':custid,'NAME':name,'GENDER':gender,
                 'ADDRESS':address,'PINCODE':pincode,'PROOF TYPE':prooftype,
                 'PROOF VALUE':proofvalue,'E-MAIL ID':email,
                 'PHONE NO.':phoneno}
    print (bookinginfo)
    option=input(" Press 'b' to go back ")
    if(option=='b'):
        frontoffice()
    if(option=='exit'):
        mainpage()
    else:
        booking()
def checkin():
    system('cls')
    print ('''
            &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
            &==== C H E C K - I N   D E T A I L S =====&
            &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
          ''')
    custid=input(' CUSTOMER ID  ')
    custname=input('  CUSTOMER NAME  ')
    checdate=input(' CHECK-IN DATE  ')
    noadult=input(' No. of ADULTS  ')
    nochild=input(' No. of CHILDS  ')
    option=input("for billing info press 'v' or 'b' to go back  ")
    if(option=='v'):
        billing()
    if(option=='b'):
        transaction()
    if(option=='exit'):
        mainpage()
    else:
        checkin()
def billing():
    system('cls')
    print ('''
           &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
           &--- B I L L I N G   I N F O R M A T I O N --- &
           &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
          ''')
    roomtype=input('''
                Select Room Type:
                  DELUX-1
                  DELUX-2
                  DELUX-3
                  DELUX-3
                ''')
    if(roomtype=="DELUX-1"):
        print ('''
                 Room Amount= 2000
                 Service Tax= 100
              ''')
        units=input('  Electricity units used  ')
        electricitybill= 7*units
        print ('  Electricity Bill=  ', electricitybill)
        total= 2000+100+electricitybill
    if(roomtype=="DELUX-2"):
        print ('''
                 Room Amount= 3500
                 Service Tax= 200
              ''')
        units=input('electricity units used')
        electricitybill= 7*units
        print ('  Electricity Bill= ', electricitybill)
        total= 3500+200+electricitybill
    if(roomtype=="DELUX-3"):
        print ('''
                 Room Amount= 5000
                 Service Tax= 300
              ''')
        units=input('electricity units used')
        electricitybill= 7*units
        print ('  Electricity Bill= ', electricitybill)
        total= 5000+300+electricitybill
    if(roomtype=="DELUX-4"):
        print ('''
                 Room Amount= 5500
                 Service Tax= 300
              ''')
        units=input('electricity units used')
        electricitybill= 7*units
        print ('  Electricity Bill= ', electricitybill)
        total= 5500+300+electricitybill
    print ('  TOTAL= ',total)
    a=input("  press 'b' to go back  ")
    if(a=='b'):
        transaction()
    if(option=='exit'):
        mainpage()
    else:
        billing()
def checkout():
    system('cls')
    print ('''
            &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
            &==== C H E C K - O U T   D E T A I L S ====&
            &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
          ''')
    custid=input(' CUSTOMER ID  ')
    custname=input('  CUSTOMER NAME  ')
    checdate=input(' CHECK-IN DATE  ')
    noadult=input(' No. of ADULTS  ')
    nochild=input(' No. of CHILDS  ')
    print ('''

              OK DONE !!!!
          ''')
    a=input("  press 'b' to go back  ")
    if(a=='b'):
        transaction()
    if(option=='exit'):
        mainpage()
    else:
        checkout()
def banquet():
    system('cls')
    print(  '''
                ^^^^^^^^^^^^^^^
                 1-MASTERS
                 2-TRANSACTION
                 3-REPORTS
                ***************
           ''')
    option=input(" choose to enter or 'b' for mainpage")
    if(option=='1'):
        bmasters()
    if(option=='2'):
        btransaction()
    if(option=='3'):
        breports()
    if(option=='b'):
        mainpage()
    if(option=='exit'):
        mainpage()
    else:
        banquet()
def bmasters():
    system('cls')
    print ('''
              &&&&&&&&&&&&&&&&&
              ^^^^^^^^^^^^^^^^^
                1-Venue
                2-Functions
                3-Menu
                4-Staff Detail
              _________________
              &&&&&&&&&&&&&&&&&
          ''')
    option=input("  Enter Option or 'b' to go back  ")
    if(option=='1'):
        venue()
    if(option=='2'):
        functions()
    if(option=='3'):
        menu()
    if(option=='4'):
        staffdetail()
    if(option=='b'):
        banquet()
    if(option=='exit'):
        mainpage()
    else:
        bmasters()
def venue():
    system('cls')
    print ('''
                 *****************
                    V E N U E 
                 ^^^^^^^^^^^^^^^^^
          ''')
    print ('''



                 ??????????????????????
                  NO DETAILS AVAILABLE

          ''')
    a=input(" press 'b' to go back  ")
    if(a=='b'):
        bmasters()
    if(option=='exit'):
        mainpage()
    else:
        venue()
def functions():
    system('cls')
    print ('''
               %%%%%%%%%%%%%%%%%%%%%%%%%
                  F U N C T I O N S
               %%%%%%%%%%%%%%%%%%%%%%%%%
          ''')
    print ('''

               >>>> MARRIAGE CELEBRATION

               >>>> BIRTHDAY PARTIES

               >>>> NIGHT SHOWS
               
               >>>> PARTIES
          ''')
    a=input(" press 'b' to go back  ")
    if(a=='b'):
        bmasters()
    if(option=='exit'):
        mainpage()
    else:
        functions()
def menu():
    system('cls')
    print ('''
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
          @           B R E A K F A S T   M E N U                 @
          @          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^                @
          @   Tea                                  Rs 7           @
          @   Coffee                               Rs 10          @
          @   Milk                                 Rs 12/glass    @
          @   Bread Pakoda                         Rs 10          @
          @   Simple Paratha                       Rs 5           @
          @   Aalu Paratha                         Rs 8           @
          @   Gobi Paratha                         Rs 10          @
          @   Egg                                  Rs 7           @
          @   Samosa                               Rs 5           @
          @   Noodles                              Rs 30/plate    @
          @   Burger                               Rs 25          @
          @   Namkeen Rice                         Rs 25/plate    @
          @   Pulaw                                Rs 25/plate    @
          @                                                       @
          @                                                       @
          @               L U N C H   M E N U                     @
          @              ^^^^^^^^^^^^^^^^^^^^^                    @
          @   Chapati                              Rs 5           @
          @   Butter Chapati                       Rs 7           @
          @   Tandoori                             Rs 7           @
          @   Puri                                 Rs 5           @
          @   Dal                                  Rs 15/plate    @
          @   Fry Dal                              Rs 20/plate    @
          @   Paneer                               Rs 20/plate    @
          @   Shahi Paneer                         Rs 30/plate    @
          @   Matar Paneer                         Rs 25/plate    @
          @   Rice                                 Rs 20/plate    @
          @   Egg Kari                             Rs 25          @
          @   Aalu Matar                           Rs 20/plate    @
          @   Mix Vegetable                        Rs 30/plate    @
          @   Sweet Lassi                          Rs 15/glass    @
          @   Namkeen Lassi                        Rs 15/glass    @
          @                                                       @
          @                                                       @
          @            D I N N E R   M E N U                      @
          @           ^^^^^^^^^^^^^^^^^^^^^^^                     @
          @   Chapati                              Rs 5           @
          @   Butter Chapati                       Rs 7           @
          @   Tandoori                             Rs 7           @
          @   Puri                                 Rs 5           @
          @   Dal                                  Rs 15/plate    @
          @   Fry Dal                              Rs 20/plate    @
          @   Paneer                               Rs 20/plate    @
          @   Shahi Paneer                         Rs 30/plate    @
          @   Matar Paneer                         Rs 25/plate    @
          @   Rice                                 Rs 20/plate    @
          @   Egg Kari                             Rs 25          @
          @   Aalu Matar                           Rs 20/plate    @
          @   Mix Vegetable                        Rs 30/plate    @
          @   Sweeties                             Rs 10          @
          @                                                       @
          @!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!@
        ''')
    a=input("  press 'b' to go back  ")
    if(a=='b'):
        bmasters()
    if(option=='exit'):
        mainpage()
    else:
        menu()
def staffdetail():
    system('cls')
    print ('''
                   @@@@@@@@@@@@@@@@@@@@@@@@@@@
                    S T A F F   M E M B E R S
                    +++++++++++++++++++++++++
          ''')
    staffdetails={1:{'NAME':'Abhijeet','Age':25,'Address':'1-Nmo bibhaag Jodhpur'},
                  2:{'NAME':'Sher Singh','Age':22,'Address':'25-Parle India Jodhpur'},
                  3:{'NAME':'AbhiAbhi','Age':20,'Address':'9-Goodday Jeevan Jodhpur'},
                  4:{'NAME':'Abhijojo','Age':21,'Address':'Ji nhi handi Jodhpur'},
                  5:{'NAME':'Anna','Age':25,'Address':'jab we met colony Jodhpur'},
                  6:{'NAME':'Raj Ji','Age':28,'Address':'32-Sikka Road Jodhpur'}
                 }
    print (staffdetails)
    need=input("  Press 'y' to enter more details  ")
    if(need=='y'):
        nesteddict()
    if(option=='exit'):
        mainpage()
    else:
        staffdetail()
def nesteddict():
    no=input("  no. of details you need to add  ")
    noo=input("  no. of nested details  ")
    dict1={}
    for i in range(no):
        key=input(" Key Name  ")
        dict1[key]={}
        for j in range(noo):
            key1=raw_input(" Nested Key Name  ")
            value=raw_input(" Enter Value  ")
            dict1[key][key1]=value
    for i in dict1:
        print (i)
        for j in dict1[i]:
            print (j),
            print (dict1[i][j])
    a=input("  press 'b' to go back  ")
    if(a=='b'):
        staffdetail()
    if(option=='exit'):
        mainpage()
    else:
        nesteddict()
def breports():
    system('cls')
    print ('''
              NOO REPORTS
              ???????????
          ''')
    a=input("  press 'b' to go back  ")
    if(a=='b'):
        banquet()
    if(option=='exit'):
        mainpage()
    else:
        breports()
def btransaction():
    system('cls')
    print ('''

               ????????????

          ''')
    a=input("  press 'b' to go back  ")
    if(a=='b'):
        banquet()
    if(option=='exit'):
        mainpage()
    else:
        btransaction()
hotelmanagement()