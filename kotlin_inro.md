Kotlin-everywhere hub


simula and BCPL was not readable so bjare invented c++ for his phd
netscape wanted to compete with IE3 so invented javascript

kotlin 
	by jetbrains
	scala,grrovy or closure: with good parts
	currently in collaboration with google
	where to use
		spring boot in kotlin
		wherever java works
	slack,reddit,adobe,netflix confluence is written in kotlin


online playgorund for kotlin

	play.kotlinlang.org

intercolation

	use curly braces for expression

	println("Sum $a + $b is ${a+b}")

create a java project
	inside that create using kotlin

	direclty selecting will not work for kotlin


immutablility is a feature in intlleij
	does not allow a val to be assigned multiple times

	It is highly functional

		fun main(){
		    val x= 45
		    val oddOrEven = if(x % 2 == 0)
		//        println("The number is even")
		        "Even"
		    else
		//        println("The number is odd")
		        "Odd"

		    println("The number is $oddOrEven")
		}

String interpolation

in java how can we create a labda funtion to be written in prinring directly
	sout("THe number is"+(lambda function that returns a value))
