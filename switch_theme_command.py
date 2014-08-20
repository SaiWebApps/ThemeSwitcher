import sublime
import sublime_plugin

""" Constants """

THEME_KEY_IN_SETTINGS = 'color_scheme'
THEMES_LIST = [
	'Packages/Color Scheme - Default/Monokai.tmTheme',
	'Packages/Color Scheme - Default/Amy.tmTheme',
	'Packages/Color Scheme - Default/SpaceCadet.tmTheme',
	'Packages/Color Scheme - Default/Zenburnesque.tmTheme',
	'Packages/Color Scheme - Default/LAZY.tmTheme',
	'Packages/Color Scheme - Default/Cobalt.tmTheme',
	'Packages/Color Scheme - Default/Blackboard.tmTheme',
	'Packages/Color Scheme - Default/Sunburst.tmTheme',
	'Packages/Color Scheme - Default/Twilight.tmTheme'
]
DEFAULT_THEME = 'Packages/Color Scheme - Default/Monokai.tmTheme'

OLD_THEME_NAME_KEY = 'old_theme_name'
NEW_THEME_NAME_KEY = 'new_theme_name'

class SwitchThemeCommand(sublime_plugin.TextCommand):
	def __dict_transition_to_next_theme(self, object_settings):

		""" 
			Transition to the next theme in THEMES_LIST. 
			Return the old theme value and the new theme value. 

			Parameters:
				object_settings --> Sublime's global settings for the current tab; 1 is color_scheme
		"""

		# Get the current theme.
		string_current_theme_name = object_settings.get(THEME_KEY_IN_SETTINGS)
		# Dict to store the old theme name and the new theme name.
		dict_return_values = {}
		# Save old theme.
		dict_return_values[OLD_THEME_NAME_KEY] = string_current_theme_name

		try:
			int_current_theme_index_in_THEMES_LIST = THEMES_LIST.index(string_current_theme_name)
	
			# Let the length of THEMES_LIST be 5.
			# If int_current_theme_index is 4, then wrap around from the end of the list to the beginning (to index 0).
			int_next_theme_index_in_THEMES_LIST = (int_current_theme_index_in_THEMES_LIST + 1) % len(THEMES_LIST)
	
			# If current theme is Twilight, then the next theme would be Monokai.
			# If current theme is Cobalt, then the next theme would be Blackboard.
			string_next_theme_name = THEMES_LIST[int_next_theme_index_in_THEMES_LIST]
		except:
			# 2 things could have gone wrong in the try block:
			# 	1. Current theme is not in THEMES_LIST for whatever reason.
			#	2. Next theme is invalid.
			# Response: Set the theme to the default theme, which here is THEMES_LIST[0].
			string_next_theme_name = DEFAULT_THEME

		# Transition to the next theme.
		object_settings.set(THEME_KEY_IN_SETTINGS, string_next_theme_name)
		# Save the new theme to dict_return_values and return the dict.
		dict_return_values[NEW_THEME_NAME_KEY] = string_next_theme_name
		return dict_return_values

	def run(self, edit):

		""" Transition to the next theme in THEMES_LIST. """

		object_sublime_settings = self.view.settings()
		dict_themes = self.__dict_transition_to_next_theme(object_sublime_settings)
		print(dict_themes[OLD_THEME_NAME_KEY] + ' ----> ' + dict_themes[NEW_THEME_NAME_KEY])
