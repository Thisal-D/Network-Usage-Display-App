
import sys
app_error = False 
try:
    from psutil import net_io_counters ,net_if_stats
except:
    print("Install Psutil Module......")
    app_error = True
try:
    from customtkinter import CTk  ,CTkButton ,CTkFrame  ,set_appearance_mode ,CTkLabel ,CTk ,CTkScrollbar
except:
    print("Install customtkinter Module......")
    app_error = True
try:
    from tkinter import Frame, Label ,PhotoImage,Canvas  ,Button
except:
    print("Install tkinter Module......")
    app_error = True
try:
    import pystray
except:
    print("Install pystray Module......")
    app_error = True
try:
    from PIL import Image
except:
    print("Install pillow Module......")
    app_error = True
try:
    import pygame
except:
    print("Install pygame Module......")
    app_error = True

try:
    import datetime
    import os 
    import threading
    import time
except:
    app_error = True

if app_error == True :
    print('ERROR FOUND !')
    sys.exit()


#install pygame
pygame.init()
audio = pygame.mixer.music
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################

#remove old files
files_temp = os.listdir("source/settings/process/")
for delf in files_temp:
    try:
        os.remove("source/settings/process/"+delf)
    except:
        pass

#running save 
state_of_program_check_file = open("source/settings/process/running.txt","w")
state_of_program_check_file = open("source/settings/process/running.txt","r")

################################################################################################################################
################################################################################################################################
################################################################################################################################
def light():
    global app_theme
    global app_theme_re

    global app_quit_main_frame_color
    global app_quit_text_color
    global app_quit_error_text_color
    global app_quit_error_text_color_1
    global app_quit_btn_color
    global app_quit_btn_color_border
    global app_quit_btn_hover_color 

    if app_theme != "light" :
        file = open("source/settings/theme/theme.txt","w")
        file.write("light")
        file.close()

        set_appearance_mode("light")
        app_theme = "light"
        app_theme_re= "dark"

        #main frames
        main_frame_temp.configure(fg_color="#e1e1e1")
        main_canvas.configure(bg="#e1e1e1")
        main_frame_for_scroll.configure(fg_color="#e1e1e1" ,bg_color="#e1e1e1")                

        #connection adapter select Frame 
        connection_adapter_select_frame.configure(fg_color="#ffffff")
        connection_adapter_select_sub_frame.configure(fg_color="#f1f1f1" ,bg_color="#ffffff")
        label_temp01.configure(bg="#f1f1f1" ,fg="#000000")
        selected_conection_label1.configure(bg="#f1f1f1" ,fg="#000000")
        connection_adapter_select_button.configure(text_color="#000000" , fg_color="#ffffff" ,border_color="#afafaf" ,hover_color = "#eeeeee")
        connection_adapter_refresh_button.configure(image=refresh_image_light ,fg_color="#ffffff" ,border_color="#afafaf" ,hover_color = "#eeeeee")

        #network performence frame
        #selected network adapter
        network_performence_frame.configure(fg_color="#e1e1e1")
        label_temp02.configure(bg="#e1e1e1" ,fg="#000000")
        selected_conection_label2.configure(bg="#e1e1e1" ,fg="#000000")
        time_usage_label.configure(bg="#e1e1e1" ,fg="#000000")
        #receive performence
        label_temp06.configure(bg="#eeeeee" ,fg="#000000")
        network_receive_performence_frame.configure(fg_color="#eeeeee")
        network_receive_performence_sub_frame.configure(fg_color="#ffffff")
        label_temp03.configure(bg="#ffffff" ,fg="#000000")
        network_receive_speed_label.configure(bg="#ffffff" ,fg="#000000")
        label_temp18.configure(bg="#ffffff" ,fg="#000000")
        network_receive_max_speed_label.configure(bg="#ffffff" ,fg="#000000")
        label_temp04.configure(bg="#ffffff" ,fg="#000000")
        network_avg_receive_speed_label.configure(bg="#ffffff" ,fg="#000000")
        label_temp05.configure(bg="#ffffff" ,fg="#000000")
        network_total_receive_label.configure(bg="#ffffff" ,fg="#000000")
        #send performence
        label_temp07.configure(bg="#eeeeee" ,fg="#000000")
        network_send_performence_frame.configure(fg_color="#eeeeee")
        network_send_performence_sub_frame.configure(fg_color="#ffffff")
        label_temp08.configure(bg="#ffffff" ,fg="#000000")
        network_send_speed_label.configure(bg="#ffffff" ,fg="#000000")
        label_temp19.configure(bg="#ffffff" ,fg="#000000")
        network_send_max_speed_label.configure(bg="#ffffff" ,fg="#000000")
        label_temp09.configure(bg="#ffffff" ,fg="#000000")
        network_avg_send_speed_label.configure(bg="#ffffff" ,fg="#000000")
        label_temp10.configure(bg="#ffffff" ,fg="#000000")
        network_total_send_label.configure(bg="#ffffff" ,fg="#000000")
        #receive & send send performence
        label_temp11.configure(bg="#eeeeee" ,fg="#000000")
        network_receive_send_performence_frame.configure(fg_color="#eeeeee")
        network_receive_send_performence_sub_frame.configure(fg_color="#ffffff")
        label_temp12.configure(bg="#ffffff" ,fg="#000000")
        network_receive_send_speed_label.configure(bg="#ffffff" ,fg="#000000")
        label_temp20.configure(bg="#ffffff" ,fg="#000000")
        network_receive_send_max_speed_label.configure(bg="#ffffff" ,fg="#000000")
        label_temp13.configure(bg="#ffffff" ,fg="#000000")
        network_avg_receive_send_speed_label.configure(bg="#ffffff" ,fg="#000000")
        label_temp14.configure(bg="#ffffff" ,fg="#000000")
        network_total_receive_send_label.configure(bg="#ffffff" ,fg="#000000")
        #dashes
        for i in range(12):
            globals()["label_dash_"+str(i)].configure(bg="#ffffff" ,fg="#000000")

        #network status barchar
        #speed
        network_speed_states_frame.configure(fg_color="#f1f1f1")
        network_speed_state_chart_frame.configure(fg_color="#ffffff")
        label_temp15.configure(bg="#f1f1f1" ,fg="#000000")
        network_speed_state_chart_canvas.configure(bg="#ffffff")
        network_speed_state_chart_hide_frame.configure(fg_color="#ffffff")
        network_speed_barchart_data_type_label.configure(bg="#ffffff" ,fg="#151515")
        for i in range(1,12):
            if i != 11:
                globals()["chart_speed_frame"+str(i)].configure(bg="#f1f1f1")
            globals()["chart_speed_label"+str(i)].configure(bg="#ffffff" ,fg="#000000")

        #average speed
        network_average_speed_state_chart_frame.configure(fg_color="#ffffff")
        label_temp16.configure(bg="#f1f1f1" ,fg="#000000")
        network_average_speed_state_chart_canvas.configure(bg="#ffffff")
        network_average_speed_state_chart_hide_frame.configure(fg_color="#ffffff")
        network_average_speed_barchart_data_type_label.configure(bg="#ffffff" ,fg="#151515")
        for i in range(1,12):
            if i != 11:
                globals()["chart_average_speed_frame"+str(i)].configure(bg="#f1f1f1")
            globals()["chart_average_speed_label"+str(i)].configure(bg="#ffffff" ,fg="#000000")

        #total usage
        network_data_usage_state_chart_frame.configure(fg_color="#ffffff")
        label_temp17.configure(bg="#e1e1e1" ,fg="#000000")
        network_data_usage_state_chart_canvas.configure(bg="#ffffff")
        network_data_usage_state_chart_hide_frame.configure(fg_color="#ffffff")
        network_data_usage_barchart_data_type_label.configure(bg="#ffffff" ,fg="#151515")
        for i in range(1,12):
            if i != 11:
                globals()["chart_data_usage_frame"+str(i)].configure(bg="#f1f1f1")
            globals()["chart_data_usage_label"+str(i)].configure(bg="#ffffff" ,fg="#000000")
    

        #customtkinter genarated buttons fg bg
        global text_color_001
        global fg_color_001
        global border_color_001
        global hover_color_001
        text_color_001 = "#000000"
        fg_color_001 = "#ffffff"
        border_color_001 = "#dddddd"
        hover_color_001 = "#e1e1e1"

        #change connection selection  button
        for button_no in range (len(connection_adapters)):
            button_var =  "connection" + str(button_no)
            try:
                globals()[button_var].configure(text_color=text_color_001,fg_color=fg_color_001,border_color=border_color_001 ,hover_color=hover_color_001)
            except:
                pass

        #side panel
        side_panel_frame.configure(fg_color="#ffffff" ,bg_color="#e1e1e1")
        
        #theme change
        theme_change_frame.configure(fg_color="#eeeeee")
        theme_label.configure(bg="#eeeeee" ,fg="#000000")
        light_btn.configure(text_color="#000000" ,fg_color="#ffffff",hover_color="#e1e1e1")
        dark_btn.configure(text_color="#000000" ,fg_color="#ffffff",hover_color="#e1e1e1")

        #transparent 
        transparent_change_frame.configure(fg_color="#eeeeee")
        transparent_label.configure(bg="#eeeeee" ,fg="#000000")
        transparent_enable_btn.configure(text_color="#000000" ,fg_color="#ffffff",hover_color="#e1e1e1")
        transparent_disable_btn.configure(text_color="#000000" ,fg_color="#ffffff",hover_color="#e1e1e1")

        #full screen  
        full_screen_change_frame.configure(fg_color="#eeeeee")
        full_screen_label.configure(bg="#eeeeee" ,fg="#000000")
        full_screen_enable_btn.configure(text_color="#000000" ,fg_color="#ffffff",hover_color="#e1e1e1")
        full_screen_disable_btn.configure(text_color="#000000" ,fg_color="#ffffff",hover_color="#e1e1e1")
        
        #speed mode change
        speed_mode_frame.configure(fg_color="#eeeeee")
        speed_mode_label.configure(bg="#eeeeee" ,fg="#000000")
        bits_speed_btn.configure(text_color="#000000" ,fg_color="#ffffff",hover_color="#e1e1e1")
        bytes_speed_btn.configure(text_color="#000000" ,fg_color="#ffffff",hover_color="#e1e1e1")
        
        #update speed 
        update_speed_change_frame.configure(fg_color="#eeeeee")
        update_speed_change_label.configure(bg="#eeeeee" ,fg="#000000")
        for i in range(6):
            globals()["update_speed_btn"+str(i)].configure(text_color="#000000" ,fg_color="#ffffff",hover_color="#e1e1e1")

        #minimize to sytem icon
        minimize_to_trayicon_change_frame.configure(fg_color="#eeeeee")
        minimize_to_trayicon_change_label.configure(bg="#eeeeee" ,fg="#000000")
        minimize_to_trayicon_change_label_2.configure(bg="#eeeeee" ,fg="#000000")
        minimize_to_trayicon_enable_btn.configure(text_color="#000000" ,fg_color="#ffffff",hover_color="#e1e1e1")
        minimize_to_trayicon_disable_btn.configure(text_color="#000000" ,fg_color="#ffffff",hover_color="#e1e1e1")
        
        #vercion
        vercion_label.configure(bg="#ffffff" ,fg="#000000")

        
        #settings button
        global setting_btn_bg_001
        global setting_btn_bg_002
        setting_btn_bg_001 = "#ffffff"
        setting_btn_bg_002 = "#e1e1e1"
        
        if side_panel_open == True:
            settings_button.configure(bg=setting_btn_bg_001 ,activebackground=setting_btn_bg_001)
        else:
            settings_button.configure(bg=setting_btn_bg_002 ,activebackground=setting_btn_bg_002)
        

        #menu frame
        menu_frame.configure(fg_color="#eeeeee" ,border_color="#aaaaaa")
        #always on top
        menu_frame_always_on_top_frame.configure(fg_color="#ffffff")
        menu_frame_always_on_top_label.configure(fg="#000000",bg="#ffffff")
        menu_frame_always_on_top_enable_btn.configure(text_color="#000000",fg_color="#ffffff" ,hover_color="#dddddd")
        menu_frame_always_on_top_disable_btn.configure(text_color="#000000",fg_color="#ffffff" ,hover_color="#dddddd")
        #full screen
        menu_frame_full_screen_change_frame.configure(fg_color="#ffffff")
        menu_frame_full_screen_label.configure(fg="#000000",bg="#ffffff")
        menu_frame_full_screen_enable_btn.configure(text_color="#000000",fg_color="#ffffff" ,hover_color="#dddddd")
        menu_frame_full_screen_disable_btn.configure(text_color="#000000",fg_color="#ffffff" ,hover_color="#dddddd")
        #speed option
        menu_frame_speed_mode_frame.configure(fg_color="#ffffff")
        menu_frame_speed_mode_label.configure(fg="#000000",bg="#ffffff")
        menu_frame_bits_speed_btn.configure(text_color="#000000",fg_color="#ffffff" ,hover_color="#dddddd")
        menu_frame_bytes_speed_btn.configure(text_color="#000000",fg_color="#ffffff" ,hover_color="#dddddd")

        #ask to quit window colors
        app_quit_main_frame_color = "#ffffff"
        app_quit_text_color = "#000000"
        app_quit_error_text_color = "#00ff00"
        app_quit_error_text_color_1 = "#ff0000"
        app_quit_btn_color='#ffffff'
        app_quit_btn_color_border='#afafaf'
        app_quit_btn_hover_color  = "#dddddd"

def dark():
    global app_theme
    global app_theme_re
    global app_quit_main_frame_color
    global app_quit_text_color
    global app_quit_error_text_color
    global app_quit_error_text_color_1
    global app_quit_btn_color
    global app_quit_btn_color_border
    global app_quit_btn_hover_color 
    if app_theme != "dark":
        file = open("source/settings/theme/theme.txt","w")
        file.write("dark")
        file.close()
        
        set_appearance_mode("dark")
        app_theme = "dark"
        app_theme_re = "light"
        
        #main frames
        main_frame_temp.configure(fg_color="#292a2b")
        main_canvas.configure(bg="#292a2b")
        main_frame_for_scroll.configure(fg_color="#292a2b" ,bg_color="#292a2b")
                
        #connection adapter select Frame 
        connection_adapter_select_frame.configure(fg_color="#292a2b")
        connection_adapter_select_sub_frame.configure(fg_color="#151515" ,bg_color="#292a2b")
        label_temp01.configure(bg="#151515" ,fg="#ffffff")
        selected_conection_label1.configure(bg="#151515" ,fg="#ffffff")
        connection_adapter_select_button.configure(text_color="#ffffff" , fg_color="#101010" ,border_color="#949a9f" ,hover_color="#303030")
        connection_adapter_refresh_button.configure(image=refresh_image_dark ,fg_color="#101010" ,border_color="#949a9f" ,hover_color="#303030")

        #network performence frame
        #selected network adapter
        network_performence_frame.configure(fg_color="#292a2b")
        label_temp02.configure(bg="#292a2b" ,fg="#ffffff")
        selected_conection_label2.configure(bg="#292a2b" ,fg="#ffffff")
        time_usage_label.configure(bg="#292a2b" ,fg="#ffffff")
        #receive performence
        label_temp06.configure(bg="#202020" ,fg="#ffffff")
        network_receive_performence_frame.configure(fg_color="#202020")
        network_receive_performence_sub_frame.configure(fg_color="#151515")
        label_temp03.configure(bg="#151515" ,fg="#ffffff")
        network_receive_speed_label.configure(bg="#151515" ,fg="#ffffff")
        label_temp18.configure(bg="#151515" ,fg="#ffffff")
        network_receive_max_speed_label.configure(bg="#151515" ,fg="#ffffff")
        label_temp04.configure(bg="#151515" ,fg="#ffffff")
        network_avg_receive_speed_label.configure(bg="#151515" ,fg="#ffffff")
        label_temp05.configure(bg="#151515" ,fg="#ffffff")
        network_total_receive_label.configure(bg="#151515" ,fg="#ffffff")
        #send performence
        label_temp07.configure(bg="#202020" ,fg="#ffffff")
        network_send_performence_frame.configure(fg_color="#202020")
        network_send_performence_sub_frame.configure(fg_color="#151515")
        label_temp08.configure(bg="#151515" ,fg="#ffffff")
        network_send_speed_label.configure(bg="#151515" ,fg="#ffffff")
        label_temp19.configure(bg="#151515" ,fg="#ffffff")
        network_send_max_speed_label.configure(bg="#151515" ,fg="#ffffff")
        label_temp09.configure(bg="#151515" ,fg="#ffffff")
        network_avg_send_speed_label.configure(bg="#151515" ,fg="#ffffff")
        label_temp10.configure(bg="#151515" ,fg="#ffffff")
        network_total_send_label.configure(bg="#151515" ,fg="#ffffff")
        #receive & send send performence
        label_temp11.configure(bg="#202020" ,fg="#ffffff")
        network_receive_send_performence_frame.configure(fg_color="#202020")
        network_receive_send_performence_sub_frame.configure(fg_color="#151515")
        label_temp12.configure(bg="#151515" ,fg="#ffffff")
        network_receive_send_speed_label.configure(bg="#151515" ,fg="#ffffff")
        label_temp20.configure(bg="#151515" ,fg="#ffffff")
        network_receive_send_max_speed_label.configure(bg="#151515" ,fg="#ffffff")
        label_temp13.configure(bg="#151515" ,fg="#ffffff")
        network_avg_receive_send_speed_label.configure(bg="#151515" ,fg="#ffffff")
        label_temp14.configure(bg="#151515" ,fg="#ffffff")
        network_total_receive_send_label.configure(bg="#151515" ,fg="#ffffff")
        #dashes
        for i in range(12):
            globals()["label_dash_"+str(i)].configure(bg="#151515" ,fg="#ffffff")

        #network status barchar
        #speed 
        network_speed_states_frame.configure(fg_color="#202020")
        network_speed_state_chart_frame.configure(fg_color="#151515")
        label_temp15.configure(bg="#202020" ,fg="#ffffff")
        network_speed_state_chart_canvas.configure(bg="#151515")
        network_speed_state_chart_hide_frame.configure(fg_color="#151515")
        network_speed_barchart_data_type_label.configure(bg="#151515" ,fg="#ffffff")
        for i in range(1,12):
            if i != 11:
                globals()["chart_speed_frame"+str(i)].configure(bg="#343638")
            globals()["chart_speed_label"+str(i)].configure(bg="#151515" ,fg="#ffffff")
        
        #average speed
        network_average_speed_state_chart_frame.configure(fg_color="#151515")
        label_temp16.configure(bg="#202020" ,fg="#ffffff")
        network_average_speed_state_chart_canvas.configure(bg="#151515")
        network_average_speed_state_chart_hide_frame.configure(fg_color="#151515")
        network_average_speed_barchart_data_type_label.configure(bg="#151515" ,fg="#ffffff")
        for i in range(1,12):
            if i != 11:
                globals()["chart_average_speed_frame"+str(i)].configure(bg="#343638")
            globals()["chart_average_speed_label"+str(i)].configure(bg="#151515" ,fg="#ffffff")
        
        #total usage
        #average speed
        network_data_usage_state_chart_frame.configure(fg_color="#151515")
        label_temp17.configure(bg="#292a2b" ,fg="#ffffff")
        network_data_usage_state_chart_canvas.configure(bg="#151515")
        network_data_usage_state_chart_hide_frame.configure(fg_color="#151515")
        network_data_usage_barchart_data_type_label.configure(bg="#151515" ,fg="#ffffff")
        for i in range(1,12):
            if i != 11:
                globals()["chart_data_usage_frame"+str(i)].configure(bg="#343638")
            globals()["chart_data_usage_label"+str(i)].configure(bg="#151515" ,fg="#ffffff")


        #customtkinter genarated buttons fg bg
        global text_color_001
        global fg_color_001
        global border_color_001
        global hover_color_001
        text_color_001 = "#ffffff"
        fg_color_001 = "#202020"
        border_color_001 = "#3e454a"
        hover_color_001 = "#404040"

        #change connection selection  button
        for button_no in range (len(connection_adapters)):
            button_var =  "connection" + str(button_no)
            try:
                globals()[button_var].configure(text_color=text_color_001,fg_color=fg_color_001,border_color=border_color_001,hover_color=hover_color_001)
            except:
                pass

        #side panel
        side_panel_frame.configure(fg_color="#151515" ,bg_color="#292a2b")
        
        #theme change
        theme_change_frame.configure(fg_color="#292a2b")
        theme_label.configure(bg="#292a2b" ,fg="#ffffff")
        light_btn.configure(text_color="#ffffff" ,fg_color="#202020",hover_color="#404040")
        dark_btn.configure(text_color="#ffffff" ,fg_color="#202020",hover_color="#404040")

        #transparent 
        transparent_change_frame.configure(fg_color="#292a2b")
        transparent_label.configure(bg="#292a2b" ,fg="#ffffff")
        transparent_enable_btn.configure(text_color="#ffffff" ,fg_color="#202020",hover_color="#404040")
        transparent_disable_btn.configure(text_color="#ffffff" ,fg_color="#202020",hover_color="#404040")
        
        #full screen 
        full_screen_change_frame.configure(fg_color="#292a2b")
        full_screen_label.configure(bg="#292a2b" ,fg="#ffffff")
        full_screen_enable_btn.configure(text_color="#ffffff" ,fg_color="#202020",hover_color="#404040")
        full_screen_disable_btn.configure(text_color="#ffffff" ,fg_color="#202020",hover_color="#404040")
        
        #speed mode change
        speed_mode_frame.configure(fg_color="#292a2b")
        speed_mode_label.configure(bg="#292a2b" ,fg="#ffffff")
        bits_speed_btn.configure(text_color="#ffffff" ,fg_color="#202020",hover_color="#404040")
        bytes_speed_btn.configure(text_color="#ffffff" ,fg_color="#202020",hover_color="#404040")
        
        #update speed 
        update_speed_change_frame.configure(fg_color="#292a2b")
        update_speed_change_label.configure(bg="#292a2b" ,fg="#ffffff")
        for i in range(6):
            globals()["update_speed_btn"+str(i)].configure(text_color="#ffffff" ,fg_color="#202020",hover_color="#404040")
        
        #minimize to sytem icon
        minimize_to_trayicon_change_frame.configure(fg_color="#292a2b")
        minimize_to_trayicon_change_label.configure(bg="#292a2b" ,fg="#ffffff")
        minimize_to_trayicon_change_label_2.configure(bg="#292a2b" ,fg="#ffffff")
        minimize_to_trayicon_enable_btn.configure(text_color="#ffffff" ,fg_color="#202020",hover_color="#404040")
        minimize_to_trayicon_disable_btn.configure(text_color="#ffffff" ,fg_color="#202020",hover_color="#404040")
        
        #vercion
        vercion_label.configure(bg="#151515" ,fg="#ffffff")

        #settings button
        global setting_btn_bg_001
        global setting_btn_bg_002
        setting_btn_bg_001 = "#151515"
        setting_btn_bg_002 = "#292a2b"
        
        if side_panel_open == True:
            settings_button.configure(bg=setting_btn_bg_001 ,activebackground=setting_btn_bg_001)
        else:
            settings_button.configure(bg=setting_btn_bg_002 ,activebackground=setting_btn_bg_002)
        
        
        #menu frame
        menu_frame.configure(fg_color="#202020" ,border_color="#9f9a9f")
        #always on top
        menu_frame_always_on_top_frame.configure(fg_color="#101010")
        menu_frame_always_on_top_label.configure(fg="#ffffff",bg="#101010")
        menu_frame_always_on_top_enable_btn.configure(text_color="#ffffff",fg_color="#101010" ,hover_color="#303030")
        menu_frame_always_on_top_disable_btn.configure(text_color="#ffffff",fg_color="#101010" ,hover_color="#303030")
        #full screen
        menu_frame_full_screen_change_frame.configure(fg_color="#101010")
        menu_frame_full_screen_label.configure(fg="#ffffff",bg="#101010")
        menu_frame_full_screen_enable_btn.configure(text_color="#ffffff",fg_color="#101010" ,hover_color="#303030")
        menu_frame_full_screen_disable_btn.configure(text_color="#ffffff",fg_color="#101010" ,hover_color="#303030")
        #speed option
        menu_frame_speed_mode_frame.configure(fg_color="#101010")
        menu_frame_speed_mode_label.configure(fg="#ffffff",bg="#101010")
        menu_frame_bits_speed_btn.configure(text_color="#ffffff",fg_color="#101010" ,hover_color="#303030")
        menu_frame_bytes_speed_btn.configure(text_color="#ffffff",fg_color="#101010" ,hover_color="#303030")

        #ask to quit window colors
        app_quit_main_frame_color = "#101010"
        app_quit_text_color = "#ffffff"
        app_quit_error_text_color = "#00ff00"
        app_quit_error_text_color_1 = "#ff0000"
        app_quit_btn_color='#252525'
        app_quit_btn_color_border='#949a9f'
        app_quit_btn_hover_color  = "#303030"
################################################################################################################################
def transparent_enable():
    global transparent_value
    global transparent_enabled
    if transparent_enabled == False :
        transparent_enabled = True
        transparent_value = 0.95
        root.attributes("-alpha",0.95)
        transaparent_save_file = open("source/settings/theme/transparent.txt","w")
        transaparent_save_file.write("enable")
        transaparent_save_file.close()

def transparent_disable():
    global transparent_value
    global transparent_enabled
    if transparent_enabled == True :
        transparent_enabled = False
        transparent_value = 1
        root.attributes("-alpha",1)
        transaparent_save_file = open("source/settings/theme/transparent.txt","w")
        transaparent_save_file.write("disable")
        transaparent_save_file.close()
  
################################################################################################################################
full_screen_enabled = False
def full_screen_enable():
    global full_screen_enabled
    if full_screen_enabled == False:
        full_screen_enabled = True
        root.attributes("-fullscreen",True)
        transaparent_save_file = open("source/settings/theme/fullsreen.txt","w")
        transaparent_save_file.write("enable")
        transaparent_save_file.close()
    
    #menu bar change
    menu_frame_full_screen_enable_btn.configure(state="disabled")
    menu_frame_full_screen_disable_btn.configure(state="normal")
    reset_menu_frame()

def full_screen_disable():
    global full_screen_enabled
    if full_screen_enabled == True:
        full_screen_enabled = False
        root.attributes("-alpha",0)
        root.attributes("-fullscreen",False)
        #custom tkinter bug 
        #aauto change title bar color need to fix
        set_appearance_mode(app_theme_re)
        set_appearance_mode(app_theme)
        root.attributes("-alpha",transparent_value)
        transaparent_save_file = open("source/settings/theme/fullsreen.txt","w")
        transaparent_save_file.write("disable")
        transaparent_save_file.close() 

    #menu bar change
    menu_frame_full_screen_enable_btn.configure(state="normal")
    menu_frame_full_screen_disable_btn.configure(state="disabled")
    reset_menu_frame()
################################################################################################################################
def system_icon_mode_enable():
    global system_icon_mode_enabled 
    if system_icon_mode_enabled == False:
        system_icon_mode_enabled = True
        system_icon_file = open("source/settings/general/system icon.txt","w")
        system_icon_file.write("enable")
        system_icon_file.close()
def system_icon_mode_disable():
    global system_icon_mode_enabled 
    if system_icon_mode_enabled == True:
        system_icon_mode_enabled = False
        system_icon_file = open("source/settings/general/system icon.txt","w")
        system_icon_file.write("disable")
        system_icon_file.close()

################################################################################################################################
#main window
root = CTk()
root.minsize(100,50)
root.geometry('1607x900')
root.title("Network Info")
root.iconbitmap("source/ui source/main.ico")

#create main frame 
main_frame_temp = CTkFrame(root)
main_frame_temp.pack(expand=True, fill='both') #.grid(row=0,column=0)
#create main canvas 
main_canvas = Canvas(main_frame_temp,bg='#000000',scrollregion=(0,0,1600,900) ,highlightthickness=0)
#create scrollbars
horizontal_scroller = CTkScrollbar(main_frame_temp ,command=main_canvas.xview ,orientation='horizontal')
horizontal_scroller.place(relwidth=1 ,rely=1 ,y=-13 ,height=13)
vertical_scroller = CTkScrollbar(main_frame_temp ,command=main_canvas.yview ,orientation='vertical')
vertical_scroller.place(relheight=1 ,relx=1 ,x=-13 ,width=13)
#maincanvas sync with scrollabars
main_canvas.configure(xscrollcommand=horizontal_scroller.set)
main_canvas.configure(yscrollcommand=vertical_scroller.set)

#create top frame for all widget 
main_frame_for_scroll = CTkFrame(main_canvas ,width=1600,height=900)
main_canvas.create_window((0,0) ,window=main_frame_for_scroll,anchor='nw')

#quit finally
def quit_app():
    global main_window_minimized_to_system
    main_window_minimized_to_system = False
    root.destroy()
#quit cancel finally
def cancel_quit_app():
    root.attributes("-topmost",always_on_top_root)
    root.iconify()
    show_error_frame.place_forget()
    root.minsize(100,50)
    root.maxsize(10000,10000)
    root.geometry('1600x900')
    root.protocol('WM_DELETE_WINDOW', hide_window)
    hide_window()

#define what happened when close app
def show_close_error_window():
    audio.load("source/ui source/error.mp3")
    root.maxsize(450,110)
    root.minsize(450,110)
    root.attributes("-topmost",True)
    show_error_frame.configure(fg_color=app_quit_main_frame_color)
    show_error_label.configure(text_color=app_quit_text_color)
    quit_application.configure(border_color=app_quit_btn_color_border ,fg_color=app_quit_btn_color 
                            ,hover_color=app_quit_btn_hover_color ,text_color=app_quit_error_text_color_1)
    cancel_quit_application.configure(border_color=app_quit_btn_color_border ,fg_color=app_quit_btn_color 
                            ,hover_color=app_quit_btn_hover_color ,text_color=app_quit_error_text_color)
    root.title("Quit Application : Network Info")
    show_error_frame.place(relwidth=1 ,relheight=1)
    root.deiconify()
    root.protocol('WM_DELETE_WINDOW', cancel_quit_app)
    audio.play(loops=1)

#Define function for quit the window
def ask_to_quit(tray_icon):
    tray_icon.stop()
    #destroy app
    show_close_error_window()
    
# Define a function to show to the window again
def show_window(tray_icon):
    global main_window_minimized_to_system
    tray_icon.stop()
    #root diplay on top
    root.attributes("-topmost",True)
    #redisplay root
    root.deiconify()
    root.attributes("-topmost",always_on_top_root)
    #start network speed display loop
    main_window_minimized_to_system = False
    display_network_speed()

def run_background_network_reader_Satate():
    while main_window_minimized_to_system :
        if os.path.exists("source/settings/process/running_2.txt"):
            try:
                os.remove("source/settings/process/running_2.txt")
                start_network_reader()
                while True:
                    if os.path.exists("source/settings/process/running_2.txt"):
                        break
                    else:
                        pass
            except:
                pass
        else:
            start_network_reader()
            while True:
                if os.path.exists("source/settings/process/running_2.txt"):
                    break
                else:
                    pass
        time.sleep(0.5)

def back_ground_service():
    threading.Thread(target=run_background_network_reader_Satate).start()    
# Hide the window and show on the system taskbar
def hide_window():
    global main_window_minimized_to_system
    try:
        #get icon
        tray_image = Image.open("source/ui source/main.ico")
        #create tray icon menu
        tray_menu=(pystray.MenuItem('Show', show_window) ,pystray.MenuItem('Quit', ask_to_quit))
        tray_icon=pystray.Icon("name", tray_image, "Network Info", tray_menu)
        
        #app run stop
        root.iconify()
        main_window_minimized_to_system = True
        #stop network speed display loop
        def waiting():
            if app_main_loop_running:
                root.after(10,waiting)
            else:
                #run service
                back_ground_service()
                #hide root
                root.withdraw()
                #disaplay tray icon
                tray_icon.run()
        waiting()
    except:
        root.destroy()

################################################################################################################################
#read connections 
connections_info = net_if_stats()
#connection adapters
connection_adapters = str(net_if_stats().keys())
connection_adapters = str(net_if_stats().keys()).replace(("dict_keys"),"")\
                    .replace("(","").replace(")","").replace("[","").replace("]","").replace(" '","").replace("'","")
#connection adapters list
connection_adapters = connection_adapters.split(",")
#get conections frame width 
max_adapter_name_lenght = 0
for name in connection_adapters:
    if len(name) > max_adapter_name_lenght:
        max_adapter_name_lenght = len(name)
length_label =  Label(root,text="A"*max_adapter_name_lenght)
conections_frame_width = length_label.winfo_reqwidth()
################################################################################################################################
def update_adapters():
    connection_adapter_refresh_button.configure(command=do_nothing)
    global connection_adapters
    global max_adapter_name_lenght
    global conections_frame_width
    #destroy connection selection frames & button
    for button_no in range (len(connection_adapters)):
        button_var =  "connection" + str(button_no)
        try:
            globals()[button_var].destroy()
        except:
            pass
    connections_frame.destroy()
    #read connections 
    connections_info = net_if_stats()
    #connection adapters
    connection_adapters = str(net_if_stats().keys())
    connection_adapters = str(net_if_stats().keys()).replace(("dict_keys"),"")\
                        .replace("(","").replace(")","").replace("[","").replace("]","").replace(" '","").replace("'","")
    #connection adapters list
    connection_adapters = connection_adapters.split(",")


    #get req length for frame
    max_adapter_name_lenght = 0
    for name in connection_adapters:
        if len(name) > max_adapter_name_lenght:
            max_adapter_name_lenght = len(name)
    length_label =  Label(root,text="A"*max_adapter_name_lenght)
    conections_frame_width = length_label.winfo_reqwidth()

    if connection_frame_open_state == True:
        display_connections()
    else:
        connection_adapter_refresh_button.configure(command=update_adapters_play_sound)
    
################################################################################################################################
refresh_image_dark  = PhotoImage(file=r"source/ui source/refresh_dark.png")
refresh_image_light  = PhotoImage(file=r"source/ui source/refresh_light.png")

################################################################################################################################
#Network connection select Frame 
connection_adapter_select_frame = CTkFrame(main_frame_for_scroll ,width=550)
connection_adapter_select_frame.place(x=10 ,y=10 ,relheight=1)

connection_adapter_select_sub_frame = CTkFrame(main_frame_for_scroll ,height=75 ,width=520)
connection_adapter_select_sub_frame.place(x=25 ,y=15)

#label
label_temp01 = Label(connection_adapter_select_sub_frame ,text="Select Connection    :" ,font=("arial",12,"bold"))
label_temp01.place(x=10 ,y=10)

#selected connection display label
selected_conection_label1 = Label(connection_adapter_select_sub_frame ,font=("arial",12,"bold") ,bg="#2e2e2e")
selected_conection_label1.place(x=210 ,y=10)



################################################################################################################################
def update_timer(s):
    second_1 = 1
    mintue_1 = 1 * 60
    hour_1   = 1 * 60 * 60
    day_1    = 1 * 60 * 60 * 24
    month_1  = 1 * 60 * 60 * 24 * 30
    year_1   = 1 * 60 * 60 * 24 * 30 * 12

    year   = int(s/year_1)
    month  = int((s-(year*year_1))/month_1)
    day    = int((s-((year*year_1)+(month*month_1)))/day_1)
    hour   = int((s-((year*year_1)+(month*month_1)+(day*day_1)))/hour_1)
    mintue = int((s-((year*year_1)+(month*month_1)+(day*day_1)+(hour*hour_1)))/mintue_1)
    second = int((s-((year*year_1)+(month*month_1)+(day*day_1)+(hour*hour_1)+(mintue*mintue_1)))/second_1)

    times  = [year ,month ,day ,hour ,mintue ,second]

    index_temp_001 = 0
    for time_1 in times :
        times[index_temp_001] = "0"*(2-len(str(time_1)))  + str(time_1)
        index_temp_001 += 1

    if s >= year_1 :
        time_converted =  "{0}y {1}m {2}d {3}h {4}m {5}s".format(times[0],times[1],times[2],times[3],times[4],times[5])
    elif s >= month_1 :
        time_converted =  "{0}m {1}d {2}h {3}m {4}s".format(times[1],times[2],times[3],times[4],times[5])
    elif s >= day_1:
        time_converted =  "{0}d {1}h {2}m {3}s".format(times[2],times[3],times[4],times[5])
    elif s >= hour_1 :
        time_converted =  "{0}h {1}m {2}s".format(times[3],times[4],times[5])
    elif s >= mintue_1 :
        time_converted =  "{0}m {1}s".format(times[4],times[5])
    else:
        time_converted =  "{0}s".format(times[5])
    
    time_usage_label.configure(text=time_converted)
    time_usage_label_place_x  = -20 + -(time_usage_label.winfo_reqwidth())
    time_usage_label.place(relx=1 ,y=10 ,x=time_usage_label_place_x)

################################################################################################################################
def get_update_speed(saved_update_speed):
    global update_speed
    update_speeds  = [3000,2000,1000,700,500,200]
    update_speed_modes = ["Very low","Low","Normal","High","Very high","Ultra high"]
    index = 0
    while update_speed_modes[index] != saved_update_speed :
        index += 1
        if index == len(update_speed_modes) :
            index = 2
            break
    update_speed  = update_speeds[index]

    update_speed_file = open("source/settings/general/update speed.txt","w")
    update_speed_file.write(update_speed_modes[index])
    update_speed_file.close()
################################################################################################################################
def speed_mode_bits():
    global speed_display_mode
    global network_average_speed_chart_reset_req
    global network_speed_chart_reset_req
    if speed_display_mode != "bits":
        speed_display_mode = "bits"
        network_average_speed_chart_reset_req = True
        network_speed_chart_reset_req = True
        speed_mode_file = open("source/settings/general/speed mode.txt","w")
        speed_mode_file.write("bits")
        speed_mode_file.close()

    #menu frame change
    reset_menu_frame()
    menu_frame_bits_speed_btn.configure(state="disabled")
    menu_frame_bytes_speed_btn.configure(state="normal")
 
def speed_mode_bytes():
    global speed_display_mode
    global network_average_speed_chart_reset_req
    global network_speed_chart_reset_req
    if speed_display_mode != "bytes":
        speed_display_mode = "bytes"
        network_average_speed_chart_reset_req = True
        network_speed_chart_reset_req = True
        speed_mode_file = open("source/settings/general/speed mode.txt","w")
        speed_mode_file.write("bytes")
        speed_mode_file.close()

    #menu frame change 
    reset_menu_frame()
    menu_frame_bits_speed_btn.configure(state="normal")
    menu_frame_bytes_speed_btn.configure(state="disabled")

#data converter 
def convert_bytes(s,type,with_decimal,special_data_type=False):
    if type == "speed" :
        datas = ["B/s","KB/s","MB/s","GB/s","TB/s","PB/s","EB/s"]
    else:
        datas = ["B","KB","MB","GB","TB","PB","EB"]
    index= 0

    if special_data_type not in datas:
        while len(str(int(s))) > 3 and (index+1) < len(datas):
            s = s /1024
            index += 1
    else:
        while special_data_type != datas[index]:
            s = s /1024
            index += 1
    
    if with_decimal == True:
        val = str(round(s,2)) + " " + datas[index]
    else:
        val = str(int(s)) + " " + datas[index]
    return val
    
def convert_bits(s,type,with_decimal,special_data_type=False):
    if type == "speed" :
        datas = ["bps","Kbps","Mbps","Gbps","Tbps","Pbps","Ebps"]
    else:
        datas = ["b","Kb","Mb","Gb","Tb","Pb","Eb"]
    index= 0
    if special_data_type not in datas:
        while len(str(int(s))) > 3 and (index+1) < len(datas): 
            s = s /1024
            index += 1
    else:
        while special_data_type != datas[index]:
            s = s /1024
            index += 1

    if with_decimal == True:
        val = str(round(s,2)) + " " + datas[index]
    else:
        val = str(int(s)) + " " + datas[index]
    return val
    
################################################################################################################################
#pass
def do_nothing():
    pass
def do_nothing_e(e):
    pass

connection_frame_open_state = False
#set connection 
def select_adapter(connection_adapter_index):
    global selected_conection 
    connections_frame.destroy()
    #destroy connection selection frames & button
    for button_no in range (len(connection_adapters)):
        button_var =  "connection" + str(button_no)
        try:
            globals()[button_var].destroy()
        except:
            pass
    selected_conection = connection_adapters[connection_adapter_index]
    display_adapter(selected_conection)

def display_adapter(selected_conection_temp):
    #set selected connection on label
    selected_conection_label1.configure(text=selected_conection_temp)
    #place back place forget
    network_speed_states_frame.place(x=10,y=90,relheight=0.9) 
    #change back command to normal
    connection_adapter_select_button.configure(command=display_connections_play_sound)
    global connection_frame_open_state
    connection_frame_open_state = False

################################################################################################################################
def cancel_adapter_selection____menu(e):
    global connection_frame_open_state
    if connection_frame_open_state == True: 
        connection_frame_open_state = False
        #destroy connection selection frames & button
        for button_no in range (len(connection_adapters)):
            button_var =  "connection" + str(button_no)
            try:
                globals()[button_var].destroy()
            except:
                pass
        #hide connection frame
        connections_frame.destroy()
        #place back place forget
        network_speed_states_frame.place(x=10,y=90,relheight=0.9) 
        #change back command to normal
        connection_adapter_select_button.configure(command=display_connections_play_sound)
    else:
        global menu_frame_display
        if menu_frame_display == False:
            menu_frame_display = True
            root_x,root_y = root.winfo_geometry().split("+")[-2:]

            if full_screen_enabled == True:
                mouse_point_x = root.winfo_pointerx() - int(root_x)
                mouse_point_y = root.winfo_pointery() - int(root_y)
            else:
                mouse_point_x = root.winfo_pointerx()  - (int(root_x)+8)
                mouse_point_y = root.winfo_pointery()  - (int(root_y)+31)
            menu_frame.place(x=mouse_point_x ,y=mouse_point_y)
        else:
            reset_menu_frame()

################################################################################################################################
def display_connections():
    def play_button_sounds_Enter_02(e):
        audio.load("source/ui source/settings.mp3")
        audio.play()

    global connection_frame_open_state
    connection_frame_open_state = True
    
    #hide network state frame 
    network_speed_states_frame.place_forget()
    root.bind("<Button-3>",do_nothing_e)
    #change button command to do nothing
    connection_adapter_select_button.configure(command=do_nothing)
    connection_adapter_refresh_button.configure(command=do_nothing)

    #buttons create & place
    global btn_palce_y
    global btn_count
    global connections_frame
    btn_count = 0
    btn_palce_y = 4

    #connections frame 
    #connections frame  show adapters name
    connections_frame = CTkFrame(connection_adapter_select_frame ,fg_color=("#f1f1f1","#151515"))
    connections_frame.place(x=255 , y=80 ,height=28*len(connection_adapters)+6 ,width=conections_frame_width ,anchor="n")
    for button in connections_frame.winfo_children():
        button.destroy()
    
    #set adapters button states to normal
    def loop2():
        global btn_count
        button_var = "connection" + str(btn_count)
        try:
            globals()[button_var].configure(state= "normal")
        except:
            pass
        btn_count += 1
        if len(connection_adapters) != btn_count :
            root.after(50,loop2)
        else:
            connection_adapter_refresh_button.configure(command=update_adapters_play_sound)
            root.bind("<Button-3>",cancel_adapter_selection____menu)

    def loop():
        global btn_count
        global btn_palce_y

        button_var =  "connection" + str(btn_count)
        globals()[button_var] = CTkButton(connections_frame ,text=connection_adapters[btn_count] ,height=25 ,width=1 ,border_width=2
                                         ,command=lambda k=btn_count: select_adapter(k) ,state="disabled" ,text_font=("arial",9,"bold")
                                         ,text_color=text_color_001 ,fg_color=fg_color_001 ,border_color=border_color_001 ,hover_color=hover_color_001)
        globals()[button_var].place(relx=0.5 ,y=btn_palce_y ,anchor="n")
        globals()[button_var].bind('<Enter>',play_button_sounds_Enter_02)
    
        btn_count += 1
        btn_palce_y += 28
        if len(connection_adapters) != btn_count:
            root.after(25,loop)
        else:
            #change buttons state to normal
            btn_count = 0
            loop2()
    loop()
################################################################################################################################


def display_connections_play_sound():
    audio.load("source/ui source/main.mp3")
    audio.play()
    display_connections()

def update_adapters_play_sound():
    audio.load("source/ui source/main.mp3")
    audio.play()
    update_adapters()
    
################################################################################################################################
#adapter select button
connection_adapter_select_button = CTkButton(connection_adapter_select_sub_frame ,text="select" ,text_font=("arial",10,"bold") ,border_width=2
                                             ,height=25 ,command=display_connections_play_sound)
connection_adapter_select_button.place(x=180 , y=40)
#refresh button
connection_adapter_refresh_button = CTkButton(connection_adapter_select_sub_frame ,text="",width=39 ,border_width=2
                                             ,height=1 ,command=update_adapters_play_sound)
                                             
connection_adapter_refresh_button.place(x=330 , y=40)

################################################################################################################################
#show network states
network_performence_frame = CTkFrame(main_frame_for_scroll)
network_performence_frame.place(x=570,y=10,relheight=1,relwidth=1 ,width=-570)

#connection name  display
label_temp02 = Label(network_performence_frame ,text="Connection      :  " ,font=("arial",11,"bold"))
label_temp02.place(x=20 ,y=10)
selected_conection_label2 = Label(network_performence_frame ,text="" ,font=("arial",11,"bold"))
selected_conection_label2.place(x=155 ,y=10)

time_usage_label = Label(network_performence_frame ,text="0 s" ,font=("arial",11,"bold"))
time_usage_label.place(relx=1 ,y=10 ,x=-50)
################################################################################################################################
#receive status
network_receive_performence_frame =  CTkFrame(network_performence_frame ,height=120)
network_receive_performence_frame.place(x=10,y=40 ,relwidth=1 ,width=-15)

#
frame_temp01 =  CTkFrame(network_receive_performence_frame ,fg_color="#ff0000" ,width=14 ,height=14 ,corner_radius=3)
frame_temp01.place(x=10 ,y=6)
label_temp06 = Label(network_receive_performence_frame ,text="Receive Status " ,font=("arial",10,"bold"))
label_temp06.place(x=35 ,y=2)

#show network recevie status
network_receive_performence_sub_frame = CTkFrame(network_receive_performence_frame ,height=90)
network_receive_performence_sub_frame.place(x=17,y=24 ,relwidth=1 ,width=-22)

#connection receive speed  
label_temp03 = Label(network_receive_performence_sub_frame ,text="Speed " ,font=("arial",11,"bold"))
label_temp03.place(x=20 ,y=5)
network_receive_speed_label = Label(network_receive_performence_sub_frame ,text="" ,font=("arial",11,"bold"))
network_receive_speed_label.place(x=175 ,y=5)

#connection max receive speed  
label_temp18 = Label(network_receive_performence_sub_frame ,text="Max Speed" ,font=("arial",11,"bold"))
label_temp18.place(x=20 ,y=25)
network_receive_max_speed_label = Label(network_receive_performence_sub_frame ,text="" ,font=("arial",11,"bold"))
network_receive_max_speed_label.place(x=175 ,y=25)

#average recevie 
label_temp04 = Label(network_receive_performence_sub_frame ,text="Average Speed" ,font=("arial",11,"bold"))
label_temp04.place(x=20 ,y=45)
network_avg_receive_speed_label = Label(network_receive_performence_sub_frame ,text="" ,font=("arial",11,"bold"))
network_avg_receive_speed_label.place(x=175 ,y=45)

#total recevied 
label_temp05 = Label(network_receive_performence_sub_frame ,text="Data Usage" ,font=("arial",11,"bold"))
label_temp05.place(x=20 ,y=65)
network_total_receive_label = Label(network_receive_performence_sub_frame ,text="" ,font=("arial",11,"bold"))
network_total_receive_label.place(x=175 ,y=65)


################################################################################################################################
#send status
network_send_performence_frame =  CTkFrame(network_performence_frame ,height=120)
network_send_performence_frame.place(x=10,y=170 ,relwidth=1 ,width=-15)

#
frame_temp02 =  CTkFrame(network_send_performence_frame ,fg_color="#00ff00" ,width=14 ,height=14 ,corner_radius=3)
frame_temp02.place(x=10 ,y=6)
label_temp07 = Label(network_send_performence_frame ,text="Send Status " ,font=("arial",10,"bold"))
label_temp07.place(x=35 ,y=2)

#show network send status
network_send_performence_sub_frame = CTkFrame(network_send_performence_frame ,height=90)
network_send_performence_sub_frame.place(x=17,y=24 ,relwidth=1 ,width=-22)

#connection send speed 
label_temp08 = Label(network_send_performence_sub_frame ,text="Speed " ,font=("arial",11,"bold"))
label_temp08.place(x=20 ,y=5)
network_send_speed_label = Label(network_send_performence_sub_frame ,text="" ,font=("arial",11,"bold"))
network_send_speed_label.place(x=175 ,y=5)

#connection max send speed  
label_temp19 = Label(network_send_performence_sub_frame ,text="Max Speed" ,font=("arial",11,"bold"))
label_temp19.place(x=20 ,y=25)
network_send_max_speed_label = Label(network_send_performence_sub_frame ,text="" ,font=("arial",11,"bold"))
network_send_max_speed_label.place(x=175 ,y=25)

#average send
label_temp09 = Label(network_send_performence_sub_frame ,text="Average Speed" ,font=("arial",11,"bold"))
label_temp09.place(x=20 ,y=45)
network_avg_send_speed_label = Label(network_send_performence_sub_frame ,text="" ,font=("arial",11,"bold"))
network_avg_send_speed_label.place(x=175 ,y=45)

#total sent 
label_temp10 = Label(network_send_performence_sub_frame ,text="Data Usage " ,font=("arial",11,"bold"))
label_temp10.place(x=20 ,y=65)
network_total_send_label = Label(network_send_performence_sub_frame ,text="" ,font=("arial",11,"bold"))
network_total_send_label.place(x=175 ,y=65)

################################################################################################################################
#receive + send status
network_receive_send_performence_frame =  CTkFrame(network_performence_frame ,height=120)
network_receive_send_performence_frame.place(x=10,y=300 ,relwidth=1 ,width=-15)

#
frame_temp03 =  CTkFrame(network_receive_send_performence_frame ,fg_color="#0000ff" ,width=14 ,height=14 ,corner_radius=3)
frame_temp03.place(x=10 ,y=6)
label_temp11 = Label(network_receive_send_performence_frame ,text="Receive & Send Status" ,font=("arial",10,"bold"))
label_temp11.place(x=35 ,y=2)

#show network recevied status
network_receive_send_performence_sub_frame = CTkFrame(network_receive_send_performence_frame ,height=90)
network_receive_send_performence_sub_frame.place(x=17,y=24 ,relwidth=1 ,width=-22)

#connection speed  display
label_temp12 = Label(network_receive_send_performence_sub_frame ,text="Speed" ,font=("arial",11,"bold"))
label_temp12.place(x=20 ,y=5)
network_receive_send_speed_label = Label(network_receive_send_performence_sub_frame ,text="" ,font=("arial",11,"bold"))
network_receive_send_speed_label.place(x=175 ,y=5)

#connection max receive & send speed  
label_temp20 = Label(network_receive_send_performence_sub_frame ,text="Max Speed" ,font=("arial",11,"bold"))
label_temp20.place(x=20 ,y=25)
network_receive_send_max_speed_label = Label(network_receive_send_performence_sub_frame ,text="" ,font=("arial",11,"bold"))
network_receive_send_max_speed_label.place(x=175 ,y=25)

#average recevie 
label_temp13 = Label(network_receive_send_performence_sub_frame ,text="Average Speed" ,font=("arial",11,"bold"))
label_temp13.place(x=20 ,y=45)
network_avg_receive_send_speed_label = Label(network_receive_send_performence_sub_frame ,text="" ,font=("arial",11,"bold"))
network_avg_receive_send_speed_label.place(x=175 ,y=45)

#total recevied 
label_temp14 = Label(network_receive_send_performence_sub_frame ,text="Data Usage" ,font=("arial",11,"bold"))
label_temp14.place(x=20 ,y=65)
network_total_receive_send_label = Label(network_receive_send_performence_sub_frame ,text="" ,font=("arial",11,"bold"))
network_total_receive_send_label.place(x=175 ,y=65)


################################################################################################################################
frames = [network_receive_performence_sub_frame ,network_send_performence_sub_frame ,network_receive_send_performence_sub_frame]
frame_index_temp = 0
dash_label_y_temp = 5
for i in range(12):
    globals()["label_dash_"+str(i)] =  Label(frames[frame_index_temp] ,text=":" ,font=("arial",11,"bold"))
    globals()["label_dash_"+str(i)].place(x=150 ,y=dash_label_y_temp)
    dash_label_y_temp += 20
    if dash_label_y_temp > 65 :
        dash_label_y_temp = 5
        frame_index_temp += 1

try:
    f = open("source/settings/adapters/last adapter info.txt","r")
    selected_conection =  f.readline()
    f.close()
    check_name_temp = net_io_counters(pernic=True)[selected_conection].bytes_recv
except:
    selected_conection = connection_adapters[0]

def start_network_reader():
    f = open("source/settings/process/reader run by app check.txt","w")
    f.close()
    try:
        reader_run_by_app = open("source/settings/process/reader run by app.txt","w")
        reader_run_by_app = open("source/settings/process/reader run by app.txt","r")
        try:
            os.startfile("network info reader.exe")
        except:
            os.startfile("network info reader.py")
    except:
        pass
    while True:
        if os.path.exists("source/settings/process/running_2.txt"):
            break
        else:
            pass

#check reader is endtask ?
def check_reader_state():
    if os.path.exists("source/settings/process/running_2.txt"):
        try:
            os.remove("source/settings/process/running_2.txt")
            start_network_reader()
            while True:
                if os.path.exists("source/settings/process/running_2.txt"):
                    break
                else:
                    pass
        except:
            pass
    else:
        start_network_reader()
        while True:
            if os.path.exists("source/settings/process/running_2.txt"):
                break
            else:
                pass
    root.after(500,check_reader_state)  
check_reader_state()  
#save apater info
def save_adapter_info(adapter):
    replace_name_list = ["/","\\",":","*","?",'"',"<",">","|"]
    for re in replace_name_list:
        adapter = adapter.replace(re,"")
    try:
        adapter_info_save_1 = open("source/settings/adapters/"+adapter+"_temp.txt","w")
        adapter_info_save_1.write(str(total_received_bytes_count)+"\n")
        adapter_info_save_1.write(str(total_sent_bytes_count)+"\n")
        adapter_info_save_1.write(str(total_received_sent_bytes_count)+"\n")
        adapter_info_save_1.write(str(total_network_use_time))
        adapter_info_save_1.close()

        adapter_info_save = open("source/settings/adapters/"+adapter+".txt","w")
        adapter_info_save.write(str(total_received_bytes_count)+"\n")
        adapter_info_save.write(str(total_sent_bytes_count)+"\n")
        adapter_info_save.write(str(total_received_sent_bytes_count)+"\n")
        adapter_info_save.write(str(total_network_use_time))
        adapter_info_save.close()
    except:
        pass
#read before info
def get_adapter_info(adapter):
    replace_name_list = ["/","\\",":","*","?",'"',"<",">","|"]
    for re in replace_name_list:
        adapter = adapter.replace(re,"")
    global saved_received_bytes_start
    global saved_sent_bytes_start
    global saved_received_sent_bytes_start
    global total_network_use_time
    try:
        adapter_info_read_1 = open("source/settings/adapters/"+adapter+"_temp.txt","r")
        saved_received_bytes_start = float(adapter_info_read_1.readline())
        saved_sent_bytes_start = float(adapter_info_read_1.readline())
        saved_received_sent_bytes_start = float(adapter_info_read_1.readline())
        total_network_use_time = float(adapter_info_read_1.readline())
        adapter_info_read.close()
    except:
        try:
            adapter_info_read = open("source/settings/adapters/"+adapter+".txt","r")
            saved_received_bytes_start = float(adapter_info_read.readline())
            saved_sent_bytes_start = float(adapter_info_read.readline())
            saved_received_sent_bytes_start = float(adapter_info_read.readline())
            total_network_use_time = float(adapter_info_read.readline())
            adapter_info_read.close()
        except:
            saved_received_bytes_start = 0
            saved_sent_bytes_start = 0
            saved_received_sent_bytes_start = 0
            total_network_use_time = 0
        
#################################################################
#################################################################
app_main_loop_running = False
def display_network_speed():
    global selected_network_adapter_name
    selected_network_adapter_name = selected_conection

    selected_conection_label2.configure(text=selected_network_adapter_name) 
    selected_conection_label1.configure(text=selected_network_adapter_name) 

    global receive_speed_data_list
    global send_speed_data_list
    global receive_send_speed_data_list

    global receive_average_speed_data_list
    global send_average_speed_data_list
    global receive_send_average_speed_data_list

    global receive_data_usage_data_list
    global send_data_usage_data_list
    global receive_send_data_usage_data_list

    global max_receive_speed 
    global max_send_speed 
    global max_receive_send_speed 

    global time_reset
    
    #save state after every 4 loop
    global save_state
    global save_state_count
    save_state = 0
    save_state_count = 4

    receive_speed_data_list = []
    send_speed_data_list = []
    receive_send_speed_data_list = []

    receive_average_speed_data_list = []
    send_average_speed_data_list = []
    receive_send_average_speed_data_list = []

    receive_data_usage_data_list = []
    send_data_usage_data_list = []
    receive_send_data_usage_data_list = []

    max_receive_speed = 0
    max_send_speed = 0
    max_receive_send_speed = 0

    time_reset = False

    def loop2():
        global app_main_loop_running
        global main_window_minimized_to_system
        if main_window_minimized_to_system == True:
            app_main_loop_running = False
        else:
            app_main_loop_running = True
            try:
                global receive_speed_data_list
                global send_speed_data_list
                global receive_send_speed_data_list

                global receive_average_speed_data_list
                global send_average_speed_data_list
                global receive_send_average_speed_data_list

                global receive_data_usage_data_list
                global send_data_usage_data_list
                global receive_send_data_usage_data_list

                global before_received_bytes_count
                global before_sent_bytes_count
                global before_received_sent_bytes_count

                global time_before
                global total_network_use_time

                global before_received_bytes_start
                global before_sent_bytes_start
                global before_received_sent_bytes_start

                global network_loop_run_count

                global max_receive_speed 
                global max_send_speed 
                global max_receive_send_speed 

                global saved_received_bytes_start
                global saved_sent_bytes_start 
                global saved_received_sent_bytes_start

                global total_received_bytes_count
                global total_sent_bytes_count
                global total_received_sent_bytes_count

                global time_reset

                global save_state
                global save_state_count

                
                #get received bytes now
                now_received_bytes_count = net_io_counters(pernic=True)[selected_network_adapter_name].bytes_recv
                #get sent bytes now
                now_sent_bytes_count = net_io_counters(pernic=True)[selected_network_adapter_name].bytes_sent
                #get sent & receive bytes now
                now_received_sent_bytes_count = now_received_bytes_count + now_sent_bytes_count

                if selected_network_adapter_name == selected_conection :
                    #check error &  if error make exception to restart 
                    if now_received_sent_bytes_count < before_received_sent_bytes_count :
                        int("make exception -> break loop")
                        #convert str in to int make value error -> exception & try restart loop

                #get time now
                time_now = float(str(datetime.datetime.now())[17:])
            
                if time_now <= time_before :
                    time_now += 1
                    time_before -= 59
                    time_reset = True

                time_delay = time_now - time_before
        
                #calculate receive speed
                receive_speed = (now_received_bytes_count-before_received_bytes_count)/(time_delay)
                receive_speed_data_list.append(int(receive_speed))
                if max_receive_speed < receive_speed :
                    max_receive_speed = receive_speed
                #calculate send speed
                send_speed = (now_sent_bytes_count-before_sent_bytes_count)/(time_delay)
                send_speed_data_list.append(int(send_speed))
                if max_send_speed < send_speed :
                    max_send_speed = send_speed
                #calculate receive & send speed
                #receive_send_speed = (now_received_sent_bytes_count - before_received_sent_bytes_start)/(time_delay)
                receive_send_speed = receive_speed + send_speed
                receive_send_speed_data_list.append(receive_send_speed)
                if max_receive_send_speed < receive_send_speed :
                    max_receive_send_speed = receive_send_speed

                try:
                    #total received time 
                    total_network_use_time += (time_delay)
                    update_timer(int(total_network_use_time))
                except:
                    time_usage_label.configure(text="Error")
                    time_usage_label_place_x  = -20 + -(time_usage_label.winfo_reqwidth())
                    time_usage_label.place(relx=1 ,y=10 ,x=time_usage_label_place_x)

                #set time before
                time_before =  time_now
                if time_reset == True:
                    time_before -= 1 
                    time_reset = False

                #total received bytes count
                total_received_bytes_count = (now_received_bytes_count - before_received_bytes_start) + saved_received_bytes_start
                receive_data_usage_data_list.append(total_received_bytes_count)
                #total sent bytes count
                total_sent_bytes_count = (now_sent_bytes_count - before_sent_bytes_start) + saved_sent_bytes_start
                send_data_usage_data_list.append(total_sent_bytes_count)
                #total received sent bytes count
                total_received_sent_bytes_count = (now_received_sent_bytes_count - before_received_sent_bytes_start ) + saved_received_sent_bytes_start
                receive_send_data_usage_data_list.append(total_received_sent_bytes_count)

                if save_state == save_state_count :
                    save_state_count += 4
                    save_adapter_info(selected_network_adapter_name)
                save_state+=1

                #average receive speed
                avg_receive_speed = total_received_bytes_count / total_network_use_time
                receive_average_speed_data_list.append(avg_receive_speed)
            
                #average send speed
                avg_send_speed = total_sent_bytes_count / total_network_use_time
                send_average_speed_data_list.append(avg_send_speed)

                #average send speed
                avg_receive_send_speed = total_received_sent_bytes_count / total_network_use_time
                receive_send_average_speed_data_list.append(avg_receive_send_speed)

            
                #reset before received bytes
                before_received_bytes_count = now_received_bytes_count
                before_sent_bytes_count = now_sent_bytes_count
                before_received_sent_bytes_count = now_received_sent_bytes_count

                if speed_display_mode == "bits":
                    #convert speed to bits mode
                    receive_speed = convert_bits(receive_speed*8,"speed",True)
                    send_speed = convert_bits(send_speed*8,"speed",True)
                    receive_send_speed = convert_bits(receive_send_speed*8,"speed",True)
                    #convert max speed to bits mode
                    max_receive_speed_temp = convert_bits(max_receive_speed*8,"speed",True)
                    max_send_speed_temp = convert_bits(max_send_speed*8,"speed",True)
                    max_receive_send_speed_temp = convert_bits(max_receive_send_speed*8,"speed",True)
                    #convert average speed to bits mode
                    avg_receive_speed = convert_bits(avg_receive_speed*8,"speed",True)
                    avg_send_speed = convert_bits(avg_send_speed*8,"speed",True)
                    avg_receive_send_speed = convert_bits(avg_receive_send_speed*8,"speed",True)
                else:
                    #convert speed to bytes mode
                    receive_speed = convert_bytes(receive_speed,"speed",True)
                    send_speed = convert_bytes(send_speed,"speed",True)
                    receive_send_speed = convert_bytes(receive_send_speed,"speed",True)
                    #convert max speed to bytes mode
                    max_receive_speed_temp = convert_bytes(max_receive_speed,"speed",True)
                    max_send_speed_temp = convert_bytes(max_send_speed,"speed",True)
                    max_receive_send_speed_temp = convert_bytes(max_receive_send_speed,"speed",True)
                    #convert average speed to bytes mode
                    avg_receive_speed = convert_bytes(avg_receive_speed,"speed",True)
                    avg_send_speed = convert_bytes(avg_send_speed,"speed",True)
                    avg_receive_send_speed = convert_bytes(avg_receive_send_speed,"speed",True)

                total_received_bytes = convert_bytes(total_received_bytes_count,"",True)
                total_sent_bytes = convert_bytes(total_sent_bytes_count,"",True)
                total_received_sent_bytes = convert_bytes(total_received_sent_bytes_count,"",True)

                #if network adapter change .. stop loop & call display_network_speed()
                if selected_network_adapter_name == selected_conection :
            
                    #display receive value
                    network_receive_speed_label.configure(text=receive_speed)
                    network_receive_max_speed_label.configure(text=max_receive_speed_temp)
                    network_avg_receive_speed_label.configure(text=avg_receive_speed)
                    network_total_receive_label.configure(text=total_received_bytes)
                    #display send value
                    network_send_speed_label.configure(text=send_speed)
                    network_send_max_speed_label.configure(text=max_send_speed_temp)
                    network_avg_send_speed_label.configure(text=avg_send_speed)
                    network_total_send_label.configure(text=total_sent_bytes)
                    #display receive & send value
                    network_receive_send_speed_label.configure(text=receive_send_speed)
                    network_receive_send_max_speed_label.configure(text=max_receive_send_speed_temp)
                    network_avg_receive_send_speed_label.configure(text=avg_receive_send_speed)
                    network_total_receive_send_label.configure(text=total_received_sent_bytes)

                    #speed
                    if network_loop_run_count == 0:
                        speed_network_chart_display(reset=True ,special_reset= False)
                    else:
                        if network_speed_chart_reset_req == True :
                            speed_network_chart_display(reset=True ,special_reset= True)
                        else:
                            if int(network_speed_state_chart_canvas.winfo_width()) > 940:
                                speed_network_chart_display(reset=True ,special_reset= True)
                            else:
                                speed_network_chart_display(reset=False ,special_reset = False)

                    #average speed 
                    if network_loop_run_count == 0:
                        average_speed_network_chart_display(reset=True ,special_reset= False)
                    else:
                        if network_average_speed_chart_reset_req == True :
                            average_speed_network_chart_display(reset=True ,special_reset= True)
                        else:
                            if int(network_average_speed_state_chart_canvas.winfo_width()) > 940:
                                average_speed_network_chart_display(reset=True ,special_reset = True)
                            else:
                                average_speed_network_chart_display(reset=False ,special_reset = False)

                    #total data usage
                    if network_loop_run_count == 0:
                        data_usage_network_chart_display(reset=True ,special_reset= False)
                    else:
                        if network_data_usage_chart_reset_req == True :
                            data_usage_network_chart_display(reset=True ,special_reset= True)
                        else:
                            if  int(network_data_usage_state_chart_canvas.winfo_width()) > 1800:
                                data_usage_network_chart_display(reset=True ,special_reset= True)
                            else:
                                data_usage_network_chart_display(reset=False ,special_reset = False)
                    
                    network_loop_run_count += 1
                    root.after(update_speed,loop2)
                else:
                    save_adapter_info(selected_network_adapter_name)
                    display_network_speed()
            except:           
                global error_seleced_network_connection
                error_seleced_network_connection  = selected_conection
                def checking_device_error():
                    global saved_received_bytes_start
                    global saved_sent_bytes_start 
                    global saved_received_sent_bytes_start
                    global total_network_use_time
                    try:
                        net_io_counters(pernic=True)[selected_conection].bytes_recv
                        display_network_speed()
                    except:
                        if main_window_minimized_to_system == True:
                            app_main_loop_running = False
                        else:
                            root.after(20,checking_device_error)
                checking_device_error()

    global before_received_bytes_count
    global before_sent_bytes_count
    global before_received_sent_bytes_count

    global time_before

    global before_received_bytes_start
    global before_sent_bytes_start
    global before_received_sent_bytes_start

    global network_loop_run_count
   
    #total of received bytes
    before_received_bytes_count = net_io_counters(pernic=True)[selected_conection].bytes_recv
    #total of sent bytes
    before_sent_bytes_count = net_io_counters(pernic=True)[selected_conection].bytes_sent
    #total of received & sent bytes
    before_received_sent_bytes_count = before_received_bytes_count + before_sent_bytes_count
    #calculate start time
    time_before = float(str(datetime.datetime.now())[17:])
    
    #total received bytes started 
    before_received_bytes_start = net_io_counters(pernic=True)[selected_conection].bytes_recv
    #total sent bytes started 
    before_sent_bytes_start = net_io_counters(pernic=True)[selected_conection].bytes_sent
    #total of received & sent bytes started
    before_received_sent_bytes_start = before_received_bytes_start + before_sent_bytes_start
    
    #loop run count
    network_loop_run_count = 0
    global saved_received_bytes_start
    global saved_sent_bytes_start
    global saved_received_sent_bytes_start
    global total_network_use_time
   
    #get before status
    get_adapter_info(selected_conection)
   
    #new loop 
    root.after(update_speed,loop2)

################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
#set speed type
def speed_set_chart_data_type():
    global speed_chart_value_data_type

    if speed_display_mode == "bits":
        highest_speed_temp = max_speed*8
        highest_speed = max_speed*8
        speed_chart_value_data_type = convert_bits(highest_speed_temp,"speed",False).split(" ")[-1]
    else:
        highest_speed_temp = max_speed
        highest_speed = max_speed
        speed_chart_value_data_type = convert_bytes(highest_speed_temp,"speed",False).split(" ")[-1]
    network_speed_barchart_data_type_label.configure(text=speed_chart_value_data_type)
    
    for speed_chart_label_no in range(1,12):
        if speed_display_mode == "bits":
            speed_network_chart_value =  convert_bits(highest_speed_temp,"speed",True ,speed_chart_value_data_type).split(" ")[0]
        else:
            speed_network_chart_value =  convert_bytes(highest_speed_temp,"speed",True ,speed_chart_value_data_type).split(" ")[0]
        if len(str(int(float(speed_network_chart_value)))) == 1 :
            speed_network_chart_value_temp = speed_network_chart_value[:3]
        else:
            speed_network_chart_value_temp = int(float(speed_network_chart_value))
        globals()["chart_speed_label"+str(speed_chart_label_no)].configure(text=speed_network_chart_value_temp)
        highest_speed_temp = highest_speed/10 * (10-speed_chart_label_no)

################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
def speed_network_chart_display(reset ,special_reset):
    global speed_special_value
    global speed_data_index
    global speed_start_x
    global speed_end_x
    global speed_receive_start_y
    global speed_receive_end_y
    global speed_send_start_y
    global speed_send_end_y
    global speed_receive_send_start_y
    global speed_receive_send_end_y
    global receive_speed_data_list
    global send_speed_data_list
    global receive_send_speed_data_list
    global max_speed 

    speed_special_value = 1

    ################################################################################################################################
    ################################################################################################################################
    if reset == True:
        global speed_data_index
        global network_speed_chart_reset_req
        global display_temp_speed_label
    
        speed_data_index = 0 
        speed_start_x = 0
        speed_end_x = 0
        
        speed_receive_end_y = 0
        speed_send_end_y = 0
        speed_receive_send_end_y = 0
        display_temp_speed_label = 6
        
        if len(receive_send_speed_data_list) > 30 :
            max_speed = max(receive_send_speed_data_list[-30:]) * 1.2
        else:
            max_speed = max(receive_send_speed_data_list)  * 1.2
        if max_speed == 0 :
            max_speed = 1

        speed_receive_start_y = 265-((265/100)*  (((receive_speed_data_list[speed_data_index]/max_speed)*100))) + 1.1
        speed_send_start_y = 265-((265/100)*  (((send_speed_data_list[speed_data_index]/max_speed)*100)))   +1.1
        speed_receive_send_start_y = 265-((265/100)*  (((receive_send_speed_data_list[speed_data_index]/max_speed)*100))) +1.1

        network_speed_state_chart_canvas.delete("all")
        speed_set_chart_data_type()

        network_speed_state_chart_canvas.configure(width=470)
        network_speed_state_chart_canvas.place(y=50,x=30)

        #barchart reset
        for i in range(1,11):
            globals()["chart_speed_frame"+str(i)].configure(width=470)
            
        #remove old label
        temp_speed_label_num = 9
        while True:
            try:
                globals()["temp_speed_label"+str(temp_speed_label_num)].destroy()
                temp_speed_label_num += 9
            except:
                break

        if special_reset == True:
            # receive_speed_data_list or send_speed_data_list ot receive_send_speed_data_list
            if len(receive_speed_data_list) > 30 :
                receive_speed_data_list = receive_speed_data_list[-30:]
                send_speed_data_list = send_speed_data_list[-30:]
                receive_send_speed_data_list = receive_send_speed_data_list[-30:]
            else:
                pass
            speed_special_value = len(receive_speed_data_list)

    
    network_speed_chart_reset_req = False
    #data type update test

    #check max speed
    global now_speed
    now_speed = receive_send_speed_data_list[-1]
    if now_speed > max_speed :
        network_speed_chart_reset_req = True
    #if final 30 s data speed lower than max speed ,update req True
    if len(receive_speed_data_list) > 55 :
        if max(receive_send_speed_data_list[-55:]) * 1.2 < max_speed :
            network_speed_chart_reset_req = True
  
    for loops in range(speed_special_value):

        speed_end_x += 15

        if speed_end_x > 450:
            now_width = int(network_speed_state_chart_canvas.winfo_width())
            now_palce_x = int(network_speed_state_chart_canvas.place_info()["x"])
            network_speed_state_chart_canvas.place(x=now_palce_x - 15 ,y=50)
            network_speed_state_chart_canvas.configure(width=now_width+15)

            for i in range(1,11):
                width_temp = int(globals()["chart_speed_frame"+str(i)].winfo_width())
                globals()["chart_speed_frame"+str(i)].configure(width=width_temp+15)
                
        #receive speed line chart
        receive_speed = (receive_speed_data_list[speed_data_index])
        speed_receive_end_y = 265-((265/100)*  (((receive_speed/max_speed)*100))) + 1.1
        network_speed_state_chart_canvas.create_line(speed_start_x,speed_receive_start_y,speed_end_x,speed_receive_end_y 
                                            ,fill="#ff0000" ,width=2.2)
        speed_receive_start_y = speed_receive_end_y

        #send speed line chart
        send_speed = (send_speed_data_list[speed_data_index])
        speed_send_end_y = 265-((265/100)*  (((send_speed/max_speed)*100)) ) + 1.1
        network_speed_state_chart_canvas.create_line(speed_start_x,speed_send_start_y,speed_end_x,speed_send_end_y 
                                            ,fill="#00ff00" ,width=2.2)
        speed_send_start_y = speed_send_end_y

        #receive send speed line chart
        receive_send_speed = (receive_send_speed_data_list[speed_data_index])
        speed_receive_send_end_y = 265-((265/100)*  (((receive_send_speed/max_speed)*100))) + 1.1
        network_speed_state_chart_canvas.create_line(speed_start_x,speed_receive_send_start_y,speed_end_x,speed_receive_send_end_y
                                            ,fill="#0000ff",width=2.2)
        speed_receive_send_start_y = speed_receive_send_end_y
        

        #place labels
        if display_temp_speed_label%9 == 0:
            if speed_display_mode == "bits":
                label_val = (convert_bits(receive_send_speed_data_list[speed_data_index]*8,"speed",True ,speed_chart_value_data_type)[0:-4])
            else:
                label_val = (convert_bytes(receive_send_speed_data_list[speed_data_index],"speed",True ,speed_chart_value_data_type)[0:-4])
            globals()["temp_speed_label"+str(display_temp_speed_label)] = CTkLabel(master=network_speed_state_chart_canvas ,text=label_val ,
                                                                                   fg_color=("#f1f1f1","#343638"),text_color=("#808080","#aaaaaa"),
                                                                                   bg_color=("#ffffff","#151515") ,width=1 ,height=1 
                                                                                   ,text_font=('arial',8,"bold"))
            globals()["temp_speed_label"+str(display_temp_speed_label)].place(x=speed_end_x ,y=speed_receive_send_start_y-20,anchor="n")
        display_temp_speed_label+=1
        

        speed_start_x = speed_end_x
        speed_data_index += 1

        
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################

#connection performence
network_speed_states_frame = CTkFrame(connection_adapter_select_frame,width=530 ,height=750)
network_speed_states_frame.place(x=10,y=90) 

#speed
#receive performence
network_speed_state_chart_frame = CTkFrame(network_speed_states_frame ,width=520 ,height=350)
network_speed_state_chart_frame.place(x=5,y=20)

#chart disaply  canvas
network_speed_state_chart_canvas = Canvas(network_speed_state_chart_frame ,width=470 ,height=265,highlightthickness=0)
network_speed_state_chart_canvas.place(x=30,y=50)

#chart hide frame
network_speed_state_chart_hide_frame =  CTkFrame(network_speed_state_chart_frame ,width=30 ,height=320)
network_speed_state_chart_hide_frame.place(x=0,y=10)

#chart name 
label_temp15 = Label(network_speed_states_frame ,font=("arial",8,"bold") ,text="Speed")
label_temp15.place(relx=0.5 ,y=0 ,anchor="n")

#chart frames 
network_speed_chart_verticle_bar_frame = Frame(network_speed_state_chart_frame ,width=2 ,height=293)
network_speed_chart_verticle_bar_frame.place(x=25,y=25)
network_speed_chart_horizontal_bar_frame = Frame(network_speed_state_chart_frame ,width=485 ,height=2)
network_speed_chart_horizontal_bar_frame.place(x=25,y=316)

#barchart speed type label
network_speed_barchart_data_type_label = Label(network_speed_state_chart_frame ,font=("arial",8,"bold") ,text="????")
network_speed_barchart_data_type_label.place(x=10,y=1)


#barchart speed labels
temp_rely_0 = 40
for i in range(1,12):
    globals()["chart_speed_label"+str(i)]=Label(network_speed_state_chart_frame ,text="?" ,font=("arial",8,"bold") ,width=2)
    globals()["chart_speed_label"+str(i)].place(x=0,y=temp_rely_0)
    temp_rely_0 += 26.5

temp_rely_1 = 0
for i in range(1,11):
    globals()["chart_speed_frame"+str(i)] = Frame(network_speed_state_chart_canvas ,width=470 ,height=1)
    globals()["chart_speed_frame"+str(i)].place(x=-1,y=temp_rely_1)
    temp_rely_1 += 26.5
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
#set speed type
def average_speed_set_chart_data_type():
    global average_speed_chart_value_data_type

    if speed_display_mode == "bits":
        highest_average_speed_temp = max_average_speed*8
        highest_average_speed = max_average_speed*8
        average_speed_chart_value_data_type = convert_bits(highest_average_speed_temp,"speed",False).split(" ")[-1]
    else:
        highest_average_speed_temp = max_average_speed
        highest_average_speed = max_average_speed
        average_speed_chart_value_data_type = convert_bytes(highest_average_speed_temp,"speed",False).split(" ")[-1]

    network_average_speed_barchart_data_type_label.configure(text=average_speed_chart_value_data_type)

    for average_speed_chart_label_no in range(1,12):
        if speed_display_mode == "bits":
            average_speed_network_chart_value =  convert_bits(highest_average_speed_temp,"speed",True ,average_speed_chart_value_data_type).split(" ")[0]
        else:
            average_speed_network_chart_value =  convert_bytes(highest_average_speed_temp,"speed",True ,average_speed_chart_value_data_type).split(" ")[0]
        if len(str(int(float(average_speed_network_chart_value)))) == 1 :
            average_speed_network_chart_value_temp = average_speed_network_chart_value[:3]
        else:
            average_speed_network_chart_value_temp = int(float(average_speed_network_chart_value))
        globals()["chart_average_speed_label"+str(average_speed_chart_label_no)].configure(text=average_speed_network_chart_value_temp)
        highest_average_speed_temp = highest_average_speed/10 * (10-average_speed_chart_label_no)
    
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
def average_speed_network_chart_display(reset ,special_reset):
    global average_speed_special_value
    global average_speed_data_index
    global average_speed_start_x
    global average_speed_end_x
    global average_speed_receive_start_y
    global average_speed_receive_end_y
    global average_speed_send_start_y
    global average_speed_send_end_y
    global average_speed_receive_send_start_y
    global average_speed_receive_send_end_y
    global receive_average_speed_data_list
    global send_average_speed_data_list
    global receive_send_average_speed_data_list
    global max_average_speed 

    average_speed_special_value = 1

    ################################################################################################################################
    ################################################################################################################################
    if reset == True:
        global average_speed_data_index
        global network_average_speed_chart_reset_req
        global display_temp_average_speed_label
    
        average_speed_data_index = 0 
        average_speed_start_x = 0
        average_speed_end_x = 0
        
        average_speed_receive_end_y = 0
        average_speed_send_end_y = 0
        average_speed_receive_send_end_y = 0
        display_temp_average_speed_label = 6

        if len(receive_send_average_speed_data_list) > 30:
            max_average_speed = max(receive_send_average_speed_data_list[-30:]) * 1.2
            
        else:
            max_average_speed = max(receive_send_average_speed_data_list) * 1.2
        if max_average_speed == 0 :
            max_average_speed = 1
        
        average_speed_receive_start_y = 265-((265/100)*  (((receive_average_speed_data_list[average_speed_data_index]/max_average_speed)*100)))  + 1.1
        average_speed_send_start_y = 265-((265/100)*  (((send_average_speed_data_list[average_speed_data_index]/max_average_speed)*100)))  + 1.1
        average_speed_receive_send_start_y = 265-((265/100)*  (((receive_send_average_speed_data_list[average_speed_data_index]/max_average_speed)*100)))  + 1.1

        network_average_speed_state_chart_canvas.delete("all")
        average_speed_set_chart_data_type()

        network_average_speed_state_chart_canvas.configure(width=470 ,height=265)
        network_average_speed_state_chart_canvas.place(y=50,x=30)

        #barchart reset
        for i in range(1,11):
            globals()["chart_average_speed_frame"+str(i)].configure(width=470)
         
        #remove old label
        temp_average_speed_label_num = 9
        while True:
            try:
                globals()["temp_average_speed_label"+str(temp_average_speed_label_num)].destroy()
                temp_average_speed_label_num += 9
            except:
                break

        if special_reset == True:
            # receive_average_speed_data_list or send_average_speed_data_list ot receive_send_average_speed_data_list
            if len(receive_average_speed_data_list) > 30 :
                receive_average_speed_data_list = receive_average_speed_data_list[-30:]
                send_average_speed_data_list = send_average_speed_data_list[-30:]
                receive_send_average_speed_data_list = receive_send_average_speed_data_list[-30:]
            else:
                pass
            average_speed_special_value = len(receive_average_speed_data_list)


    network_average_speed_chart_reset_req = False
    #data type update test

    #check max average_speed
    global now_average_speed
    now_average_speed = receive_send_average_speed_data_list[-1]
    if now_average_speed  > max_average_speed:
        network_average_speed_chart_reset_req = True
    #if final 30 s data average_speed lower than max average_speed ,update req True
    if len(receive_send_average_speed_data_list) > 55 :
        if max(receive_send_average_speed_data_list[-55:])*1.2 < max_average_speed :
            network_average_speed_chart_reset_req = True
  
    for loops in range(average_speed_special_value):
        average_speed_end_x += 15

        if average_speed_end_x > 450:
            now_width = int(network_average_speed_state_chart_canvas.winfo_width())
            now_palce_x = int(network_average_speed_state_chart_canvas.place_info()["x"])
            network_average_speed_state_chart_canvas.place(x=now_palce_x - 15 ,y=50)
            network_average_speed_state_chart_canvas.configure(width=now_width+15)
        
            for i in range(1,11):
                width_temp = int(globals()["chart_average_speed_frame"+str(i)].winfo_width())
                globals()["chart_average_speed_frame"+str(i)].configure(width=width_temp+15)
              
        #receive average_speed line chart
        receive_average_speed = (receive_average_speed_data_list[average_speed_data_index])
        average_speed_receive_end_y = 265-((265/100)*  (((receive_average_speed/max_average_speed)*100))) + 1.1
        network_average_speed_state_chart_canvas.create_line(average_speed_start_x,average_speed_receive_start_y,average_speed_end_x,average_speed_receive_end_y 
                                            ,fill="#ff0000" ,width=2.2)
        average_speed_receive_start_y = average_speed_receive_end_y

        #send average_speed line chart
        send_average_speed = (send_average_speed_data_list[average_speed_data_index])
        average_speed_send_end_y = 265-((265/100)*  (((send_average_speed/max_average_speed)*100)) )  +1.1
        network_average_speed_state_chart_canvas.create_line(average_speed_start_x,average_speed_send_start_y,average_speed_end_x,average_speed_send_end_y 
                                            ,fill="#00ff00" ,width=2.2)
        average_speed_send_start_y = average_speed_send_end_y

        #receive send average_speed line chart
        receive_send_average_speed = (receive_send_average_speed_data_list[average_speed_data_index])
        average_speed_receive_send_end_y = 265-((265/100)*  (((receive_send_average_speed/max_average_speed)*100)))  + 1.1
        network_average_speed_state_chart_canvas.create_line(average_speed_start_x,average_speed_receive_send_start_y,average_speed_end_x,average_speed_receive_send_end_y
                                            ,fill="#0000ff",width=2.2)
        average_speed_receive_send_start_y = average_speed_receive_send_end_y

        #place labels
        if display_temp_average_speed_label%9 == 0:
            if speed_display_mode == "bits":
                label_val = (convert_bits(receive_send_average_speed_data_list[average_speed_data_index]*8,"speed",True ,average_speed_chart_value_data_type)[0:-4])
            else:
                label_val = (convert_bits(receive_send_average_speed_data_list[average_speed_data_index],"speed",True ,average_speed_chart_value_data_type)[0:-4])
            globals()["temp_average_speed_label"+str(display_temp_average_speed_label)] = CTkLabel(master=network_average_speed_state_chart_canvas ,text=label_val ,
                                                                                   fg_color=("#f1f1f1","#343638"),text_color=("#808080","#aaaaaa"),
                                                                                   bg_color=("#ffffff","#151515") ,width=1 ,height=1 
                                                                                   ,text_font=('arial',8,"bold"))
            globals()["temp_average_speed_label"+str(display_temp_average_speed_label)].place(x=average_speed_end_x ,y=average_speed_receive_send_start_y-20,anchor="n")
        display_temp_average_speed_label+=1

        average_speed_start_x = average_speed_end_x
        average_speed_data_index += 1

    
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################

#receive performence
network_average_speed_state_chart_frame = CTkFrame(network_speed_states_frame ,width=520 ,height=350)
network_average_speed_state_chart_frame.place(x=5,y=400)

#chart disaply  canvas
network_average_speed_state_chart_canvas = Canvas(network_average_speed_state_chart_frame ,width=470 ,height=265,highlightthickness=0)
network_average_speed_state_chart_canvas.place(x=30,y=50)

#chart hide frame
network_average_speed_state_chart_hide_frame =  CTkFrame(network_average_speed_state_chart_frame ,width=30 ,height=320)
network_average_speed_state_chart_hide_frame.place(x=0,y=10)

#chart name 
label_temp16= Label(network_speed_states_frame ,font=("arial",8,"bold") ,text="Average speed")
label_temp16.place(relx=0.5 ,y=380 ,anchor="n")

#chart frames 
network_average_speed_chart_verticle_bar_frame = Frame(network_average_speed_state_chart_frame ,width=2 ,height=293)
network_average_speed_chart_verticle_bar_frame.place(x=25,y=25)
network_average_speed_chart_horizontal_bar_frame = Frame(network_average_speed_state_chart_frame ,width=485 ,height=2)
network_average_speed_chart_horizontal_bar_frame.place(x=25,y=316)

#barchart average_speed type label
network_average_speed_barchart_data_type_label = Label(network_average_speed_state_chart_frame ,font=("arial",8,"bold") ,text="????")
network_average_speed_barchart_data_type_label.place(x=10,y=1)


#barchart average_speed labels
temp_rely_0 = 40
for i in range(1,12):
    globals()["chart_average_speed_label"+str(i)]=Label(network_average_speed_state_chart_frame ,text="?" ,font=("arial",8,"bold") ,width=2)
    globals()["chart_average_speed_label"+str(i)].place(x=0,y=temp_rely_0)
    temp_rely_0 += 26.5

temp_rely_1 = 0
for i in range(1,11):
    globals()["chart_average_speed_frame"+str(i)] = Frame(network_average_speed_state_chart_canvas ,width=470 ,height=1)
    globals()["chart_average_speed_frame"+str(i)].place(x=-1,y=temp_rely_1)
    temp_rely_1 += 26.5

################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
#set speed type
def data_usage_set_chart_data_type():
    highest_data_usage_temp = max_data_usage
    highest_data_usage = max_data_usage
    data_usage_chart_value_data_type = convert_bytes(highest_data_usage_temp,"",False).split(" ")[-1]
    network_data_usage_barchart_data_type_label.configure(text=data_usage_chart_value_data_type)
    for data_usage_chart_label_no in range(1,12):
        data_usage_network_chart_value =  convert_bytes(highest_data_usage_temp,"none",True ,data_usage_chart_value_data_type).split(" ")[0]
        if len(str(int(float(data_usage_network_chart_value)))) == 1 :
            data_usage_network_chart_value_temp = data_usage_network_chart_value[:3]
        else:
            data_usage_network_chart_value_temp = int(float(data_usage_network_chart_value))
        globals()["chart_data_usage_label"+str(data_usage_chart_label_no)].configure(text=data_usage_network_chart_value_temp)
        highest_data_usage_temp = highest_data_usage/10 * (10-data_usage_chart_label_no)

################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
def data_usage_network_chart_display(reset ,special_reset):
    global data_usage_special_value
    global data_usage_data_index
    global data_usage_start_x
    global data_usage_end_x
    global data_usage_receive_start_y
    global data_usage_receive_end_y
    global data_usage_send_start_y
    global data_usage_send_end_y
    global data_usage_receive_send_start_y
    global data_usage_receive_send_end_y
    global receive_data_usage_data_list
    global send_data_usage_data_list
    global receive_send_data_usage_data_list
    global max_data_usage 

    data_usage_special_value = 1

    ################################################################################################################################
    ################################################################################################################################
    if reset == True:
        global data_usage_data_index
        global network_data_usage_chart_reset_req
    
        data_usage_data_index = 0 

        data_usage_start_x = 0
        data_usage_end_x = 0
        
        data_usage_receive_end_y = 0
        data_usage_send_end_y = 0
        data_usage_receive_send_end_y = 0

        max_data_usage = receive_send_data_usage_data_list[-1]*1.3
        if max_data_usage == 0:
            max_data_usage = 1
            
        data_usage_receive_start_y = 265-((265/100)*  (((receive_data_usage_data_list[data_usage_data_index]/(max_data_usage))*100)))  + 1.1
        data_usage_send_start_y = 265-((265/100)*  (((send_data_usage_data_list[data_usage_data_index]/(max_data_usage))*100)))  + 1.1
        data_usage_receive_send_start_y = 265-((265/100)*  (((receive_send_data_usage_data_list[data_usage_data_index]/(max_data_usage))*100)))  + 1.1

        network_data_usage_state_chart_canvas.delete("all")
        data_usage_set_chart_data_type()

        network_data_usage_state_chart_canvas.configure(width=900)
        network_data_usage_state_chart_canvas.place(y=50,x=30)

        if special_reset == True:
            # receive_data_usage_data_list or send_data_usage_data_list ot receive_send_data_usage_data_list
            if len(receive_data_usage_data_list) > 60 :
                receive_data_usage_data_list = receive_data_usage_data_list[-60:]
                send_data_usage_data_list = send_data_usage_data_list[-60:]
                receive_send_data_usage_data_list = receive_send_data_usage_data_list[-60:]
            else:
                pass
            data_usage_special_value = len(receive_data_usage_data_list)


    network_data_usage_chart_reset_req = False
    #data type update test

    #check max data_usage
    global now_data_usage
    now_data_usage = receive_send_data_usage_data_list[-1] * 1
    if now_data_usage  > max_data_usage :
        network_data_usage_chart_reset_req = True

    for loops in range(data_usage_special_value):
        data_usage_end_x += 15

        if data_usage_end_x > 900:
            now_width = int(network_data_usage_state_chart_canvas.winfo_width())
            now_palce_x = int(network_data_usage_state_chart_canvas.place_info()["x"])
            network_data_usage_state_chart_canvas.place(x=now_palce_x - 15 ,y=50)
            network_data_usage_state_chart_canvas.configure(width=now_width+15)


        #receive data_usage line chart
        receive_data_usage = (receive_data_usage_data_list[data_usage_data_index])
        data_usage_receive_end_y = 265-((265/100)*  (((receive_data_usage/(max_data_usage))*100))) + 1.1
        network_data_usage_state_chart_canvas.create_line(data_usage_start_x,data_usage_receive_start_y,data_usage_end_x,data_usage_receive_end_y 
                                            ,fill="#ff0000" ,width=2.2)
        data_usage_receive_start_y = data_usage_receive_end_y

        #send data_usage line chart
        send_data_usage = (send_data_usage_data_list[data_usage_data_index])
        data_usage_send_end_y = 265-((265/100)*  (((send_data_usage/(max_data_usage))*100)) ) + 1.1
        network_data_usage_state_chart_canvas.create_line(data_usage_start_x,data_usage_send_start_y,data_usage_end_x,data_usage_send_end_y 
                                            ,fill="#00ff00" ,width=2.2)
        data_usage_send_start_y = data_usage_send_end_y

        #receive send data_usage line chart
        receive_send_data_usage = (receive_send_data_usage_data_list[data_usage_data_index])
        data_usage_receive_send_end_y = 265-((265/100)*  (((receive_send_data_usage/(max_data_usage))*100))) + 1.1
        network_data_usage_state_chart_canvas.create_line(data_usage_start_x,data_usage_receive_send_start_y,data_usage_end_x,data_usage_receive_send_end_y
                                            ,fill="#0000ff",width=2.2)
        data_usage_receive_send_start_y = data_usage_receive_send_end_y

        data_usage_start_x = data_usage_end_x
        data_usage_data_index += 1

    
#total data usage
#receive performence
network_data_usage_state_chart_frame = CTkFrame(network_performence_frame ,width=990 ,height=350)
network_data_usage_state_chart_frame.place(x=20,y=485)

#chart disaply  canvas
network_data_usage_state_chart_canvas = Canvas(network_data_usage_state_chart_frame ,width=920 ,height=265,highlightthickness=0)
network_data_usage_state_chart_canvas.place(x=30,y=50)

#chart hide frame
network_data_usage_state_chart_hide_frame =  CTkFrame(network_data_usage_state_chart_frame ,width=30 ,height=320)
network_data_usage_state_chart_hide_frame.place(x=0,y=10)

#chart name 
label_temp17= Label(network_performence_frame ,font=("arial",8,"bold") ,text="Data Usage")
label_temp17.place(x=480 ,y=465)

#chart frames 
network_data_usage_chart_verticle_bar_frame = Frame(network_data_usage_state_chart_frame ,width=2 ,height=293)
network_data_usage_chart_verticle_bar_frame.place(x=25,y=25)
network_data_usage_chart_horizontal_bar_frame = Frame(network_data_usage_state_chart_frame ,width=940 ,height=2)
network_data_usage_chart_horizontal_bar_frame.place(x=25,y=316)

#barchart data_usage type label
network_data_usage_barchart_data_type_label = Label(network_data_usage_state_chart_frame ,font=("arial",8,"bold") ,text="????")
network_data_usage_barchart_data_type_label.place(x=10,y=1)

#barchart data_usage labels
temp_rely = 40
for i in range(1,12):
    if i != 11:
        globals()["chart_data_usage_frame"+str(i)] = Frame(network_data_usage_state_chart_frame ,width=920 ,height=1)
        globals()["chart_data_usage_frame"+str(i)].place(x=29,y=temp_rely + 10)
    globals()["chart_data_usage_label"+str(i)]=Label(network_data_usage_state_chart_frame ,text="?" ,font=("arial",8,"bold") ,width=2)
    globals()["chart_data_usage_label"+str(i)].place(x=0,y=temp_rely)
    temp_rely += 26.5

################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
#side panel
side_panel_frame = CTkFrame(root ,width=400)

#change theme
theme_change_frame = CTkFrame(side_panel_frame ,width=290 ,height=90)
theme_change_frame.place(y=20 ,x=20)
theme_label = Label(theme_change_frame ,text="App Theme     :" ,font=("Arial",10,"bold"))
theme_label.place(x=20 ,y=10)
light_btn = CTkButton(theme_change_frame,command=light,text="Light",width=100 ,border_width=2 ,text_font=("arial",9,"bold"))
light_btn.place(x=160,y=10)
dark_btn = CTkButton(theme_change_frame,command=dark,text="Dark",width=100 ,border_width=2 ,text_font=("arial",9,"bold"))
dark_btn.place(x=160,y=45)

#transparent 
transparent_change_frame = CTkFrame(side_panel_frame ,width=340 ,height=90)
transparent_change_frame.place(y=130 ,x=325)
transparent_label = Label(transparent_change_frame ,text="Transparency Effects     :" ,font=("Arial",10,"bold"))
transparent_label.place(x=20 ,y=10)
transparent_enable_btn = CTkButton(transparent_change_frame,command=transparent_enable,text="Enable",width=100 ,border_width=2 ,text_font=("arial",9,"bold"))
transparent_enable_btn.place(x=210,y=10)
transparent_disable_btn = CTkButton(transparent_change_frame,command=transparent_disable,text="Disable",width=100 ,border_width=2 ,text_font=("arial",9,"bold"))
transparent_disable_btn.place(x=210,y=45)

#full screen  
full_screen_change_frame = CTkFrame(side_panel_frame ,width=290 ,height=90)
full_screen_change_frame.place(y=130 ,x=20)
full_screen_label = Label(full_screen_change_frame ,text="Full Screen     :" ,font=("Arial",10,"bold"))
full_screen_label.place(x=20 ,y=10)
full_screen_enable_btn = CTkButton(full_screen_change_frame,command=full_screen_enable,text="Enable",width=100 ,border_width=2 ,text_font=("arial",9,"bold"))
full_screen_enable_btn.place(x=160,y=10)
full_screen_disable_btn = CTkButton(full_screen_change_frame,command=full_screen_disable,text="Disable",width=100 ,border_width=2 ,text_font=("arial",9,"bold"))
full_screen_disable_btn.place(x=160,y=45)
full_screen_enabled = False
def full_screen_change(e):
    if full_screen_enabled == True:
        full_screen_disable()
    else:
        full_screen_enable()
root.bind("<F11>",full_screen_change)

#speed bytes\s or bits\s
speed_mode_frame = CTkFrame(side_panel_frame ,width=340 ,height=90)
speed_mode_frame.place(y=20 ,x=325)
speed_mode_label = Label(speed_mode_frame ,text="Speed Option     :" ,font=("Arial",10,"bold"))
speed_mode_label.place(x=20 ,y=10)
bits_speed_btn = CTkButton(speed_mode_frame,command=speed_mode_bits,text="Bits per second",width=150 ,border_width=2 ,text_font=("arial",9,"bold"))
bits_speed_btn.place(x=160,y=10)
bytes_speed_btn = CTkButton(speed_mode_frame,command=speed_mode_bytes,text="Bytes per second",width=150 ,border_width=2 ,text_font=("arial",9,"bold"))
bytes_speed_btn.place(x=160,y=45)

#update speed 
update_speed_change_frame = CTkFrame(side_panel_frame ,width=300 ,height=215)
update_speed_change_frame.place(y=20 ,x=680)
update_speed_change_label = Label(update_speed_change_frame ,text="Update Speed    :" ,font=("Arial",10,"bold"))
update_speed_change_label.place(x=20 ,y=10)


#update speed buttons
update_speed_modes = ["Very low","Low","Normal","High","Very high","Ultra high"]
update_speed_btn_x = 160
update_speed_btn_y = 10 # +40
for index_temp in range(6):
    globals()["update_speed_btn"+str(index_temp)] = CTkButton(update_speed_change_frame,text=update_speed_modes[index_temp]
                                                             ,width=110 ,border_width=2 ,command= lambda update_speed_mode=update_speed_modes[index_temp]: get_update_speed(update_speed_mode),
                                                             text_font=("arial",9,"bold"))
    globals()["update_speed_btn"+str(index_temp)].place(x=update_speed_btn_x ,y = update_speed_btn_y)
    update_speed_btn_y += 32


#always set on trayicon 
minimize_to_trayicon_change_frame = CTkFrame(side_panel_frame ,width=340 ,height=90)
minimize_to_trayicon_change_frame.place(y=240 ,x=20)
minimize_to_trayicon_change_label = Label(minimize_to_trayicon_change_frame ,text="Minimize to System Icons    :" ,font=("Arial",10,"bold"))
minimize_to_trayicon_change_label.place(x=20 ,y=10)
minimize_to_trayicon_change_label_2 = Label(minimize_to_trayicon_change_frame ,text="(When app start by \n startup or user)" ,font=("Arial",8,"bold"))
minimize_to_trayicon_change_label_2.place(x=45 ,y=30)
minimize_to_trayicon_enable_btn = CTkButton(minimize_to_trayicon_change_frame,command=system_icon_mode_enable,text="Enable",width=100 ,border_width=2 ,text_font=("arial",9,"bold"))
minimize_to_trayicon_enable_btn.place(x=220,y=10)
minimize_to_trayicon_disable_btn = CTkButton(minimize_to_trayicon_change_frame,command=system_icon_mode_disable,text="Disable",width=100 ,border_width=2 ,text_font=("arial",9,"bold"))
minimize_to_trayicon_disable_btn.place(x=220,y=45)


#vercion
vercion_label = Label(side_panel_frame ,text="V 2.1.1 ",font=("arial",9 ,"bold"))
vercion_label.place(x=10 ,rely=1 ,y=-20 )
################################################################################################################################

side_panel_open = False
def show_side_panel():
    global side_panel_open
    side_panel_open = True
    #hide data usage chart
    network_data_usage_state_chart_frame.place_forget()
    label_temp17.place_forget()

    #change settings button
    settings_button.configure(bg=setting_btn_bg_001 ,activebackground=setting_btn_bg_001)

    global show_side_panel_place_y
    settings_button.configure(command=close_side_panel)
    show_side_panel_place_y = root.winfo_height()
    def openning():
        global show_side_panel_place_y
        side_panel_frame.place(x=590,y=show_side_panel_place_y,relheight=1,relwidth=1 ,width=-600 ,height=-470)  
        show_side_panel_place_y -= 20
        if show_side_panel_place_y > 450 :
            root.after(5,openning)
    openning()

def close_side_panel() :
    global side_panel_open
    side_panel_open = False
    global close_side_panel_place_y
    settings_button.configure(command=show_side_panel)

    close_side_panel_place_y = int(side_panel_frame.place_info()["y"])
    def closing():
        global close_side_panel_place_y
        side_panel_frame.place(x=590,y=close_side_panel_place_y,relheight=1,relwidth=1 ,width=-600 ,height=-470)  
        close_side_panel_place_y += 20
        if close_side_panel_place_y <=  root.winfo_height() :
            root.after(5,closing)
        else:
            #change settings button
            settings_button.configure(bg=setting_btn_bg_002 ,activebackground=setting_btn_bg_002)
            #total close side panel
            side_panel_frame.place_forget()
            #place data usage chart
            label_temp17.place(x=480 ,y=465)
            network_data_usage_state_chart_frame.place(x=20,y=485)
    closing()

#setting button
setting_btn_image_01 = PhotoImage(file=r"source/ui source/settings_01.png")
setting_btn_image_02 = PhotoImage(file=r"source/ui source/settings_02.png")
settings_button = Button(root ,image=setting_btn_image_01 ,command=show_side_panel ,borderwidth=0 ,cursor="hand2")


def change_settings_btn(e):
    settings_button.configure(image=setting_btn_image_02)
def change_settings_btn_back(e):
    settings_button.configure(image=setting_btn_image_01)

settings_button.bind("<Enter>" ,change_settings_btn)
settings_button.bind("<Leave>" ,change_settings_btn_back)

################################################################################################################################
#menu
menu_frame_display = False
def root_menu_hide(e):
    menu_frame.place_forget()
    reset_menu_frame()
def reset_menu_frame():
    global menu_frame_display
    menu_frame_display = False
    menu_frame.place_forget()

menu_frame = CTkFrame(root,width=152 ,height=280,border_width=2 )

#alwayson top button
always_on_top_root = False
def always_on_top_enable():
    global always_on_top_root
    always_on_top_root = True
    menu_frame_always_on_top_enable_btn.configure(state="disabled")
    menu_frame_always_on_top_disable_btn.configure(state="normal")
    root.attributes('-topmost' ,True)
    reset_menu_frame()
    
def always_on_top_disable():
    global always_on_top_root
    always_on_top_root = False
    menu_frame_always_on_top_enable_btn.configure(state="normal")
    menu_frame_always_on_top_disable_btn.configure(state="disabled")
    root.attributes('-topmost' ,False)
    reset_menu_frame()

#always on top settings
menu_frame_always_on_top_frame = CTkFrame(menu_frame,width=140 ,height=80)
menu_frame_always_on_top_frame.place(x=6,y=10)
menu_frame_always_on_top_label = Label(menu_frame_always_on_top_frame,text="Always on Top :",font=("arial",9,"bold"))
menu_frame_always_on_top_label.place(x=2 ,y=4)
menu_frame_always_on_top_enable_btn=CTkButton(menu_frame_always_on_top_frame,text="Enable" ,command=always_on_top_enable ,
                                             text_font=("arial",8,"bold"), border_width=2)
menu_frame_always_on_top_enable_btn.place(x=60 ,y=25 ,width=70 ,height=20)
menu_frame_always_on_top_disable_btn=CTkButton(menu_frame_always_on_top_frame,text="Disable" ,command=always_on_top_disable ,
                                             text_font=("arial",8,"bold"), border_width=2 ,state="disabled")
menu_frame_always_on_top_disable_btn.place(x=60 ,y=50 ,width=70 ,height=20)

#full screen  
menu_frame_full_screen_change_frame = CTkFrame(menu_frame,width=140 ,height=80)
menu_frame_full_screen_change_frame.place(x=6 ,y=100)
menu_frame_full_screen_label = Label(menu_frame_full_screen_change_frame ,text="Full Screen     :" ,font=("Arial",9,"bold"))
menu_frame_full_screen_label.place(x=2 ,y=4)
menu_frame_full_screen_enable_btn = CTkButton(menu_frame_full_screen_change_frame,command=full_screen_enable,text="Enable",
                                             width=100,text_font=("arial",8,"bold") ,border_width=2 )
menu_frame_full_screen_enable_btn.place(x=60 ,y=25 ,width=70 ,height=20)
menu_frame_full_screen_disable_btn = CTkButton(menu_frame_full_screen_change_frame,command=full_screen_disable,text="Disable",
                                                width=100 ,text_font=("arial",8,"bold"),border_width=2 ,state="disabled" )
menu_frame_full_screen_disable_btn.place(x=60 ,y=50 ,width=70 ,height=20)


#speed bytes\s or bits\s
menu_frame_speed_mode_frame = CTkFrame(menu_frame ,width=140 ,height=80)
menu_frame_speed_mode_frame.place(x=6 ,y=190)
menu_frame_speed_mode_label = Label(menu_frame_speed_mode_frame ,text="Speed Option     :" ,font=("Arial",9,"bold"))
menu_frame_speed_mode_label.place(x=2 ,y=4)
menu_frame_bits_speed_btn = CTkButton(menu_frame_speed_mode_frame,command=speed_mode_bits,text="Bits/s",width=150 ,border_width=2 ,
                                    text_font=("arial",8,"bold"))
menu_frame_bits_speed_btn.place(x=60 ,y=25 ,width=70 ,height=20)
menu_frame_bytes_speed_btn = CTkButton(menu_frame_speed_mode_frame,command=speed_mode_bytes,text="Bytes/s",width=150 ,border_width=2 ,
                                    text_font=("arial",8,"bold"))
menu_frame_bytes_speed_btn.place(x=60 ,y=50 ,width=70 ,height=20)

root.bind("<Button-3>",cancel_adapter_selection____menu)
root.bind("<Button-1>",root_menu_hide)

################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################


def play_button_sounds_Enter_01(e):
    audio.load("source/ui source/settings.mp3")
    audio.play()

button_list = [menu_frame_always_on_top_enable_btn ,menu_frame_always_on_top_disable_btn ,menu_frame_full_screen_enable_btn ,menu_frame_full_screen_disable_btn,
               menu_frame_bits_speed_btn ,menu_frame_bytes_speed_btn ,
               light_btn ,dark_btn ,transparent_enable_btn ,transparent_disable_btn,
               full_screen_enable_btn ,full_screen_disable_btn ,bits_speed_btn ,bytes_speed_btn]
for button in button_list :
    button.bind('<Enter>',play_button_sounds_Enter_01)
for index_temp in range(6):
    globals()["update_speed_btn"+str(index_temp)].bind('<Enter>',play_button_sounds_Enter_01)

################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################

#get theme
try:
    file = open("source/settings/theme/theme.txt","r")
    saved_theme = file.readline()
    file.close()
except:
    saved_theme = "dark"
if saved_theme == "light":
    app_theme = "dark"
    light()
else:
    app_theme = "light"
    dark()

################################################################################################################################
###############################################################################################################################
show_error_frame= CTkFrame()
show_error_frame.place(relwidth=1 ,relheight=1)

show_error_label= CTkLabel(show_error_frame,text="If you quit application \n Data usage calculation won't be continue..",
                    text_font=('arial','11','bold') )
show_error_label.place(relx=0.5 ,rely=0.27 ,anchor="center")

quit_application = CTkButton(show_error_frame ,text="Quit app" ,width=100 ,
                        border_width=2,text_font=('arial',9,'bold'),
                        command=quit_app)
quit_application.place(y=70 ,x=100)
cancel_quit_application = CTkButton(show_error_frame ,text="Cancel" ,width=100 ,
                    border_width=2,text_font=('arial',9,'bold'),
                    command=cancel_quit_app)
cancel_quit_application.place(y=70 ,x=250)
show_error_frame.place_forget()
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################

################################################################################################################################
#get transparent
try:
    file = open("source/settings/theme/transparent.txt","r")
    saved_transparent = file.readline()
    file.close()
except Exception :
    saved_transparent = "disable"
if saved_transparent == "enable":
    transparent_enabled = False
    transparent_enable()
else:
    transparent_enabled = True
    transparent_disable()

################################################################################################################################
#get speed mode
try:
    file = open("source/settings/general/speed mode.txt","r")
    saved_speed_mode = file.readline()
    file.close()
except:
    saved_speed_mode = "bytes"
if saved_speed_mode == "bits":
    speed_display_mode = "bytes"
    speed_mode_bits()
else:
    speed_display_mode = "bits"
    speed_mode_bytes()

################################################################################################################################
#get update speed
try:
    file = open("source/settings/general/update speed.txt","r")
    saved_update_speed = file.readline()
    file.close()
except:
    saved_update_speed = "normal"
get_update_speed(saved_update_speed)
################################################################################################################################
try:
    file = open("source/settings/general/system icon.txt","r")
    saved_system_icon_mode=file.readline()
except:
    saved_system_icon_mode="enable"

if saved_system_icon_mode == "enable":
    system_icon_mode_enabled = True
    val_waiting_for_hide = 0
    def waiting_for_hide():
        global val_waiting_for_hide
        val_waiting_for_hide += 1
        if val_waiting_for_hide < 2 :
            root.after(1000,waiting_for_hide)
        else:
            hide_window()
    waiting_for_hide()
    main_window_minimized_to_system = True
else:
    #display network speed
    main_window_minimized_to_system = False
    system_icon_mode_enabled = False
    display_network_speed()

################################################################################################################################
root.protocol('WM_DELETE_WINDOW', hide_window)


def hide_scrollbars_settings_button__side_panel(event):
    if event.width >= 1607:
        horizontal_scroller.place_forget()
    else:
        horizontal_scroller.place(relwidth=1 ,rely=1 ,y=-13 ,height=13)
    if event.height >=900:
        vertical_scroller.place_forget()
       
    else:
        vertical_scroller.place(relheight=1 ,relx=1 ,x=-13 ,width=13)

    if event.width >= 1607 and event.height >=900:
         settings_button.place(rely=1 ,relx=1 ,y=-55 ,x=-56)
    else:
        settings_button.place_forget()
        if side_panel_open == True:
            close_side_panel()
#hide scrollbars 
main_frame_temp.bind('<Configure>',hide_scrollbars_settings_button__side_panel)

main_canvas.pack(side='left',expand=True,fill='both')
root.mainloop()

#save last selected adapter
f = open("source/settings/adapters/last adapter info.txt","w")
f.write(selected_conection)
f.close()