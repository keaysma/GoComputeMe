# the compiler: gcc for C program, define as g++ for C++
CC = g++

# compiler flags:
#  -g    adds debugging information to the executable file
#  -Wall turns on most, but not all, compiler warnings
CFLAGS  = --std=c++17 -g -Wall

# the build target executable:
TARGET = test

$(TEST): $(TEST).cpp
	$(CC) $(CFLAGS) -o $(TARGET) $(TEST).cpp $(TARGET).cpp

all: $(TARGET)

$(TARGET): $(TARGET).cpp
	$(CC) $(CFLAGS) -o $(TARGET) *.cpp

clean:
	$(RM) $(TARGET)