Hierarchy Theory
================
Widgets in GTK+ are built on top of each other to create what the user views on screen. This is done to varying degrees of complexity depending on the widget, with the lines blurred between some and more clear between others.

One of the useful features of widget hierarchy is that it allows code to be shared between widgets, so that they behave in similar ways making development much easier once the initial learning curve is overcome.

=======
Example
=======
All visible widgets are based on GtkWidget. This is a base class which contains a range of methods. These methods can be used by any widget which inherits from GtkWidget. One example would be the ``.set_tooltip_text()`` method which allows a string of text describing the widget to be attached to it.

This means that the method, due to inheritance, can also be used by GtkButton or GtkEntry.

=========
Structure
=========
The structure of widgets and objects in GTK+ is shown below::

  +GtkWidget
  +---GtkContainer
  +------GtkBin
  +---------GtkWindow
  +------------GtkDialog
  +---------------GtkAboutDialog
  +---------------GtkAppChooserDialog
  +---------------GtkColorSelectionDialog
  +---------------GtkFileChooserDialog
  +---------------GtkFontChooserDialog
  +---------------GtkMessageDialog
  +---------------GtkPageSetupUnixDialog
  +---------------GtkPrintUnixDialog
  +---------------GtkRecentChooserDialog
  +------------GtkApplicationWindow
  +------------GtkAssistant
  +------------GtkOffscreenWindow
  +------------GtkPlug
  +------------GtkShortcutsWindow
  +---------GtkActionBar
  +---------GtkAlignment
  +---------GtkComboBox
  +------------GtkAppChooserButton
  +------------GtkComboBoxText
  +---------GtkFrame
  +------------GtkAspectFrame
  +---------GtkButton
  +------------GtkToggleButton
  +---------------GtkCheckButton
  +------------------GtkRadioButton
  +---------------GtkMenuButton
  +------------GtkColorButton
  +------------GtkFontButton
  +------------GtkLinkButton
  +------------GtkLockButton
  +------------GtkModelButton
  +------------GtkScaleButton
  +---------------GtkVolumeButton
  +---------GtkMenuItem
  +------------GtkCheckMenuItem
  +---------------GtkRadioMenuItem
  +------------GtkSeparatorMenuItem
  +---------GtkEventBox
  +---------GtkExpander
  +---------GtkFlowBoxChild
  +---------GtkHandleBox
  +---------GtkListBoxRow
  +---------GtkToolItem
  +------------GtkToolButton
  +---------------GtkMenuToolButton
  +---------------GtkToggleToolButton
  +------------------GtkRadioToolButton
  +---------GtkOverlay
  +---------GtkScrolledWindow
  +------------GtkPlacesSidebar
  +---------GtkPopover
  +------------GtkPopoverMenu
  +---------GtkRevealer
  +---------GtkSearchBar
  +---------GtkSearchSidebar
  +---------GtkViewport
  +------GtkBox
  +---------GtkAppChooserWidget
  +---------GtkButtonBox
  +---------GtkColorChooserWidget
  +---------GtkFileChooserButton
  +---------GtkFileChooserWidget
  +---------GtkFontChooserWidget
  +---------GtkInfoBar
  +---------GtkRecentChooserWidget
  +---------GtkShortcutsSelection
  +---------GtkShortcutsGroup
  +---------GtkShortcutsShortcut
  +---------GtkStackSwitcher
  +------GtkFixed
  +------GtkGrid
  +------GtkPaned
  +------GtkIconView
  +------GtkLayout
  +------GtkMenuShell
  +---------GtkMenuBar
  +---------GtkMenu
  +------------GtkRecentChooserMenu
  +------GtkNotebook
  +------GtkSocket
  +------GtkTable
  +------GtkTextView
  +------GtkToolbar
  +------GtkToolItemGroup
  +------GtkToolPalette
  +------GtkTreeView
  +---GtkMisc
  +------GtkLabel
  +---------GtkAccelLabel
  +------GtkImage
  +---GtkCalendar
  +---GtkDrawingArea
  +---GtkEntry
  +------GtkSearchEntry
  +------GtkSpinButton
  +---GtkRange
  +------GtkScale
  +------GtkScrollbar
  +---GtkSeparator
  +---GtkInvisible
  +---GtkProgressBar
  +---GtkSpinner
  +---GtkSwitch
  +---GtkLevelbar

