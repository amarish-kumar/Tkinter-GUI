"""Submenus"""
bfox_create_submenu = Menu(bfox_filemenu)
bfox_create_submenu.add_command(label="File",command=create)
bfox_create_submenu.add_command(label="Directory",command=create)

"""Menuitems"""
# bfox_filemenu.add_command(label="Create",command=create)
bfox_filemenu.add_cascade(label="Create",menu=bfox_create_submenu)
bfox_filemenu.add_command(label="Read",command=create)
bfox_filemenu.add_command(label="Update",command=create)
bfox_filemenu.add_command(label="Delete",command=create)
bfox_filemenu.add_separator()
bfox_filemenu.add_command(label="Close",command=create)
bfox_menubar.add_cascade(label="Crud",menu=bfox_filemenu)