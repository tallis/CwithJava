 #### C with JAVA using JNA ####
 ### Author: Rui Costa ###
 # 
 # Python script that compiles and runs
 # the Java application that makes use of
 # C code.
 ##
  
#!/usr/bin/env python
import os
import sys
import commands

## Compile a C program
def compileC(cLib, cFile):
	os.system("gcc -o %s -shared %s" % (cLib, cFile) )

def downloadJNA():
	if (os.path.isfile("jna.jar") == True):
		print "[CinJava] JNA Already Installed"
	else:
		print "[CinJava] JNA Not Found. Installing..."
		os.system( "wget https://github.com/twall/jna/zipball/master -O - | tar xz")
		os.system( "cp twall-jna-c1289c0/dist/jna.jar .")
		os.system("sudo rm -r twall-jna-c1289c0") 


def compileJava(javaFile):
	javaName = javaFile.split('.')
	os.system("javac -classpath jna.jar %s.java" % (javaName[0]))

def runJava(clibName, jFileName):
	javaName = jFileName.split('.')
	parsedLibs = cLibName.split('.')
	while(True):
		run = raw_input("[CinJava] Do you want to run your Java program? (Y/N): " )
		if (run == "Y"):
			os.system( "java -classpath jna.jar:. %s %s" % (javaName[0],parsedLibs[0]))
			cleanFiles()
			print "[CinJava] All clean! Exiting."
			break
		elif (run == "N"):
			print "[CinJava] Exiting."
			break
		else:
			print "[CinJava] Insert Y or N."
			continue


def cleanFiles():
	libclean = raw_input("[CinJava] Do you want to clean libraries and .class files? (Y/N): " )
	if(libclean == "Y"):
		os.system("sudo rm lib%s" % (cLibName))
		os.system("sudo rm *.class")
		return
	else:
		return

def listFiles(criteria):
	status, output = commands.getstatusoutput("ls %s" % (criteria))
	searchedFiles = output.split(' ')
	for fileName in searchedFiles:
		print fileName

## MAIN ##
print "## Welcome to CinJava ##"
print "[CinJava] Listing .C files in directory: "
listFiles("*.c")
cFileName = raw_input("[CinJava] Insert C filename: ")
# detect system
cLibName = raw_input("[CinJava] Choose C Lib name (.dylib for MacOS):" )

print "[CinJava] Compiling C file"
compileC("lib"+cLibName, cFileName)

print "[CinJava] Checking for JNA"
downloadJNA()

listFiles("*.java")
jFileName = raw_input("[CinJava] Insert JAVA filename: ")
compileJava(jFileName)

## Run generated JAVA code
runJava(cLibName, jFileName)

