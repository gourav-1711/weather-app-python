layout = """
#:import get_color_from_hex kivy.utils.get_color_from_hex

<TopBar>:
    orientation: "horizontal"
    spacing: "8dp" 
    padding: ["12dp", "10dp", "12dp", "0dp"]
    adaptive_height: True
    pos_hint: {"top": 1} 
    
    # --- GLASSY SEARCH BAR (outline mode, fully rounded) ---
    MDTextField:
        id: search_field
        mode: "outlined"
        
        size_hint: (0.85, None)
        height: "44dp"
        pos_hint: {"center_y": 0.5}
        
        # --- TEXT COLORS ---
        text_color_normal: 1, 1, 1, 1
        text_color_focus: 1, 1, 1, 1
        
        # --- OUTLINE BORDER ---
        line_color_normal: 1, 1, 1, 0.3
        line_color_focus: 1, 1, 1, 0.6
        
        # --- SHAPE ---
        radius: [22, 22, 22, 22]
        on_text_validate: root.on_search()
        
        # --- HINT TEXT ---
        MDTextFieldHintText:
            text: "Search city..."
            text_color_normal: 1, 1, 1, 0.6
            text_color_focus: 1, 1, 1, 0.8

    # --- GLASSY SEARCH BUTTON ---
    MDIconButton:
        icon: "magnify"
        style: "standard"
        
        user_font_size: "22sp"
        size_hint: (None, None)
        size: "44dp", "44dp"
        
        theme_icon_color: "Custom"
        icon_color: 1, 1, 1, 1
        
        md_bg_color: 1, 1, 1, 0.2
        
        pos_hint: {"center_y": 0.5}
        on_release: root.on_search()
"""
