package utils

import (
	"demo/chatroom/common/message"
	"encoding/binary"
	"encoding/json"
	"errors"
	"fmt"
	"net"
)

type Transfer struct {
	// 分析应该有哪些字段
	Conn net.Conn
	Buf  [8096]byte
}

func (this *Transfer) ReadPkg() (mes message.Message, err error) {
	fmt.Println("读取服务器发送的数据。。。", mes)
	// conn.Read 在conn没有被关闭的情况下，才会阻塞
	// 如果客户端关闭了 conn，则不会阻塞了
	_, err = this.Conn.Read(this.Buf[:4])
	if err != nil {
		fmt.Println("conn.Read err=", err)
		// err = errors.New("read Pkg header error")
		return
	}
	// fmt.Println("服务器读取客户端发送的数据：", string(buf[:4]))

	// 根据buf[:4]转成uint32类型
	var pkgLen uint32
	pkgLen = binary.BigEndian.Uint32(this.Buf[:4])
	// 根据pkgLen读取消息内容
	n, err := this.Conn.Read(this.Buf[:pkgLen])
	if n != int(pkgLen) || err != nil {
		fmt.Println("conn.Read err=", err)
		err = errors.New("read Pkg body error")
		return
	}

	// 把pkgLen 反序列化成 message.Message
	err = json.Unmarshal(this.Buf[:pkgLen], &mes)
	if err != nil {
		fmt.Println("json.Unmarshal err=", err)
		return
	}

	return
}

func (this *Transfer) WritePkg(data []byte) (err error) {
	// 先发送一个长度给对方
	var pkgLen uint32
	pkgLen = uint32(len(data))
	binary.BigEndian.PutUint32(this.Buf[:4], pkgLen)
	// 发送长度
	n, err := this.Conn.Write(this.Buf[:4])
	if n != 4 || err != nil {
		fmt.Println("conn.Write err:", err)
		return
	}

	// 发送data本身
	n, err = this.Conn.Write(data)
	if n != int(pkgLen) || err != nil {
		fmt.Println("conn.Write err:", err)
		return
	}
	return
}
