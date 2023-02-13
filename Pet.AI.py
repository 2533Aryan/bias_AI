from tkinter import *
import tkinter.font as font
import time as time

'''
This program helps us choosing pet when provided with pet features.
So far the AI we build seems flawless!
'''

# Importing our AI model for making prediction
from ai_classifier import *



# Start Pet.AI
def start_pet_AI():

    # Columns: Energetic, Cuddly, Soft, Quiet
    features = [[0, 0, 0, 0]]    # Initial Pet features


    # Main GUI
    main = Tk()
    
    
    # Set the font for buttons
    button_font = font.Font(family='Helvetica', size=17, weight='bold')
    
    
    # Title of the main window
    main.title("Pet.AI")
    main.configure(bg='#ec9578')
    #main.configure(bg='#E9AFA3')



    # Centering main Window on Screen

    # Gets the requested values of the height and widht.
    windowWidth = main.winfo_reqwidth()
    windowHeight = main.winfo_reqheight()
    
    # Gets both half the screen width/height and window width/height
    positionRight = int(main.winfo_screenwidth()/9 - windowWidth/9)
    positionDown = int(main.winfo_screenheight()/4.5 - windowHeight/4.5)
    
    # Positions the window in the center of the page.
    main.geometry("+{}+{}".format(positionRight, positionDown))



    pet_icon = PhotoImage(file='Images/pet_icon.png')
    # Setting icon of master window
    main.iconphoto(False, pet_icon)


    # Heading
    heading = Label(main, text = '                        Choose the features that you discovered in your desired pet!                         ')
    heading.configure(font= ("Helvetica 22 italic bold"), background='light grey')
    heading.grid(row = 0, columnspan = 4)


    # Creating a photoimage object to use image
    energetic_photo = PhotoImage(file = r"Images/energetic_image.png")
    cuddly_photo = PhotoImage(file = r"Images/cuddly_image.png")
    soft_photo = PhotoImage(file = r"Images/soft_image.png")
    quiet_photo = PhotoImage(file = r"Images/quiet_image.png")



    # Lock button & change features
    def energetic_disable():
        energetic.configure(state=DISABLED)
        features[0][0] = 1

    def cuddly_disable():
        cuddly.configure(state=DISABLED)
        features[0][1] = 1

    def soft_disable():
        soft.configure(state=DISABLED)
        features[0][2] = 1

    def quiet_disable():
        quiet.configure(state=DISABLED)
        features[0][3] = 1



    # Column names:  Energetic, Cuddly, Soft, Quiet, Happiness
    energetic = Button(main, text='Energetic', image = energetic_photo, command=energetic_disable)
    energetic.grid(row = 1, column = 0)

    cuddly = Button(main, text='Cuddly', image = cuddly_photo, command=cuddly_disable)
    cuddly.grid(row = 1, column = 1)

    soft = Button(main, text='Soft', image = soft_photo, command=soft_disable)
    soft.grid(row = 1, column = 2)

    quiet = Button(main, text='Quiet', image = quiet_photo, command=quiet_disable)
    quiet.grid(row = 1, column = 3)



    # Mentioning columns:  Energetic, Cuddly, Soft, Quiet, Happiness
    energetic_title = Label(main, text='Energetic')
    energetic_title.configure(font= ("Helvetica 18 bold"), background="light grey")
    energetic_title.grid(row = 2, column = 0)

    cuddly_title = Label(main, text='Cuddly')
    cuddly_title.configure(font= ("Helvetica 18 bold"), background="light grey")
    cuddly_title.grid(row = 2, column = 1)

    soft_title = Label(main, text='Soft')
    soft_title.configure(font= ("Helvetica 18 bold"), background="light grey")
    soft_title.grid(row = 2, column = 2)

    quiet_title = Label(main, text='Quiet')
    quiet_title.configure(font= ("Helvetica 18 bold"), background="light grey")
    quiet_title.grid(row = 2, column = 3)



    # Single line space
    space1 = Label(main, text='')
    space1.configure(font= ("Helvetica 15 bold"), background='#ec9578')
    space1.grid(row = 3, column = 3)



    # New Window for the results (AI predictions)
    def new_window():

        main.destroy()

        results = Tk()
        results.title("Pet.AI")
        results.configure(bg='#ec9578')

        # Set the font for buttons
        button_font = font.Font(family='Helvetica', size=17, weight='bold')
    

        # Centering results Window on Screen

        # Gets the requested values of the height and widht.
        windowWidth = results.winfo_reqwidth()
        windowHeight = results.winfo_reqheight()

        # Gets both half the screen width/height and window width/height
        positionRight = int(results.winfo_screenwidth()/3 - windowWidth/3)
        positionDown = int(results.winfo_screenheight()/5 - windowHeight/4)

        # Positions the window in the center of the page.
        results.geometry("+{}+{}".format(positionRight, positionDown))


        # Setting icon of the window
        pet_icon = PhotoImage(file='Images/pet_icon.png')
        results.iconphoto(False, pet_icon)

        # New window heading
        new_heading = Label(results, text = '                  Pet.AI has predicted that:                 ')
        new_heading.configure(font= ("Helvetica 22 italic bold"), background="light grey")
        new_heading.grid(row = 0, columnspan = 5)


        # Single line space
        space6 = Label(results, text='')
        space6.configure(font= ("Helvetica 15 bold"), background='#ec9578')
        space6.grid(row = 1, column = 0)


        # if prediction is "YES"
        if mlp.predict(features)[0]:
            # Photoimage object
            happy_photo = PhotoImage(file = r"Images/happy_image.png").subsample(2,2)
            happy = Label(results, text='Energetic', image = happy_photo)
            happy.grid(row = 2, columnspan = 5)

            # Single line space
            space3 = Label(results, text='')
            space3.configure(font= ("Helvetica 15 bold"), background='#ec9578')
            space3.grid(row = 3, column = 0)

            # Description
            description1 = Label(results, text = ' Pet.AI thinks you will be happy buying this pet.   ')
            description1.configure(font= ("Helvetica 20 italic bold"), background="light grey")
            description1.grid(row = 4, columnspan = 5)

            description2 = Label(results, text = '                                 Go for it!!                              ')
            description2.configure(font= ("Helvetica 20 italic bold"), background="light grey")
            description2.grid(row = 5, columnspan = 6)


        # if prediction is "NO"
        else:
            # Photoimage object
            sad_photo = PhotoImage(file = r"Images/sad_image.png").subsample(2,2)
            sad = Label(results, text='Energetic', image = sad_photo)
            sad.grid(row = 2, columnspan = 5)

            # Single line space
            space3 = Label(results, text='')
            space3.configure(font= ("Helvetica 15 bold"), background='#ec9578')
            space3.grid(row = 3, column = 0)

            # Description
            description1 = Label(results, text = 'Pet.AI thinks you will be unhappy buying this pet.')
            description1.configure(font= ("Helvetica 20 italic bold"), background="light grey")
            description1.grid(row = 4, columnspan = 5)

            description2 = Label(results, text = '                             Do not buy it!!                           ')
            description2.configure(font= ("Helvetica 20 italic bold"), background="light grey")
            description2.grid(row = 5, columnspan = 5)



        # Restart the program
        def restart_program():
            results.destroy()
            start_pet_AI()



        # Single line space
        space4 = Label(results, text='')
        space4.configure(font= ("Helvetica 15 bold"), background='#ec9578')
        space4.grid(row = 6, column = 0)



        # Button to exit the window
        exit_button = Button(results, text='EXIT', width=11, bg='blue', fg='white', command=results.destroy)
        # Apply font to the button label
        exit_button['font'] = button_font
        exit_button.grid(row=7, column=0 , columnspan=3)


        # Button to restart the window
        restart_button = Button(results, text='RESTART', width=11, bg='blue', fg='white', command=restart_program)
        # Apply font to the button label
        restart_button['font'] = button_font
        restart_button.grid(row=7, column=2 , columnspan=3)


        # Single line space
        space5 = Label(results, text='')
        space5.configure(font= ("Helvetica 15 bold"), background='#ec9578')
        space5.grid(row = 8, column = 0)


        results.mainloop()



    # Refresh the system (enable the lock button)
    def changeState():
        energetic['state'] = NORMAL
        cuddly['state'] = NORMAL
        soft['state'] = NORMAL
        quiet['state'] = NORMAL
        features[0][0] = 0
        features[0][1] = 0
        features[0][2] = 0
        features[0][3] = 0
        



    # Refresh Button
    refresh_button = Button(main, text="RESET", width=11, bg='blue', fg='white', command=changeState)
    refresh_button['font'] = button_font
    refresh_button.grid(row = 4, columnspan = 2)



    # Button to predict if a user will be happy buying pet
    happiness = Button(main, text='HAPPINESS?', width=11, bg='blue', fg='white', command=new_window)
    # Apply font to the button label
    happiness['font'] = button_font
    happiness.grid(row = 4, columnspan = 4)


    # Exit Button
    exit_button = Button(main, text="EXIT", width=11, bg='blue', fg='white', command=main.destroy)
    exit_button['font'] = button_font
    exit_button.grid(row = 4, column = 2, columnspan = 4)


    # Stretch buttons when window is resized
    main.rowconfigure((0,1), weight=1)  
    main.columnconfigure((0,2), weight=1)



    # Single line space
    space2 = Label(main, text='')
    space2.configure(font= ("Helvetica 15 bold"), background='#ec9578')
    space2.grid(row = 5, column = 3)


    main.mainloop()




# Intro window
def intro_window():
    intro = Tk()
    
    # Title of the intro window
    intro.title("Pet.AI")


    # Centering intro Window on Screen

    # Gets the requested values of the height and widht.
    windowWidth = intro.winfo_reqwidth()
    windowHeight = intro.winfo_reqheight()
    
    # Gets both half the screen width/height and window width/height
    positionRight = int(intro.winfo_screenwidth()/2 - windowWidth/1)
    positionDown = int(intro.winfo_screenheight()/2 - windowHeight/1)
    
    # Positions the window in the center of the page.
    intro.geometry("+{}+{}".format(positionRight, positionDown))


    # Setting icon of intro window
    pet_icon = PhotoImage(file='Images/pet_icon.png')
    intro.iconphoto(False, pet_icon)

        
    # Intro window heading
    intro_heading = Label(intro, text = '      Welcome to Pet.AI      ')
    intro_heading.configure(font= ("Helvetica 22 italic bold"), background="#ec9578")
    intro_heading.grid(row=0, column = 0)

    
    # Space
    intro_space1 = Label(intro, text = '')
    intro_space1.grid(row = 1, column = 0)

    
    intro_photo = PhotoImage(file = r"Images/pet_icon.png").subsample(2,2)
    intro_label = Label(intro, text='Energetic', image = intro_photo)
    intro_label.grid(row = 2, column = 0)


    # Space
    intro_space2 = Label(intro, text = '')
    intro_space2.grid(row = 3, column = 0)


    #Automatically close the window after 3 seconds
    intro.after(6000,lambda:intro.destroy())


    intro.mainloop()



# Start program
if(__name__=="__main__"):
    intro_window()
    
    start_pet_AI()

