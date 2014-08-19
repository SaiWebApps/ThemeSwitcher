Sublime Text 3 - Theme Switcher Plugin
===========================================

<h4> High-Level Requirements </h4>
1. When the user presses "CTRL" + "ALT" + "T" on the keyboard, Sublime's current theme shall change. <br>
	1a. The user shall specify the theme paths and their order in a list global variable within the plugin.
	1b. If a user-specified theme cannot be found, the plugin should try to install it from 
	<a href="http://colorsublime.com/">http://colorsublime.com/</a>.

2. All Python code shall conform to PEP 8. <br>

<h4> Prerequisites </h4>
1. Python 2.7 or up <br>
2. Sublime Text 3

<h4> Development Plan </h4>
<table>
	<tr>
		<th> Task </th>
		<th> Started </th>
		<th> Completion Date </th>
	</tr>

	<tr>
		<td> Develop a simple plugin that can change the theme whenever it is executed on the console. </td>
		<td> 08/18/2014 </td>
		<td> 08/19/2014 </td>
	</tr>

	<tr>
		<td> Refactor the above plugin to change the theme when the user presses "CTRL" + "ALT" + "T". </td>
		<td> 08/19/2014 </td>
		<td> 08/19/2014 </td>
	</tr>

	<tr>
		<td> Install color scheme from <a href="http://colorsublime.com/">http://colorsublime.com/</a> 
		if it cannot be found. </td>
		<td> 08/19/2014 </td>
		<td> ? </td>
	</tr>
</table>

<h4> Keyboard Mapping in Sublime </h4>
In Sublime's main menu, click "Preferences -> Key Bindings - User." <br>
Then copy-and-paste the following information:

<pre>
[
	{
		"keys": ["ctrl+alt+t"], "command": "switch_theme"
	}
]
</pre>

Essentially, I am mapping "CTRL+ALT+T" to the SwitchThemeCommand