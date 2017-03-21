on run {input, parameters}
	tell application "System Preferences"
		activate
		name of panes
		set current pane to pane id "com.apple.preferences.bluetooth"
	end tell
	return input
end run
