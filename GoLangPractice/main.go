package main

import "fmt"

func main() {
	fmt.Println("Hello world !")

	var str string = "hello world"
	var n, m int
	var mn float32

	var (
		name string = "Rakesh Kombali"
		email string
		age string
	)

    n =  10
	m =12
	mn = 3.354
	email = "numerouno51@gmail.com"
	age ="36"

	fmt.Println(str+", "+name)
	fmt.Println(n, m, mn)
	fmt.Println(email+","+age)

	// defining datatype
	country := "IN"
	val := 15
	fmt.Println(country,val)
}
