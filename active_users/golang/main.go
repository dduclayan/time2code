package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

type file struct {
	filepath string
}


func getActiveUsers(fb file) []string {
	var activeUserList []string

	f, err := os.Open(fb.filepath)
	if err != nil {
		panic(err)
	}
	scanner := bufio.NewScanner(f)

	scanner.Scan() // skips header row aka [Username IsActive]
	for scanner.Scan(){
		line := scanner.Text()
		splitLines := strings.Fields(line)
		user := splitLines[0]
		status := splitLines[1]

		if status == "Yes" {
			activeUserList = append(activeUserList, user)
		}
	}
	f.Close()

	return activeUserList

}

func printActiveUsers(ul []string) {
	fileA := file{filepath: "D:\\Documents\\go_workspace\\src\\learningGoAgain\\activeUsers\\fileA.log"}
	var foundUserInList []string
	defaultPh := "(444) 123-1233"

	f, err := os.Open(fileA.filepath)
	if err != nil{
		log.Panic(err)
	}

	scanner := bufio.NewScanner(f)

	for scanner.Scan(){
		line := scanner.Text()
		splitLine := strings.SplitN(line, " ", 2)
		fullEmail := splitLine[0]
		ph := splitLine[1]
		user := strings.Split(fullEmail,"@")[0]

		exists := nameInList(user, ul)
		if exists == true{
			//fmt.Println("ok is true. value = ", exists)
			fmt.Printf("%v\t%v\n", user, ph)
			foundUserInList = append(foundUserInList, user)
		}
	}

	for _, val := range ul {
		exists := nameInList(val, foundUserInList)

		if exists == false {
			fmt.Printf("%v\t%v\n", val, defaultPh)
		}
	}

	f.Close()

}

func nameInList (n string, list []string) bool {
	exists := false
	for _, val := range list {
		if n == val {
			exists = true
		}
	}
	return exists
}

func main() {
	fileB := file{filepath: "D:\\Documents\\go_workspace\\src\\learningGoAgain\\activeUsers\\fileB.log"}
	activeUserList := getActiveUsers(fileB)
	printActiveUsers(activeUserList)
}
