Sub createLink()

    Dim x As Integer
    Dim LastRow As Integer
    
    Dim regexOne As Object
    Set regexOne = New RegExp
    regexOne.Pattern = "\="
    regexOne.Global = False
    regexOne.IgnoreCase = True
    Dim str As Object
    Dim a As Object
    
    LastRow = Cells(Rows.Count, Mid(ActiveCell.Address, 2, 1)).End(xlUp).Row
'    myNum = Application.InputBox("Enter a sheetname for oringinal reference")
    
    With ThisWorkbook.Worksheets("Sheet2")
        For x = 1 To LastRow
            Debug.Print regexOne.Replace(ActiveCell.Formula, "")
            Cells(x, Mid(ActiveCell.Address, 2, 1)).Activate
            .Hyperlinks.Add Anchor:=Selection, Address:="", _
            SubAddress:=regexOne.Replace(ActiveCell.Formula, ""), TextToDisplay:="Main Sheet"
        Next x
    End With
    
End Sub




