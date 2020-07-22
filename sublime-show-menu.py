import sublime
from sublime_plugin import EventListener

class HideMenu(EventListener):
  def on_new(self, view):
    window = view.window()
    if not window.is_menu_visible():
      window.set_menu_visible(True)
