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
			object_settings --> Sublime's global settings; 1 is color_scheme
		"""

		string_current_theme_name = object_settings.get(THEME_KEY_IN_SETTINGS)
		return_values_dict = {}
		return_values_dict[OLD_THEME_NAME_KEY] = string_current_theme_name

		try:
			int_current_theme_index_in_THEMES_LIST = THEMES_LIST.index(string_current_theme_name)
	
			# If current_theme_index is 4, (4+1) % 5 = 0 - we wrap around to beginning from end.
			int_next_theme_index_in_THEMES_LIST = (int_current_theme_index_in_THEMES_LIST + 1) % len(THEMES_LIST)
	
			# If current theme is Twilight, then the next theme would be Monokai.
			# If current theme is Cobalt, then the next theme would be Blackboard.
			string_next_theme_name = THEMES_LIST[int_next_theme_index_in_THEMES_LIST]

			# Save new theme value in return_values dict, and update theme in settings.
			return_values_dict[NEW_THEME_NAME_KEY] = string_next_theme_name
			object_settings.set(THEME_KEY_IN_SETTINGS, string_next_theme_name)

		except:
			# 2 sources of error:
			#   a. Current theme is not THEMES_LIST.
			#	b. Next theme's name is invalid (no such theme exists).
			# 
			# How to handle:
			# 	a. Reset theme to DEFAULT_THEME.
			#	b. Map NEW_THEME_NAME_KEY to DEFAULT_THEME in return_values_dict.
			object_settings.set(THEME_KEY_IN_SETTINGS, DEFAULT_THEME)
			return_values_dict[NEW_THEME_NAME_KEY] = DEFAULT_THEME
		
		return return_values_dict

	def run(self, edit):

		""" Transition to the next theme in THEMES_LIST. """

		object_sublime_settings = self.view.settings()
		dict_themes = self.__dict_transition_to_next_theme(object_sublime_settings)
		print(dict_themes[OLD_THEME_NAME_KEY] + ' ----> ' + dict_themes[NEW_THEME_NAME_KEY])