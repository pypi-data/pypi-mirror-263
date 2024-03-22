from tkinter import Widget


class NavigationError(Exception):
  pass


class Navigator:

  def __init__(self):
    self.pages: dict[str, Widget] = {}
    self.current_page: str | None = None
    self.history: list[str] = []

  def add_page(self, page_name: str, page_widget: Widget) -> bool:
    """Add page to navigator
    Args:
        page_name (str): used to identify the page, must be unique
        page_widget (Widget): tkinter frame widget (or similar)

    Raises:
        NavigationError: if page already exists

    Returns:
        bool: True if page is added
    """
    if self.pages.get(page_name, False):
      raise NavigationError("PAGE ALREADY EXISTS!")

    # add page
    self.pages[page_name] = page_widget
    return True

  def remove_page(self, page_name: str) -> bool:
    """Remove page from navigator

    Args:
        page_name (str): name of the page to be removed

    Raises:
        NavigationError: if page doesn't exist

    Returns:
        bool: True if page exists
    """

    if not self.pages.get(page_name, False):
      raise NavigationError("PAGE DOES NOT EXIST!")

    # delete page
    del self.pages[page_name]
    return True

  def navigate_to(self, page_name: str) -> bool:
    """Navigate to page

    Args:
        page_name (str): name of page to navigate to

    Raises:
        NavigationError: if page doesn't exist

    Returns:
        bool: True if navigation successful
    """
    if not self.pages.get(page_name, False):
      raise NavigationError("PAGE DOES NOT EXIST!")

    if self.current_page is not None:
      # add page to history
      self.history.append(self.current_page[::])
      # remove the current page from view
      self.pages[self.current_page].pack_forget()

    # render new page
    self.current_page = page_name
    self.pages[self.current_page].pack()
    return True

  def get_history(self) -> list[str]:
    """Get History (most recent page first)

    Returns:
        list[str]: navigation history
    """
    return self.history[::-1]
