Dim WShell
Set WShell = CreateObject("WScript.Shell")
Set arg = WScript.Arguments
WShell.Run arg(0), 0
Set WShell = Nothing