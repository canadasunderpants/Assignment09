#------------------------------------------#
# Title: CD_Inventory.py
# Desc: The CD Inventory App main Module
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
# jdenhaan, 2022-Dec-11, Added secondary menu to allow user to interact with track functions, added error handling
#------------------------------------------#

import ProcessingClasses as PC
import IOClasses as IO

lstFileNames = ['AlbumInventory.txt', 'TrackInventory.txt']
lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)

while True:
    IO.ScreenIO.print_menu()
    strChoice = IO.ScreenIO.menu_choice()

    if strChoice == 'x':
        break
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            try:
                lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)
                IO.ScreenIO.show_inventory(lstOfCDObjects)
            except Exception as e:
                print(e)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'a':
        tplCdInfo = IO.ScreenIO.get_CD_info()
        try:
            PC.DataProcessor.add_CD(tplCdInfo, lstOfCDObjects)
        except Exception as e:
            print(e)
            input('press any key to continue')
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'd':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'c':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        cd_idx = input('Select the CD / Album index: ')
        Album = PC.DataProcessor.select_cd(lstOfCDObjects, cd_idx)
        IO.ScreenIO.print_CD_menu()
        choice = IO.ScreenIO.menu_CD_choice()
        
        while True:
            if choice == 'a':
                print('adding a track to:', Album)
                print('current tracks:\n')
                try:
                    IO.ScreenIO.show_tracks(Album)
                except Exception as e:
                    print(e)
                    print('These guys aren\'t John Cage, let\'s add a track or two!')
                trk_data = IO.ScreenIO.get_track_info()
                PC.DataProcessor.add_track(trk_data, Album)
                choice = input('press [e] to escape to main menu, or press [a] to add another track').strip()
                if choice == 'e':
                    break 
                elif choice == 'a':
                    continue
                else:
                    print ('There was a general error')
            if choice == 'd':
                try:
                    IO.ScreenIO.show_tracks(Album)
                except Exception as e:
                    print(e)
                input('press any key to return to main menu')  
                break
            if choice == 'r':
                try:
                    IO.ScreenIO.show_tracks(Album)
                except Exception as e:
                    print(e)
                    break
                trk_sel = input ('Select the index of the track you wish to delete: ').strip()
                try:
                    Album.rmv_track(trk_sel)
                except Exception as e:
                    print(e)
                break
            if choice == 'x':
                break
            else:
                print('There was a general error')
        # TODONE add code to handle tracks on an individual CD
    elif strChoice == 's':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            try:
                IO.FileIO.save_inventory(lstFileNames, lstOfCDObjects)
            except Exception as e:
                print(e)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    else:
        print('General Error')