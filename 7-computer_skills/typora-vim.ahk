#SingleInstance Force
vimNormalMode := false ; 默认插入模式

#HotIf WinActive("ahk_exe Typora.exe")

; Esc 进入Vim普通模式
Esc:: {
    global vimNormalMode, originalCursor
    vimNormalMode := true
    ToolTip("NORMAL MODE")
    SetTimer(ToolTip, -1200)
}

; i / a 切换插入模式
$i:: {
    global vimNormalMode, originalCursor
    if vimNormalMode {
        vimNormalMode := false
        ToolTip("INSERT MODE")
        SetTimer(ToolTip, -1200)
    } else {
        SendInput "i"
    }
}

$a:: {
    global vimNormalMode, originalCursor
    if vimNormalMode {
        vimNormalMode := false
        ToolTip("INSERT MODE")
        SetTimer(ToolTip, -1200)
    } else {
        SendInput "a"
    }
}

; hjkl 移动
$h:: {
    global vimNormalMode
    if vimNormalMode
        SendInput "{Left}"
    else
        SendInput "h"
}
$j:: {
    global vimNormalMode
    if vimNormalMode
        SendInput "{Down}"
    else
        SendInput "j"
}
$k:: {
    global vimNormalMode
    if vimNormalMode
        SendInput "{Up}"
    else
        SendInput "k"
}
$l:: {
    global vimNormalMode
    if vimNormalMode
        SendInput "{Right}"
    else
        SendInput "l"
}

; 0 跳到行首
$0:: {
    global vimNormalMode
    if vimNormalMode
        SendInput "{Home}"
    else
        SendInput "0"
}

; ====== 修复：原来 $$:: 报错，改用 $ 字符热键 ======
; $ 跳到行尾
+4:: {
    global vimNormalMode
    if vimNormalMode
        SendInput "{End}"
    else
        SendInput "$"
}

; x 删除字符
$x:: {
    global vimNormalMode
    if vimNormalMode
        SendInput "{Del}"
    else
        SendInput "x"
}

; u 撤销
$u:: {
    global vimNormalMode
    if vimNormalMode
        SendInput "^z"
    else
        SendInput "u"
}

; dd 删除整行
$d:: {
    global vimNormalMode
    static lastD := 0
    now := A_TickCount
    if vimNormalMode {
        if (now - lastD < 300) {
            SendInput "^d" ; dd 剪切整行
            lastD := 0
        } else {
            lastD := now
        }
    } else {
        SendInput "d"
    }
}

; yy 复制整行
$y:: {
    global vimNormalMode
    static lastY := 0
    now := A_TickCount
    if vimNormalMode {
        if (now - lastY < 300) {
            SendInput "^c" ; 复制整行
            lastY := 0
        } else {
            lastY := now
        }
    } else {
        SendInput "y"
    }
}

; p 粘贴
$p:: {
    global vimNormalMode
    if vimNormalMode {
        SendInput "^v"
    } else {
        SendInput "p"
    }
}

; o 下方新建行，进入插入模式
$o:: {
    global vimNormalMode
    if vimNormalMode {
        SendInput "{End}{Enter}"
        vimNormalMode := false
    } else {
        SendInput "o"
    }
}

; O Shift+o 上方新建行，进入插入模式
$+o:: {
    global vimNormalMode
    if vimNormalMode {
        SendInput "{Home}{Enter}{Up}"
        vimNormalMode := false
    } else {
        SendInput "O"
    }
}

#HotIf