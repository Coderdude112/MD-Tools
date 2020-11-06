Set WshShell = CreateObject("WScript.Shell")
working_dir = CreateObject("Scripting.FileSystemObject").GetParentFolderName(WScript.ScriptFullName)
WshShell.Run chr(34) & working_dir + "\Starter 1.bat" & Chr(34), 0
Set WshShell = Nothing